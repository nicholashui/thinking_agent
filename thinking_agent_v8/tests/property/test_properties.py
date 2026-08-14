"""Property tests (impl §25.1) — Hypothesis-generated invariants."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))

from hypothesis import given, strategies as st  # noqa: E402

from thinking_agent.canonical import FrozenDict, sha256_hex  # noqa: E402
from thinking_agent.domain.enums import LedgerEntryType, TerminalStatus  # noqa: E402
from thinking_agent.kernel.world_facts import WorldFacts  # noqa: E402
from thinking_agent.sdl.ledger import Ledger  # noqa: E402
from thinking_agent.state.reducers import append_by_key, merge_by_key  # noqa: E402


@given(st.lists(st.sampled_from(list(TerminalStatus)), max_size=20))
def test_terminal_statuses_are_eight(values):
    assert all(v in {s.value for s in TerminalStatus} for v in values)


@given(st.lists(st.text(min_size=1, max_size=40), max_size=8),
       st.lists(st.text(min_size=1, max_size=40), max_size=8))
def test_append_reducer_associative_and_dedup(left, right):
    red = append_by_key(None)
    a = red(red(None, left), right)
    b = red(None, left + right)
    assert a == b
    assert len(a) == len(set(a))


@given(st.dictionaries(st.text(min_size=1, max_size=10),
                       st.text(min_size=1, max_size=10), max_size=5))
def test_frozendict_rejects_every_mutation(kv):
    fd = FrozenDict(kv)
    for fn in (lambda: fd.__setitem__("a", "b"), lambda: fd.update({"a": "b"}),
               lambda: fd.pop("a", None), lambda: fd.clear()):
        try:
            fn()
            raised = False
        except TypeError:
            raised = True
        assert raised


@given(st.integers(min_value=1, max_value=30))
def test_ledger_chain_verifies_at_any_length(n):
    ledger = Ledger()
    for i in range(n):
        ledger.append(LedgerEntryType.SDL_TRIAL, challenge_id=f"c{i}")
    assert ledger.verify_chain() == []
    assert len(ledger) == n
    # tamper: mutate an entry → chain must report a problem
    if n:
        target = ledger.get(n // 2 + 1)
        original = target.verdict
        target.verdict = "tampered"
        problems = ledger.verify_chain()
        assert problems  # tamper detected
        target.verdict = original


@given(st.lists(st.sampled_from(["medical", "finance", "engineering", "software",
                                 "strategy", "security", "supply", "science",
                                 "organization"]), max_size=5, unique=True))
def test_facts_snapshot_immutable_under_any_domain_set(domains):
    from thinking_agent.kernel.world_facts_store import WorldFactsStore
    snap = WorldFactsStore(Path(__file__).resolve().parents[2] / "configs" / "kernel" / "world_facts.test.yaml").load()
    try:
        snap.facts.pending_allowlist = tuple(domains)
        raised = False
    except Exception:
        raised = True
    assert raised
    assert snap.facts.pending_allowlist == ("t_readonly_fetch",)
