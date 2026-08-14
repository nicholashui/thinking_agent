"""Interpretation pricing (rule 41 / impl §13.9).

When source numbers admit multiple consistent readings: enumerate each,
price each, state which interpretation is used, test decision robustness.
A decision that flips with the reading is not a decision — NEEDS_EVIDENCE.
"""

from dataclasses import dataclass, field


@dataclass
class Interpretation:
    reading_id: str
    description: str
    priced_outcome: str


@dataclass
class PricingResult:
    readings: list[Interpretation] = field(default_factory=list)
    selected_reading: str = ""
    decision_robust: bool = True
    needs_evidence: bool = False
    notes: list[str] = field(default_factory=list)


def price_interpretations(
    readings: list[Interpretation],
    decision_factory,
) -> PricingResult:
    """Enumerates readings, prices each, and checks robustness.

    `decision_factory(reading)` returns the decision under that reading;
    robustness = all readings yield the SAME decision key.
    """
    result = PricingResult(readings=readings)
    decisions = {}
    for r in readings:
        try:
            decisions[r.reading_id] = decision_factory(r)
        except Exception as exc:  # an unpriceable reading is evidence, not error
            result.notes.append(f"{r.reading_id}: unpriceable ({exc})")
            continue
    if not decisions:
        result.needs_evidence = True
        result.decision_robust = False
        result.notes.append("no reading priceable → NEEDS_EVIDENCE")
        return result
    keys = set(decisions.values())
    result.decision_robust = len(keys) == 1
    if not result.decision_robust:
        result.needs_evidence = True
        result.notes.append("decision flips across readings → NEEDS_EVIDENCE or clarification")
    result.selected_reading = next(iter(decisions))
    return result
