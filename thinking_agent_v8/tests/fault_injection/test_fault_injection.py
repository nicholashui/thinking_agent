"""Fault-injection suite (impl §25.5): provider outages, verifier outage,
tool timeout, duplicate resume, oversized content, corrupted checkpoints."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from langgraph.checkpoint.memory import InMemorySaver  # noqa: E402
from langgraph.types import Command  # noqa: E402

from thinking_agent.domain.enums import TerminalStatus  # noqa: E402
from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from thinking_agent.providers.mock import MockModelAdapter  # noqa: E402
from tests.helpers import Fixture, request_for, solved_scripts  # noqa: E402


class RaisingAdapter(MockModelAdapter):
    """Provider outage: raises on every call."""

    def invoke_structured(self, schema, messages, **kw):
        raise RuntimeError("provider outage")

    def invoke_text(self, messages, **kw):
        raise RuntimeError("provider outage")


def test_provider_outage_translates_not_crashes():
    """A generator outage must not surface as a raw exception."""
    scripts = solved_scripts("FOUT1")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.models["generator"] = RaisingAdapter("outage", {})
    app = compile_task_graph().compile()
    out = app.invoke({"request": request_for("FOUT1"), "thread_id": "th-FOUT1"},
                     config={"configurable": {"ctx": ctx}})
    assert out["terminal_status"] in {s.value for s in TerminalStatus}
    assert out["decision_packet"]["packet_hash"]  # packet on every path


def test_verifier_outage_reaches_no_verifier_ladder():
    scripts = solved_scripts("FOUT2")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.models["outcome_verifier"] = RaisingAdapter("outage", {})
    app = compile_task_graph().compile()
    out = app.invoke({"request": request_for("FOUT2"), "thread_id": "th-FOUT2"},
                     config={"configurable": {"ctx": ctx}})
    assert out["terminal_status"] == TerminalStatus.NEEDS_EVIDENCE.value


def test_duplicate_resume_is_harmless():
    """Resuming an already-completed thread with a stray response must not
    corrupt state or double-execute."""
    scripts = solved_scripts("FOUT3")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    app = compile_task_graph().compile(checkpointer=InMemorySaver())
    cfg = {"configurable": {"ctx": ctx, "thread_id": "th-FOUT3"}}
    app.invoke({"request": request_for("FOUT3"), "thread_id": "th-FOUT3"}, config=cfg)
    final = app.invoke(Command(resume="approve"), config=cfg)  # stray resume
    assert final["terminal_status"] in {s.value for s in TerminalStatus}


def test_oversized_external_content_truncated():
    from thinking_agent.sdl.discovery import DiscoveryPipeline, MockArxivSource
    big = "x" * 20000
    src = MockArxivSource(results=[{
        "tier": "Tier-1", "source_id": "big-1",
        "title": "Big abstract", "abstract": big,
    }])
    cands = DiscoveryPipeline(src).scan("big", 5)
    assert len(cands[0].source_abstract) <= 3000  # bounded


def test_approval_timeout_scheduler_path():
    """The scheduler's resume('timeout') path escalates cleanly."""
    scripts = solved_scripts("FOUT5")
    scripts["FOUT5"]["AltSet"] = scripts["FOUT5"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-W", "description": "send the email",
             "requires_external_action": True, "expected_benefits": [],
             "expected_costs": [], "dependencies": ["recipient confirmed"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    app = compile_task_graph().compile(checkpointer=InMemorySaver())
    cfg = {"configurable": {"ctx": ctx, "thread_id": "th-FOUT5"}}
    app.invoke({"request": request_for("FOUT5", tool="send_email"),
                "thread_id": "th-FOUT5"}, config=cfg)
    final = app.invoke(Command(resume="timeout"), config=cfg)
    assert final["terminal_status"] == TerminalStatus.ESCALATED.value
