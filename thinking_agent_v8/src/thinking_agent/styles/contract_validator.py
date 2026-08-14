"""Style completion contracts (impl §13.6 / v6 §II.2.9).

A style pass that does not produce its mandatory outputs has not run.
The 12 explicit typed contracts below are the corpus-derived ones; every
other style gets a generic contract from its strengths/weaknesses.
"""

from thinking_agent.domain.alternatives import StylePassResult

EXPLICIT_CONTRACTS: dict[str, dict[str, object]] = {
    "m003": {"outputs": ["failure_categories>=6", "ranked_likelihood_impact",
                         "unmitigable_residual", "never_always_reframing"]},
    "m006": {"outputs": ["likelihood_scenarios>=3", "posterior_range",
                         "decision_threshold_flip", "artifact_in_packet"]},
    "m007": {"outputs": ["full_outcome_distribution", "ruin_check", "one_shot_check",
                         "floor_or_kelly", "probability_provenance"]},
    "m011": {"outputs": ["stocks_flows_loops", "falsifying_observable",
                         "local_data_first", "cheap_fix_as_experiment"]},
    "m019": {"outputs": ["exploit_vectors", "quantified_exposure",
                         "unconsulted_stakeholders", "baseline_risk_comparison"]},
    "m022": {"outputs": ["all_branches_priced", "negative_branch_priced",
                         "probability_sensitivity"]},
    "m033": {"outputs": ["intervention", "control", "randomization", "blinding",
                         "exact_outcome_measure"]},
    "m097": {"outputs": ["reference_class_named", "base_rate_distribution",
                         "inside_outside_separated"]},
    "m101": {"outputs": ["prior_likelihood_posterior", "independence_load_quantified",
                         "order_invariance", "flip_prior"]},
    "m102": {"outputs": ["unmeasured_quantity_named", "likelihood_scenarios>=3",
                         "specificity_floor", "sae_ledger"]},
    "m103": {"outputs": ["binding_constraint", "exploit_before_elevate",
                         "forced_lift_chain", "bundle_interpretation_priced"]},
    "m104": {"outputs": ["five_forces_evidence", "aggregate_verdict",
                         "direction_robust_reading", "redeploy_opportunity_cost"]},
}


def contract_for(style_id: str, style_name: str, strengths: list[str],
                 weaknesses: list[str]) -> dict[str, object]:
    if style_id in EXPLICIT_CONTRACTS:
        return EXPLICIT_CONTRACTS[style_id]
    return {
        "outputs": [f"demonstrated:{s}" for s in strengths],
        "trap_checklist": [f"gate-checked:{w}" for w in weaknesses],
        "generic": True,
    }


class ContractValidator:
    """Validates a StylePassResult against its completion contract.

    The mock/model-driven pass reports which contract outputs it produced;
    a pass missing any mandatory output is INCOMPLETE (impl §13.6: recorded
    as incomplete, general route governs)."""

    def validate(self, result: StylePassResult,
                 contract: dict[str, object]) -> StylePassResult:
        required = [str(o).split(":")[-1] for o in contract.get("outputs", [])]
        produced = set(result.claims)
        gaps = [o for o in required
                if o not in produced
                and not any(p == o or p.endswith(":" + o) or p.endswith(o)
                           for p in produced)]
        result.contract_met = not gaps
        result.contract_gaps = gaps
        return result
