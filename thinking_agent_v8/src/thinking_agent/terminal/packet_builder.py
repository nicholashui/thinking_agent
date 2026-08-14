"""Decision-packet builder (impl §15.2): every terminal path produces one."""

from typing import Any

from thinking_agent.canonical import sha256_hex
from thinking_agent.domain.decision_packet import (
    DecisionPacket,
    PacketDiagnosis,
    PacketExecution,
    PacketProvenance,
    PacketResources,
    PacketReview,
    PacketRoute,
    PacketSafety,
    PacketSolution,
    PacketVerification,
)
from thinking_agent.domain.enums import TerminalStatus
from thinking_agent.version import GRAPH_STATE_VERSION


def build_packet(state: dict[str, Any], audit_refs: list[str] | None = None) -> DecisionPacket:
    route = state.get("route") or {}
    routing_scores = state.get("routing_scores") or {}
    verification = state.get("verification") or {}
    plan = state.get("plan") or {}
    auth = state.get("authorization") or {}
    review = state.get("review") or {}
    loop_status = state.get("loop_status") or {}
    budget = state.get("budget_snapshot") or {}
    world_ref = state.get("world_facts_ref") or {}

    packet = DecisionPacket(
        packet_id=f"pkt-{state.get('task_id', 'unknown')}",
        task_id=state.get("task_id", ""),
        thread_id=state.get("thread_id", ""),
        terminal_status=TerminalStatus(state["terminal_status"]),
        terminal_reason=state.get("terminal_reason", ""),
        request_summary=(state.get("request") or {}).get("input_text", "")[:400],
        goal=(state.get("frame") or {}).get("goal", ""),
        success_criteria=(state.get("frame") or {}).get("success_metrics", []),
        scope=(state.get("frame") or {}).get("scope", ""),
        constraints=(state.get("frame") or {}).get("constraints", []),
        route=PacketRoute(
            effort_level=route.get("effort_level", ""),
            signature=(state.get("final_signature") or state.get("preliminary_signature") or {}),
            routed_styles=[s.get("style_id", "") for s in state.get("routed_styles", [])],
            routing_scores=routing_scores,
            confidence_gate=(state.get("routing_gate") or {}).get("gate", ""),
            historical_refs=state.get("historical_refs", []),
            solo_contract_mode=bool(state.get("solo_contract_mode")),
        ),
        diagnosis=PacketDiagnosis(
            hypotheses=[
                {"id": h.get("hypothesis_id"), "statement": h.get("statement"),
                 "probability": h.get("estimated_probability")}
                for h in state.get("hypotheses", [])
            ],
            evidence_refs=[e.get("evidence_id", "") for e in state.get("evidence", [])],
            missing_evidence=[
                m.get("description", m.get("evidence_id", ""))
                for m in state.get("missing_evidence", [])
                if not m.get("filled_by")
            ],
            falsifiers=[
                {"claim": f.get("claim_id"), "falsifier": f.get("falsifier"),
                 "outcome": f.get("outcome")}
                for f in state.get("falsification_evidence", [])
            ],
            residual_uncertainty=(state.get("diagnosis_result") or {}).get(
                "residual_uncertainty", ""
            ),
        ),
        solution=PacketSolution(
            alternatives=[
                {"id": a.get("alternative_id"), "description": a.get("description"),
                 "requires_external_action": a.get("requires_external_action")}
                for a in state.get("alternatives", [])
            ],
            selected_decision=state.get("decision") or {},
            error_bound=(state.get("decision") or {}).get("error_bound", ""),
            infeasibility_findings=(state.get("diagnosis_result") or {}).get(
                "infeasibility_findings", []
            ),
            approximation_details=(
                (state.get("decision") or {}).get("approximation_available")
                and "bounded-error approximation recorded"
            ) or "",
        ),
        safety=PacketSafety(
            declared_action_class=state.get("declared_action_class", ""),
            attested_action_class=state.get("attested_action_class", ""),
            authorization_status=auth.get("status", ""),
            permissions=plan.get("required_permissions", []),
            risks=[r.get("description", r.get("risk_hash", "")) for r in state.get("risks", [])],
            pending_subset=auth.get("allowed_subset", []),
            required_human_actions=state.get("required_human_actions", []),
        ),
        verification=PacketVerification(
            candidate_reports=[
                {"candidate_id": c.get("candidate_id"), "success": c.get("success"),
                 "reliability": c.get("reliability"), "verifier": c.get("verifier_identity")}
                for c in state.get("candidate_reports", [])
            ],
            selected_report=(state.get("selected_report") or {}),
            outcome_report=verification,
            reliability_bar=verification.get("class_bar", 0.0),
            verifier_identities=verification.get("verifier_identities", []),
            second_verifier_satisfied=verification.get("second_verifier_satisfied", False),
            cache_usage=state.get("outcome_cache_refs", []),
        ),
        execution=PacketExecution(
            plan={"plan_id": plan.get("plan_id", ""),
                  "decision_id": plan.get("decision_id", "")},
            actions=[
                {"idempotency_key": a.get("idempotency_key"), "tool": a.get("tool_name"),
                 "success": a.get("success")}
                for a in state.get("executed_actions", [])
            ],
            observations=[
                {"id": o.get("observation_id"), "summary": o.get("content_summary"),
                 "trust": o.get("trust")}
                for o in state.get("observations", [])
            ],
            stop_conditions=plan.get("stop_conditions", []),
            escalation_conditions=plan.get("escalation_conditions", []),
            compensation=plan.get("compensation_steps", []),
        ),
        review=PacketReview(
            review_summary=review.get("what_happened", ""),
            lessons=[
                {"id": lesson.get("lesson_id"), "content": lesson.get("content"),
                 "procedural": lesson.get("procedural")}
                for lesson in state.get("lessons", [])
            ],
            memory_commits=[lesson.get("lesson_id", "") for lesson in state.get("lessons", [])],
            improvement_proposal_refs=[
                p.get("proposal_id", "") for p in state.get("improvement_proposals", [])
            ],
        ),
        resources=PacketResources(
            iterations=loop_status.get("iteration", 0),
            model_calls=budget.get("cognitive_calls_used", 0),
            verifier_calls=len(state.get("candidate_reports", []))
            + (1 if verification else 0),
            tool_calls=len(state.get("executed_actions", [])),
            cognitive_tokens=budget.get("tokens_used", 0),
            bookkeeping_calls=budget.get("bookkeeping_calls", 0),
            stop_reason=state.get("stop_reason", ""),
        ),
        provenance=PacketProvenance(
            world_facts_version=world_ref.get("version", ""),
            model_identities=state.get("model_identities", []),
            prompt_versions=state.get("prompt_versions", []),
            registry_version="1.0",
            routing_kb_version=(state.get("routing_gate") or {}).get("routing_kb_version", ""),
            graph_version=GRAPH_STATE_VERSION,
            checkpoint_refs=state.get("checkpoint_refs", []),
            audit_refs=audit_refs or state.get("audit_refs", []),
        ),
        answer=(state.get("decision") or {}).get("expected_outcome", ""),
        confidence=verification.get("reliability", 0.0),
    )
    packet.packet_hash = sha256_hex(packet.model_dump(exclude={"packet_hash"}))
    return packet
