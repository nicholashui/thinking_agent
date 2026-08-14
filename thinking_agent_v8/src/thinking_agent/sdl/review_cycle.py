"""Review cycle (v8 §IV.8 / impl §18.12): quick + deep reviews.

All outputs are PROPOSALS (rule 42 / S50): the review writes NOTHING —
no KB changes, no contract changes, no gap-map application. Follow-through
(rule 48): candidates that remain DISCOVERED across a review boundary are
reported as a monitored failure signal.
"""

from dataclasses import dataclass
from typing import Any

from thinking_agent.domain.enums import CandidateStatus
from thinking_agent.domain.sdl import ReviewReport


@dataclass
class ReviewCycle:
    quick_review_trials: int = 10
    _trials_since_review: int = 0

    def note_trial(self) -> bool:
        self._trials_since_review += 1
        return self._trials_since_review >= self.quick_review_trials

    def reset(self) -> None:
        self._trials_since_review = 0

    def run(self, kind: str, ledger: Any, gap_map: Any,
            candidate_pool: list[Any], floors: dict[str, float] | None = None) -> ReviewReport:
        report = ReviewReport(report_id=f"review-{kind}-{self._trials_since_review}",
                              review_kind=kind)
        # discovered-but-not-attempted: rule 48 follow-through signal
        report.discovered_not_attempted = [
            c.candidate_id for c in candidate_pool
            if c.status == CandidateStatus.DISCOVERED
        ]
        # regressions: dimension floors crossed (proposal only — S50)
        if floors:
            dims = floors.get("dimensions", {})
            for dim, floor in dims.items():
                mean = floors.get("means", {}).get(dim, floor)
                if mean < floor:
                    report.regressed.append(f"{dim}: {mean} < floor {floor}")
                    report.gap_refresh_proposal.append(
                        {"gap_type": "dimension_gap", "dimension": dim,
                         "magnitude": round(floor - mean, 3)})
        report.metrics = {"trials_since_review": self._trials_since_review}
        return report
