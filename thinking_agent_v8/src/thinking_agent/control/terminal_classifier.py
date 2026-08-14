"""State-only terminal classifier (impl §11.7, v5 V7/V8 semantics).

Deterministic; reads ONLY graph state + kernel-provided verification values.
Never reads raw task declarations for security-sensitive decisions (the
declared fields it consults are already gated/attested upstream).

Classification order (impl §11.7):
  L2 no-verifier escalation → L1 evidence degradation → ambiguous
  verification → reliability block → evidence gap → probe → infeasibility
  → resource stop → approximation → producer-specific result.
"""

from dataclasses import dataclass
from typing import Any

from thinking_agent.domain.enums import TerminalStatus


@dataclass
class Classification:
    status: TerminalStatus
    reason: str


def classify(
    *,
    verification: dict[str, Any] | None,
    state: dict[str, Any],
) -> Classification:
    """Returns the terminal classification for a completed (or stopped) episode."""
    v = verification or {}

    # 1. SOLVED — outcome verifier is the sole producer (impl §15.1)
    if v.get("success"):
        return Classification(TerminalStatus.SOLVED, "outcome verification passed")

    # 2. UNSAFE — safety kernel producer (replication, misattestation, denial)
    if state.get("internal_fault") == "UNSAFE" or v.get("unsafe"):
        return Classification(TerminalStatus.UNSAFE, "safety kernel denial")

    # 3. L2 no-verifier escalation (v5: reliability blocked w/o verifier)
    if v.get("reliability_blocked"):
        return Classification(
            TerminalStatus.ESCALATED, "reliability below bar / second verifier missing"
        )

    # 4. ambiguous verification → evidence degradation ladder (v5 L1)
    if v.get("ambiguous"):
        if state.get("verifier_outage"):
            return Classification(
                TerminalStatus.NEEDS_EVIDENCE, "ambiguous verification, verifier outage (L1)"
            )
        return Classification(
            TerminalStatus.NEEDS_EVIDENCE, "verification ambiguous; evidence insufficient"
        )

    # 5. evidence gap
    missing = state.get("missing_evidence") or []
    if missing:
        fillable = all(m.get("fillable") for m in missing) and state.get("fillable_gap")
        if not fillable:
            return Classification(
                TerminalStatus.NEEDS_EVIDENCE, "unfillable evidence gap"
            )

    # 6. probe available
    if state.get("probe_available"):
        return Classification(
            TerminalStatus.NEEDS_EXPERIMENT, "safe probe available"
        )

    # 7. infeasibility (constraint screen / plan stop condition)
    if state.get("infeasible"):
        return Classification(TerminalStatus.INFEASIBLE, "constraints unsatisfiable")

    # 8. resource/budget stop (BudgetController / LoopMonitor producers)
    stop_reason = state.get("stop_reason") or ""
    if stop_reason in {
        "iteration ceiling", "deadline exceeded",
        "reserved epilogue budget would be exhausted",
        "novelty plateau", "EVOC exhausted", "token ceiling", "call ceiling",
    }:
        return Classification(TerminalStatus.RESOURCE_LIMITED, stop_reason)

    # 9. escalation producers (authorization, gates, owner, pending timeout) —
    # these outrank approximation: an escalated episode is not approvable
    if state.get("escalate"):
        return Classification(
            TerminalStatus.ESCALATED, state.get("escalate_reason") or "escalation required"
        )

    # 10. approximation (selector recorded a bounded error)
    if state.get("approximation_available"):
        return Classification(
            TerminalStatus.APPROXIMATED, "bounded-error approximation recorded"
        )

    # residual: no decision reachable under policy → evidence needed
    return Classification(
        TerminalStatus.NEEDS_EVIDENCE, "no terminal producer matched; evidence required"
    )
