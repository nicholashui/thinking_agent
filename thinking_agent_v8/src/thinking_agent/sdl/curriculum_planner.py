"""Curriculum Planner (v8 §IV.4 / impl §18.7): gap-weighted challenge
selection at the competence boundary.

learning_value = gap_weight × verdict_uncertainty × novelty − practice_cost
verdict_uncertainty = 4 × p_success × (1 − p_success)  (peaks at p=0.5)
Every selected item must reference its gap entry and score components.
"""

from dataclasses import dataclass
from typing import Any

from thinking_agent.domain.enums import CandidateStatus, PlanStatus
from thinking_agent.domain.sdl import ChallengeCandidate, LearningPlan, LearningPlanItem


@dataclass
class Selection:
    item: LearningPlanItem
    score: float
    components: dict[str, float]


class CurriculumPlanner:
    def __init__(self, gap_map: Any, pool_min: int = 20,
                 estimated_success: float = 0.5):
        self.gap_map = gap_map
        self.pool_min = pool_min
        self.estimated_success = estimated_success

    def uncertainty(self, p_success: float) -> float:
        return 4 * p_success * (1 - p_success)

    def score(self, candidate: ChallengeCandidate,
              practice_cost: float) -> Selection | None:
        gap_weight = self.gap_map.gap_weight(candidate.signature)
        if gap_weight <= 0:
            return None  # never select a zero-gap candidate (G3)
        unc = self.uncertainty(self.estimated_success)
        novelty = candidate.novelty_score
        value = gap_weight * unc * novelty - practice_cost
        return Selection(
            item=LearningPlanItem(
                item_id=f"item-{candidate.candidate_id}",
                challenge_id=candidate.candidate_id,
                source=candidate.source_id,
                signature=candidate.signature,
                expected_styles=[],
                target_gap_id=f"gap:{candidate.signature}",
                expected_closure=value,
                trial_budget=0,
                max_attempts=2,  # anti-obsession rule
            ),
            score=value,
            components={"gap_weight": gap_weight, "uncertainty": unc,
                        "novelty": novelty, "cost": practice_cost},
        )

    SELECTABLE = {CandidateStatus.DISCOVERED, CandidateStatus.PLANNED,
                  CandidateStatus.APPROVED, CandidateStatus.QUEUED}

    def propose_plan(self, candidates: list[ChallengeCandidate],
                     review_ref: str = "", max_items: int = 5,
                     budget_per_item: float = 1.0) -> LearningPlan:
        """DRAFT plan — cannot execute (invariant 14). Suppressed or rejected
        candidates never reach selection (impl §18.3 suppression rules)."""
        selections: list[Selection] = []
        for c in candidates:
            if c.status not in self.SELECTABLE:
                continue
            s = self.score(c, budget_per_item)
            if s is not None:
                c.status = CandidateStatus.PLANNED  # follow-through bookkeeping
                selections.append(s)
        selections.sort(key=lambda s: -s.score)
        plan = LearningPlan(
            plan_id=f"plan-{len(selections)}",
            review_ref=review_ref,
            status=PlanStatus.DRAFT,
            items=[s.item for s in selections[:max_items]],
            total_budget=int(max_items * budget_per_item),
        )
        return plan
