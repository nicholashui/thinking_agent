"""The learned style router (impl §13): IDF scoring, confidence gates,
mandatory protective modules, home-turf promotion, design-record isolation.

Design rules (invariant 12 / §13.2):
- DESIGN records never contribute pos_win_rate / neg_failure_rate.
- DESIGN records never create Gap Map entries.
- m101–m104 execute only under the counter-design canary (kernel fact).
"""

from pathlib import Path

from thinking_agent.domain.enums import RecordEvidenceStatus
from thinking_agent.domain.routing import (
    RoutingDecision,
    RoutingGateResult,
    RoutingRecord,
    StyleModel,
)
from thinking_agent.domain.task import SituationSignature
from thinking_agent.styles.idf import IDFWeights, route_score

DEFAULT_RECORDS_DIR = Path(__file__).resolve().parents[3] / "data" / "routing_records"

# mandatory protective modules (impl §13.5)
MANDATORY = {
    "adversarial": "m019",
    "one_shot": "m007",
    "high_stakes": "m007",
    "unmeasured": "m006",
    "guarantee": "m003",
    "maximize": "m019",
}

# home-turf promotion map (impl §13.8)
HOME_TURF = {
    "strategy": "m071",      # industry-structure decision → Five Forces
    "engineering": "m014",   # serial-flow constraint → Constraint Theory
    "supply": "m014",
    "medical": "m006",       # Bayesian test update
    "software": "m022",      # decision branches → Decision Tree
    "science": "m012",       # causal identification
}

COUNTER_MODELS = {"m101", "m102", "m103", "m104"}


class StyleRouter:
    def __init__(self, models: list[StyleModel], records: list[RoutingRecord],
                 kb_version: str = "v8-import"):
        self.models = {m.id: m for m in models}
        self.records = records
        self.idf = IDFWeights(models)
        self.kb_version = kb_version
        # precompute measured rates once (they change only via judge-pipeline
        # updates, which construct a new router) — removes 44k record scans
        # per route() call
        self._pos_rates = {m.id: self._compute_pos_win_rate(m) for m in models}
        self._neg_rates = {m.id: self._compute_neg_failure_rate(m) for m in models}

    # ---- rates (measured only) ----
    def pos_win_rate(self, model_id: str) -> float | None:
        return self._pos_rates.get(model_id)

    def neg_failure_rate(self, model_id: str) -> float | None:
        return self._neg_rates.get(model_id)

    def _compute_pos_win_rate(self, m: StyleModel) -> float | None:
        rel = [r for r in self.records
               if r.human_model == m.name
               and r.evidence_status == RecordEvidenceStatus.MEASURED]
        pos = [r for r in rel if r.case_type == "POS"]
        if not pos:
            return None
        wins = sum(1 for r in pos if r.outcome in ("human",))
        return wins / len(pos)

    def _compute_neg_failure_rate(self, m: StyleModel) -> float | None:
        rel = [r for r in self.records
               if r.human_model == m.name
               and r.evidence_status == RecordEvidenceStatus.MEASURED]
        neg = [r for r in rel if r.case_type == "NEG"]
        if not neg:
            return None
        fails = sum(1 for r in neg if r.outcome == "human")  # style lost on NEG = trap fired
        return fails / len(neg)

    # ---- routing ----
    def route(self, signature: SituationSignature) -> RoutingDecision:
        terms = (signature.domains + signature.goals + signature.context)
        scores: dict[str, dict[str, float]] = {}
        for m in self.models.values():
            wm = self.idf.weighted_match([t for t in terms if t in m.triggers])
            s = route_score(wm, self.pos_win_rate(m.id), self.neg_failure_rate(m.id))
            scores[m.id] = {"score": s, "weighted_match": wm}
        top = sorted(scores, key=lambda k: scores[k]["score"], reverse=True)

        gates: list[RoutingGateResult] = []
        top_styles = top[:3]
        if len(top) >= 2 and scores[top[0]]["score"] - scores[top[1]]["score"] <= 0.5:
            gates.append(RoutingGateResult(gate="G1", fired=True,
                                           detail="top1-top2 <= 0.5 → dual pass"))
        if scores[top[0]]["score"] <= 1.0:
            gates.append(RoutingGateResult(gate="G2", fired=True,
                                           detail="top1 <= 1.0 → general route + gates; "
                                                  "curriculum gap recorded"))

        # mandatory protective modules (context-driven)
        mandatory = [MANDATORY[c] for c in signature.context if c in MANDATORY]
        mandatory += [MANDATORY[g] for g in signature.goals if g in MANDATORY]
        mandatory = list(dict.fromkeys(mandatory))

        # home-turf promotion (rule 40): core-structure style runs first-class
        promotions = []
        for dom in signature.domains:
            if dom in HOME_TURF and HOME_TURF[dom] not in top_styles[:2]:
                promotions.append(HOME_TURF[dom])
        if promotions:
            gates.append(RoutingGateResult(gate="HOME_TURF", fired=True,
                                           detail=f"promoted {promotions}"))

        solo = (len(top) >= 2 and scores[top[0]]["score"] - scores[top[1]]["score"] > 0.5
                and signature.is_complete())

        return RoutingDecision(
            signature=signature,
            top_styles=top_styles,
            scores={k: v["score"] for k, v in scores.items()},
            score_components=scores,
            confidence_gate="CLEAR" if (len(top) >= 2 and scores[top[0]]["score"] - scores[top[1]]["score"] > 0.5) else "AMBIGUOUS",
            gates_fired=gates,
            mandatory_modules=mandatory,
            historical_refs=[],
            solo_contract_mode=solo,
            home_turf_promotions=promotions,
            routing_kb_version=self.kb_version,
        )

    def counters_canary_allowed(self, decision: RoutingDecision, kernel) -> bool:
        """m101–m104 execute only under the kernel canary (impl §13.10)."""
        if not kernel.sdl_enabled:
            return False
        return kernel._snapshot.facts.sdl.counter_design_canary_enabled and any(
            s in COUNTER_MODELS for s in decision.top_styles
        )


def load_routing_records(dir_path: Path | str | None = None) -> list[RoutingRecord]:
    import io
    import json

    d = Path(dir_path) if dir_path else DEFAULT_RECORDS_DIR
    out: list[RoutingRecord] = []
    for name in ("measured_records.jsonl", "design_records.jsonl"):
        p = d / name
        if not p.exists():
            continue
        for line in io.open(p, encoding="utf-8"):
            line = line.strip()
            if line:
                out.append(RoutingRecord.model_validate(json.loads(line)))
    return out
