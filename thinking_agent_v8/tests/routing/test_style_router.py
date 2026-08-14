"""Phase 5 exit-gate tests: registry validation, design isolation, IDF routing,
mandatory modules, home-turf promotion, solo-contract detection."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.task import SituationSignature  # noqa: E402
from thinking_agent.styles.registry import StyleRegistry  # noqa: E402
from thinking_agent.styles.router import StyleRouter, load_routing_records  # noqa: E402
from thinking_agent.styles.contract_validator import (  # noqa: E402
    ContractValidator,
    EXPLICIT_CONTRACTS,
    contract_for,
)


def test_registry_loads_and_validates():
    reg = StyleRegistry.load()
    problems = reg.validate()
    assert problems == [], problems
    assert len(reg.all()) == 104


def test_records_load_216_with_4_design():
    records = load_routing_records()
    measured = [r for r in records if r.evidence_status == "MEASURED"]
    design = [r for r in records if r.evidence_status == "DESIGN"]
    assert len(measured) == 212, len(measured)
    assert len(design) == 4, len(design)


def test_design_records_never_change_rates():
    reg = StyleRegistry.load()
    records = load_routing_records()
    router = StyleRouter(reg.all(), records)
    # build an identical router from MEASURED-only records; rates must match
    measured_only = [r for r in records if r.evidence_status == "MEASURED"]
    router_m = StyleRouter(reg.all(), measured_only)
    for m in reg.all():
        assert router.pos_win_rate(m.id) == router_m.pos_win_rate(m.id)
        assert router.neg_failure_rate(m.id) == router_m.neg_failure_rate(m.id)


def test_mandatory_modules_activate_on_context():
    reg = StyleRegistry.load()
    router = StyleRouter(reg.all(), load_routing_records())
    sig = SituationSignature(domains=["finance"], goals=["guarantee"],
                             context=["adversarial", "unmeasured", "one_shot"])
    decision = router.route(sig)
    assert "m003" in decision.mandatory_modules  # guarantee → inversion
    assert "m019" in decision.mandatory_modules  # adversarial → red team
    assert "m006" in decision.mandatory_modules  # unmeasured → provenance
    assert "m007" in decision.mandatory_modules  # one_shot → ruin screen


def test_home_turf_promotion_on_strategy():
    reg = StyleRegistry.load()
    router = StyleRouter(reg.all(), load_routing_records())
    sig = SituationSignature(domains=["strategy"], goals=["decide"])
    decision = router.route(sig)
    # rule 40: industry-structure decision → Five Forces runs first-class
    assert "m071" in decision.home_turf_promotions, decision.home_turf_promotions


def test_solo_contract_detection():
    reg = StyleRegistry.load()
    router = StyleRouter(reg.all(), load_routing_records())
    sig = SituationSignature(domains=["medical"], goals=["diagnose", "predict"],
                             context=[], completeness_score=0.9)
    decision = router.route(sig)
    # solo-contract activates only when: gap > 0.5 AND signature complete
    top, second = decision.top_styles[0], decision.top_styles[1]
    gap = decision.scores[top] - decision.scores[second]
    if gap > 0.5:
        assert decision.solo_contract_mode is True


def test_explicit_contracts_cover_counter_models():
    for cid in ("m101", "m102", "m103", "m104"):
        assert cid in EXPLICIT_CONTRACTS, cid


def test_contract_validator_flags_incomplete_pass():
    from thinking_agent.domain.alternatives import StylePassResult
    validator = ContractValidator()
    result = StylePassResult(style_id="m101", claims=["prior_likelihood_posterior"])
    contract = EXPLICIT_CONTRACTS["m101"]
    out = validator.validate(result, contract)
    assert out.contract_met is False
    assert "independence_load_quantified" in out.contract_gaps
