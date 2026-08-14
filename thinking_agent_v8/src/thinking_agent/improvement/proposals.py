"""ImprovementEngine (impl §17.5): proposal intake, canonical dedup,
baseline-frozen evaluation gate, canary, retain/rollback.

Invariants honored here: no candidate improvement may modify hidden tests,
judge prompts, frozen-baseline results, routing history, or ledger entries;
evaluation runs ONLY when the baseline is frozen (kernel fact).
"""

from dataclasses import dataclass

from thinking_agent.canonical import sha256_hex


@dataclass
class ImprovementProposal:
    proposal_id: str
    canonical_hash: str
    description: str
    risk_level: str = "R1"  # R1 scenario | R2 gate | R3 module
    status: str = "QUEUED"
    evaluation_ref: str = ""


class ImprovementEngine:
    def __init__(self, baseline_frozen: bool = True, rate_cap: int = 10):
        self.baseline_frozen = baseline_frozen
        self.rate_cap = rate_cap
        self._seen: set[str] = set()
        self._queue: list[ImprovementProposal] = []
        self._retained: list[str] = []
        self._rolled_back: list[str] = []

    def propose(self, description: str, risk_level: str = "R1") -> ImprovementProposal | None:
        canonical = sha256_hex({"description": description, "risk": risk_level})
        if canonical in self._seen:
            return None  # canonical dedup — duplicates never queue twice
        self._seen.add(canonical)
        if len(self._queue) >= self.rate_cap:
            return None  # global rate cap
        p = ImprovementProposal(
            proposal_id=f"imp-{len(self._seen):04d}",
            canonical_hash=canonical,
            description=description,
            risk_level=risk_level,
        )
        self._queue.append(p)
        return p

    def evaluate(self, proposal: ImprovementProposal,
                 hidden_tests_pass: bool,
                 regression_vs_baseline_pass: bool) -> str:
        """Frozen-baseline evaluation (impl §17.5). Returns
        retain | rollback | skip — evaluation requires a frozen baseline."""
        if not self.baseline_frozen:
            proposal.status = "SKIPPED_UNFROZEN"
            return "skip"
        if proposal.risk_level == "R3":
            proposal.status = "PENDING_REVIEW"  # modules need independent review + canary
            return "pending_review"
        if hidden_tests_pass and regression_vs_baseline_pass:
            self._retained.append(proposal.proposal_id)
            proposal.status = "RETAINED"
            return "retain"
        self._rolled_back.append(proposal.proposal_id)
        proposal.status = "ROLLED_BACK"
        return "rollback"

    def queue_size(self) -> int:
        return len(self._queue)
