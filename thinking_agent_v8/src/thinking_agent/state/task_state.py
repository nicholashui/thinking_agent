"""TaskGraph state (impl plan §8.5). TypedDict schema for LangGraph state.

Only repository identifiers, references, and serializable values live here —
no model clients, DB connections, or kernel objects (impl plan §8.1).
"""

from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph

from thinking_agent.state.reducers import (
    append_by_key,
    merge_by_key,
)


class TaskState(TypedDict, total=False):
    # --- identity and runtime ---
    schema_version: str
    task_id: str
    thread_id: str
    run_id: str
    request: dict[str, Any]
    world_facts_ref: dict[str, Any]
    stage: str
    iteration: int
    started_at: str
    started_monotonic: float
    deadline_at: str

    # --- routing ---
    route: dict[str, Any]
    preliminary_signature: dict[str, Any]
    final_signature: dict[str, Any]
    routed_styles: Annotated[list[dict[str, Any]], merge_by_key("style_id")]
    routing_scores: dict[str, float]
    routing_gate: dict[str, Any]
    historical_refs: Annotated[list[str], append_by_key(None)]
    tempo_mode: bool
    solo_contract_mode: bool
    stabilized: bool

    # --- WHAT and WHY ---
    frame: dict[str, Any]
    evidence: Annotated[list[dict[str, Any]], append_by_key("evidence_id")]
    hypotheses: Annotated[list[dict[str, Any]], append_by_key("hypothesis_id")]
    missing_evidence: Annotated[list[dict[str, Any]], append_by_key("evidence_id")]
    falsification_evidence: Annotated[list[dict[str, Any]], append_by_key("claim_id")]
    probe_available: bool
    fillable_gap: bool
    gate_wait: bool

    # --- WHY extras ---
    diagnosis_result: dict[str, Any]
    escalate: bool
    escalate_reason: str
    early_terminal: str
    selected_report: dict[str, Any]
    model_identities: Annotated[list[str], append_by_key(None)]
    prompt_versions: Annotated[list[str], append_by_key(None)]

    # --- HOW ---
    style_results: Annotated[list[dict[str, Any]], merge_by_key(("style_id", "generation"))]
    general_route_result: dict[str, Any]
    alternatives: Annotated[list[dict[str, Any]], append_by_key("alternative_id")]
    minority_reports: Annotated[list[str], append_by_key(None)]
    unresolved_disagreements: Annotated[list[str], append_by_key(None)]
    candidate_reports: Annotated[list[dict[str, Any]], merge_by_key(("candidate_id", "verifier_identity"))]
    decision: dict[str, Any]
    approximation_available: bool
    infeasible: bool
    previous_alternative_signature: str

    # --- HOW machinery (Phase 5) ---
    insights: Annotated[list[str], append_by_key(None)]
    structure_scan: dict[str, Any]
    premortem: Annotated[list[dict[str, Any]], append_by_key("risk_hash")]
    council: dict[str, Any]
    divergence: dict[str, Any]

    # --- safety and verification ---
    stakes: str
    declared_action_class: str
    attested_action_class: str
    identity_count: int
    verifier_outage: bool
    reliability_blocked: bool
    risks: Annotated[list[dict[str, Any]], append_by_key("risk_hash")]
    verification: dict[str, Any]
    candidate_cache_refs: Annotated[list[str], append_by_key(None)]
    outcome_cache_refs: Annotated[list[str], append_by_key(None)]

    # --- DO ---
    plan: dict[str, Any]
    authorization: dict[str, Any]
    subset_executed: bool
    pending_wait: bool
    pending_deadline: str
    executed_actions: Annotated[list[dict[str, Any]], append_by_key("idempotency_key")]
    observations: Annotated[list[dict[str, Any]], append_by_key("observation_id")]
    previous_observation_signature: str

    # --- loop and budget ---
    budget_snapshot: dict[str, Any]
    loop_status: dict[str, Any]
    novelty_signatures: Annotated[list[str], append_by_key(None)]
    progress_markers: Annotated[list[str], append_by_key(None)]
    stop_reason: str

    # --- review and result ---
    review: dict[str, Any]
    lessons: Annotated[list[dict[str, Any]], append_by_key("lesson_id")]
    improvement_proposals: Annotated[list[dict[str, Any]], append_by_key("proposal_id")]
    terminal_status: str
    terminal_reason: str
    required_human_actions: Annotated[list[str], append_by_key(None)]
    decision_packet: dict[str, Any]
    audit_refs: Annotated[list[str], append_by_key(None)]
    checkpoint_refs: Annotated[list[str], append_by_key(None)]
    internal_fault: str


def build_task_graph() -> "StateGraph":
    """Compiles the TaskGraph skeleton (nodes wired in later phases)."""
    return StateGraph(TaskState)


# canonical state keys used by tests
STATE_GROUPS = [
    "identity_and_runtime", "routing", "what_why", "how",
    "safety_and_verification", "do", "loop_and_budget", "review_and_result",
]
