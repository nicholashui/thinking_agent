"""Tool Broker tests (impl §16): allowlist, idempotency, sanitation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.enums import ActionClass, AuthorizationStatus  # noqa: E402
from thinking_agent.tools.broker import ToolBroker, ToolSpec, builtin_tools  # noqa: E402


def _plan(tool_name, args, action_class="A1"):
    return {
        "plan_id": "p1",
        "tasks": [{
            "plan_task_id": "t1", "tool_name": tool_name, "arguments": args,
            "action_class": action_class, "idempotency_key": "task:p1:t1:1",
        }],
    }


def _auth(action_class="A1", status=AuthorizationStatus.APPROVED.value):
    return {"status": status, "action_class": action_class}


def test_calculator_arithmetic():
    broker = ToolBroker(builtin_tools())
    actions, obs = broker.execute_plan(_plan("calculator", {"expr": "2+3*4"}), _auth(), {}, None)
    assert actions[0]["success"] is True
    assert "14" in obs[0]["content_summary"]


def test_calculator_rejects_code():
    broker = ToolBroker(builtin_tools())
    actions, _ = broker.execute_plan(
        _plan("calculator", {"expr": "__import__('os').system('dir')"}), _auth(), {}, None)
    assert actions[0]["success"] is False  # AST whitelist rejected it


def test_idempotency_never_double_executes():
    calls = []

    def handler(query):
        calls.append(query)
        return f"hit:{query}"

    broker = ToolBroker({"lookup": ToolSpec(name="lookup", action_class=ActionClass.A1,
                                            handler=handler, allowed_args={"query"})})
    plan = _plan("lookup", {"query": "q1"})
    broker.execute_plan(plan, _auth(), {}, None)
    broker.execute_plan(plan, _auth(), {}, None)
    assert len(calls) == 1  # second execution returned the prior receipt


def test_unregistered_tool_never_executes():
    broker = ToolBroker(builtin_tools())
    actions, obs = broker.execute_plan(_plan("evil_tool", {}), _auth(), {}, None)
    assert actions == [] and obs == []


def test_token_class_below_required_blocks():
    broker = ToolBroker(builtin_tools())
    # http_retrieval is A2; an A1 token must not cover it
    actions, _ = broker.execute_plan(_plan("http_retrieval", {"url": "x"}), _auth("A1"), {}, None)
    assert actions == []


def test_compensation_runs_for_failed_a3_task():
    from thinking_agent.tools.broker import ToolBroker, ToolSpec
    from thinking_agent.tools.execution_monitor import ExecutionMonitor, run_compensation

    def fail_handler(**kw):
        raise ValueError("boom")

    def comp_handler(**kw):
        return "rolled-back"

    broker = ToolBroker({
        "risky": ToolSpec(name="risky", action_class=ActionClass.A3,
                          handler=fail_handler, allowed_args={"x"}),
        "rollback": ToolSpec(name="rollback", action_class=ActionClass.A3,
                             handler=comp_handler, allowed_args={}),
    })
    plan = {"plan_id": "p1", "tasks": [
        {"plan_task_id": "t1", "tool_name": "risky", "arguments": {"x": 1},
         "action_class": "A3", "idempotency_key": "task:p1:t1:1",
         "compensation_task_id": "t2"},
        {"plan_task_id": "t2", "tool_name": "rollback", "arguments": {},
         "action_class": "A3", "idempotency_key": "task:p1:t2:1"},
    ]}
    auth = {"status": "APPROVED", "action_class": "A3"}
    actions, _ = broker.execute_plan(plan, auth, {}, None)
    report = ExecutionMonitor().check(plan, actions, None)
    assert report.compensation_required is True
    comp = run_compensation(plan, actions, broker, auth, {}, None)
    assert comp and comp[0]["success"] is True
    assert comp[0]["compensation_for"] == "task:p1:t1:1"


def test_approval_timeout_resume_escalates():
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from thinking_agent.domain.enums import TerminalStatus
    from thinking_agent.graphs.task_graph import compile_task_graph
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.types import Command
    from tests.helpers import Fixture, request_for, solved_scripts

    scripts = solved_scripts("STIMEOUT")
    scripts["STIMEOUT"]["AltSet"] = scripts["STIMEOUT"]["AltSet"] | {
        "alternatives": [
            {"alternative_id": "alt-T", "description": "send the email",
             "requires_external_action": True, "expected_benefits": [], "expected_costs": [],
             "dependencies": ["recipient confirmed"]},
        ]
    }
    fx = Fixture(scripts=scripts)
    ctx = fx.build()
    app = compile_task_graph().compile(checkpointer=InMemorySaver())
    cfg = {"configurable": {"ctx": ctx, "thread_id": "th-STIMEOUT"}}
    app.invoke({"request": request_for("STIMEOUT", tool="send_email"),
                "thread_id": "th-STIMEOUT"}, config=cfg)
    final = app.invoke(Command(resume="timeout"), config=cfg)
    assert final["terminal_status"] == TerminalStatus.ESCALATED.value
    assert "timed out" in final["terminal_reason"]
