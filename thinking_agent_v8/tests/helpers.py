"""Scenario fixtures: deterministic runtime context + scripted mock model.

One runtime context per scenario test; the mock adapter's scripts key on
(scenario, schema-name) so every cognitive call is deterministic.
"""

from dataclasses import dataclass, field
from typing import Any

from thinking_agent.domain.alternatives import (
    AltSet,
    Alternative,
    CandidateVerificationReport,
    Decision,
)
from thinking_agent.domain.enums import TerminalStatus
from thinking_agent.domain.framing import (
    DiagnosisResult,
    FalsificationRecord,
    Hypothesis,
    MissingEvidence,
    ProblemFrame,
)
from thinking_agent.domain.task import SituationSignature
from thinking_agent.domain.verification import OutcomeVerification
from thinking_agent.kernel.authority_tokens import AuthorityTokenStore
from thinking_agent.kernel.safety_kernel import SafetyKernel
from thinking_agent.kernel.world_facts_store import WorldFactsStore
from thinking_agent.observability.audit import AuditService
from thinking_agent.providers.mock import MockModelAdapter
from thinking_agent.runtime.context import RuntimeContext, SystemClock

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TEST_POLICY = REPO_ROOT / "configs" / "kernel" / "world_facts.test.yaml"


@dataclass
class Fixture:
    ctx: RuntimeContext = field(default_factory=lambda: None)
    scripts: dict[str, Any] = field(default_factory=dict)

    def build(self, policy_update: dict | None = None) -> RuntimeContext:
        snapshot = WorldFactsStore(TEST_POLICY).load()
        if policy_update:
            # frozen models: policy changes are new instances, never
            # mutations — merged through WorldFacts validation so sub-model
            # fields (VerificationFacts etc.) are re-validated, not raw dicts
            from thinking_agent.kernel.world_facts import WorldFacts, _deep_freeze
            facts_dict = snapshot.facts.model_dump()
            facts_dict.update(_deep_freeze(policy_update))
            snapshot = snapshot.model_copy(update={
                "facts": WorldFacts.model_validate(facts_dict)})
        kernel = SafetyKernel(snapshot, AuthorityTokenStore())
        from thinking_agent.memory.manager import MemoryManager
        from thinking_agent.tools.broker import ToolBroker, builtin_tools
        from thinking_agent.styles.registry import StyleRegistry
        from thinking_agent.styles.router import StyleRouter, load_routing_records
        from thinking_agent.sdl.ledger import JudgePipeline, Ledger
        from thinking_agent.sdl.gap_map import GapMap
        ledger = Ledger()
        ctx = RuntimeContext(
            world_facts=snapshot,
            kernel=kernel,
            ledger=ledger,
            judge_pipeline=JudgePipeline(ledger),
            gap_map=GapMap(),
            memory=MemoryManager(),  # production parity (api.py)
            style_router=StyleRouter(StyleRegistry.load().all(),
                                     load_routing_records()),
            models={"main": MockModelAdapter("mock-main", self.scripts),
                    "frame_builder": MockModelAdapter("mock-frame", self.scripts),
                    "diagnostician": MockModelAdapter("mock-diag", self.scripts),
                    "generator": MockModelAdapter("mock-gen", self.scripts),
                    "verifier": MockModelAdapter("mock-verifier", self.scripts),
                    "outcome_verifier": MockModelAdapter("mock-outcome", self.scripts)},
            tools=ToolBroker(builtin_tools()),  # production parity (api.py)
            audit=AuditService(policy_version=snapshot.version),
            verification_cache={},
            clock=SystemClock(),
        )
        self.ctx = ctx
        return ctx


def solved_scripts(scenario: str = "S1") -> dict[str, Any]:
    """Scripts for a clean end-to-end SOLVED episode."""
    return {
        scenario: {
            "ProblemFrame": ProblemFrame(
                goal="Decide whether to fund program A",
                owner="eng-owner",
                stakeholders=["eng"],
                success_metrics=["throughput >= 90/hr within budget"],
                constraints=["budget $200k", "deadline 12 weeks"],
                permissions=["read-only analysis"],
                scope="one production line",
                stakes="medium",
                ambiguities=[],
                assumptions=["rates constant"],
            ).model_dump(),
            "DiagnosisResult": DiagnosisResult(
                hypotheses=[
                    Hypothesis(hypothesis_id="h1", statement="S2 binds throughput",
                                falsification_condition="WIP signature elsewhere",
                                estimated_probability=0.9,
                                supporting_evidence_ids=["e1"]),
                ],
                missing_evidence=[],
                falsifications=[
                    FalsificationRecord(claim_id="h1", falsifier="WIP only at S2 input",
                                        outcome="SURVIVED"),
                ],
                residual_uncertainty="low: arithmetic checkable",
                probe_available=False,
            ).model_dump(),
            "AltSet": AltSet(
                alternatives=[
                    Alternative(alternative_id="alt-A", description="Fund program A only",
                                expected_benefits=["throughput 100/hr"],
                                expected_costs=["$200k"],
                                risks=["training slip"],
                                failure_branch="S3 caps at 100/hr — priced",
                                requires_external_action=False),
                ]
            ).model_dump(),
            "CandidateVerificationReport": _echo_verifier_report(),
            "OutcomeVerification": OutcomeVerification(
                success=True, reliability=0.85, external_identity_present=True,
                second_verifier_satisfied=True, class_bar=0.7,
                reliability_blocked=False, ambiguous=False,
                findings=["goal satisfied"],
            ).model_dump(),
        }
    }




def _echo_verifier_report():
    """Verifier script that echoes the candidate under verification — so
    selection always binds the report to the alternative it verified."""
    import re

    def _script(messages):
        blob = str(messages)
        m = re.search(r"candidate[\"']?\s*[:=]\s*['\"]?([A-Za-z0-9_\-]+)", blob)
        cid = m.group(1) if m else "unknown"
        return CandidateVerificationReport(
            candidate_id=cid, verifier_identity="verifier-alpha",
            verifier_kind="mock", success=True, logical_validity=1.0,
            evidence_adequacy=0.9, constraint_compliance=1.0, reliability=0.85,
            findings=[], cache_key=f"k-{cid}",
        ).model_dump()
    return _script


def request_for(scenario: str, **meta: Any) -> dict[str, Any]:
    m = dict(meta)
    m.setdefault("scenario", scenario)
    return {
        "task_id": f"t-{scenario}",
        "input_text": meta.get("input_text", "engineering supply: decide diagnose deadline"),
        "task_metadata": m,
    }
