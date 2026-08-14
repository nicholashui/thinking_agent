"""S1–S45 1:1 graph-level port (impl §25.3).

Every legacy harness scenario, asserted against its v5-asserted terminal
state, driven through the LangGraph TaskGraph with scripted mocks per
producer. The mapping table is transcribed from the harness's own report
(spec/validation/harness.py, v5 column).

Producer keys:
  solved          default clean episode → SOLVED
  solved_e0       E0 fast path → SOLVED
  solved_gapfill  memory retrieval satisfies a fillable gap → SOLVED
  solved_warm     warm verifier: TWO identities satisfy the second-verifier
                  rule on an A3 action → SOLVED
  resource        unproductive HOW loop → plateau → RESOURCE_LIMITED
  needs_evidence  unfillable gap / gate expiry / ambiguous outcome → NEEDS_EVIDENCE
  needs_exper     safe probe → NEEDS_EXPERIMENT
  approximated    bounded error, outcome not success → APPROXIMATED
  infeasible      constraint screen → INFEASIBLE
  unsafe          replication / misattestation → UNSAFE
  escalated       human gate (timeout), second-verifier block, L3 outage,
                  owner unavailable → ESCALATED
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

import pytest  # noqa: E402
from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
from langgraph.types import Command  # noqa: E402

from thinking_agent.domain.alternatives import AltSet  # noqa: E402
from thinking_agent.domain.enums import TerminalStatus  # noqa: E402
from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from thinking_agent.providers.mock import MockModelAdapter  # noqa: E402
from tests.helpers import Fixture, request_for, solved_scripts  # noqa: E402

# (scenario, v5-asserted status, producer, meta)
SCENARIOS = [
    ("S1_trivial_arithmetic", "SOLVED", "solved", {}),
    ("S2_stuck_executor", "RESOURCE_LIMITED", "resource", {}),
    ("S3_reframe_oscillation", "SOLVED", "solved", {}),
    ("S4_high_stakes_clear", "ESCALATED", "escalated_human", {"tool": "send_email"}),
    ("S5_verifier_outage", "ESCALATED", "escalated_l3", {"tool": "external_api_write"}),
    ("S6_uncertain_outcome", "NEEDS_EVIDENCE", "needs_ambiguous", {}),
    ("S7_deterministic_solver", "SOLVED", "solved", {}),
    ("S8_injection_attempt", "SOLVED", "solved", {}),
    ("S9_budget_exhaustion", "RESOURCE_LIMITED", "resource", {}),
    ("S10_proposal_flood", "SOLVED", "solved", {}),
    ("S11_high_stakes_denied", "ESCALATED", "escalated_human", {"tool": "payment"}),
    ("S12_action_class_bypass", "UNSAFE", "unsafe_misattest", {"tool": "send_email"}),
    ("S13_red_team_catch", "SOLVED", "solved", {}),
    ("S14_memory_contradiction", "SOLVED", "solved", {}),
    ("S15_no_success_metrics", "NEEDS_EVIDENCE", "needs_what_gate", {}),
    ("S16_probe_available", "NEEDS_EXPERIMENT", "needs_exper", {}),
    ("S17_approximation_available", "APPROXIMATED", "approximated", {}),
    ("S18_infeasible", "INFEASIBLE", "infeasible", {}),
    ("S19_plan_stop_condition", "INFEASIBLE", "infeasible", {}),
    ("S20_pending_authorization", "ESCALATED", "escalated_human", {"tool": "send_email"}),
    ("S21_crash_resume", "SOLVED", "solved", {}),
    ("S22_competence_feedback", "SOLVED", "solved", {}),
    ("S23_council_minority", "SOLVED", "solved", {"council": True}),
    ("S24_calls_budget", "RESOURCE_LIMITED", "resource", {}),
    ("S25_l1_ladder", "NEEDS_EVIDENCE", "needs_ambiguous", {}),
    ("S26_warm_verifier", "SOLVED", "solved_warm", {"tool": "external_api_write"}),
    ("S27_history_calibration", "RESOURCE_LIMITED", "resource", {}),
    ("S28_a5_single_verifier", "ESCALATED", "escalated_second", {"tool": "external_api_write"}),
    ("S29_l3_ladder", "ESCALATED", "escalated_l3", {"tool": "external_api_write"}),
    ("S30_why_gate", "NEEDS_EVIDENCE", "needs_why_gate", {}),
    ("S31_escalation_condition", "ESCALATED", "escalated_human", {"tool": "send_email"}),
    ("S33_minted_procedure", "SOLVED", "solved", {}),
    ("S34_voi_gap_fillable", "SOLVED", "solved_gapfill", {}),
    ("S35_chaotic_crisis", "ESCALATED", "escalated_human",
     {"tool": "send_email", "effort": "E5_CHAOTIC_STABILIZE_FIRST", "chaotic": True}),
    ("S36_search_loop", "RESOURCE_LIMITED", "resource", {"search": True}),
    ("S37_fast_path_governance", "SOLVED", "solved_e0", {}),
    ("S38_allowlist_negative", "ESCALATED", "escalated_human", {"tool": "send_email"}),
    ("S39_second_verifier_blocks", "ESCALATED", "escalated_second",
     {"tool": "external_api_write"}),
    ("S40_real_retrieval", "SOLVED", "solved_gapfill", {}),
    ("S41_owner_unavailable", "ESCALATED", "escalated_owner", {}),
    ("S42_no_falsification", "NEEDS_EVIDENCE", "needs_why_gate", {}),
    ("S43_plateau_limited", "RESOURCE_LIMITED", "resource", {}),
    ("S44_replicate_denied", "UNSAFE", "unsafe_replicate", {"tool": "replicate"}),
    ("S45_competence_self_rating_rejected", "SOLVED", "solved",
     {"declared_accuracy": 1.0}),
]


def _scripts(producer: str, scenario: str) -> dict:
    scripts = solved_scripts(scenario)
    if producer == "solved" or producer == "solved_e0" or producer == "solved_gapfill":
        return scripts
    if producer == "resource":
        scripts[scenario]["AltSet"] = AltSet(alternatives=[]).model_dump()
        return scripts
    if producer in ("needs_what_gate",):
        scripts[scenario]["ProblemFrame"] = scripts[scenario]["ProblemFrame"] | {
            "goal": "", "owner": "", "success_metrics": [],
        }
        return scripts
    if producer == "needs_why_gate":
        scripts[scenario]["DiagnosisResult"] = scripts[scenario]["DiagnosisResult"] | {
            "falsifications": [],
        }
        return scripts
    if producer == "needs_ambiguous":
        scripts[scenario]["OutcomeVerification"] = scripts[scenario]["OutcomeVerification"] | {
            "success": False, "ambiguous": True,
        }
        return scripts
    if producer == "needs_exper":
        scripts[scenario]["DiagnosisResult"] = scripts[scenario]["DiagnosisResult"] | {
            "probe_available": True,
        }
        return scripts
    if producer == "approximated":
        scripts[scenario]["OutcomeVerification"] = scripts[scenario]["OutcomeVerification"] | {
            "success": False, "ambiguous": False,
        }
        return scripts
    if producer == "infeasible":
        scripts[scenario]["AltSet"] = {
            "alternatives": [], "infeasible": True,
            "infeasibility_findings": ["constraints mutually inconsistent"]}
        return scripts
    if producer == "unsafe_misattest":
        scripts[scenario]["ProblemFrame"] = scripts[scenario]["ProblemFrame"] | {
            "declared_action_class": "A1",  # planner under-classifies
        }
        # NOTE: fall through — the external alternative is injected below
    if producer == "escalated_owner":
        scripts[scenario]["ProblemFrame"] = scripts[scenario]["ProblemFrame"] | {
            "goal": "", "owner": "", "owner_unavailable": True,
        }
        return scripts
    # external-action producers need an external alternative
    external = {
        "alternatives": [
            {"alternative_id": "alt-X", "description": "external action",
             "requires_external_action": True, "expected_benefits": [],
             "expected_costs": [], "dependencies": ["precondition"]},
        ]
    }
    if producer in ("escalated_human", "escalated_second", "escalated_l3",
                    "unsafe_misattest", "unsafe_replicate", "solved_warm"):
        scripts[scenario]["AltSet"] = scripts[scenario]["AltSet"] | external
    return scripts


@pytest.mark.parametrize("scenario,expected,producer,meta", SCENARIOS,
                         ids=[s[0] for s in SCENARIOS])
def test_scenario_port(scenario, expected, producer, meta):
    scripts = _scripts(producer, scenario)
    policy_update: dict = {"pending_allowlist": ["t_readonly_fetch"]}
    if producer == "escalated_l3":
        policy_update["verification"] = {"verifier_outage": True}
    if producer == "escalated_second":
        # harness S28/S39: only ONE registered identity in the scenario
        # world facts → second-verifier rule blocks
        policy_update["verification"] = {"verifier_identities": [
            {"identity_id": "verifier-alpha", "model_id": "mock-verifier",
             "lineage": "primary", "accepted": True}]}
    fx = Fixture(scripts=scripts)
    ctx = fx.build(policy_update=policy_update)
    if producer == "solved_gapfill":
        # gap scripts are prepared BEFORE the run so the mock adapters hold
        # the fillable-gap diagnosis; memory is seeded pre-hypothesis
        scripts[scenario]["DiagnosisResult"] = scripts[scenario]["DiagnosisResult"] | {
            "missing_evidence": [{"evidence_id": "g1",
                                  "description": "market data for the decision",
                                  "fillable": True}],
        }
        ctx.models = {k: MockModelAdapter(k, scripts) for k in ctx.models}
        ctx.memory.commit({"content": "market data for the decision: verified",
                           "provenance": "corpus"})
    if producer == "solved_warm":
        # two verifier identities report on the same candidate
        from thinking_agent.domain.alternatives import CandidateVerificationReport
        state = {"calls": 0}

        def two_identities(messages):
            state["calls"] += 1
            cid = "alt-X"
            ident = "verifier-alpha" if state["calls"] == 1 else "verifier-beta"
            return CandidateVerificationReport(
                candidate_id=cid, verifier_identity=ident, verifier_kind="mock",
                success=True, logical_validity=1.0, evidence_adequacy=0.9,
                constraint_compliance=1.0, reliability=0.85,
                cache_key=f"k-{cid}-{ident}").model_dump()
        ctx.models["verifier"]._scripts[scenario]["CandidateVerificationReport"] = two_identities

    app = compile_task_graph().compile(checkpointer=InMemorySaver())
    cfg = {"configurable": {"ctx": ctx, "thread_id": f"th-{scenario}"}}
    meta = dict(meta)
    if producer == "unsafe_misattest":
        meta["declared_action_class"] = "A1"
    req = request_for(scenario, **meta)
    out = app.invoke({"request": req, "thread_id": f"th-{scenario}"}, config=cfg)

    if producer == "escalated_human":
        state = app.get_state(cfg)
        if any(t.interrupts for t in state.tasks):
            out = app.invoke(Command(resume="timeout"), config=cfg)

    assert out["terminal_status"] == expected, (
        f"{scenario}: expected {expected}, got {out.get('terminal_status')} "
        f"({out.get('terminal_reason')})")
