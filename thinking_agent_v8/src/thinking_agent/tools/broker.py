"""Tool Broker (impl §16): proposal→execution conversion, allowlist,
validation, idempotency, timeouts, receipts, sanitation.

Observations are untrusted until verified (EvidenceTrust.TOOL_UNTRUSTED).
"""

from dataclasses import dataclass, field
from typing import Any, Callable

from thinking_agent.canonical import content_hash, sha256_hex
from thinking_agent.domain.enums import ActionClass, AuthorizationStatus, EvidenceTrust


@dataclass
class ToolSpec:
    name: str
    action_class: ActionClass
    handler: Callable[..., Any]
    allowed_args: set[str] = field(default_factory=set)
    max_output_chars: int = 4000
    # domain allowlist for retrieval-class tools; empty = no network access
    allowed_domains: set[str] = field(default_factory=set)
    require_domain_allowlist: bool = False


class ToolBroker:
    """Executes plan tasks: validates authorization + allowlist + args,
    enforces idempotency keys, produces receipts and untrusted observations."""

    def __init__(self, tools: dict[str, ToolSpec] | None = None):
        self._tools = tools or {}
        self._idempotency: dict[str, dict[str, Any]] = {}

    def register(self, spec: ToolSpec) -> None:
        self._tools[spec.name] = spec

    def execute_plan(self, plan: dict[str, Any], authorization: dict[str, Any],
                     state: dict[str, Any], ctx: Any) -> tuple[list[dict], list[dict]]:
        actions: list[dict[str, Any]] = []
        observations: list[dict[str, Any]] = []
        for task in plan.get("tasks", []):
            receipt = self._execute_task(task, authorization, plan, state, ctx)
            if receipt is None:
                continue
            actions.append({
                "idempotency_key": receipt["idempotency_key"],
                "tool_name": receipt["tool_name"],
                "success": receipt["success"],
                "receipt_id": receipt["receipt_id"],
            })
            observations.append({
                "observation_id": f"obs-{receipt['receipt_id']}",
                "content_summary": receipt["output_summary"],
                "content_hash": receipt["output_hash"],
                "source": receipt["tool_name"],
                "trust": EvidenceTrust.TOOL_UNTRUSTED.value,
                "from_tool_receipt": receipt["receipt_id"],
            })
        return actions, observations

    def _execute_task(self, task: dict[str, Any], authorization: dict[str, Any],
                      plan: dict[str, Any], state: dict[str, Any], ctx: Any) -> dict | None:
        tool_name = task.get("tool_name")
        spec = self._tools.get(tool_name)
        if spec is None:
            return None  # unregistered tool: never executes (allowlist)

        # authorization token must cover this action class (rank order —
        # A5 > A4 > A3 > A2 > A1; the token's class must be >= the tool's)
        if authorization.get("status") != AuthorizationStatus.APPROVED.value:
            return None
        rank = {c: i for i, c in enumerate(ActionClass)}
        if rank[ActionClass(authorization.get("action_class"))] < rank[spec.action_class]:
            return None  # token class below required class

        idem_key = task.get("idempotency_key") or (
            f"{state.get('task_id')}:{plan.get('plan_id')}:{task.get('plan_task_id')}"
        )
        if idem_key in self._idempotency:
            return self._idempotency[idem_key]  # return prior receipt — never re-run

        args = {k: v for k, v in task.get("arguments", {}).items()
                if k in spec.allowed_args}
        # network-class tools must pass the domain allowlist before the
        # handler is ever invoked (impl §16.2: read-only HTTP for approved domains)
        if spec.require_domain_allowlist and not self._domain_ok(
                str(args.get("url", "")), spec.allowed_domains):
            receipt = self._receipt(task, idem_key, tool_name, False,
                                    "error: domain not in allowlist")
            self._idempotency[idem_key] = receipt
            return receipt
        try:
            output = spec.handler(**args)
        except Exception as exc:
            receipt = self._receipt(task, idem_key, tool_name, False, f"error: {exc}")
            self._idempotency[idem_key] = receipt
            return receipt
        summary = self._sanitize(str(output))[: spec.max_output_chars]
        receipt = self._receipt(task, idem_key, tool_name, True, summary)
        self._idempotency[idem_key] = receipt
        return receipt

    def _receipt(self, task: dict[str, Any], idem_key: str, tool_name: str,
                 success: bool, summary: str) -> dict[str, Any]:
        return {
            "receipt_id": f"rcpt-{content_hash((idem_key, summary))}",
            "plan_task_id": task.get("plan_task_id", ""),
            "tool_name": tool_name,
            "idempotency_key": idem_key,
            "success": success,
            "output_hash": sha256_hex(summary),
            "output_summary": summary,
            "sanitized": True,
        }

    @staticmethod
    def _sanitize(text: str) -> str:
        import re

        text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)
        return text

    @staticmethod
    def _domain_ok(url: str, allowed: set[str]) -> bool:
        if not url or not allowed:
            return False  # empty allowlist = no network access
        try:
            from urllib.parse import urlparse
            host = (urlparse(url).hostname or "").lower()
        except ValueError:
            return False
        return any(host == d or host.endswith("." + d) for d in allowed)


def builtin_tools() -> dict[str, ToolSpec]:
    return {
        "calculator": ToolSpec(
            name="calculator", action_class=ActionClass.A1,
            handler=lambda expr: _calc(expr), allowed_args={"expr"},
        ),
        "knowledge_lookup": ToolSpec(
            name="knowledge_lookup", action_class=ActionClass.A1,
            handler=lambda query: f"lookup-result:{content_hash(query)}",
            allowed_args={"query"},
        ),
        "http_retrieval": ToolSpec(
            name="http_retrieval", action_class=ActionClass.A2,
            handler=lambda url: f"fetched:{content_hash(url)}",
            allowed_args={"url"},
            require_domain_allowlist=True,  # read-only HTTP for approved domains
            allowed_domains={"arxiv.org", "huggingface.co"},
        ),
    }


def _calc(expr: str) -> str:
    """Safe arithmetic: AST-whitelist evaluation — only Constant, UnaryOp,
    BinOp over + - * / and parentheses. No names, attributes, or calls can
    ever execute (no eval)."""
    import ast
    import operator

    OPS = {
        ast.Add: operator.add, ast.Sub: operator.sub,
        ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.USub: operator.neg, ast.UAdd: operator.pos,
    }

    def _eval(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
            return OPS[type(node.op)](_eval(node.operand))
        raise ValueError("unallowed expression element")

    if len(expr) > 100:
        raise ValueError("expression too long")
    try:
        tree = ast.parse(expr, mode="eval")
        return str(_eval(tree))
    except Exception as exc:
        raise ValueError(f"unparseable: {exc}") from exc
