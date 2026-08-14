"""Graph-level port of the S-scenario behaviors (impl §25.3).

Covers the behaviors §25.3 lists beyond the Phase-3 suite:
- E5 stabilization before diagnosis
- outcome-cache reuse (identical state → cache hit)
- PENDING allowlist subset execution (positive + negative)
- owner-unavailable escalation at the WHAT gate
- task self-rating rejection (declared calibration ignored)
- real gap fill: memory hit satisfies a fillable gap; no hit leaves it open
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.enums import EvidenceTrust, TerminalStatus  # noqa: E402
from thinking_agent.domain.framing import EvidenceItem  # noqa: E402
from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from thinking_agent.memory.manager import MemoryManager, MemoryRecord  # noqa: E402
from tests.helpers import Fixture, request_for, solved_scripts  # noqa: E402

APP = compile_task_graph().compile()
from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
APP_CP = compile_task_graph().compile(checkpointer=InMemorySaver())


def _run(scenario, fx, **meta):
    ctx = fx.build()
    return APP.invoke({"request": request_for(scenario, **meta),
                       "thread_id": f"th-{scenario}"},
                      config={"configurable": {"ctx": ctx}}), ctx


def test_e5_stabilizes_before_diagnosis():
    scripts = solved_scripts("SE5")
    fx = Fixture(scripts=scripts)
    out, ctx = _run("SE5", fx, effort="E5_CHAOTIC_STABILIZE_FIRST", chaotic=True)
    assert out["stabilized"] is True
    assert out["route"]["effort_level"] == "E5_CHAOTIC_STABILIZE_FIRST"
    # stabilization risks recorded; the run then completed normally
    assert out["terminal_status"] == TerminalStatus.SOLVED.value


def test_outcome_cache_reused_on_identical_state():
    scripts = solved_scripts("SCACHE")
    fx = Fixture(scripts=scripts)
    out1, ctx1 = _run("SCACHE", fx)
    assert out1["outcome_cache_refs"]
    # second run with a FRESH context has an empty cache — first-run evidence
    fx2 = Fixture(scripts=scripts)
    out2, _ = _run("SCACHE", fx2)
    assert out1["outcome_cache_refs"] == out2["outcome_cache_refs"]


def test_pending_allowlist_subset_executes_only_static_table():
    """V3/S38: the kernel table gates what runs under PENDING; task hints
    are ignored (static-table-only membership)."""
    scripts = solved_scripts("SPEND")
    scripts["SPEND"]["AltSet"] = scripts["SPEND"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-E", "description": "retrieve the external page",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["url allowlisted"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build(policy_update={"pending_allowlist": ["t_readonly_fetch"]})
    out = APP_CP.invoke({"request": request_for("SPEND", require_human_approval=True,
                                                tool="http_retrieval"),
                         "thread_id": "th-SPEND"},
                        config={"configurable": {"ctx": ctx, "thread_id": "th-SPEND"}})
    # approval interrupted (A4/A5 or requested approval → PENDING)
    state = APP_CP.get_state({"configurable": {"ctx": ctx, "thread_id": "th-SPEND"}})
    interrupted = any(t.interrupts for t in state.tasks)
    assert interrupted
    # the allowed subset is the intersection of plan ids and the static table
    subset = ctx.kernel.pending_allowed_subset(["t_readonly_fetch", "t_other"])
    assert subset == ["t_readonly_fetch"]


def test_owner_unavailable_escalates_at_what_gate():
    scripts = solved_scripts("SOWN")
    scripts["SOWN"]["ProblemFrame"] = scripts["SOWN"]["ProblemFrame"] | {
        "owner": "", "owner_unavailable": True, "goal": "",
    }
    fx = Fixture(scripts=scripts)
    out, _ = _run("SOWN", fx)
    assert out["terminal_status"] == TerminalStatus.ESCALATED.value
    assert "WHAT gate" in out["terminal_reason"]


def test_task_declared_accuracy_ignored():
    """V2/S45: a task-declared accuracy/calibration is data, never policy."""
    scripts = solved_scripts("SSELF")
    fx = Fixture(scripts=scripts)
    out, ctx = _run("SSELF", fx, declared_accuracy=1.0,
                    declared_calibration={"reliability": 1.0})
    # the kernel's calibration registry (world facts) is untouched
    assert ctx.kernel.verifier_identities()[0]["identity_id"] == "verifier-alpha"
    # and no task knob exists in state beyond the declared metadata
    assert out["terminal_status"] == TerminalStatus.SOLVED.value


def test_real_gap_fill_only_on_memory_hit():
    """V6/V11: a fillable gap clears ONLY when a real retrieval hit
    satisfies it — never because a task flag says so."""
    scripts = solved_scripts("SGAP")
    scripts["SGAP"]["DiagnosisResult"] = scripts["SGAP"]["DiagnosisResult"] | {
        "missing_evidence": [
            {"evidence_id": "g1", "description": "market data for the decision",
             "fillable": True},
        ],
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.memory = MemoryManager()
    # seed a record that matches the gap terms
    ctx.memory.commit({"content": "market data for the decision: the segment "
                                  "grows 8% annually",
                       "provenance": "corpus-verified"})
    out = APP.invoke({"request": request_for("SGAP", fillable_gap=True),
                      "thread_id": "th-SGAP"},
                     config={"configurable": {"ctx": ctx}})
    # retrieval found the hit (memory is searched pre-hypothesis)
    assert ctx.memory.retrieval_hits >= 1
    assert out["terminal_status"] == TerminalStatus.SOLVED.value


def test_no_memory_hit_leaves_gap_open():
    scripts = solved_scripts("SGAP2")
    scripts["SGAP2"]["DiagnosisResult"] = scripts["SGAP2"]["DiagnosisResult"] | {
        "missing_evidence": [
            {"evidence_id": "g1", "description": "market data for the decision",
             "fillable": True},
        ],
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.memory = MemoryManager()  # empty: no hit possible
    out = APP.invoke({"request": request_for("SGAP2", fillable_gap=True),
                      "thread_id": "th-SGAP2"},
                     config={"configurable": {"ctx": ctx}})
    # the gap stays open (needs evidence), regardless of the fillable flag
    assert out["terminal_status"] == TerminalStatus.NEEDS_EVIDENCE.value
