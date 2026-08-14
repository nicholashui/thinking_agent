"""EvaluationEpisodeGraph (impl §18.10): task → external judge → verdict-
derived writes (ledger append + gap-map update) → plan closeout.

Authority: the JUDGE pipeline writes; the task model never does. A judge
failure leaves the trial unjudged and produces NO learning writes (§23.1).
"""

from typing import Any, TypedDict

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph


class EvalState(TypedDict, total=False):
    task_request: dict[str, Any]
    packet: dict[str, Any]
    human_packet: dict[str, Any]
    human_overall: float
    challenge_id: str
    source: str
    signature: dict[str, Any]
    routed_styles: list[str]
    plan_ref: str
    verdict: dict[str, Any]
    ledger_entry_id: str
    gap_update: dict[str, Any]
    judge_failed: bool


def run_task(state: EvalState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    task_graph = config["configurable"]["task_graph"]
    result = task_graph.invoke({"request": state["task_request"],
                                "thread_id": f"th-{state.get('challenge_id', 'trial')}"},
                               config={"configurable": {"ctx": ctx}})
    return {"packet": result.get("decision_packet", {})}


def judge_episode(state: EvalState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    judge = ctx.judge
    try:
        result = judge.adjudicate(state.get("packet") or {},
                                  state.get("human_packet"),
                                  state.get("human_overall"))
    except Exception as exc:  # judge failure → no learning writes
        return {"judge_failed": True, "verdict": {"error": str(exc)}}
    return {"verdict": result}


def write_verdict_derived(state: EvalState, *, config: RunnableConfig) -> dict[str, Any]:
    """The ONLY learning-write path: judge pipeline → ledger + gap map."""
    if state.get("judge_failed"):
        return {"ledger_entry_id": "", "gap_update": {}}
    ctx = config["configurable"]["ctx"]
    verdict = (state.get("verdict") or {}).get("first") or {}
    dims = verdict.get("dimensions", {})
    entry = ctx.judge_pipeline.record_verdict(
        challenge_id=state.get("challenge_id", ""),
        source=state.get("source", ""),
        signature=state.get("signature"),
        routed_styles=state.get("routed_styles", []),
        verdict=verdict.get("winner", "ai"),
        dimensions=dims,
        gap_delta=0.0,
        lessons=[verdict.get("learning_signal") or "",
                 verdict.get("suggested_improvement") or ""],
        plan_ref=state.get("plan_ref", ""),
    )
    gap_update = {}
    overall = dims.get("Overall Quality")
    if overall is not None and overall < 4.3:
        # dimension-gap signal: verdict-derived gap-map write (FR-2)
        g = ctx.gap_map.apply_verdict(
            signature=state.get("signature"),
            gap_type="dimension_gap",
            magnitude=round(4.3 - overall, 3),
            evidence_ref=entry.entry_id,
        )
        if g is not None:
            gap_update = {"gap_id": g.gap_id, "magnitude": g.magnitude}
    return {"ledger_entry_id": entry.entry_id, "gap_update": gap_update}


def compile_evaluation_graph() -> StateGraph:
    g = StateGraph(EvalState)
    g.add_node("run_task", run_task)
    g.add_node("judge_episode", judge_episode)
    g.add_node("write_verdict_derived", write_verdict_derived)
    g.add_edge(START, "run_task")
    g.add_edge("run_task", "judge_episode")
    g.add_edge("judge_episode", "write_verdict_derived")
    g.add_edge("write_verdict_derived", END)
    return g
