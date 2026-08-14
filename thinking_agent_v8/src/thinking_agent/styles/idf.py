"""IDF-weighted trigger scoring (impl §13.3, v6 §II.2.5 v1.1).

idf(term) = log((1 + model_count) / (1 + models_containing_term)) + 1
weighted_match = Σ idf(domain terms) + Σ idf(goal terms) + Σ idf(context terms)
route_score    = weighted_match × pos_win_rate − 0.5 × neg_failure_rate
"""

import math
from collections import defaultdict

from thinking_agent.domain.routing import StyleModel


class IDFWeights:
    def __init__(self, models: list[StyleModel]):
        self.model_count = len(models)
        self.term_models: dict[str, set[str]] = defaultdict(set)
        for m in models:
            for term in m.triggers:
                self.term_models[term].add(m.id)

    def idf(self, term: str) -> float:
        n = len(self.term_models.get(term, set()))
        return math.log((1 + self.model_count) / (1 + n)) + 1

    def weighted_match(self, terms: list[str]) -> float:
        return sum(self.idf(t) for t in terms)


def route_score(
    weighted_match: float,
    pos_win_rate: float | None,
    neg_failure_rate: float | None,
) -> float:
    """The v6 scoring function. Design records never contribute rates —
    models without measured rates use neutral priors (pos=1.0, neg=0.0 is
    NOT used: absence of evidence is not a win)."""
    p = pos_win_rate if pos_win_rate is not None else 0.5
    n = neg_failure_rate if neg_failure_rate is not None else 0.0
    return weighted_match * p - 0.5 * n
