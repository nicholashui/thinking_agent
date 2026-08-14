"""Gap Map (v8 §IV.3 / impl §18.6): verdict-derived weakness inventory.

Write policy: ONLY judge verdicts create or alter entries (invariant 11).
Design predictions never create entries (invariant 12). The review cycle
calculates refresh proposals but cannot apply them directly.
"""

from typing import Any

from thinking_agent.domain.enums import GapType
from thinking_agent.domain.sdl import GapMapEntry


class GapMap:
    def __init__(self):
        self._entries: dict[str, GapMapEntry] = {}

    def apply_verdict(self, *, signature: Any, gap_type: GapType, magnitude: float,
                      evidence_ref: str) -> GapMapEntry | None:
        """Verdict-derived write — the ONLY writer."""
        if magnitude <= 0:
            return None
        key = self._key(signature)
        existing = self._entries.get(key)
        if existing is None:
            entry = GapMapEntry(
                gap_id=f"gap-{len(self._entries) + 1:04d}",
                signature=signature, gap_type=gap_type, magnitude=magnitude,
                evidence_ref=evidence_ref,
            )
        else:
            entry = existing.model_copy(deep=True)
            entry.magnitude = magnitude
            entry.gap_type = gap_type
            entry.evidence_ref = evidence_ref
            entry.trend_last_three = (existing.trend_last_three + [existing.magnitude])[-3:]
        self._entries[key] = entry
        return entry

    def gap_weight(self, signature: Any) -> float:
        return self._entries.get(self._key(signature), GapMapEntry(
            gap_id="", gap_type=GapType.UNEXPLORED, magnitude=0.0)).magnitude

    def entries(self) -> list[GapMapEntry]:
        return list(self._entries.values())

    @staticmethod
    def _key(signature: Any) -> str:
        if signature is None:
            return "untyped"
        d = signature.model_dump() if hasattr(signature, "model_dump") else dict(signature)
        return "+".join(sorted(d.get("domains", []))) + "|" + "+".join(sorted(d.get("goals", [])))
