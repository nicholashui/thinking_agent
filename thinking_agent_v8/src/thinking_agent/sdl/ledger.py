"""Learning Ledger (v8 §IV.6 / impl §18.11): append-only, hash-chained,
kernel-held write path (invariant 13).

Writers: the judge pipeline only (verdicts, calibration, corrections,
human-approved review reports). The task model has NO write credential —
`agent_append` does not exist; proposals go through `propose_*` which are
queued for the judge pipeline.
"""

import threading
from typing import Any

from thinking_agent.canonical import sha256_hex
from thinking_agent.domain.enums import LedgerEntryType
from thinking_agent.domain.sdl import LedgerEntry


class Ledger:
    def __init__(self):
        self._entries: dict[int, LedgerEntry] = {}
        self._lock = threading.Lock()
        self._hash_prev = ""  # genesis: empty previous hash

    def append(self, entry_type: LedgerEntryType, *, challenge_id: str = "",
               source: str = "", signature: Any = None, routed_styles: list[str] | None = None,
               verdict: str = "", dimensions: dict[str, float] | None = None,
               gap_delta: float = 0.0, lessons: list[str] | None = None,
               when_to_use_triggers: list[str] | None = None, plan_ref: str = "",
               supersedes_entry_id: str = "") -> LedgerEntry:
        """Judge-pipeline append (the ONLY writer). Atomic, monotonic."""
        with self._lock:
            seq = len(self._entries) + 1
            entry = LedgerEntry(
                sequence_number=seq,
                entry_id=f"entry-{seq:06d}",
                entry_type=entry_type,
                challenge_id=challenge_id,
                source=source,
                signature=signature,
                routed_styles=routed_styles or [],
                verdict=verdict,
                dimensions=dimensions or {},
                gap_delta=gap_delta,
                lessons=lessons or [],
                when_to_use_triggers=when_to_use_triggers or [],
                plan_ref=plan_ref,
                supersedes_entry_id=supersedes_entry_id,
                hash_prev=self._hash_prev,
            )
            entry.payload_hash = sha256_hex(self._payload(entry))
            entry.hash = sha256_hex(
                f"{entry.sequence_number}:{entry.entry_id}:{entry.hash_prev}:{entry.payload_hash}"
            )
            self._hash_prev = entry.hash
            self._entries[seq] = entry
            return entry

    @staticmethod
    def _payload(entry: LedgerEntry) -> dict[str, Any]:
        return {
            "entry_type": entry.entry_type.value,
            "challenge_id": entry.challenge_id,
            "source": entry.source,
            "signature": entry.signature.model_dump() if entry.signature else None,
            "routed_styles": entry.routed_styles,
            "verdict": entry.verdict,
            "dimensions": entry.dimensions,
            "gap_delta": entry.gap_delta,
            "lessons": entry.lessons,
            "when_to_use_triggers": entry.when_to_use_triggers,
            "plan_ref": entry.plan_ref,
            "supersedes_entry_id": entry.supersedes_entry_id,
            "timestamp": entry.timestamp.isoformat(),
        }

    def verify_chain(self) -> list[str]:
        """Integrity verification: recompute every hash; tamper = problem."""
        problems: list[str] = []
        prev = ""
        for seq in sorted(self._entries):
            e = self._entries[seq]
            if e.hash_prev != prev:
                problems.append(f"{e.entry_id}: broken prev-link")
            ph = sha256_hex(self._payload(e))
            h = sha256_hex(f"{e.sequence_number}:{e.entry_id}:{e.hash_prev}:{ph}")
            if h != e.hash:
                problems.append(f"{e.entry_id}: hash mismatch")
            prev = e.hash
        return problems

    def get(self, seq: int) -> LedgerEntry:
        return self._entries[seq]

    def __len__(self) -> int:
        return len(self._entries)

    def query(self, *, signature_domains: list[str] | None = None,
              entry_type: LedgerEntryType | None = None) -> list[LedgerEntry]:
        out = []
        for e in self._entries.values():
            if entry_type and e.entry_type != entry_type:
                continue
            if signature_domains:
                doms = set((e.signature.domains if e.signature else []))
                if not doms.intersection(signature_domains):
                    continue
            out.append(e)
        return out


class JudgePipeline:
    """The only component that holds the ledger write path. The task model
    never receives a Ledger instance; it receives this facade's propose-only
    surface or nothing at all."""

    def __init__(self, ledger: Ledger):
        self._ledger = ledger

    def record_verdict(self, **kw: Any) -> LedgerEntry:
        return self._ledger.append(LedgerEntryType.SDL_TRIAL, **kw)

    def record_correction(self, supersedes_entry_id: str, **kw: Any) -> LedgerEntry:
        return self._ledger.append(LedgerEntryType.CORRECTION,
                                   supersedes_entry_id=supersedes_entry_id, **kw)

    def record_plan_closeout(self, plan_ref: str, **kw: Any) -> LedgerEntry:
        """Plan closeout entry (impl §18.10 step 10) — judge pipeline write."""
        return self._ledger.append(LedgerEntryType.PLAN_CLOSEOUT, plan_ref=plan_ref, **kw)

    def record_review(self, approved: bool, **kw: Any) -> LedgerEntry:
        """Review reports append only after human approval (invariant 13)."""
        if not approved:
            raise PermissionError("review report requires human approval before append")
        return self._ledger.append(LedgerEntryType.REVIEW, **kw)
