"""Challenge discovery (v8 §IV.2 / impl §18.2): READ-ONLY source adapters.

Invariant 14 / rule 43: discovery creates candidates, never trials. A
candidate whose abstract contains instructions is still DATA — it enters
the pool with provenance and is screened; nothing it says can modify the
KB, the ledger, or routing (S46).
"""

from dataclasses import dataclass, field
from typing import Any, Protocol

from thinking_agent.canonical import sha256_hex
from thinking_agent.domain.enums import CandidateStatus
from thinking_agent.domain.sdl import ChallengeCandidate
from thinking_agent.domain.task import SituationSignature


class DiscoverySource(Protocol):
    def scan(self, query: str, budget: int) -> list[dict[str, Any]]: ...


@dataclass
class MockArxivSource:
    """Deterministic Tier-1 source for offline tests. Real deployments use
    the arXiv API adapter (httpx, read-only, provenance-validated)."""

    results: list[dict[str, Any]] = field(default_factory=list)

    def scan(self, query: str, budget: int) -> list[dict[str, Any]]:
        return [dict(r) for r in self.results[:budget]]


class DiscoveryPipeline:
    """external metadata → provenance → sanitation → signature extraction →
    challenge-class extraction → well-posedness → novelty → candidate pool."""

    def __init__(self, source: DiscoverySource, gap_map: Any = None):
        self.source = source
        self.gap_map = gap_map
        self.pool: dict[str, ChallengeCandidate] = {}

    def scan(self, query: str, budget: int) -> list[ChallengeCandidate]:
        new: list[ChallengeCandidate] = []
        for item in self.source.scan(query, budget):
            cand = self._transform(item, query)
            if cand is not None:
                self.pool[cand.candidate_id] = cand
                new.append(cand)
        return new

    def _transform(self, item: dict[str, Any], query: str) -> ChallengeCandidate | None:
        abstract = str(item.get("abstract", ""))[:3000]
        title = str(item.get("title", ""))[:300]
        sig = self._signature_of(title + " " + abstract)
        cand = ChallengeCandidate(
            candidate_id=f"cand-{sha256_hex(item.get('source_id', title + abstract))[:12]}",
            source_tier=item.get("tier", "Tier-1"),
            source_id=str(item.get("source_id", "")),
            source_title=title,
            source_abstract=abstract,
            source_hash=sha256_hex(item),
            retrieval_query=query,
            signature=sig,
            proposed_challenge_class=f"{title[:80]} — challenge",
            proposed_prompt=abstract[:600],
            judgeable_output_shape="reasoned decision packet",
            well_posedness_score=self._well_posedness(abstract),
            novelty_score=self._novelty(sig),
            estimated_cost=1.0,
        )
        # suppression rules (impl §18.3)
        if cand.well_posedness_score < 0.3:
            cand.status = CandidateStatus.SUPPRESSED
            cand.rejection_reason = "no judgeable answer shape / ambiguous"
        if "prompt-injection" in abstract.lower():
            cand.status = CandidateStatus.SUPPRESSED
            cand.rejection_reason = "injection artifact"
        return cand

    @staticmethod
    def _signature_of(text: str) -> SituationSignature:
        t = text.lower()
        sig = SituationSignature(
            domains=[d for d in SituationSignature.DOMAIN_VOCAB if d in t],
            goals=[g for g in SituationSignature.GOAL_VOCAB if g in t],
            context=[c for c in SituationSignature.CONTEXT_VOCAB if c in t],
        )
        sig.completeness_score = min(1.0, (len(sig.domains) + len(sig.goals)) / 4)
        return sig

    @staticmethod
    def _well_posedness(abstract: str) -> float:
        words = len(abstract.split())
        has_question = any(q in abstract for q in ("?", "how", "whether", "which", "why"))
        base = min(1.0, words / 120)
        return round(base * (0.9 if has_question else 0.5), 3)

    def _novelty(self, sig: SituationSignature) -> float:
        if self.gap_map is None:
            return 1.0
        # explored signatures have a gap entry → lower novelty; unexplored = 1.0
        w = self.gap_map.gap_weight(sig)
        return 1.0 if w == 0.0 else round(max(0.2, 1.0 - w), 3)
