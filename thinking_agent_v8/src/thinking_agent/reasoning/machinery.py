"""Reasoning machinery (impl §11.5): structure-first scan, insight pass,
premortem, red team, bounded council, general-route comparison.

Every model-driven call degrades DETERMINISTICALLY when no mock script or
provider response exists — the graph must never crash on a missing script;
the fallback records a conservative result instead (falsification-flavored
defaults, not optimistic ones).
"""

from dataclasses import dataclass, field
from typing import Any

from thinking_agent.domain.task import SituationSignature

# deterministic structure detectors per domain (impl §11.5 `structure_first_scan`)
STRUCTURE_CUES = {
    "systems": ["feedback", "loop", "stock", "flow", "delay"],
    "causal": ["cause", "effect", "confound", "intervention"],
    "tree": ["branch", "decision tree", "scenario"],
    "incentive": ["stakeholder", "incentive", "reward", "auction"],
    "constraint": ["capacity", "bottleneck", "min", "serial", "throughput"],
    "reference_class": ["base rate", "reference class", "distribution"],
}

STRUCTURE_DOMAINS = {"engineering", "supply", "science", "organization",
                     "strategy", "finance"}


@dataclass
class StructureScan:
    domains: list[str] = field(default_factory=list)
    structures: list[str] = field(default_factory=list)
    cues: dict[str, list[str]] = field(default_factory=dict)
    required: bool = False


def structure_first_scan(text: str, signature: SituationSignature) -> StructureScan:
    """Deterministic structure detection. Mandatory for systems/causal/
    organizational/strategy/finance signatures (impl §11.5)."""
    t = text.lower()
    scan = StructureScan(domains=signature.domains,
                         required=bool(set(signature.domains) & STRUCTURE_DOMAINS))
    for name, cues in STRUCTURE_CUES.items():
        found = [c for c in cues if c in t]
        if found:
            scan.structures.append(name)
            scan.cues[name] = found
    return scan


def insight_pass(model: Any, state: dict[str, Any]) -> list[str]:
    """Non-obvious insights; deterministic fallback derived from alternatives."""
    try:
        out = model.invoke_text(_messages(state, "insight_pass"))
        return [line for line in out.splitlines() if line.strip()][:5]
    except RuntimeError:
        alts = state.get("alternatives") or []
        if not alts:
            return ["no alternatives to inspect"]
        return [f"failure branch priced for {a.get('alternative_id')}: "
                f"{a.get('failure_branch', 'unspecified')}" for a in alts][:3]


def premortem(model: Any, state: dict[str, Any]) -> list[dict[str, Any]]:
    """Failure-mode ranking connected to alternatives (impl §11.5)."""
    try:
        out = model.invoke_text(_messages(state, "premortem"))
        lines = [line for line in out.splitlines() if line.strip()]
        return [{"risk_hash": str(i), "description": line} for i, line in enumerate(lines[:8])]
    except RuntimeError:
        risks = []
        for a in state.get("alternatives") or []:
            for r in a.get("risks") or []:
                risks.append({"risk_hash": str(len(risks)), "description": r,
                              "alternative": a.get("alternative_id")})
        return risks or [{"risk_hash": "pm0", "description": "no risks declared"}]


def red_team(model: Any, state: dict[str, Any]) -> dict[str, Any]:
    """Material-flaw screen on changed candidate content (impl §11.5)."""
    try:
        out = model.invoke_text(_messages(state, "red_team"))
        return {"findings": [line for line in out.splitlines() if line.strip()],
                "reject": False}
    except RuntimeError:
        findings = []
        for a in state.get("alternatives") or []:
            if "INFEASIBLE" in (a.get("description") or "").upper():
                findings.append(f"{a.get('alternative_id')}: infeasibility marker")
            if not (a.get("risks") or a.get("failure_branch")):
                findings.append(f"{a.get('alternative_id')}: no failure branch priced")
        return {"findings": findings, "reject": False}


def council(model: Any, state: dict[str, Any], roles: tuple[str, ...] = (
        "proposer", "challenger", "adjudicator")) -> dict[str, Any]:
    """Bounded council: proposal, counterproposal, independent adjudication.
    Minority reports retained; selection stays verification-governed."""
    out: dict[str, Any] = {"roles": {}, "minority_reports": [], "bounded": len(roles)}
    for role in roles:
        try:
            text = model.invoke_text(_messages(state, f"council:{role}"))
            out["roles"][role] = text[:400]
        except RuntimeError:
            out["roles"][role] = f"{role}: deterministic default (no script)"
    return out


def general_route_summary(alternatives: list[dict[str, Any]]) -> str:
    """The general governed route's own conclusion (for divergence checks)."""
    if not alternatives:
        return "no viable alternative"
    return "selected:" + ",".join(sorted(a.get("alternative_id", "") for a in alternatives))


def _messages(state: dict[str, Any], role: str) -> list[dict]:
    meta = (state.get("request") or {}).get("task_metadata") or {}
    content = {"scenario": meta.get("scenario", "default"), "role": role,
               "frame": state.get("frame") or {},
               "alternatives": state.get("alternatives") or [],
               "decision": state.get("decision") or {}}
    return [{"role": "system", "content": "Governed reasoning pass. Return concise text."},
            {"role": "user", "content": repr(content)}]
