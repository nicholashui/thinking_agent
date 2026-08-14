<!-- ============================================================
  LP10 — Implementation, MVTA & Roadmap (落地)
  Source file: thinking_agent.v8.md  (split part 10/12)
  ============================================================ -->
## 24. Reference Implementation Specification

### 24.1 Components

*(The v4 component table. Every component's interface appears in §24.3 — inlined in full, not by reference (V9): MetaRouter (route, compose), FrameCritic/Diagnostician (gates, diagnose), Explorer (generate, reject), CouncilOrchestrator (run\_council), SearchController (explore), Premortem, RedTeam, VerifierRegistry (verify\_candidate, verify\_outcome, needs\_second), Planner (build), SafetyKernel (attest, authorize, allowed\_subset, interrupt, issue\_authority\_token), ToolBroker (execute\_transactional), MemoryManager (retrieve, commit), ReviewEngine (review), CompetenceModel (update), ImprovementEngine (queue, evaluate), LoopMonitor, BudgetController, ExecutionMonitor (check — call site kept, design-level), AuditLog (record), TaskScheduler (checkpoint, resume), GoalManager (renegotiate — Phase-2, disclosed). The world binding is the ordered tuple of §24.1's components plus telemetry, audit-log, and the environment flag — the exact binding is the harness's* *`make_world()`* *(19 components + telemetry), documented in §24.3 (V9: no 22-name claim).)*

### 24.2 Shared task state

*(The v4 schema plus:* *`world`* *(the kernel-held facts store, V1),* *`identity_count`* *(V4),* *`stabilized`* *(V10),* *`outcome_cache`* *(V7),* *`gate_wait`* *(V8),* *`pending_wait`,* *`attested_class`,* *`verifier_outage`,* *`stakes`,* *`reliability_blocked`, producers,* *`_prev_alt_sig`,* *`result.status_reason/pending_timeout/l3`.)*

### 24.3 Core interface (inlined, v5)

*(The complete interface block — every signature the algorithm calls, plus the declared pseudocode-local helpers:* *`initialize_task_state`,* *`direct_answer`,* *`frame`,* *`check_exit_gate`,* *`diagnose`,* *`generate`,* *`constraints_violated`,* *`content_hash`,* *`tag_untrusted`,* *`should_reframe`* *(reads review content),* *`settle_best_of`,* *`verifier_unavailable`,* *`owner_unavailable`,* *`voi_positive`,* *`plan_stop_conditions_met`,* *`plan_escalation_conditions_met`,* *`authorized_procedural`,* *`verifier_kind`,* *`pending_record`,* *`classify_terminal`,* *`build_decision_packet`,* *`query_for(state)`* *(task-derived retrieval terms),* *`stabilize_pass(state)`* *(E5 containment triage),* *`state_hash(state)`* *(the outcome-cache key over observations/hypotheses/frame/alternatives),* *`report_for(decision_id, reports)`* *(selected-decision lookup),* *`observations_changed(state)`* *— each with a one-line contract (V9).* *`verifier_unavailable`* *and* *`voi_positive`* *are retained contracts (the v5 fill path replaces their v4 call sites; disclosed).)*

### 24.4 Main algorithm (v5 governed loop)

```python
def solve(request, context, checkpoint=None, world=default_world):
    # world.bind(): ordered components + telemetry + audit_log + env flags
    # world.facts: kernel-held store — ALL security knobs read only here (V1)
    state = initialize_task_state(request, context)
    state.stakes = world.facts["stakes"]                  # schema field (C1)
    state.identity_count = len(world.facts.get("verifier_identities", ["external_model"]))   # V4
    if checkpoint:
        state = task_scheduler.resume(checkpoint)         # HMAC-verified (§20.5)

    state.route = meta_router.route(state)                # competence-aware; compose()
    budget.consume(state, "route")

    # --- Fast path (E0/E1) — C6/C7 ---
    if state.route.effort_level <= 1:
        budget.consume(state, "fast_path")
        state.decision = direct_answer(state)             # internal-only (C6)
        state.verification = verifier.verify_outcome(state)
        state.result.status = ("SOLVED" if state.verification.success
                               else classify_terminal(state, telemetry))
        state.result.packet = build_decision_packet(state, state.result.status)
        audit_log.record("fast_path", telemetry.stats())
        task_scheduler.checkpoint(state, "FAST_PATH")
        if state.route.requires_review:                   # C7: E1 learning epilogue
            state.review = review_engine.review(state)
            competence_model.update(state, state.review.calibration)
            memory_manager.commit(state, state.review)
            if state.review.lessons:
                improvement_engine.queue(state, state.review)
        return state

    # --- Governed main loop ---
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        audit_log.record("loop_top", telemetry.stats())
        if ex := budget.check(state, telemetry):
            state.result.status = "RESOURCE_LIMITED"; state.result.status_reason = ex
            break
        cont, reason = loop_monitor.should_continue(state, telemetry)
        if not cont:
            state.result.status = ("RESOURCE_LIMITED"
                                   if ("budget" in reason or "iterations" in reason
                                       or "expected value" in reason
                                       or "unproductive" in reason or "plateau" in reason)
                                   else classify_terminal(state, telemetry))   # V8
            state.result.status_reason = reason
            break

        # V10: E5 stabilization — Chaotic tasks stabilize BEFORE diagnosis
        # (Cynefin act → sense → respond), bounded to one pass
        if state.route.effort_level == 5 and not state.stabilized:
            state.stabilized = True
            stabilize_pass(state)                          # containment triage
            state.risks.append({"mode": "stabilization", "contained": True})
            continue

        # WHAT: frame + gate (owner-unavailable → ESCALATED, V8/S41)
        if not state.frame:
            state.stage = "WHAT"
            state.frame = frame(state)
            gate = check_exit_gate("WHAT", state)
            if not gate.passed:
                state.risks.append(gate); state.frame = None
                state.gate_wait = True                     # V8: re-entry is progress
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result.status = ("ESCALATED" if owner_unavailable(state)
                                           else "NEEDS_EVIDENCE")
                    break
                continue
            audit_log.record("what", telemetry.stats())
            task_scheduler.checkpoint(state, "WHAT")

        # WHY: retrieve (V6: pre-hypothesis, priced by hits) → diagnose → gate
        if state.route.requires_diagnosis and not state.hypotheses:
            state.stage = "WHY"
            hits = memory_manager.retrieve(query_for(state), state)   # V6
            state.evidence.extend(hits)
            diagnose(state)                                # producers from world facts
            gate = check_exit_gate("WHY", state)           # G-WHY-4/-5 (V8/S42)
            if not gate.passed:
                state.risks.append(gate); state.hypotheses = []
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result.status = "NEEDS_EVIDENCE"
                    break
                continue
            audit_log.record("why", telemetry.stats())
            task_scheduler.checkpoint(state, "WHY")
            if (state.missing_evidence or state.probe_available or state.verifier_outage):
                if state.missing_evidence and world.facts.get("fillable_gap"):
                    fill = memory_manager.retrieve(world.facts["fillable_gap"], state)
                    if fill:                               # V11: REAL fill, not a flag
                        state.evidence.extend(fill)
                        state.missing_evidence = [g for g in state.missing_evidence
                                                  if g != world.facts["fillable_gap"]]
                elif state.verifier_outage and \
                     world.facts.get("action_class", "A2") in ("A3", "A4", "A5") and \
                     world.facts.get("requires_external_action", True):
                    pass                                   # V5: proceed to attest-time L3
                else:
                    state.result.status = classify_terminal(state, telemetry)
                    break

        # HOW: council / search / explorer → gated premortem → delta-verify
        if state.route.requires_generation and not state.alternatives:
            state.stage = "HOW"
            if state.route.use_council:
                (state.alternatives, state.minority_reports,
                 state.unresolved_disagreements) = council_orchestrator.run_council(state, verifier)
            elif state.route.requires_search:
                search_controller.explore(state, budget); generate(state)
            else:
                generate(state)
            audit_log.record("how", telemetry.stats())
        if not state.alternatives:
            state.result.status = classify_terminal(state, telemetry)
            break
        if constraints_violated(state):
            state.infeasible = True
            state.result.status = classify_terminal(state, telemetry)
            break
        candidates_new = content_hash(state.alternatives) != state._prev_alt_sig
        if candidates_new:                                 # C9: progress gating
            premortem(state)
            state._prev_alt_sig = content_hash(state.alternatives)
        reports = []
        for alt in state.alternatives:                     # §15.6 SHA-256 + kind
            h = sha256(content(alt) + verifier_kind(state))
            reports.append(state.verification_history.get(h)
                           or state.verification_history.setdefault(
                               h, verifier.verify_candidate(state, alt)))
        state.decision = select(state.alternatives, reports)
        if state.decision is None:
            state.result.status = classify_terminal(state, telemetry)
            break
        if state.decision.error_bound is not None:         # §15.5 producer
            state.approximation_available = True
            state.result.status = classify_terminal(state, telemetry)
            break
        gate = check_exit_gate("HOW", state)
        if not gate.passed:
            state.risks.append(gate)
            state.result.status = classify_terminal(state, telemetry)
            break
        # C8 + V4/V5/V14: attest early; deny misattestation and REPLICATE (V8);
        # L3 on the ATTESTED class; bar + identity on the SELECTED decision
        if state.decision.requires_external_action:
            attestation = safety_kernel.attest(state)
            if attestation.startswith("misattested"):
                state.result.status = "UNSAFE"
                safety_kernel.interrupt(state.task_id)
                break
            state.attested_class = attestation
            if state.verifier_outage and state.attested_class in ("A3", "A4", "A5"):
                state.result.status = "ESCALATED"          # L3 (V5/S29)
                state.result.l3 = True
                break
            bar, needs_second = verifier.class_bar(state)
            selected_rel = report_for(state.decision.id, reports).verifier_reliability
            if selected_rel < bar:                         # V14: SELECTED, not max
                state.reliability_blocked = True
                state.result.status = classify_terminal(state, telemetry)
                break
            if needs_second and state.identity_count < 2:  # V4: pre-DO, S39
                state.reliability_blocked = True
                state.result.status = classify_terminal(state, telemetry)
                break
        if candidates_new:                                 # C9
            if rejection := red_team.attack(state):
                state.risks.append(rejection)
                explorer.reject(state.decision.id)
                state.alternatives = []
                continue

        # DO: plan-once (V7) → authorize → PENDING kernel allowlist (V3) → execute
        if state.decision.requires_external_action:
            state.stage = "DO"
            if not state.plan:
                state.plan = planner.build(state, state.decision)   # V7: once per decision
            authorization = safety_kernel.authorize(state.plan, state.permissions,
                                                    state.risks, state.attested_class)
            if authorization.status in ("UNSAFE", "ESCALATED"):
                state.result.status = authorization.status
                safety_kernel.interrupt(state.task_id)
                break
            if authorization.status == "PENDING":
                if not state.subset_executed:              # V3: kernel table ONLY
                    subset = safety_kernel.allowed_subset(state.plan, world.facts)
                    for t in subset:
                        tool_broker.execute_transactional(state.plan, t, authorization.token)
                    state.subset_executed = True
                    state.risks.append(pending_record(subset))
                if state.iteration >= world.facts["pending_timeout"]:   # V1
                    state.result.status = "ESCALATED"
                    state.result.pending_timeout = True
                    break
                state.pending_wait = True                  # V8: wait exemption
                continue
            observations = tool_broker.execute_transactional(state.plan, authorization.token)
            state.observations.extend(tag_untrusted(observations))
            audit_log.record("do", telemetry.stats())
            task_scheduler.checkpoint(state, "DO")
            if plan_stop_conditions_met(state.plan, state):
                state.result.status = classify_terminal(state, telemetry)
                break
            if plan_escalation_conditions_met(state.plan, state):
                state.result.status = "ESCALATED"
                break
            monitor = execution_monitor.check(state)       # design-level findings

        # V7: outcome verification delta-cached on the state hash
        outcome_key = sha256(state_hash(state))
        if outcome_key in state.outcome_cache:
            state.verification = dict(state.outcome_cache[outcome_key])
            state.reliability_blocked = state.verification.reliability_blocked  # preserve
        else:
            state.verification = verifier.verify_outcome(state)
            state.outcome_cache[outcome_key] = dict(state.verification)
        if state.verification.success:
            state.result.status = "SOLVED"
            break

        # V7: in-loop review gated on delta; should_reframe reads review content
        if candidates_new or state.verification.ambiguous or observations_changed(state):
            state.review = review_engine.review(state)
            state._prev_obs = list(state.observations)
        if should_reframe(state.review, state):
            if state.iteration < REFRAME_BUDGET:
                state.frame = None; state.hypotheses = []; state.alternatives = []
                continue
            state.frame = settle_best_of(state.frame, state.review)
            state.hypotheses = []; state.alternatives = []
            continue
        if (state.verification.ambiguous or state.missing_evidence
                or state.reliability_blocked or state.probe_available
                or state.approximation_available or state.infeasible):
            state.result.status = classify_terminal(state, telemetry)
            break

    # --- Common epilogue (V7: review gated on outcome/decision/lessons) ---
    if state.decision is not None or state.executed_actions or world.facts.get("lesson_type"):
        state.review = review_engine.review(state)
        competence_model.update(state, state.review.calibration)   # V2 provenance gate
        if authorized_procedural(state):                   # world policy, not task flag
            tok = safety_kernel.issue_authority_token("procedural")
            for lesson in state.review.lessons:
                lesson.authority = tok
        else:
            safety_kernel.issue_authority_token("procedural")     # audit trail
        memory_manager.commit(state, state.review)
        if state.route.requires_review and state.review.lessons:
            queued = improvement_engine.queue(state, state.review)
            if queued and world.facts["baseline_frozen"]:          # V1
                for p in state.improvement_proposals:
                    improvement_engine.evaluate(state, p)
    state.result.packet = build_decision_packet(state, state.result.status)
    audit_log.record("epilogue", telemetry.stats())
    task_scheduler.checkpoint(state, "EPILOGUE")
    return state
```

Guarantees (each demonstrated by the harness, §32):

1. **Termination** — bounded by LoopMonitor: iteration/token/call budgets, novelty plateau (→ RESOURCE\_LIMITED, V8), repetition, EVOC; waits exempt but budget-bounded (V8).
2. **State completeness** — all eight states reachable through world-fact-driven producers (S1–S45).
3. **Packet completeness** — every terminal path, including denials, PENDING timeouts, and early exits, produces the packet; decided-early exits skip empty reviews (V7).
4. **Verification independence** — SOLVED requires external identity ∧ reliability ≥ bar ∧ identity-registry second-verifier rule; reliability is kernel-held (C2) with provenance-gated competence (V2); no below-bar or below-identity execution (V4/V14).
5. **Cost boundedness** — envelope metered; progress gating (C9); planner-once (V7); outcome delta-cache (V7); priced-by-result retrieval (V6); deterministic 0-price (C32).
6. **Gate enforcement** — WHAT/WHY/HOW gates; WHY re-evaluable (C15) with G-WHY-4/-5 exercisable (V8); plan stop/escalation conditions consumed (C16).
7. **Review in loop** — gated AAR on non-terminal exits; gated terminal review; competence once per episode with kernel feed (V2).
8. **Resume** — checkpoints at stage boundaries; crash/resume without double-execution (S21); integrity boundary per §20.5/§32.4.

### 24.5 Session and scheduler layer

*(Per v4: TaskScheduler identity/priority/checkpoint-resume;* *`renegotiate`* *Phase-2, disclosed; LearningScheduler triggers defined, design-level.)*

### 24.6 Component–call-site map

*(The v4 map, updated: MemoryManager* *`retrieve`* *(pre-hypothesis, in* *`diagnose`), SafetyKernel* *`allowed_subset`* *(PENDING, world-keyed),* *`attest`* *(REPLICATE denial), CompetenceModel (provenance gate), LoopMonitor (gate\_wait/pending\_wait exemptions), stabilize pass (E5), outcome cache (V7), ExecutionMonitor (call site kept, findings design-level).)*

***

## 25. Minimal Viable Thinking Agent

*(The 11-step MVP order per v4 with the inlined 5-test suite (each mapping to a harness assert), the freeze procedure, and the Phase-0/Phase-1 tool dependencies stated. The world-facts store is the MVP's kernel config file, read-only to the model's tools — the read path is v5-enforced; the write path's process boundary is Phase-1 (disclosed).)*

***

## 26. Roadmap Toward AGI and ASI Research

*(Phases 0–7 per v4: Phase 1 adds the world-store write boundary and checkpoint HMAC key management; Phase 2 adds EvaluationPlane batch feedback, the co-scaling gate, and* *`renegotiate`; Phase 3 model heterogeneity; Phase 4 the probe life-cycle; Phase 5 open-ended search.)*

***

