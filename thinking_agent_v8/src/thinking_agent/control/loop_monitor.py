"""LoopMonitor: EVOC, novelty plateau, wait exemptions (impl §11.2 / v5 V8).

`pending_wait` and `gate_wait` are exempt from EVOC/plateau churn checks but
never from hard budgets (impl §11.2 — enforced in budget_guard, not here).
"""

from dataclasses import dataclass, field


@dataclass
class LoopMonitorState:
    evoc: float = 0.0
    novelty_signatures: list[str] = field(default_factory=list)
    plateau_streak: int = 0
    unproductive_streak: int = 0


class LoopMonitor:
    def __init__(self, evoc_base: float, evoc_decay: float, novelty_plateau: int):
        self.evoc_base = evoc_base
        self.evoc_decay = evoc_decay
        self.novelty_plateau = novelty_plateau
        self.state = LoopMonitorState()

    def value_of_continued_computation(self, progress: bool, novelty: bool) -> float:
        """EVOC proxy: base * decay^unproductive; novelty resets the streak."""
        if novelty:
            self.state.unproductive_streak = 0
        elif not progress:
            self.state.unproductive_streak += 1
        self.state.evoc = self.evoc_base * (self.evoc_decay ** self.state.unproductive_streak)
        return self.state.evoc

    def register_signature(self, signature: str) -> bool:
        """Returns True when the signature is new (novel)."""
        if signature in self.state.novelty_signatures:
            self.state.plateau_streak += 1
            return False
        self.state.novelty_signatures.append(signature)
        self.state.plateau_streak = 0
        return True

    def plateau_reached(self) -> bool:
        return self.state.plateau_streak >= self.novelty_plateau

    def should_stop(self, wait_exempt: bool = False) -> str | None:
        """RESOURCE_LIMITED producers for loop-level unproductivity."""
        if wait_exempt:
            return None  # pending/gate waits never churn
        if self.plateau_reached():
            return "novelty plateau"
        if self.state.evoc <= 0.01:
            return "EVOC exhausted"
        return None
