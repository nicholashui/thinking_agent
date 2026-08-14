#!/usr/bin/env python3
"""Cost / latency measurement (impl Phase 11): per-terminal-state scenario
matrix — status, wall time, cognitive-call count, token estimate, cache hits.

Runs the deterministic mock scenarios; live-provider measurement swaps the
mock adapters for OpenAICompatibleAdapter instances (same matrix, real cost).
"""

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from tests.helpers import Fixture, request_for, solved_scripts  # noqa: E402

SCENARIOS = ["SOLVED1", "GAP1", "PROBE1", "PLATEAU1"]


def run_one(name: str, fx: Fixture, meta: dict) -> dict:
    ctx = fx.build()
    app = compile_task_graph().compile()
    start = time.monotonic()
    out = app.invoke({"request": request_for(name, **meta), "thread_id": f"th-{name}"},
                     config={"configurable": {"ctx": ctx}})
    return {
        "status": out.get("terminal_status"),
        "wall_ms": round((time.monotonic() - start) * 1000, 1),
        "iterations": (out.get("loop_status") or {}).get("iteration", 0),
        "cognitive_calls": (out.get("budget_snapshot") or {}).get("cognitive_calls_used", 0),
        "bookkeeping": (out.get("budget_snapshot") or {}).get("bookkeeping_calls", 0),
        "outcome_cache_refs": len(out.get("outcome_cache_refs") or []),
    }


def main() -> None:
    from thinking_agent.domain.alternatives import AltSet
    print("scenario | status | wall_ms | iterations | cognitive | bookkeeping | cache")
    # solved
    fx = Fixture(scripts=solved_scripts("SOLVED1"))
    print(run_one("SOLVED1", fx, {}))
    # needs-evidence (unfillable gap)
    scripts = solved_scripts("GAP1")
    scripts["GAP1"]["DiagnosisResult"] = scripts["GAP1"]["DiagnosisResult"] | {
        "missing_evidence": [{"evidence_id": "g1", "description": "missing data",
                              "fillable": False}]}
    print(run_one("GAP1", Fixture(scripts=scripts), {}))
    # needs-experiment (probe)
    scripts = solved_scripts("PROBE1")
    scripts["PROBE1"]["DiagnosisResult"] = scripts["PROBE1"]["DiagnosisResult"] | {
        "probe_available": True}
    print(run_one("PROBE1", Fixture(scripts=scripts), {}))
    # resource-limited (plateau)
    scripts = solved_scripts("PLATEAU1")
    scripts["PLATEAU1"]["AltSet"] = AltSet(alternatives=[]).model_dump()
    print(run_one("PLATEAU1", Fixture(scripts=scripts), {}))


if __name__ == "__main__":
    main()
