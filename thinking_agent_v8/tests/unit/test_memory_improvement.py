"""Phase 7 tests: memory contradiction + procedural authority; improvement
dedup + baseline-frozen evaluation."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.improvement.proposals import ImprovementEngine  # noqa: E402
from thinking_agent.memory.manager import MemoryManager  # noqa: E402


def test_procedural_lesson_quarantined_without_authority():
    mm = MemoryManager()
    out = mm.commit({"content": "always route to style X", "procedural": True,
                     "provenance": "self"})
    assert out["quarantined"] is True


def test_procedural_lesson_committed_with_authority():
    mm = MemoryManager()
    out = mm.commit({"content": "always route to style X", "procedural": True,
                     "provenance": "review"}, authority_token="tok-1",
                    authorized=True)
    assert out["quarantined"] is False


def test_contradicting_records_marked():
    mm = MemoryManager()
    mm.commit({"content": "the sky is never blue in this domain"})
    mm.commit({"content": "the sky is blue in this domain"})
    assert len(mm.conflicts()) >= 1


def test_improvement_dedup_and_unfrozen_skip():
    eng = ImprovementEngine(baseline_frozen=False)
    p1 = eng.propose("add scenario X")
    p2 = eng.propose("add scenario X")  # canonical dedup
    assert p1 is not None and p2 is None
    assert eng.queue_size() == 1
    assert eng.evaluate(p1, True, True) == "skip"


def test_improvement_retain_and_rollback():
    eng = ImprovementEngine(baseline_frozen=True)
    p = eng.propose("add scenario Y")
    assert eng.evaluate(p, True, True) == "retain"
    p2 = eng.propose("add scenario Z")
    assert eng.evaluate(p2, True, False) == "rollback"  # regression vs baseline


def test_r3_module_requires_review():
    eng = ImprovementEngine(baseline_frozen=True)
    p = eng.propose("install module M", risk_level="R3")
    assert eng.evaluate(p, True, True) == "pending_review"
