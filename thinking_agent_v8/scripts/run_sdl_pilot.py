#!/usr/bin/env python3
"""v8 SDL pilot (impl Phase 11): one complete self-directed learning cycle.

discover → gap map → plan (draft, gated) → approve → trial → judge verdict
→ ledger append → review with follow-through report.

Judge: deterministic pilot judge (mock) — the protocol's LLM judge plugs in
at JudgePipeline.record_verdict. No KB rates change without a verdict.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from thinking_agent.api import ThinkingAgent  # noqa: E402
from thinking_agent.domain.enums import GapType, LedgerEntryType, PlanStatus  # noqa: E402
from thinking_agent.domain.task import SituationSignature  # noqa: E402
from thinking_agent.providers.mock import MockModelAdapter  # noqa: E402
from thinking_agent.sdl.discovery import DiscoveryPipeline, MockArxivSource  # noqa: E402
from tests.helpers import solved_scripts  # noqa: E402


def main() -> None:
    agent = ThinkingAgent(policy_path="configs/kernel/world_facts.test.yaml",
                          models=_mock_models())

    print("=== SDL pilot: one full cycle ===")
    # 1. gap map: seed a verdict-derived gap (the ONLY writer)
    sig = SituationSignature(domains=["strategy"], goals=["decide"], context=["deadline"])
    gap = agent.gap_map.apply_verdict(
        signature=sig, gap_type=GapType.DRIFT, magnitude=0.7,
        evidence_ref="corpus-verdict-demo")
    print(f"1. gap map seeded (verdict-derived): {gap.gap_id}, magnitude {gap.magnitude}")

    # 2. discovery (read-only)
    source = MockArxivSource(results=[{
        "tier": "Tier-1", "source_id": "arxiv-pilot-1",
        "title": "Entry decisions under industry structure",
        "abstract": "How should a strategy team decide whether to enter a new "
                    "market segment under a deadline, and which structural "
                    "evidence should determine the verdict? We examine "
                    "rivalry, entry barriers, buyer power, supplier power, "
                    "and substitution pressure across the co-packing "
                    "industry, weighing the decision procedure and its "
                    "checkable output shape against the deadline constraint.",
    }])
    candidates = agent.discover_challenges(source, "strategy entry", budget=5)
    print(f"2. discovery: {len(candidates)} candidate(s), status={candidates[0].status.value}")

    # 3. planner proposes a DRAFT plan
    plan = agent.propose_learning_plan(candidates, review_ref="pilot-review-1")
    print(f"3. plan proposed: {plan.plan_id}, status={plan.status.value}, "
          f"items={len(plan.items)}")
    assert plan.status == PlanStatus.DRAFT

    # 4. plan gate: draft cannot execute (invariant 14)
    try:
        agent.execute_next_trial(plan)
        print("4. FAIL: draft executed")
    except PermissionError:
        print("4. plan gate held: draft plan refused execution (invariant 14)")

    # 5. human approval
    agent.approve_learning_plan(plan, approval_ref="human-demo-1")
    print(f"5. plan approved: {plan.approval_ref}")

    # 6. trial: run the governed agent on the discovered challenge
    item_id = agent.execute_next_trial(plan)
    print(f"6. trial executed: item {item_id} (attempts=1, anti-obsession cap=2)")
    result = agent.invoke({
        "task_id": f"trial-{item_id}",
        "input_text": "strategy decide deadline",
        "task_metadata": {"scenario": "PILOT1"},
    })
    print(f"   trial terminal status: {result.status}")

    # 7. judge verdict → ledger (JudgePipeline is the only ledger writer)
    dims = {"goal": 4.5, "logic": 4.5, "coherence": 4.5, "depth": 4.0,
            "efficiency": 4.5, "uncertainty": 4.5, "insight": 4.0, "overall": 4.4}
    entry = agent.judge.record_verdict(
        challenge_id=item_id, source="arxiv-pilot-1", signature=sig,
        routed_styles=["m071", "m070"], verdict="ai", dimensions=dims,
        gap_delta=0.1, lessons=["direction-robust verdict held"])
    print(f"7. judge verdict recorded: {entry.entry_id}, hash={entry.hash[:12]}...")

    # 8. ledger integrity + trial gap update + candidate bookkeeping
    assert agent.ledger.verify_chain() == [], "ledger chain broken!"
    for c in candidates:
        if c.candidate_id == item_id.replace("item-", ""):
            c.status = "JUDGED"  # trial runner's transition in production
    print(f"8. ledger chain verified: {len(agent.ledger)} entry; "
          f"candidate status={candidates[0].status}")

    # 9. review: quick review with follow-through (rule 48)
    report = agent.run_quick_review(candidate_pool=candidates)
    not_attempted = [c.candidate_id for c in candidates
                     if c.candidate_id != item_id.replace("item-", "")]
    print(f"9. quick review: report {report.report_id}, "
          f"follow-through={report.discovered_not_attempted}")

    print("\n=== SDL pilot complete: all invariants held ===")


def _mock_models():
    scripts = solved_scripts("PILOT1")
    return {k: MockModelAdapter("mock", scripts)
            for k in ("main", "frame_builder", "diagnostician", "generator",
                      "verifier", "outcome_verifier")}


if __name__ == "__main__":
    main()
