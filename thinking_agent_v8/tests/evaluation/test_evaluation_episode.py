"""EvaluationEpisodeGraph tests (impl §18.10): judge → verdict-derived writes."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.task import SituationSignature  # noqa: E402
from thinking_agent.evaluation.judge import Judge, JudgeVerdict  # noqa: E402
from thinking_agent.graphs.evaluation_episode_graph import compile_evaluation_graph  # noqa: E402
from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from thinking_agent.providers.mock import MockModelAdapter  # noqa: E402
from tests.helpers import Fixture, solved_scripts  # noqa: E402


def _judge_scripts(overall: float = 4.8, confidence: float = 0.9):
    def _verdict(messages):
        return JudgeVerdict(
            dimensions={"Overall Quality": overall, "Goal Achievement": 5.0},
            winner="ai", confidence=confidence, judge_identity="judge-1",
        ).model_dump()
    return {"t-c-eval": {"JudgeVerdict": _verdict},
            "t-c-evalg": {"JudgeVerdict": _verdict}}


def _invoke(ctx, scenario, challenge, task_scenario):
    eval_graph = compile_evaluation_graph().compile()
    return eval_graph.invoke(
        {"task_request": {"task_id": f"t-{challenge}",
                          "input_text": "engineering supply decide",
                          "task_metadata": {"scenario": task_scenario}},
         "challenge_id": challenge, "source": "arxiv-x",
         "signature": SituationSignature(domains=["engineering"],
                                         goals=["decide"]).model_dump(),
         "routed_styles": ["m014"], "plan_ref": "plan-1"},
        config={"configurable": {"ctx": ctx,
                                 "task_graph": compile_task_graph().compile()}},
    )


def test_evaluation_episode_writes_verdict_derived():
    scripts = solved_scripts("EVALT")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.judge = Judge(MockModelAdapter("judge", _judge_scripts()), identity="judge-1")
    out = _invoke(ctx, "EVALJ", "c-eval", "EVALT")
    assert out["packet"]["terminal_status"] == "SOLVED"
    assert out["verdict"]["first"]["winner"] == "ai"
    assert out["ledger_entry_id"].startswith("entry-")
    assert ctx.ledger.verify_chain() == []


def test_evaluation_episode_gap_write_on_low_score():
    scripts = solved_scripts("EVALG")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.judge = Judge(MockModelAdapter("judge", _judge_scripts(overall=4.0)),
                      identity="judge-1")
    out = _invoke(ctx, "EVALG", "c-evalg", "EVALG")
    assert out["gap_update"].get("gap_id")  # verdict-derived gap write


def test_judge_failure_produces_no_writes():
    scripts = solved_scripts("EVALF")
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    ctx.judge = Judge(MockModelAdapter("judge", {}), identity="judge-1")  # no scripts
    out = _invoke(ctx, "EVALF", "c-evalf", "EVALF")
    assert out["judge_failed"] is True
    assert out["ledger_entry_id"] == ""
    assert len(ctx.ledger) == 0  # no learning writes on judge failure
