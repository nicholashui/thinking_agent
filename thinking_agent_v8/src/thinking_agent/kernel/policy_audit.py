"""Read-path policy audit (impl §9.5 — the V1 assertion, production form).

Two layers:
1. AST scan: task-node source files must not READ security-knob names from
   request/state/config objects — only through the kernel facade.
2. Behavioral test hook: assert no Pydantic output schema carries a field
   that can override a kernel knob.
"""

import ast
from pathlib import Path

SECURITY_KNOB_NAMES = {
    # v5 harness knob list (world-facts class), normalized
    "pending_timeout", "calls_ceiling", "evoc", "evoc_base", "evoc_decay",
    "novelty_plateau", "calibration", "identities", "verifier_identities",
    "outage", "verifier_outage", "baseline_frozen", "write_authorization",
    "class_bars", "pending_allowlist", "action_taxonomy", "trust_margin",
    "consolidation_threshold", "procedural_write_authorized", "sdl_enabled",
    "pool_min", "quick_review_trials", "deep_review_schedule",
    "counter_design_canary_enabled", "discovery_budget_candidates",
    "agents_per_round", "gate_reentry_budget", "reframe_budget",
    "pending_timeout_seconds", "deadline_seconds", "tokens", "iterations",
}

FORBIDDEN_SOURCES = {"request", "state", "config", "task_request", "metadata"}


class ReadPathViolation:
    def __init__(self, file: str, line: int, knob: str, source: str):
        self.file, self.line, self.knob, self.source = file, line, knob, source

    def __str__(self) -> str:
        return f"{self.file}:{self.line}: knob {self.knob!r} read from {self.source!r}"


def scan_file(path: Path) -> list[ReadPathViolation]:
    """Finds `source.knob` attribute reads of security knobs in task code."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    violations: list[ReadPathViolation] = []

    class V(ast.NodeVisitor):
        def visit_Attribute(self, node: ast.Attribute) -> None:
            if (
                isinstance(node.value, ast.Name)
                and node.value.id in FORBIDDEN_SOURCES
                and node.attr in SECURITY_KNOB_NAMES
            ):
                violations.append(
                    ReadPathViolation(str(path), node.lineno, node.attr, node.value.id)
                )
            self.generic_visit(node)

    V().visit(tree)
    return violations


def scan_directory(root: Path, exclude_dirs: set[str] | None = None) -> list[ReadPathViolation]:
    exclude = exclude_dirs or {"kernel", "control", "__pycache__"}
    out: list[ReadPathViolation] = []
    for p in sorted(root.rglob("*.py")):
        if any(part in exclude for part in p.parts):
            continue
        out.extend(scan_file(p))
    return out


def assert_no_knob_override_fields(model_fields: set[str]) -> list[str]:
    """Behavioral half: a model output schema must not expose kernel knobs."""
    return sorted(model_fields & SECURITY_KNOB_NAMES)
