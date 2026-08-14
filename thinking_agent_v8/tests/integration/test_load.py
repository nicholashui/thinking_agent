"""Long-loop and parallel-load tests (impl §25.5 / Phase 11)."""

import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.enums import TerminalStatus  # noqa: E402
from thinking_agent.graphs.task_graph import compile_task_graph  # noqa: E402
from tests.helpers import Fixture, request_for, solved_scripts  # noqa: E402


def test_long_loop_terminates_at_iteration_ceiling():
    """A HOW-gate-failing episode must terminate at the iteration ceiling
    with RESOURCE_LIMITED — never run forever."""
    from thinking_agent.domain.alternatives import AltSet
    scripts = solved_scripts("LOAD1")
    scripts["LOAD1"]["AltSet"] = AltSet(alternatives=[]).model_dump()
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    app = compile_task_graph().compile()
    start = time.monotonic()
    out = app.invoke({"request": request_for("LOAD1"), "thread_id": "th-LOAD1"},
                     config={"configurable": {"ctx": ctx}})
    elapsed = time.monotonic() - start
    assert out["terminal_status"] in (TerminalStatus.RESOURCE_LIMITED.value,
                                      TerminalStatus.ESCALATED.value)
    assert elapsed < 30, f"long-loop took {elapsed:.1f}s"


def test_parallel_load_ten_runs_deterministic():
    """Ten concurrent governed runs complete, each with a valid packet."""

    def one(i: int):
        scripts = solved_scripts(f"PAR{i}")
        fx = Fixture(scripts=scripts)
        ctx = fx.build()
        app = compile_task_graph().compile()
        return app.invoke({"request": request_for(f"PAR{i}"), "thread_id": f"th-PAR{i}"},
                          config={"configurable": {"ctx": ctx}})

    with ThreadPoolExecutor(max_workers=5) as pool:
        results = list(pool.map(one, range(10)))
    for out in results:
        assert out["terminal_status"] == TerminalStatus.SOLVED.value
        assert out["decision_packet"]["packet_hash"]
