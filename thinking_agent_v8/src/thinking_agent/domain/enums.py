"""All public enums (impl plan §8.2). Values are normative."""

from enum import StrEnum


class TerminalStatus(StrEnum):
    """The eight — and only eight — public terminal states (§1.3)."""

    SOLVED = "SOLVED"
    APPROXIMATED = "APPROXIMATED"
    NEEDS_EVIDENCE = "NEEDS_EVIDENCE"
    NEEDS_EXPERIMENT = "NEEDS_EXPERIMENT"
    INFEASIBLE = "INFEASIBLE"
    UNSAFE = "UNSAFE"
    ESCALATED = "ESCALATED"
    RESOURCE_LIMITED = "RESOURCE_LIMITED"


class Stage(StrEnum):
    BOOTSTRAP = "BOOTSTRAP"
    META = "META"
    WHAT = "WHAT"
    WHY = "WHY"
    HOW = "HOW"
    DO = "DO"
    VERIFY = "VERIFY"
    REVIEW = "REVIEW"
    EPILOGUE = "EPILOGUE"
    TERMINAL = "TERMINAL"


class EffortLevel(StrEnum):
    E0_DIRECT = "E0_DIRECT"
    E1_DIRECT_WITH_REVIEW = "E1_DIRECT_WITH_REVIEW"
    E2_STRUCTURED = "E2_STRUCTURED"
    E3_DEEP = "E3_DEEP"
    E4_COUNCIL_OR_SEARCH = "E4_COUNCIL_OR_SEARCH"
    E5_CHAOTIC_STABILIZE_FIRST = "E5_CHAOTIC_STABILIZE_FIRST"


class ActionClass(StrEnum):
    A1 = "A1"  # informational / internal-only
    A2 = "A2"  # low-impact, reversible external
    A3 = "A3"  # material external
    A4 = "A4"  # high-impact / regulated / financial
    A5 = "A5"  # critical / irreversible / unknown

    @classmethod
    def default_unknown(cls) -> "ActionClass":
        return cls.A5


class AuthorizationStatus(StrEnum):
    APPROVED = "APPROVED"
    PENDING = "PENDING"
    DENIED_UNSAFE = "DENIED_UNSAFE"
    DENIED_ESCALATE = "DENIED_ESCALATE"


class EvidenceTrust(StrEnum):
    KERNEL = "KERNEL"
    VERIFIED_EXTERNAL = "VERIFIED_EXTERNAL"
    MEMORY_TRUSTED = "MEMORY_TRUSTED"
    MEMORY_UNVERIFIED = "MEMORY_UNVERIFIED"
    TOOL_UNTRUSTED = "TOOL_UNTRUSTED"
    USER_DECLARED = "USER_DECLARED"


class RecordEvidenceStatus(StrEnum):
    MEASURED = "MEASURED"
    DESIGN = "DESIGN"


class GateDisposition(StrEnum):
    PASS = "PASS"
    REENTER = "REENTER"
    TERMINATE = "TERMINATE"


class PlanStatus(StrEnum):
    DRAFT = "DRAFT"
    REVIEWED = "REVIEWED"
    APPROVED = "APPROVED"
    EXECUTING = "EXECUTING"
    CLOSED = "CLOSED"
    REJECTED = "REJECTED"


class CandidateStatus(StrEnum):
    DISCOVERED = "DISCOVERED"
    SUPPRESSED = "SUPPRESSED"
    REJECTED = "REJECTED"
    PLANNED = "PLANNED"
    APPROVED = "APPROVED"
    QUEUED = "QUEUED"
    ATTEMPTED = "ATTEMPTED"
    JUDGED = "JUDGED"
    CLOSED = "CLOSED"


class LedgerEntryType(StrEnum):
    CORPUS_VERDICT = "CORPUS_VERDICT"
    SDL_TRIAL = "SDL_TRIAL"
    CORRECTION = "CORRECTION"
    REVIEW = "REVIEW"
    DESIGN_REFERENCE = "DESIGN_REFERENCE"
    PLAN_CLOSEOUT = "PLAN_CLOSEOUT"


class GapType(StrEnum):
    REGISTERED_WEAKNESS = "weakness"
    DRIFT = "drift"
    RECALL_MISS = "recall_miss"
    DIMENSION_GAP = "dimension_gap"
    UNEXPLORED = "unexplored"
