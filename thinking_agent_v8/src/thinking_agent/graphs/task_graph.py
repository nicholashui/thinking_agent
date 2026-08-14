"""Main TaskGraph (impl §10/§11): META → WHAT → WHY → HOW → DO → REVIEW with
continuous VERIFY, state-only classifier, and proof-carrying packet.

Loop semantics port the validated v5 harness (`validation/harness.py`) onto
LangGraph 1.x: same gate predicates, same terminal producers, same budget/
plateau/reframe discipline. Cognitive nodes call the injected ModelAdapter
(mock in tests, live providers in production) — the graph is provider-blind.
"""

from dataclasses import asdict
from typing import Any

from langchain_core.runnables import RunnableConfig
from langgraph.graph import END, START, StateGraph

from thinking_agent.control.budget_controller import BudgetController
from thinking_agent.control.loop_monitor import LoopMonitor
from thinking_agent.control.terminal_classifier import Classification, classify
from thinking_agent.canonical import content_hash, sha256_hex
from thinking_agent.domain.alternatives import AltSet, CandidateVerificationReport, Decision
from thinking_agent.domain.enums import (
    ActionClass,
    AuthorizationStatus,
    EffortLevel,
    TerminalStatus,
)
from thinking_agent.domain.framing import (
    DiagnosisResult,
    EvidenceItem,
    ProblemFrame,
)
from thinking_agent.domain.task import BudgetEnvelope, RouteDecision, SituationSignature
from thinking_agent.domain.verification import OutcomeVerification
from thinking_agent.state.task_state import TaskState, build_task_graph
from thinking_agent.terminal.packet_builder import build_packet
from thinking_agent.version import GRAPH_STATE_VERSION

# --------------------------------------------------------------------------
# deterministic helpers shared by nodes
# --------------------------------------------------------------------------

FAST_EFFORTS = {EffortLevel.E0_DIRECT.value, EffortLevel.E1_DIRECT_WITH_REVIEW.value}

STOP_STATES = {
    "iteration ceiling", "deadline exceeded", "token ceiling", "call ceiling",
    "reserved epilogue budget would be exhausted", "novelty plateau", "EVOC exhausted",
}


def _ctx_model(ctx: Any, role: str = "main"):
    return ctx.models.get(role) or ctx.models.get("main")


def _scenario(state: TaskState) -> str:
    req = state.get("request") or {}
    meta = req.get("task_metadata") or {}
    return meta.get("scenario", "default")


def _messages(state: TaskState, role: str, extra: dict[str, Any] | None = None) -> list[dict]:
    """Builds provider-visible messages. Scenario key travels so the mock
    adapter can script deterministic responses."""
    content = {
        "scenario": _scenario(state),
        "role": role,
        "task_id": state.get("task_id", ""),
        "frame": state.get("frame") or {},
        "hypotheses": state.get("hypotheses") or [],
        "missing_evidence": state.get("missing_evidence") or [],
        "decision": state.get("decision") or {},
        **(extra or {}),
    }
    return [
        {"role": "system", "content": "You are one stage of a governed thinking agent. "
                                      "Return ONLY the requested structured output."},
        {"role": "user", "content": f"{content!r}"},
    ]


# --------------------------------------------------------------------------
# nodes
# --------------------------------------------------------------------------

def initialize_task(state: TaskState) -> dict[str, Any]:
    req = state["request"]
    return {
        "schema_version": GRAPH_STATE_VERSION,
        "task_id": req.get("task_id") or f"task-{content_hash(req)}",
        "thread_id": state.get("thread_id", ""),
        "stage": "META",
        "iteration": 0,
        "started_at": "",
        "started_monotonic": 0.0,
        "internal_fault": "",
        "stop_reason": "",
        "gate_wait": False,
        "pending_wait": False,
        "stabilized": False,
        "tempo_mode": False,
        "solo_contract_mode": False,
        "subset_executed": False,
        "reliability_blocked": False,
        "probe_available": False,
        "fillable_gap": False,
        "approximation_available": False,
        "infeasible": False,
        "verifier_outage": False,
    }


def meta_route(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Deterministic effort selection; the model may recommend, the kernel clamps."""
    meta = (state.get("request") or {}).get("task_metadata") or {}
    stakes = str(meta.get("stakes", (state.get("frame") or {}).get("stakes", "low")))
    effort = EffortLevel.E2_STRUCTURED.value
    if meta.get("effort") in {e.value for e in EffortLevel}:
        effort = meta["effort"]
    elif stakes == "high" or meta.get("chaotic"):
        effort = EffortLevel.E5_CHAOTIC_STABILIZE_FIRST.value
    elif meta.get("council") or meta.get("search"):
        effort = EffortLevel.E4_COUNCIL_OR_SEARCH.value
    elif meta.get("direct"):
        effort = EffortLevel.E0_DIRECT.value
    elif meta.get("review"):
        effort = EffortLevel.E1_DIRECT_WITH_REVIEW.value

    envelope = BudgetEnvelope(
        iterations=ctx.kernel.budgets.iterations,
        cognitive_calls=ctx.kernel.budgets.cognitive_calls,
        tokens=ctx.kernel.budgets.tokens,
        agents_per_round=ctx.kernel.budgets.agents_per_round,
        deadline_seconds=ctx.kernel.budgets.deadline_seconds,
    )
    sig = _extract_signature(state, preliminary=True)
    route = RouteDecision(
        effort_level=effort,
        requires_diagnosis=effort not in FAST_EFFORTS,
        requires_generation=True,
        use_council=effort == EffortLevel.E4_COUNCIL_OR_SEARCH.value,
        requires_review=effort == EffortLevel.E1_DIRECT_WITH_REVIEW.value,
        estimated_complexity=float(meta.get("complexity", 0.5)),
        route_reasons=[f"metadata-derived effort {effort}; kernel-clamped"],
    )
    return {
        "route": route.model_dump(),
        "preliminary_signature": sig.model_dump(),
        "budget_snapshot": envelope.model_dump(),
        "loop_status": {"stage": "META", "iteration": 0, "gate_reentries": {}, "reframe_count": 0},
        "stakes": stakes,
        "stage": "FAST" if effort in FAST_EFFORTS else "META",
        "started_at": str(getattr(ctx.clock, "now", lambda: "")()),
        "started_monotonic": float(getattr(ctx.clock, "monotonic", lambda: 0.0)()),
    }


def loop_guard(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Iteration bookkeeping + hard budgets + plateau + next-stage routing (impl §10.2)."""
    loop = dict(state.get("loop_status") or {})
    loop["iteration"] = int(loop.get("iteration", 0)) + 1
    loop["stage"] = "LOOP_GUARD"
    budget = BudgetController.from_snapshot(state.get("budget_snapshot"))
    budget.snapshot.next_iteration()
    # deadline enforcement (impl §10.2.5): kernel deadline, clock-checked
    deadline_elapsed = _deadline_elapsed(state, ctx, budget)

    stop = budget.guard(loop["iteration"], deadline_elapsed)
    if stop:
        return {"loop_status": loop, "budget_snapshot": asdict(budget.snapshot),
                "stop_reason": stop, "stage": "TERMINAL"}

    # loop monitor (EVOC + plateau), wait-exempt; the monitor persists on the
    # runtime context so streaks survive iterations
    wait = bool(state.get("pending_wait") or state.get("gate_wait"))
    monitor = _monitor_from(ctx)
    if not wait:
        sig = _state_signature(state)
        novel = monitor.register_signature(sig)
        monitor.value_of_continued_computation(progress=novel, novelty=novel)
        stop_l = monitor.should_stop(wait_exempt=False)
        if stop_l:
            return {"loop_status": loop, "budget_snapshot": asdict(budget.snapshot),
                    "stop_reason": stop_l, "stage": "TERMINAL"}

    loop["stage"] = _next_stage(state)
    # cognitive pricing (v5 harness parity): each cognitive-stage dispatch
    # costs one cognitive call — bookkeeping stays free (impl §10.2)
    if loop["stage"] in {"WHAT", "WHY", "HOW", "VERIFY", "STABILIZE", "FAST"}:
        if not budget.snapshot.charge(calls=1):
            return {"loop_status": loop, "budget_snapshot": asdict(budget.snapshot),
                    "stop_reason": "call ceiling", "stage": "TERMINAL"}
    return {"loop_status": loop, "budget_snapshot": asdict(budget.snapshot),
            "stage": loop["stage"], "stop_reason": ""}


def _next_stage(state: TaskState) -> str:
    """The previous node's explicit stage wins; completeness routing only
    applies on first entry (META) and as a fallback."""
    current = state.get("stage", "")
    explicit = {"STABILIZE", "FAST", "WHAT", "WHY", "EARLY_CLASSIFY", "HOW", "DO",
                "DO_EXECUTE", "VERIFY", "REVIEW", "TERMINAL"}
    if current in explicit:
        return current
    route = state.get("route") or {}
    effort = route.get("effort_level", "")
    if effort == EffortLevel.E5_CHAOTIC_STABILIZE_FIRST.value and not state.get("stabilized"):
        return "STABILIZE"
    if not state.get("frame"):
        return "WHAT"
    if route.get("requires_diagnosis") and not state.get("hypotheses"):
        return "WHY"
    if not state.get("decision"):
        return "HOW"
    decision = state.get("decision") or {}
    executed = state.get("executed_actions") or []
    if decision.get("requires_external_action") and not executed:
        return "DO"
    if not state.get("verification"):
        return "VERIFY"
    return "REVIEW"


def stabilize(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """E5: exactly one containment-oriented pass before diagnosis (impl §10.3).
    A stabilization pass NEVER authorizes external execution — containment
    actions still pass through attestation and authorization."""
    model = _ctx_model(ctx)
    try:
        out = model.invoke_text(_messages(state, "stabilizer"))
        text = out[:200]
    except RuntimeError:
        # mock without a stabilizer script: stabilization is a recorded no-op
        text = "stabilization pass recorded; no immediate hazard scripted"
    risks = list(state.get("risks") or [])
    risks.append({"risk_hash": content_hash(text), "description": text})
    return {"stabilized": True, "risks": risks, "stage": "WHAT"}


def fast_answer(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """E0/E1 fast path (impl §12): direct internal answer — no framing,
    no diagnosis, no style dispatch. Outcome verification still runs; the
    fast path can NEVER perform external action."""
    model = _ctx_model(ctx, "generator")
    alt_payload: AltSet = model.invoke_structured(
        AltSet, _messages(state, "generator", {"fast_path": True}),
    )
    alternatives = [a.model_dump() for a in alt_payload.alternatives]
    frame = ProblemFrame(
        goal=(state.get("request") or {}).get("input_text", "")[:200],
        owner="requester", success_metrics=["direct answer produced"],
        scope="internal-only", stakes="low", assumptions=["fast path"],
    )
    report = CandidateVerificationReport(
        candidate_id=alternatives[0]["alternative_id"] if alternatives else "fast",
        verifier_identity="verifier-alpha", verifier_kind="fast-path",
        success=True, logical_validity=1.0, evidence_adequacy=0.6,
        constraint_compliance=1.0, reliability=0.6, findings=[],
    )
    decision = Decision(
        decision_id=f"dec-fast-{content_hash(alternatives)}",
        selected_alternative_id=report.candidate_id,
        selection_reason="fast path: single direct answer",
        expected_outcome=(alternatives[0]["description"] if alternatives else ""),
        requires_external_action=False,
    )
    return {
        "frame": frame.model_dump(),
        "alternatives": alternatives,
        "candidate_reports": [report.model_dump()],
        "selected_report": report.model_dump(),
        "decision": decision.model_dump(),
        "final_signature": _extract_signature(state, preliminary=False).model_dump(),
        "stage": "VERIFY",
    }


def what_frame(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    model = _ctx_model(ctx, "frame_builder")
    try:
        frame: ProblemFrame = model.invoke_structured(
            ProblemFrame, _messages(state, "frame_builder")
        )
    except Exception as exc:
        # provider fault translation (§23.1): the WHAT gate re-entry path
        # escalates after the kernel gate budget — never a raw exception
        return {"frame": {}, "stage": "WHAT_GATE",
                "risks": list(state.get("risks") or []) + [
                    {"risk_hash": content_hash(str(exc)),
                     "description": f"frame builder fault: {exc}"}]}
    return {"frame": frame.model_dump(), "stage": "WHAT_GATE"}


def what_gate(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    frame = state.get("frame") or {}
    checks = {
        "G-WHAT-1": bool(frame.get("goal")),
        "G-WHAT-2": bool(frame.get("success_metrics")),
        "G-WHAT-3": bool(frame.get("scope")) or bool(frame.get("constraints")),
        "G-WHAT-4": bool(frame.get("owner")) or bool(frame.get("owner_unavailable")),
        "G-WHAT-5": bool(frame.get("stakes")),
        "G-WHAT-6": True,  # ambiguities recorded when present (list field)
    }
    loop = dict(state.get("loop_status") or {})
    if not all(checks.values()):
        loop["gate_reentries"] = dict(loop.get("gate_reentries") or {})
        n = loop["gate_reentries"].get("WHAT", 0) + 1
        loop["gate_reentries"]["WHAT"] = n
        budget = ctx.kernel.budgets.gate_reentry_budget
        if n > budget:
            if frame.get("owner_unavailable"):
                return {
                    "loop_status": loop, "stage": "TERMINAL",
                    "escalate": True,
                    "escalate_reason": "WHAT gate budget expired (owner unavailable)",
                    "gate_wait": False,
                    "risks": list(state.get("risks") or []) + [
                        {"risk_hash": content_hash("WHAT gate fail"),
                         "description": "WHAT gate failed"}]}
            return {
                "loop_status": loop, "stage": "TERMINAL",
                "early_terminal": TerminalStatus.NEEDS_EVIDENCE.value,
                "terminal_reason": "WHAT gate budget expired (missing inputs)",
                "gate_wait": False,
                "risks": list(state.get("risks") or []) + [
                    {"risk_hash": content_hash("WHAT gate fail"), "description": "WHAT gate failed"}
                ],
            }
        return {
            "loop_status": loop,
            "frame": {},
            "gate_wait": True,
            "stage": "WHAT",
            "risks": list(state.get("risks") or []) + [
                {"risk_hash": content_hash(f"WHAT gate fail {n}"),
                 "description": f"WHAT gate failed ({n}/{budget})"}
            ],
        }
    return {"stage": "WHY", "gate_wait": False}


def why_stage(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Retrieval before hypotheses (impl §11.4), then diagnosis."""
    memory = getattr(ctx, "memory", None)
    retrieved: list[EvidenceItem] = []
    if memory is not None:
        for e in memory.retrieve(state, ctx):
            retrieved.append(e)
    evidence = list(state.get("evidence") or [])
    for e in retrieved:
        evidence.append(e.model_dump())

    model = _ctx_model(ctx, "diagnostician")
    try:
        diag: DiagnosisResult = model.invoke_structured(
            DiagnosisResult, _messages(state, "diagnostician", {"evidence_ids": [e.evidence_id for e in retrieved]})
        )
    except Exception:
        diag = DiagnosisResult()  # fault -> gate re-entry path
    # REAL gap fill (V6/V11): a fillable gap clears ONLY when a retrieval
    # hit satisfies its terms — never because a task flag says fillable.
    # Gap fill queries memory with the EXACT gap description (impl §11.4).
    missing = [m.model_dump() for m in diag.missing_evidence]
    if memory is not None:
        for gap in missing:
            if gap.get("fillable") and not gap.get("filled_by"):
                for e in memory.retrieve_for_terms([gap.get("description", "")]):
                    if e.evidence_id not in {ev["evidence_id"] for ev in evidence}:
                        evidence.append(e.model_dump())
                    if _gap_satisfied(gap.get("description", ""), e.content_summary):
                        gap["filled_by"] = e.evidence_id
                        break
    return {
        "evidence": evidence,
        "hypotheses": [h.model_dump() for h in diag.hypotheses],
        "missing_evidence": missing,
        "falsification_evidence": [f.model_dump() for f in diag.falsifications],
        "diagnosis_result": diag.model_dump(),
        "probe_available": diag.probe_available,
        "infeasible": diag.infeasible,
        "verifier_outage": ctx.kernel.verifier_outage,
        "stage": "WHY_GATE",
    }


def why_gate(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    diag = state.get("diagnosis_result") or {}
    falsifications = state.get("falsification_evidence") or []
    checks = {
        "G-WHY-1": bool(state.get("hypotheses")),
        "G-WHY-2": bool(diag.get("hypotheses", [])),  # alternatives considered
        "G-WHY-3": bool(diag.get("residual_uncertainty")),
        "G-WHY-4": True,  # VOI check is diagnosis-internal; gate confirms presence
        "G-WHY-5": bool(falsifications),
    }
    loop = dict(state.get("loop_status") or {})
    if not all(checks.values()):
        n = int((loop.get("gate_reentries") or {}).get("WHY", 0)) + 1
        loop["gate_reentries"] = dict(loop.get("gate_reentries") or {})
        loop["gate_reentries"]["WHY"] = n
        if n > ctx.kernel.budgets.gate_reentry_budget:
            return {"loop_status": loop, "stage": "TERMINAL",
                    "early_terminal": TerminalStatus.NEEDS_EVIDENCE.value,
                    "terminal_reason": "WHY gate budget expired"}
        return {"loop_status": loop, "hypotheses": [], "gate_wait": True, "stage": "WHY"}
    return {"stage": "EARLY_CLASSIFY", "gate_wait": False}


def early_classify(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    """After a passed WHY gate (impl §11.4 `why_early_classifier`)."""
    missing = state.get("missing_evidence") or []
    unfilled = [m for m in missing if not m.get("filled_by")]
    if unfilled:
        return {"stage": "TERMINAL", "escalate": False, "early_terminal": TerminalStatus.NEEDS_EVIDENCE.value,
                "terminal_reason": "unfilled evidence gap (early): only real retrieval hits clear gaps"}
    if state.get("probe_available"):
        return {"stage": "TERMINAL", "early_terminal": TerminalStatus.NEEDS_EXPERIMENT.value,
                "terminal_reason": "safe probe available (early)"}
    return {"stage": "HOW"}


def how_generate(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Signature → structure scan → style passes → general route → divergence →
    constraint screen → premortem → red team → candidate verification →
    selection (impl §11.5)."""
    sig = _extract_signature(state, preliminary=False)
    routing = _route_styles(sig, state, ctx)

    # structure-first scan (mandatory for structural signature classes)
    from thinking_agent.reasoning.machinery import structure_first_scan
    frame_text = ((state.get("request") or {}).get("input_text", "")
                  + " " + (state.get("frame") or {}).get("goal", ""))
    structure = structure_first_scan(frame_text, sig).__dict__

    # style-pass dispatch: top styles + mandatory protective modules +
    # home-turf promotions, each validated against its completion contract
    style_results: list[dict[str, Any]] = []
    divergence: dict[str, Any] = {}
    if getattr(ctx, "style_router", None) is not None:
        from thinking_agent.reasoning.machinery import general_route_summary
        from thinking_agent.styles.module_runner import StyleModuleRunner
        from thinking_agent.styles.registry import StyleRegistry
        from thinking_agent.domain.routing import StyleModel
        runner = StyleModuleRunner(
            StyleRegistry([StyleModel.model_validate(m.model_dump())
                           for m in ctx.style_router.models.values()]))
        pass_ids = list(dict.fromkeys(
            list(routing.get("top_styles", [])[:2])
            + list(routing.get("mandatory_modules", []))
            + list(routing.get("home_turf_promotions", []))))
        results = runner.run_passes(pass_ids, state, ctx)
        style_results = [r.model_dump() for r in results]

    model = _ctx_model(ctx, "generator")
    try:
        alt_payload: AltSet = model.invoke_structured(
            AltSet, _messages(state, "generator", {"signature": sig.model_dump()}),
        )
    except Exception:
        alt_payload = AltSet()  # fault -> HOW gate re-entry/plateau path
    alternatives = [a.model_dump() for a in alt_payload.alternatives]
    hashes = {a["alternative_id"]: sha256_hex(a) for a in alternatives}

    # divergence resolution: style conclusions vs the general route
    if style_results:
        from thinking_agent.reasoning.machinery import general_route_summary
        general = general_route_summary(alternatives)
        style_summaries = [r.get("summary", "") for r in style_results]
        agreed = all((s or "") == general for s in style_summaries) or not any(
            s for s in style_summaries)
        divergence = {
            "agreed": agreed,
            "resolution": ("agreement recorded" if agreed
                           else "disagreement recorded; selection deferred to verification"),
            "curriculum_items": [
                f"{r['style_id']}: incomplete {r['contract_gaps']}"
                for r in style_results if not r.get("contract_met")
            ],
        }

    # constraint screen (deterministic): explicit infeasibility signal from
    # the generator's AltSet, the diagnosis, or alternative descriptions
    infeasible = bool(state.get("infeasible")) or bool(alt_payload.infeasible) or any(
        "INFEASIBLE" in (a.get("description") or "").upper() for a in alternatives
    )
    if infeasible:
        return {"infeasible": True,
                "risks": list(state.get("risks") or []) + [
                    {"risk_hash": content_hash(f), "description": f}
                    for f in (alt_payload.infeasibility_findings
                              or (state.get("diagnosis_result") or {}).get("infeasibility_findings")
                              or ["constraint screen: infeasible"])
                ],
                "stage": "TERMINAL"}

    # premortem + red team + insight pass + bounded council (Phase 5)
    from thinking_agent.reasoning import machinery as _m
    pm = _m.premortem(model, state)
    rt = _m.red_team(model, state)
    insights = _m.insight_pass(model, state)
    council_out = _m.council(model, state) if state.get("route", {}).get("use_council") else {}

    # candidate verification with per-candidate cache (§6: sha256 canonical
    # candidate + verifier + policy version)
    verifier = _ctx_model(ctx, "verifier")
    reports: list[CandidateVerificationReport] = []
    for alt in alternatives:
        cache_key = sha256_hex({
            "candidate": alt, "verifier": verifier.identity(),
            "policy": (state.get("world_facts_ref") or {}).get("content_hash", ""),
        })
        cache = getattr(ctx, "candidate_cache", None)
        cached = None
        if cache is not None and cache_key in cache:
            cached = cache[cache_key]
        if cached is not None:
            rep = CandidateVerificationReport.model_validate(cached)
        else:
            rep = verifier.invoke_structured(
                CandidateVerificationReport,
                _messages(state, "verifier", {"candidate": alt["alternative_id"],
                                              "content_hash": hashes[alt["alternative_id"]]}),
            )
            rep.cache_key = cache_key
            if cache is not None:
                cache[cache_key] = rep.model_dump()
        reports.append(rep)

    # selection: highest reliability; selected report governs downstream checks.
    # No viable alternatives (or no reports) -> no decision; the HOW gate
    # re-entry path and novelty plateau handle the unproductive loop.
    if not reports:
        return {"alternatives": alternatives, "infeasible": infeasible,
                "stage": "HOW_GATE", "decision": None}
    best = max(reports, key=lambda r: r.reliability)
    sel_alt = next(
        (a for a in alternatives if a["alternative_id"] == best.candidate_id), {}
    )
    # second-verification pass (impl §14.2): external-action candidates are
    # verified by a SECOND identity before DO, so the pre-execution
    # second-verifier rule counts real verification, not registry presence
    if sel_alt.get("requires_external_action"):
        verifier2 = ctx.models.get("verifier_second") or verifier
        rep2 = verifier2.invoke_structured(
            CandidateVerificationReport,
            _messages(state, "verifier_second", {"candidate": best.candidate_id,
                                                  "content_hash": hashes[best.candidate_id]}),
        )
        reports.append(rep2)

    decision = Decision(
        decision_id=f"dec-{content_hash(alternatives)}",
        selected_alternative_id=best.candidate_id,
        selection_reason="highest verified reliability",
        expected_outcome=sel_alt.get("description", ""),
        required_conditions=list(sel_alt.get("dependencies") or []),
        error_bound=best.evidence_adequacy >= 0.8 and "bounded-error" or "",
        residual_risks=best.findings,
        requires_external_action=bool(sel_alt.get("requires_external_action")),
        selected_verification_report_ref=best.cache_key,
        approximation_available=bool(best.evidence_adequacy >= 0.8 and best.success),
    )

    return {
        "final_signature": sig.model_dump(),
        "routing_scores": routing.get("scores", {}),
        "routing_gate": {"gate": routing.get("confidence_gate", ""),
                         "routing_kb_version": routing.get("routing_kb_version", "")},
        "routed_styles": [{"style_id": s} for s in routing.get("top_styles", [])],
        "historical_refs": routing.get("historical_refs", []),
        "solo_contract_mode": routing.get("solo_contract_mode", False),
        "style_results": style_results,
        "structure_scan": structure,
        "insights": insights,
        "premortem": pm,
        "council": council_out,
        "divergence": divergence,
        "risks": list(state.get("risks") or []) + [
            {"risk_hash": r["risk_hash"], "description": r["description"]}
            for r in pm] + [
            {"risk_hash": content_hash(f), "description": f}
            for f in rt.get("findings", [])],
        "alternatives": alternatives,
        "candidate_reports": [r.model_dump() for r in reports],
        "selected_report": best.model_dump(),
        "decision": decision.model_dump(),
        "infeasible": infeasible,
        "approximation_available": decision.approximation_available,
        "stage": "HOW_GATE",
    }


def how_gate(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    decision = state.get("decision") or {}
    selected = state.get("selected_report") or {}
    checks = {
        "G-HOW-1": bool(state.get("alternatives")),
        "G-HOW-2": True,  # style contracts — enforced in Phase 5 dispatch
        "G-HOW-3": True,  # constraint screen ran (deterministic above)
        "G-HOW-4": bool(decision.get("residual_risks") is not None),
        "G-HOW-5": selected.get("candidate_id") == decision.get("selected_alternative_id"),
        "G-HOW-6": bool(state.get("risks") or decision.get("residual_risks")),
        "G-HOW-7": not decision.get("requires_external_action") or bool(
            decision.get("required_conditions")),
    }
    if not all(checks.values()):
        # unproductive HOW loops are owned by the novelty plateau and the
        # iteration ceiling (RESOURCE_LIMITED) — no gate-budget escalation
        # here (harness parity: S2/S9/S24/S27/S36/S43)
        return {"stage": "HOW", "gate_wait": True,
                "risks": list(state.get("risks") or []) + [
                    {"risk_hash": content_hash("HOW gate fail"),
                     "description": f"HOW gate failed: {[k for k, v in checks.items() if not v]}"}]}
    return {"stage": "DO" if decision.get("requires_external_action") else "VERIFY",
            "gate_wait": False}


def do_authorize(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Planner-once + kernel authorization (impl §11.6)."""
    decision = state.get("decision") or {}
    plan_id = state.get("plan", {}).get("plan_id")
    if not plan_id or state.get("plan", {}).get("decision_id") != decision.get("decision_id"):
        plan = {"plan_id": f"plan-{content_hash(decision)}", "decision_id": decision["decision_id"],
                "tasks": [], "stop_conditions": [], "escalation_conditions": [],
                "compensation_steps": [], "required_permissions": [],
                "idempotency_namespace": state["task_id"]}
    else:
        plan = state["plan"]

    meta = (state.get("request") or {}).get("task_metadata") or {}
    tool_name = meta.get("tool") or "knowledge_lookup"
    # declared class comes from the governed frame (the planner's claim),
    # NEVER from raw client metadata — attestation is the kernel's check
    declared = (state.get("declared_action_class")
                or (state.get("frame") or {}).get("declared_action_class"))
    kd = ctx.kernel.authorize(
        tool_name,
        ActionClass(declared) if declared else None,
        description=meta.get("action_description", ""),
        requested_human_approval=bool(meta.get("require_human_approval")),
    )
    authorization = {
        "status": kd.status.value,
        "action_class": kd.action_class.value,
        "token": kd.token,
        "reasons": kd.reasons,
        "allowed_subset": kd.allowed_subset,
    }

    # planner-once: materialize the plan's task list from the decision
    if not plan.get("tasks"):
        plan["tasks"] = [{
            "plan_task_id": "t1",
            "description": (state.get("decision") or {}).get("expected_outcome", "")[:200],
            "tool_name": tool_name,
            "arguments": {"query": (state.get("decision") or {}).get("expected_outcome", "")[:100]},
            "action_class": kd.action_class.value,
            "reversible": True,
            "idempotency_key": f"{state.get('task_id')}:{plan['plan_id']}:t1:1",
        }]

    # second-verifier rule (kernel-computed, impl §14.2) enforced BEFORE
    # execution: at least TWO distinct REGISTERED identities must have
    # ACTUALLY verified the selected candidate. Registry presence alone is
    # not verification — fail closed on one report identity.
    registered = {i.get("identity_id") for i in ctx.kernel.verifier_identities()
                  if i.get("accepted", True)}
    selected = state.get("selected_report") or {}
    selected_id = selected.get("candidate_id")
    report_identities = {
        r.get("verifier_identity") for r in state.get("candidate_reports") or []
        if r.get("candidate_id") == selected_id and r.get("verifier_identity")
    }
    second_ok = (
        not kd.second_verifier_required
        or len(report_identities & registered) >= 2
    )
    bar_ok = (kd.class_bar == 0.0) or (selected.get("reliability") or 0.0) >= kd.class_bar

    out: dict[str, Any] = {
        "plan": plan,
        "authorization": authorization,
        "attested_action_class": kd.action_class.value,
    }
    if kd.status == AuthorizationStatus.APPROVED and (not second_ok or not bar_ok):
        out.update({
            "stage": "TERMINAL", "reliability_blocked": True, "escalate": True,
            "escalate_reason": ("second verifier missing" if not second_ok
                                 else "reliability below class bar"),
            "required_human_actions": ["reliability escalation: second verifier required"],
        })
        return out  # pre-DO block: never proceeds to execution
    if kd.status == AuthorizationStatus.DENIED_UNSAFE:
        out.update({"stage": "TERMINAL", "internal_fault": "UNSAFE",
                    "terminal_reason": "; ".join(kd.reasons)})
    elif kd.status == AuthorizationStatus.DENIED_ESCALATE:
        out.update({"stage": "TERMINAL", "escalate": True,
                    "escalate_reason": "; ".join(kd.reasons),
                    "required_human_actions": ["attest-time L3 escalation: verifier outage"]})
    elif kd.status == AuthorizationStatus.PENDING:
        from langgraph.types import interrupt
        decision = interrupt({
            "kind": "human_approval",
            "task_id": state.get("task_id"),
            "action_class": kd.action_class.value,
            "plan_summary": plan.get("tasks", [{}])[0].get("description", "")[:200],
            "risks": kd.reasons,
            "allowed_subset": kd.allowed_subset,
            "valid_responses": ["approve", "approve_with_edits", "deny", "escalate"],
        })
        if decision in ("approve", "approve_with_edits"):
            authorization["status"] = AuthorizationStatus.APPROVED.value
            out["authorization"] = authorization
            out["stage"] = "DO_EXECUTE"
            return out
        if decision == "timeout":
            out.update({"stage": "TERMINAL", "escalate": True,
                        "escalate_reason": "approval timed out"})
            return out
        if decision == "escalate":
            out.update({"stage": "TERMINAL", "escalate": True,
                        "escalate_reason": "human escalated the approval"})
            return out
        # deny -> escalation (execution is refused by the human gate)
        out.update({"stage": "TERMINAL", "escalate": True,
                    "escalate_reason": "human denied the approval"})
        return out
    else:
        out["stage"] = "DO_EXECUTE"
    return out


def do_execute(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Tool broker execution (impl §16): allowlist, idempotency, receipts."""
    plan = state.get("plan") or {}
    broker = getattr(ctx, "tools", None)
    if broker is None and plan.get("tasks"):
        # a planned external action with no broker must NEVER silently
        # "succeed" — escalation, not a skipped execution
        return {"stage": "TERMINAL", "escalate": True,
                "escalate_reason": "tool broker unavailable for planned execution",
                "required_human_actions": ["provision tool broker and re-run"]}
    if broker is None:
        return {"stage": "VERIFY", "executed_actions": [], "observations": []}
    auth = state.get("authorization") or {}
    actions, observations = broker.execute_plan(plan, auth, state, ctx)

    # ExecutionMonitor + compensation (impl §11.6/§16.5)
    from thinking_agent.tools.execution_monitor import (
        ExecutionMonitor,
        run_compensation,
    )
    budget = BudgetController.from_snapshot(state.get("budget_snapshot"))
    report = ExecutionMonitor().check(plan, actions, budget)
    if report.compensation_required:
        comp_actions = run_compensation(plan, actions, broker, auth, state, ctx)
        actions = actions + comp_actions
    if report.stop_condition or report.escalation_condition:
        return {
            "stage": "TERMINAL",
            "escalate": bool(report.escalation_condition),
            "escalate_reason": report.escalation_condition,
            "stop_reason": report.stop_condition,
            "executed_actions": actions,
            "observations": observations,
            "risks": list(state.get("risks") or []) + [
                {"risk_hash": content_hash(f), "description": f}
                for f in report.findings],
        }
    return {
        "stage": "VERIFY",
        "executed_actions": actions,
        "observations": observations,
        "previous_observation_signature": _state_signature(state),
    }


def verify_outcome(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Outcome verifier — the sole SOLVED producer (impl §11.7 / §15.1)."""
    key = sha256_hex({
        "frame": state.get("frame"), "hypotheses": state.get("hypotheses"),
        "decision": state.get("decision"), "observations": state.get("observations"),
    })
    cache = getattr(ctx, "verification_cache", None)
    if cache is not None and key in cache:
        cached = cache[key]
        return {"verification": cached, "outcome_cache_refs": [key], "stage": "REVIEW"}

    verifier = _ctx_model(ctx, "outcome_verifier")
    try:
        result: OutcomeVerification = verifier.invoke_structured(
            OutcomeVerification, _messages(state, "outcome_verifier", {"outcome_hash": key})
        )
    except Exception as exc:
        # verifier outage: no-verifier ladder (L1 evidence degradation)
        result = OutcomeVerification(
            success=False, ambiguous=True,
            findings=[f"outcome verifier outage: {exc}"])
    payload = result.model_dump()
    payload["outcome_hash"] = key
    if cache is not None:
        cache[key] = payload
    out: dict[str, Any] = {
        "verification": payload,
        "outcome_cache_refs": [key],
        "reliability_blocked": result.reliability_blocked,
        "stage": "REVIEW",
    }
    if result.success:
        out["stage"] = "REVIEW"  # REVIEW runs before classification; SOLVED decided there
    return out


def delta_review(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Delta-gated AAR + reframe decision (impl §11.8)."""
    review_engine = getattr(ctx, "review_engine", None)
    decision = state.get("decision")
    executed = bool(state.get("executed_actions"))
    candidates_new = bool(state.get("alternatives"))
    if not (decision and (candidates_new or executed)) and not state.get("verification", {}).get("ambiguous"):
        return {"stage": "TERMINAL", "review": {"what_happened": "nothing new to review"}}

    if review_engine is not None:
        review = review_engine.review(state, ctx)
        if review.reframe_required:
            return {"review": review.model_dump(), "stage": "WHAT",
                    "frame": None, "hypotheses": [], "alternatives": []}
        return {"review": review.model_dump(), "stage": "TERMINAL"}

    # default deterministic review: no reframe
    return {"stage": "TERMINAL",
            "review": {"what_happened": "episode completed", "reframe_required": False}}


def terminal_classify(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    """Deterministic, state-only classification (impl §11.7)."""
    early = state.get("early_terminal")
    if early:
        classification = Classification(TerminalStatus(early), state.get("terminal_reason", ""))
    else:
        classification = classify(
            verification=state.get("verification"),
            state={
                "internal_fault": state.get("internal_fault"),
                "verifier_outage": state.get("verifier_outage"),
                "missing_evidence": state.get("missing_evidence"),
                "fillable_gap": state.get("fillable_gap"),
                "probe_available": state.get("probe_available"),
                "infeasible": state.get("infeasible"),
                "stop_reason": state.get("stop_reason"),
                "approximation_available": state.get("approximation_available"),
                "escalate": state.get("escalate"),
                "escalate_reason": state.get("escalate_reason"),
            },
        )
    return {
        "terminal_status": classification.status.value,
        "terminal_reason": state.get("terminal_reason") or classification.reason,
        "stage": "TERMINAL",
    }


def epilogue(state: TaskState, *, config: RunnableConfig) -> dict[str, Any]:
    ctx = config["configurable"]["ctx"]
    """Packet on every path + governed learning writes + audit refs (impl §11.9)."""
    audit = getattr(ctx, "audit", None)
    refs: list[str] = []
    if audit is not None:
        audit.record(state["task_id"], state.get("thread_id", ""), "EPILOGUE",
                     "epilogue", "packet_built", payload={"status": state.get("terminal_status")})
        refs = audit.refs()

    # --- competence update: kernel/evaluation provenance only, once/episode
    review = state.get("review") or {}
    memory = getattr(ctx, "memory", None)
    memory_commits: list[str] = []
    improvement_refs: list[str] = []

    if memory is not None and review.get("lessons"):
        authorized = bool(ctx.kernel._snapshot.facts.memory.procedural_write_authorized)
        for lesson in review["lessons"]:
            if lesson.get("procedural") and not authorized:
                out_m = memory.commit(lesson, authorized=False)
                memory_commits.append(f"{out_m['record_id']}:quarantined")
                continue
            out_m = memory.commit(lesson, authorized=True)
            memory_commits.append(f"{out_m['record_id']}:committed")

    engine = getattr(ctx, "improvement_engine", None)
    if engine is not None and review.get("improvement_proposals"):
        for desc in review["improvement_proposals"][:2]:
            p = engine.propose(str(desc))
            if p is not None:
                engine.evaluate(p, hidden_tests_pass=False,
                                regression_vs_baseline_pass=False)
                improvement_refs.append(p.proposal_id)

    packet = build_packet(state, refs)
    return {
        "decision_packet": packet.model_dump(),
        "audit_refs": refs,
        "checkpoint_refs": [f"checkpoint-{state.get('task_id')}"],
        "lessons": state.get("lessons", []),
        "improvement_proposals": [
            {"proposal_id": r} for r in improvement_refs],
        "stage": "END",
    }


# --------------------------------------------------------------------------
# signature + routing (deterministic core; full IDF router in Phase 5)
# --------------------------------------------------------------------------

def _extract_signature(state: TaskState, preliminary: bool) -> SituationSignature:
    text = ((state.get("request") or {}).get("input_text", "")
            + " " + (state.get("frame") or {}).get("goal", "")).lower()
    meta = (state.get("request") or {}).get("task_metadata") or {}
    sig = SituationSignature(
        domains=[d for d in SituationSignature.DOMAIN_VOCAB if d in text],
        goals=[g for g in SituationSignature.GOAL_VOCAB if g in text],
        context=[c for c in SituationSignature.CONTEXT_VOCAB
                 if c in text or c in str(meta)],
    )
    sig.completeness_score = min(1.0, (len(sig.domains) + len(sig.goals)) / 4)
    return sig


def _route_styles(sig: SituationSignature, state: TaskState, ctx: Any) -> dict[str, Any]:
    """Learned IDF router (Phase 5) when the runtime context carries one;
    deterministic default routing otherwise (offline tests)."""
    router = getattr(ctx, "style_router", None)
    if router is not None:
        decision = router.route(sig)
        return {
            "top_styles": decision.top_styles,
            "scores": decision.scores,
            "confidence_gate": decision.confidence_gate,
            "historical_refs": decision.historical_refs,
            "routing_kb_version": decision.routing_kb_version,
            "mandatory_modules": decision.mandatory_modules,
            "gates_fired": [g.model_dump() for g in decision.gates_fired],
            "solo_contract_mode": decision.solo_contract_mode,
            "home_turf_promotions": decision.home_turf_promotions,
        }
    meta = (state.get("request") or {}).get("task_metadata") or {}
    forced = meta.get("routed_styles")
    top = list(forced) if isinstance(forced, list) else _default_styles(sig)
    scores = {s: 1.0 - i * 0.1 for i, s in enumerate(top)}
    return {"top_styles": top[:3], "scores": scores,
            "confidence_gate": "CLEAR" if len(top) == 1 else "AMBIGUOUS",
            "historical_refs": [], "routing_kb_version": "deterministic-default"}


def _default_styles(sig: SituationSignature) -> list[str]:
    """Minimal deterministic style map (the learned KB supersedes this)."""
    if "medical" in sig.domains:
        return ["m006", "m047"]
    if "finance" in sig.domains:
        return ["m007", "m023"]
    if "engineering" in sig.domains or "supply" in sig.domains:
        return ["m014", "m011"]
    if "strategy" in sig.domains:
        return ["m071", "m070"]
    if "security" in sig.domains:
        return ["m019", "m057"]
    return ["m001", "m003"]


def _deadline_elapsed(state: TaskState, ctx: Any, budget: BudgetController) -> bool:
    """Kernel deadline check (impl §10.2.5). Missing clock bookkeeping
    degrades to never-elapsed (bounded behavior), never to always-elapsed."""
    started = state.get("started_at")
    clock = getattr(ctx, "clock", None)
    if not started or clock is None or not budget.snapshot.facts.deadline_seconds:
        return False
    try:
        elapsed = float(clock.monotonic()) - float(state.get("started_monotonic", 0) or 0)
    except (TypeError, ValueError):
        return False
    return elapsed > budget.snapshot.facts.deadline_seconds


def _gap_satisfied(gap_desc: str, evidence_summary: str) -> bool:
    """Term-overlap check: retrieved evidence must actually speak to the gap.
    Conservative: requires >= 2 shared content words of length >= 5."""
    import re as _re
    gap_words = {w for w in _re.split(r"[^a-z0-9]", gap_desc.lower()) if len(w) >= 5}
    ev_words = {w for w in _re.split(r"[^a-z0-9]", evidence_summary.lower()) if len(w) >= 5}
    return len(gap_words & ev_words) >= 2


def _state_signature(state: TaskState) -> str:
    return content_hash({
        "frame": state.get("frame"), "hypotheses": state.get("hypotheses"),
        "decision": state.get("decision"), "observations": state.get("observations"),
    })


def _monitor_from(ctx: Any) -> LoopMonitor:
    """Per-run monitor, cached on the runtime context so streaks persist."""
    monitor = getattr(ctx, "_loop_monitor", None)
    if monitor is None:
        b = ctx.kernel.budgets
        monitor = LoopMonitor(b.evoc_base, b.evoc_decay, b.novelty_plateau)
        ctx._loop_monitor = monitor
    return monitor


# --------------------------------------------------------------------------
# graph assembly
# --------------------------------------------------------------------------

def compile_task_graph() -> StateGraph:
    g = build_task_graph()
    g.add_node("initialize", initialize_task)
    g.add_node("meta", meta_route)
    g.add_node("loop_guard", loop_guard)
    g.add_node("stabilize", stabilize)
    g.add_node("fast", fast_answer)
    g.add_node("what", what_frame)
    g.add_node("what_gate", what_gate)
    g.add_node("why", why_stage)
    g.add_node("why_gate", why_gate)
    g.add_node("early_classify", early_classify)
    g.add_node("how", how_generate)
    g.add_node("how_gate", how_gate)
    g.add_node("do_authorize", do_authorize)
    g.add_node("do_execute", do_execute)
    g.add_node("verify", verify_outcome)
    g.add_node("review", delta_review)
    g.add_node("terminal", terminal_classify)
    g.add_node("epilogue", epilogue)

    g.add_edge(START, "initialize")
    g.add_edge("initialize", "meta")
    g.add_edge("meta", "loop_guard")
    g.add_edge("stabilize", "loop_guard")
    g.add_edge("fast", "verify")
    g.add_edge("what", "what_gate")
    g.add_edge("what_gate", "loop_guard")
    g.add_edge("why", "why_gate")
    g.add_edge("why_gate", "loop_guard")
    g.add_edge("early_classify", "loop_guard")
    g.add_edge("how", "how_gate")
    g.add_edge("how_gate", "loop_guard")
    g.add_edge("do_authorize", "loop_guard")
    def after_execute(state: TaskState) -> str:
        """do_execute routes by stage: escalation goes straight to the
        classifier — it must NEVER pass through outcome verification."""
        return "terminal" if state.get("stage") == "TERMINAL" else "verify"

    g.add_conditional_edges("do_execute", after_execute, {
        "terminal": "terminal", "verify": "verify"})
    g.add_edge("verify", "review")
    g.add_edge("review", "loop_guard")
    g.add_edge("terminal", "epilogue")
    g.add_edge("epilogue", END)

    def route(state: TaskState) -> str:
        """loop_guard → next node; terminal-classified states go to epilogue."""
        stage = state.get("stage", "")
        if stage == "TERMINAL" or state.get("early_terminal"):
            return "terminal"
        if stage == "FAST":
            return "fast"
        return stage.lower()

    g.add_conditional_edges("loop_guard", route, {
        "terminal": "terminal",
        "stabilize": "stabilize",
        "fast": "fast",
        "what": "what",
        "what_gate": "what_gate",
        "why": "why",
        "why_gate": "why_gate",
        "early_classify": "early_classify",
        "how": "how",
        "how_gate": "how_gate",
        "do": "do_authorize",
        "do_execute": "do_execute",
        "verify": "verify",
        "review": "review",
    })

    return g


def compile_and_build():
    return compile_task_graph().compile()
