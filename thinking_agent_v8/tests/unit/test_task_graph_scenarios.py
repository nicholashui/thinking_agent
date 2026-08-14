"""TaskGraph end-to-end scenario tests (Phase 3 exit gate).

Proves: graph runs end-to-end; every terminal path produces a valid packet;
the eight-state contract holds through the classifier.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.decision_packet import PacketValidator  # noqa: E402
from thinking_agent.domain.enums import TerminalStatus  # noqa: E402
from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from tests.helpers import Fixture, request_for, solved_scripts  # noqa: E402

APP = compile_task_graph().compile()


def run(scenario: str, fixture: Fixture, **meta):
    ctx = fixture.build()
    config = {"configurable": {"ctx": ctx}}
    result = APP.invoke(
        {"request": request_for(scenario, **meta), "thread_id": f"th-{scenario}"},
        config=config,
    )
    return result


def test_solved_end_to_end():
    fx = Fixture(scripts=solved_scripts("S1"))
    out = run("S1", fx)
    assert out["terminal_status"] == TerminalStatus.SOLVED.value, out.get("terminal_reason")
    packet = out["decision_packet"]
    assert packet["packet_id"]
    assert packet["terminal_status"] == "SOLVED"
    assert packet["packet_hash"]
    # packet validates (§15.3)
    from thinking_agent.domain.decision_packet import DecisionPacket
    problems = PacketValidator().validate(DecisionPacket.model_validate(packet))
    assert problems == [], problems
    # loop ran the full governed path
    assert out["frame"]["goal"].startswith("Decide")
    assert out["alternatives"]
    assert out["decision"]["selected_alternative_id"] == "alt-A"


def test_needs_evidence_when_diagnosis_finds_unfillable_gap():
    scripts = solved_scripts("S2")
    scripts["S2"]["DiagnosisResult"] = scripts["S2"]["DiagnosisResult"] | {
        "missing_evidence": [
            {"evidence_id": "g1", "description": "missing market data",
             "fillable": False},
        ],
    }
    fx = Fixture(scripts=scripts)
    out = run("S2", fx)
    assert out["terminal_status"] == TerminalStatus.NEEDS_EVIDENCE.value, out.get("terminal_reason")
    assert out["decision_packet"]["diagnosis"]["missing_evidence"]


def test_needs_experiment_when_safe_probe_available():
    scripts = solved_scripts("S3")
    scripts["S3"]["DiagnosisResult"] = scripts["S3"]["DiagnosisResult"] | {
        "probe_available": True,
        "probe_description": "cheap two-week measurement",
    }
    fx = Fixture(scripts=scripts)
    out = run("S3", fx)
    assert out["terminal_status"] == TerminalStatus.NEEDS_EXPERIMENT.value


def test_unsafe_on_replicate_tool():
    scripts = solved_scripts("S4")
    scripts["S4"]["AltSet"] = scripts["S4"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-R", "description": "replicate the agent",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["human approval required"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    out = run("S4", fx, tool="replicate", action_description="copy self")
    assert out["terminal_status"] == TerminalStatus.UNSAFE.value, out.get("terminal_reason")


def test_resource_limited_on_plateau():
    """No cognitive progress: identical state signature every loop → plateau."""
    scripts = solved_scripts("S5")
    scripts["S5"]["AltSet"] = AltSetForPlateau()  # alternatives never appear
    fx = Fixture(scripts=scripts)
    out = run("S5", fx)
    assert out["terminal_status"] in (
        TerminalStatus.RESOURCE_LIMITED.value,
        TerminalStatus.ESCALATED.value,
    ), out.get("terminal_status")


def AltSetForPlateau():
    # HOW gate repeatedly fails (no viable alternative) -> identical state
    # signature each pass -> novelty plateau -> RESOURCE_LIMITED
    from thinking_agent.domain.alternatives import AltSet
    return AltSet(alternatives=[]).model_dump()


def test_fast_path_e0_direct():
    """E0: direct internal answer, outcome verification, packet — no diagnosis."""
    scripts = solved_scripts("S6")
    fx = Fixture(scripts=scripts)
    out = run("S6", fx, effort="E0_DIRECT", direct=True)
    assert out["terminal_status"] == TerminalStatus.SOLVED.value
    assert out["route"]["effort_level"] == "E0_DIRECT"
    assert not out.get("hypotheses")  # diagnosis skipped


def test_approximated_on_bounded_error():
    """Selector records a bounded error → APPROXIMATED (no external action)."""
    scripts = solved_scripts("S7")
    scripts["S7"]["OutcomeVerification"] = scripts["S7"]["OutcomeVerification"] | {
        "success": False, "ambiguous": False,
    }
    fx = Fixture(scripts=scripts)
    out = run("S7", fx)
    assert out["terminal_status"] == TerminalStatus.APPROXIMATED.value, out.get("terminal_reason")


def test_infeasible_on_constraint_screen():
    """Generator declares infeasibility → INFEASIBLE via the constraint screen."""
    scripts = solved_scripts("S8")
    scripts["S8"]["AltSet"] = {
        "alternatives": [],
        "infeasible": True,
        "infeasibility_findings": ["constraints mutually inconsistent"],
    }
    fx = Fixture(scripts=scripts)
    out = run("S8", fx)
    assert out["terminal_status"] == TerminalStatus.INFEASIBLE.value, out.get("terminal_reason")


def test_needs_evidence_on_why_gate_budget():
    """WHY gate budget expired → NEEDS_EVIDENCE (impl §11.4)."""
    scripts = solved_scripts("S9")
    scripts["S9"]["DiagnosisResult"] = scripts["S9"]["DiagnosisResult"] | {
        "falsifications": [],  # G-WHY-5 can never pass
    }
    fx = Fixture(scripts=scripts)
    out = run("S9", fx)
    assert out["terminal_status"] == TerminalStatus.NEEDS_EVIDENCE.value, out.get("terminal_reason")


# ---------------- Phase 6: verification, safety, execution ----------------

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command


def _app_with_checkpointer():
    from thinking_agent.graphs.task_graph import compile_task_graph
    return compile_task_graph().compile(checkpointer=InMemorySaver())


def test_second_verifier_blocks_a3_with_single_identity():
    """A3 external action with only one verifier identity → reliability block
    → ESCALATED before any execution (impl §14.2, v5 V4)."""
    scripts = solved_scripts("S10")
    scripts["S10"]["AltSet"] = scripts["S10"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-X", "description": "write to external API",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["api credentials verified"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    # harness S28/S39 semantics: the scenario world-facts register only ONE
    # accepted identity, so the kernel-computed second-verifier rule blocks
    ctx = fx.build(policy_update={
        "verification": {"verifier_identities": [
            {"identity_id": "verifier-alpha", "model_id": "mock-verifier",
             "lineage": "primary", "accepted": True}]}})
    out = APP.invoke({"request": request_for("S10", tool="external_api_write"),
                      "thread_id": "th-S10"},
                     config={"configurable": {"ctx": ctx}})
    assert out["terminal_status"] == TerminalStatus.ESCALATED.value, out.get("terminal_reason")
    assert out["reliability_blocked"] is True
    assert not out.get("executed_actions")  # nothing executed


def test_human_approval_interrupt_and_resume():
    """A4 action → PENDING interrupt; resume('approve') completes the run."""
    scripts = solved_scripts("S11")
    scripts["S11"]["AltSet"] = scripts["S11"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-Y", "description": "send the email",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["recipient confirmed"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    app = _app_with_checkpointer()
    cfg = {"configurable": {"ctx": ctx, "thread_id": "th-S11"}}
    first = app.invoke({"request": request_for("S11", tool="send_email"), "thread_id": "th-S11"},
                       config=cfg)
    # paused on the human-approval interrupt
    interrupt_payload = None
    for task in app.get_state(cfg).tasks:
        interrupt_payload = task.interrupts[0].value
    assert interrupt_payload["kind"] == "human_approval"
    assert interrupt_payload["action_class"] == "A4"
    # resume with approval
    final = app.invoke(Command(resume="approve"), config=cfg)
    assert final["terminal_status"] == TerminalStatus.SOLVED.value, final.get("terminal_reason")
    assert final["authorization"]["status"] == "APPROVED"


def test_human_denial_escalates():
    scripts = solved_scripts("S12")
    scripts["S12"]["AltSet"] = scripts["S12"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-Z", "description": "send the email",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["recipient confirmed"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    app = _app_with_checkpointer()
    cfg = {"configurable": {"ctx": ctx, "thread_id": "th-S12"}}
    app.invoke({"request": request_for("S12", tool="send_email"), "thread_id": "th-S12"},
               config=cfg)
    final = app.invoke(Command(resume="deny"), config=cfg)
    assert final["terminal_status"] == TerminalStatus.ESCALATED.value
    assert "denied" in final["terminal_reason"]


def _echo_style_pass(complete=True):
    """Style-pass script that echoes the routed style and its contract:
    reads style_id + required_outputs from the message content."""
    import re
    from thinking_agent.domain.alternatives import StylePassResult

    def _script(messages):
        blob = str(messages)
        m = re.search(r"style_id['\"]?\s*[:=]\s*['\"]?([A-Za-z0-9_]+)", blob)
        sid = m.group(1) if m else "unknown"
        # required_outputs appears in the repr as a list of strings
        req = re.search(r"required_outputs['\"]?\s*[:=]\s*\[(.*?)\]", blob)
        outputs = []
        if req:
            outputs = [o.strip().strip("'").strip('"')
                       for o in req.group(1).split(",")
                       if o.strip().strip("'").strip('"')]
        claims = outputs if complete else (outputs[:1] if outputs else [])
        return StylePassResult(style_id=sid, style_name=sid, claims=claims,
                               summary="contract-complete pass" if complete else "partial",
                               contract_met=complete).model_dump()
    return _script


def test_style_pass_dispatch_with_contract_validation():
    """Phase 5 wiring: routed styles run as first-class passes through the
    contract validator; complete passes leave no curriculum items."""
    scripts = solved_scripts("SSTYLE")
    scripts["SSTYLE"]["StylePassResult"] = _echo_style_pass(complete=True)
    fx = Fixture(scripts=scripts)
    out = run("SSTYLE", fx)
    assert out["terminal_status"] == TerminalStatus.SOLVED.value
    assert out["style_results"], "style passes must be recorded"
    for r in out["style_results"]:
        assert r["contract_met"] is True, r["style_id"]
    assert out["divergence"]["curriculum_items"] == []
    assert out["structure_scan"]["required"] is True  # engineering signature


def test_style_pass_incomplete_becomes_curriculum_item():
    scripts = solved_scripts("SSTYLE2")
    scripts["SSTYLE2"]["StylePassResult"] = _echo_style_pass(complete=False)
    fx = Fixture(scripts=scripts)
    out = run("SSTYLE2", fx)
    assert any(not r["contract_met"] for r in out["style_results"])
    assert any("incomplete" in item for item in out["divergence"]["curriculum_items"])
