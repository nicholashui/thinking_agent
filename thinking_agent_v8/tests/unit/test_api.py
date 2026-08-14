"""Public API tests (impl §21): ThinkingAgent facade end-to-end."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.api import ThinkingAgent  # noqa: E402
from thinking_agent.domain.enums import PlanStatus  # noqa: E402
from thinking_agent.providers.mock import MockModelAdapter  # noqa: E402
from tests.helpers import solved_scripts  # noqa: E402


def test_api_invoke_end_to_end():
    scripts = solved_scripts("API1")
    agent = ThinkingAgent(
        policy_path=str(Path(__file__).resolve().parents[2] / "configs" / "kernel" / "world_facts.test.yaml"),
        models={"main": MockModelAdapter("mock", scripts),
                "frame_builder": MockModelAdapter("mock", scripts),
                "diagnostician": MockModelAdapter("mock", scripts),
                "generator": MockModelAdapter("mock", scripts),
                "verifier": MockModelAdapter("mock", scripts),
                "outcome_verifier": MockModelAdapter("mock", scripts)},
    )
    result = agent.invoke({"task_id": "t-api", "input_text": "engineering supply decide",
                           "task_metadata": {"scenario": "API1"}})
    assert result.status == "SOLVED"
    assert result.decision_packet.packet_id == "pkt-t-api"
    assert result.decision_packet.packet_hash


def test_api_sdl_plan_gate():
    agent = ThinkingAgent(policy_path=str(Path(__file__).resolve().parents[2] / "configs" / "kernel" / "world_facts.test.yaml"))
    plan = agent.propose_learning_plan([])
    assert plan.status == PlanStatus.DRAFT
    try:
        agent.execute_next_trial(plan)
        raised = False
    except PermissionError:
        raised = True
    assert raised  # invariant 14
    agent.approve_learning_plan(plan, "human-1")
    assert agent.execute_next_trial(plan) == "plan-closed"


def test_api_ledger_verify_chain():
    agent = ThinkingAgent(policy_path=str(Path(__file__).resolve().parents[2] / "configs" / "kernel" / "world_facts.test.yaml"))
    agent.judge.record_verdict(challenge_id="c1", verdict="ai")
    agent.judge.record_verdict(challenge_id="c2", verdict="ai")
    assert agent.ledger.verify_chain() == []


def test_langsmith_metadata_env_gated(monkeypatch):
    from thinking_agent.observability.tracing import langsmith_enabled, run_metadata
    monkeypatch.delenv("LANGSMITH_TRACING", raising=False)
    monkeypatch.delenv("LANGSMITH_API_KEY", raising=False)
    assert langsmith_enabled() is False  # off by default — no data leaves
    monkeypatch.setenv("LANGSMITH_TRACING", "true")
    monkeypatch.setenv("LANGSMITH_API_KEY", "test-key")
    assert langsmith_enabled() is True
    meta = run_metadata("t-1", "th-1", "test-1")
    assert meta["task_id"] == "t-1"
    assert meta["world_facts_version"] == "test-1"
    # the audit surface contains no chain-of-thought fields
    assert "chain_of_thought" not in meta
