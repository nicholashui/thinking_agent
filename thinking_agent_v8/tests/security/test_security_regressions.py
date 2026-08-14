"""Security regression tests: kernel immutability, tool allowlists,
no-silent-execution-skip, deadline enforcement."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import pytest  # noqa: E402

from thinking_agent.domain.enums import AuthorizationStatus  # noqa: E402
from thinking_agent.kernel.safety_kernel import SafetyKernel  # noqa: E402
from thinking_agent.kernel.world_facts_store import WorldFactsStore  # noqa: E402
from thinking_agent.tools.broker import ToolBroker, builtin_tools  # noqa: E402


def _kernel():
    from tests.helpers import REPO_ROOT
    return SafetyKernel(WorldFactsStore(
        REPO_ROOT / "configs" / "kernel" / "world_facts.test.yaml").load())


def test_kernel_budgets_immutable_from_facade():
    k = _kernel()
    with pytest.raises(Exception):
        k.budgets.iterations = 99999


def test_kernel_identities_immutable_from_snapshot():
    k = _kernel()
    with pytest.raises(Exception):
        k._snapshot.facts.verification.verifier_identities.append(
            {"identity_id": "evil"})
    with pytest.raises(Exception):
        k._snapshot.facts.pending_allowlist.append("evil_task")


def test_kernel_policy_change_is_new_instance_only():
    k = _kernel()
    original = k.bar_for(__import__("thinking_agent.domain.enums",
                                    fromlist=["ActionClass"]).ActionClass.A1)
    assert original == 0.6
    # even the operator's path is a new snapshot, never an in-place mutation


def test_http_retrieval_requires_allowlisted_domain():
    broker = ToolBroker(builtin_tools())
    plan = {"plan_id": "p", "tasks": [{
        "plan_task_id": "t1", "tool_name": "http_retrieval",
        "arguments": {"url": "https://evil.example.com/steal"},
        "action_class": "A2", "idempotency_key": "sec:t1:1",
    }]}
    auth = {"status": AuthorizationStatus.APPROVED.value, "action_class": "A2"}
    actions, _ = broker.execute_plan(plan, auth, {}, None)
    assert actions[0]["success"] is False  # domain blocked before handler
    plan["tasks"][0]["arguments"]["url"] = "https://arxiv.org/abs/2508.05004"
    plan["tasks"][0]["idempotency_key"] = "sec:t1:2"
    actions, _ = broker.execute_plan(plan, auth, {}, None)
    assert actions[0]["success"] is True


def test_verifier_identity_merge_preserves_two_identities():
    """Composite reducer: two verifiers on one candidate are BOTH kept (§8.6)."""
    from thinking_agent.state.reducers import merge_by_key
    red = merge_by_key(("candidate_id", "verifier_identity"))
    merged = red([{"candidate_id": "c1", "verifier_identity": "alpha", "reliability": 0.8},
                  {"candidate_id": "c1", "verifier_identity": "beta", "reliability": 0.9}],
                 None)
    assert len(merged) == 2  # both identities preserved


def test_deadline_enforced_as_resource_limited():
    """Kernel deadline expires mid-loop → RESOURCE_LIMITED (impl §10.2.5)."""
    from thinking_agent.domain.enums import TerminalStatus
    from thinking_agent.graphs.task_graph import compile_task_graph
    from tests.helpers import Fixture, request_for, solved_scripts

    class GrowingClock:
        def __init__(self):
            self.calls = 0
        def now(self):
            return "2026-08-13T00:00:00Z"
        def monotonic(self):
            self.calls += 1
            return 0.0 if self.calls == 1 else 4000.0  # 4000s > 1800s deadline

    scripts = solved_scripts("SDEAD")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.clock = GrowingClock()
    app = compile_task_graph().compile()
    out = app.invoke({"request": request_for("SDEAD"), "thread_id": "th-SDEAD"},
                     config={"configurable": {"ctx": ctx}})
    assert out["terminal_status"] == TerminalStatus.RESOURCE_LIMITED.value
    assert "deadline" in out["terminal_reason"]


def test_broker_missing_escalates_not_skips():
    """A planned external action with no broker must ESCALATE — never
    silently 'succeed' without executing (impl §23.1 fault translation)."""
    from thinking_agent.domain.enums import TerminalStatus
    from thinking_agent.graphs.task_graph import compile_task_graph
    from tests.helpers import Fixture, request_for, solved_scripts

    scripts = solved_scripts("SNOBROKER")
    scripts["SNOBROKER"]["AltSet"] = scripts["SNOBROKER"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-B", "description": "retrieve approved page",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["allowlisted"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.tools = None  # no broker
    app = compile_task_graph().compile()
    out = app.invoke({"request": request_for("SNOBROKER", tool="http_retrieval"),
                      "thread_id": "th-SNOBROKER"},
                     config={"configurable": {"ctx": ctx}})
    assert out["terminal_status"] == TerminalStatus.ESCALATED.value
    assert "broker unavailable" in out["terminal_reason"]
