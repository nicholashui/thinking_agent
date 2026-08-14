"""Budget controller (impl §11.2 `budget_guard`): hard limits + reserved epilogue."""

from dataclasses import dataclass

from thinking_agent.kernel.world_facts import BudgetFacts


@dataclass
class BudgetSnapshot:
    facts: BudgetFacts
    iterations_used: int = 0
    cognitive_calls_used: int = 0
    tokens_used: int = 0
    agents_used: int = 0
    bookkeeping_calls: int = 0
    reserved_for_epilogue: int = 3  # classification + packet + checkpoint
    stop_reason: str = ""
    stopped: bool = False

    def reserve_ok(self) -> bool:
        return (
            self.cognitive_calls_used + self.reserved_for_epilogue
            <= self.facts.cognitive_calls
        )

    def charge(self, calls: int = 0, tokens: int = 0, agents: int = 0, bookkeeping: int = 0) -> bool:
        if (
            self.cognitive_calls_used + calls > self.facts.cognitive_calls
            or self.tokens_used + tokens > self.facts.tokens
            or self.agents_used + agents > self.facts.agents_per_round
        ):
            return False
        self.cognitive_calls_used += calls
        self.tokens_used += tokens
        self.agents_used += agents
        self.bookkeeping_calls += bookkeeping
        return True

    def hit_hard_limit(self, iteration: int, deadline_elapsed: bool) -> str | None:
        if self.iterations_used >= self.facts.iterations:
            return "iteration ceiling"
        if not self.reserve_ok():
            return "reserved epilogue budget would be exhausted"
        if deadline_elapsed:
            return "deadline exceeded"
        return None

    def next_iteration(self) -> None:
        self.iterations_used += 1


class BudgetController:
    """Owns the RESOURCE_LIMITED producer's hard-limit predicates."""

    def __init__(self, facts: BudgetFacts):
        self.snapshot = BudgetSnapshot(facts=facts)

    def guard(self, iteration: int, deadline_elapsed: bool = False) -> str | None:
        return self.snapshot.hit_hard_limit(iteration, deadline_elapsed)

    @classmethod
    def from_snapshot(cls, snapshot: dict | None) -> "BudgetController":
        """Rebuilds from the checkpointed budget_snapshot dict."""
        facts = BudgetFacts(
            iterations=int((snapshot or {}).get("iterations", 12)),
            cognitive_calls=int((snapshot or {}).get("cognitive_calls", 24)),
            tokens=int((snapshot or {}).get("tokens", 40000)),
            agents_per_round=int((snapshot or {}).get("agents_per_round", 6)),
            deadline_seconds=int((snapshot or {}).get("deadline_seconds", 1800)),
        )
        ctl = cls(facts)
        if snapshot:
            ctl.snapshot.iterations_used = int(snapshot.get("iterations_used", 0))
            ctl.snapshot.cognitive_calls_used = int(snapshot.get("cognitive_calls_used", 0))
            ctl.snapshot.tokens_used = int(snapshot.get("tokens_used", 0))
        return ctl
