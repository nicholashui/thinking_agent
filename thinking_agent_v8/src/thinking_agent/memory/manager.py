"""Memory Manager (impl §17): retrieval-before-hypotheses, contradiction
handling, procedural authority, quarantined writes.

Trust ladder: KERNEL > VERIFIED_EXTERNAL > MEMORY_TRUSTED >
MEMORY_UNVERIFIED > TOOL_UNTRUSTED > USER_DECLARED.
"""

from dataclasses import dataclass, field
from typing import Any

from thinking_agent.canonical import sha256_hex
from thinking_agent.domain.enums import EvidenceTrust
from thinking_agent.domain.framing import EvidenceItem

TRUST_RANK = {
    EvidenceTrust.USER_DECLARED: 0,
    EvidenceTrust.TOOL_UNTRUSTED: 1,
    EvidenceTrust.MEMORY_UNVERIFIED: 2,
    EvidenceTrust.MEMORY_TRUSTED: 3,
    EvidenceTrust.VERIFIED_EXTERNAL: 4,
    EvidenceTrust.KERNEL: 5,
}


@dataclass
class MemoryRecord:
    record_id: str
    content: str
    provenance: str = ""
    trust: EvidenceTrust = EvidenceTrust.MEMORY_UNVERIFIED
    procedural: bool = False
    authority_token: str = ""
    quarantined: bool = False
    when_to_use_triggers: list[str] = field(default_factory=list)
    content_hash: str = ""


class MemoryManager:
    def __init__(self, trust_margin: float = 0.1):
        self._records: dict[str, MemoryRecord] = {}
        self._conflicts: list[dict[str, Any]] = []
        self._trust_margin = trust_margin
        self.retrieval_hits = 0

    def retrieve(self, state: dict[str, Any], ctx: Any) -> list[EvidenceItem]:
        """Pre-hypothesis retrieval (impl §11.4): query terms from goal,
        domains, entities, constraints. Empty retrieval = deterministic no-op.
        Priced: each hit costs one cognitive unit (retrieval_hits)."""
        frame = state.get("frame") or {}
        sig = (state.get("preliminary_signature") or state.get("final_signature") or {})
        terms = [str(frame.get("goal", ""))]
        terms += [str(t) for t in (sig.get("domains") or [])]
        terms += [str(c) for c in (frame.get("constraints") or [])]
        return self.retrieve_for_terms(terms)

    def retrieve_for_terms(self, terms: list[str]) -> list[EvidenceItem]:
        """Term-based retrieval used both pre-hypothesis and for gap fill
        (the gap-fill query uses the EXACT gap description as its terms)."""
        hits: list[EvidenceItem] = []
        for rec in self._records.values():
            if rec.quarantined:
                continue
            hay = (rec.content + " " + " ".join(rec.when_to_use_triggers)).lower()
            if any(t and t.lower() in hay for t in terms if t):
                self.retrieval_hits += 1
                hits.append(EvidenceItem(
                    evidence_id=f"mem-{rec.record_id}",
                    content_summary=rec.content[:400],
                    source=rec.provenance,
                    source_type="memory",
                    trust=rec.trust,
                    content_hash=rec.content_hash or sha256_hex(rec.content),
                    metadata={"procedural": rec.procedural},
                ))
        return hits

    def commit(self, lesson: dict[str, Any], authority_token: str = "",
               authorized: bool = False) -> dict[str, Any]:
        """Governed commit (impl §17.4): contradiction rules, provenance,
        procedural authority, quarantine."""
        record = MemoryRecord(
            record_id=f"rec-{len(self._records) + 1:05d}",
            content=str(lesson.get("content", ""))[:2000],
            provenance=str(lesson.get("provenance", "")),
            trust=EvidenceTrust.MEMORY_UNVERIFIED,
            procedural=bool(lesson.get("procedural")),
            authority_token=authority_token,
            when_to_use_triggers=list(lesson.get("when_to_use_triggers") or []),
        )
        record.content_hash = sha256_hex(record.content)
        # contradiction: compare against the most recent window (perf bound —
        # O(1) per commit instead of O(n) over the full store)
        recent = list(self._records.values())[-50:]
        for existing in recent:
            if self._contradicts(existing, record):
                if TRUST_RANK[record.trust] >= TRUST_RANK[existing.trust] + self._trust_margin:
                    continue  # new dominates — keep both paths below
                self._conflicts.append({"a": existing.record_id, "b": record.record_id,
                                        "resolution": "both preserved; conflict marked"})
        if record.procedural and not authorized:
            record.quarantined = True
        self._records[record.record_id] = record
        return {"record_id": record.record_id, "quarantined": record.quarantined}

    def _contradicts(self, a: MemoryRecord, b: MemoryRecord) -> bool:
        # conservative heuristic: opposite-polarity claims sharing key tokens
        tokens_a = set(a.content.lower().split())
        tokens_b = set(b.content.lower().split())
        overlap = tokens_a & tokens_b
        if not overlap or len(overlap) < 3:
            return False
        neg_a = any(w in a.content.lower() for w in ("never", "not", "no "))
        neg_b = any(w in b.content.lower() for w in ("never", "not", "no "))
        return neg_a != neg_b

    def conflicts(self) -> list[dict[str, Any]]:
        return list(self._conflicts)

    def record_count(self) -> int:
        return len(self._records)
