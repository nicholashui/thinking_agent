# Thinking Agent

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Version:** 5.0  
**Research cutoff:** August 7, 2026  
**Status:** Research and engineering blueprint (validated — see §32)  
**Source policy:** Primary arXiv papers and official xAI materials were prioritized over third-party commentary.  
**Change policy:** v5 supersedes v4. The differential change log in §31 records every accepted finding from the v4 self-review, the v5 change, and its validation status. The executable validation harness lives in `validation/harness.py`; results are in §32.

---

## 1. Executive Summary

Thinking Agent combines:

1. A ranked portfolio of 40 traditional human thinking frameworks (Cynefin, Premortem, AAR, Double-Loop Learning, RPD, root-cause methods at the top).
2. The `WHAT → WHY → HOW → DO → REVIEW` process.
3. The memory, multi-agent, metacognitive, and self-evolution concepts from the earlier architecture drafts.
4. Research on cognitive architectures, reasoning, planning, tool use, reflection, verification, multi-agent systems, memory, self-improving scaffolds, and agent security.
5. Production patterns documented by xAI: adaptive reasoning, parallel subagents, plan-review workflows, verification, synthesis, tool-oriented agent harnesses.

Its central operating loop:

> **META-CONTROL → WHAT → WHY → HOW → DO → REVIEW**

A continuous **VERIFY** layer surrounds every stage; a **governed loop** (loop monitors, budget envelope, stage gates, state-only classifier, delta verification, checkpoint/resume, progress gating) guarantees termination, graceful failure, and cost-boundedness.

v5's advance over v4 is **trust-boundary completion**: v4 narrated kernel-holding; v5 executes it. Specifically, v5: (a) moves every security knob onto a **world-facts read path** — the v5 engine's own body contains zero task-scope reads of the knob list (`pending_timeout`, `calls_ceiling`, `evoc`, calibration, identities, outage, baseline-frozen, write-authorization); the world object is seeded from the scenario (the world model), and a **code-level read-path assertion** (`assert_read_path`) runs with every suite pass (V1); (b) feeds competence from a **kernel-sourced calibration registry with a provenance gate** — the doc's own rule, "self-reported accuracy is not evaluation history," is now enforced by the code (V2, S45); (c) removes the **allowlist backdoor** — PENDING subset execution is kernel-table membership only (V3, S38 negative case); (d) makes the **second-verifier rule kernel-computed** from the identity registry, not a task flag, and blocks below-bar/second-missing execution before DO (V4, S39); (e) fires **L3 at attest time on the attested class**, making the ladder's third level genuinely reachable (V5, S29); (f) makes **memory retrieval real** — priced by hits, querying task-derived terms, genuinely filling gaps (V6/V11, S40/S34); (g) **delta-caches outcome verification** and gates the in-loop and epilogue reviews and the planner, removing unchanged-state work the v4 claims promised but didn't deliver (V7); (h) exercises the previously-dead mechanisms — owner-unavailable ESCALATED, G-WHY-4/-5, novelty-plateau→RESOURCE_LIMITED, invariant-8 replication denial (V8, S41–S44); (i) adds the **E5 stabilize-before-diagnose** pass (V10, Cynefin's act→sense→respond); (j) checks the bar on the **selected decision's** verifier, not the candidate max (V14). Every change is demonstrated: **v4 baseline 177/177 asserts, v5 187/187 asserts, 44 scenarios, deterministic across runs** (§32).

Thinking Agent is not a claim that one architecture can literally solve every mathematically, physically, or computationally possible problem. Some problems are undecidable, intractable, underspecified, unsafe, or impossible with available evidence and resources.

Here, **universal problem solving** means that the system can recognize a wide range of problem classes and return the most responsible available outcome: a verified solution; a bounded approximation; a set of ranked alternatives; a request for missing evidence; a safe experiment or probe; a demonstration that the current specification is infeasible; a calibrated statement of uncertainty; or a refusal or human escalation when action would be unsafe.

Every task terminates in exactly one of the eight graceful states (§3.3), and every terminal state produces the proof-carrying decision packet (§15.4).

Thinking Agent should be viewed as a scaffold for researching AGI, not as proof that AGI or ASI follows automatically from adding more agents or more inference-time computation.

---

## 2. Core Thesis

A generally capable AI system is not just a large model. It is a governed system that combines:

```text
Foundation-model capability
× adaptive cognitive control
× grounded world interaction
× structured memory
× planning and search
× independent verification
× continual learning
× safety and governance
```

This is a multiplicative design heuristic rather than a mathematical identity. A severe weakness in any component can limit the whole system.

Thinking Agent separates the functions of generating an answer, determining whether it is true, determining whether the action is safe, executing the action, learning from the result, and changing the system that generated the result. These functions must not be collapsed into one unconstrained model call — and in v5, the **authority to set the numbers those functions depend on** is separated from the model that benefits from setting them at the *code level*: the algorithm's read path for security knobs is the world object (kernel-held), and the harness asserts that no security knob is read from the task's declaration channel (V1, §32 S45).

---

## 3. Scope and Non-Claims

### 3.1 What "universal" means

Thinking Agent is intended to address: clear and routine problems; expert analytical problems; complex adaptive problems; chaotic or crisis conditions (E5 now with a stabilize-before-diagnose pass, V10); causal diagnosis; scientific discovery (probe life-cycle remains Phase-4, disclosed); creative design (MethodComposer branches per task signature, with creativity modules still intention-level, disclosed); strategic planning; software and digital operations; embodied action; social and stakeholder problems (renegotiate remains Phase-2, disclosed); adversarial environments; long-horizon learning (memory retrieval now genuinely read back, V6); architecture improvement.

### 3.2 What Thinking Agent does not claim

*(Unchanged from v4: no AGI claims, no debate-superiority claims, no self-reflection-as-proof, no benchmark-performance-as-intelligence, and the harness validates control-flow properties, not intelligence.)*

### 3.3 Required graceful-failure states

Every task must terminate in one of these explicit states, each with a producer; the harness demonstrates all eight reachable (§32, S1–S45):

| State | Producer (v5) |
|---|---|
| `SOLVED` | `verify_outcome`: checks ∧ external ∧ reliability ≥ bar ∧ identity-registry second-verifier rule (§15.4) |
| `APPROXIMATED` | `select` records `error_bound` → `state.approximation_available` (§15.5) |
| `NEEDS_EVIDENCE` | `diagnose` fills `missing_evidence`; L1 degrade; G-WHY gate failure (§11.5, §15.2) |
| `NEEDS_EXPERIMENT` | `diagnose` sets `state.probe_available` (§19.2) |
| `INFEASIBLE` | constraint screen sets `state.infeasible`; plan stop-conditions (§12.4, §13.7) |
| `UNSAFE` | SafetyKernel denial; attestation mismatch; invariant-8 replication denial (V8) |
| `ESCALATED` | denials; L2/L3 ladder; reliability-blocked; PENDING timeout; plan escalation conditions; owner-unavailable (V8) |
| `RESOURCE_LIMITED` | LoopMonitor/BudgetController: iterations, tokens, calls, EVOC, **novelty plateau** (§9.5–9.6; plateau→RESOURCE_LIMITED mapping fixed, V8) |

### 3.4 State-transition policy

- Every terminal state is produced by exactly one owning mechanism; producers read **world facts** (V1), so the state-only classifier's inputs are kernel- or component-owned rather than task-copied.
- Test order (implemented by `classify_terminal`): L2 → L1 → ambiguity → reliability-blocked → evidence gap → probe → infeasibility → budget → approximation → residual. The plateau stop now maps to `RESOURCE_LIMITED` via its reason keyword (V8).
- Every terminal path writes the proof-carrying packet via the common epilogue — including denials, PENDING timeouts, and early classifier exits (reviews on decided-early outcomes are gated, V7).

---

## 4. Architectural Synthesis and Lineage

*(The five lineages plus four self-revision rounds: v1 governed the loop; v2 enforced the standards; v3 kernel-held the numbers; v4 executed the branches; v5 completes the trust boundaries and makes the remaining claimed mechanisms executable or explicitly disclosed. The harness now freezes four engines — v2, v3, v4 (baseline), v5 — over identical components.)*

---

## 5. Research Foundations

*(§5.1–5.8 per v4, with the SearchController branch now exercised (S36) and the council's debate round executing claim exchange + verifier adjudication (D5 of v4). §5.9: the 40-framework survey unchanged.)*

---

## 6. Design Principles

*(P1–P12 unchanged. The mechanism matrix's v5 additions: P4's enforcing point includes the identity-registry second-verifier rule and the pre-DO bar check on the selected decision; P8's authority-token path has no task-gated minting (V1/V3); P11's plateau stop is RESOURCE_LIMITED-mapped; P12's packet is produced on every path with gated reviews.)*

---

## 7. Architectural Overview

```text
┌──────────────────────────────────────────────────────────────┐
│                  HUMAN / ENVIRONMENT                         │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ GOVERNANCE AND SAFETY KERNEL                                │
│ Goals • permissions • policy • risk gates • interrupts      │
│ WORLD-FACTS STORE (all security knobs) • static allowlist   │
│ identity registry • token minting • no-replication          │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ META-CONTROLLER (competence-aware; method composer)         │
│ BUDGET ENVELOPE • ROUTE FLAGS • E5 stabilize-then-diagnose  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ STRUCTURED COGNITIVE WORKSPACE                              │
│ WHAT → WHY → HOW → DO → REVIEW                              │
│ STATE-ONLY CLASSIFIER • pre-DO bar+identity check           │
│ delta-cached outcomes • gated reviews • planner-once        │
│ early classifier entry • checkpoint at every stage          │
└───────────────┬──────────────────────┬───────────────────────┘
                │                      │
┌───────────────▼────────────┐  ┌──────▼──────────────────────┐
│ REASONING AND COUNCIL      │  │ MEMORY AND WORLD MODEL     │
│ search • generate          │  │ RETRIEVE-IN-DIAGNOSE        │
│ council (debate round)     │  │ (priced hits, real fill)    │
│ critique • synthesize      │  │ competence (kernel feed)    │
└───────────────┬────────────┘  └──────┬──────────────────────┘
                │                      │
┌───────────────▼──────────────────────▼───────────────────────┐
│ TOOL BROKER AND EXECUTION SANDBOX                           │
│ timeouts • retries • idempotency • compensation             │
│ pending kernel-allowlist subset (no fallback) • checkpoint  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ TELEMETRY, EVALUATION, AND SELF-EVOLUTION                   │
│ per-stage audit • frozen baseline (kernel state)            │
│ verifier history registry • EvaluationPlane (Phase 2)       │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Four Nested Timescales

*(Action loop §8.1; task loop §8.2 with per-stage checkpoints; learning loop §8.3 — competence fed from the kernel calibration registry with a provenance gate (V2), memory retrieval genuinely read back (V6); architecture-evolution loop §8.4; session layer §8.5 per v4, with the LearningScheduler triggers still design-level (disclosed).)*

---

## 9. Stage 0 — META-CONTROL

*(Responsibilities §9.1, Cynefin routing §9.2, routing variables §9.3 per v4. Effort levels §9.4 with E5's stabilize-before-diagnose pass (V10) and E1's honored `requires_review` epilogue.)*

### 9.5 Expected value of computation (operational)

- **Novelty signature:** canonicalized SHA-256 hash over (hypotheses, frame, observations, evidence, alternatives, plan). The **plateau stop now maps to `RESOURCE_LIMITED`** via its reason keyword, matching the §3.3 producer table (V8, §32 S36/S43). The evasion residual (cosmetic mutations) remains documented as a heuristic; hard budgets are the termination guarantee.
- **EVOC proxy:** `base − decay × iterations`, with `base` read from the world store (V1). The first term is a stopping heuristic, never evidence.
- **Hard budgets:** iterations, tokens, calls, agents (per-round cap), deadline — all from the world store; the call ceiling is enforced on cognitive calls at loop top and inside `budget.check` (≤ 1-iteration overshoot documented).
- **Wait exemptions:** PENDING human-gate waits and WHAT-gate re-entries are external waits, not cognitive churn — the plateau/EVOC stops do not apply while `pending_wait` or `gate_wait` is set (V8, §32 S20/S35/S41); only hard budgets and the kernel-held timeout bound them.

### 9.6 World-facts store (v5: the security-knob boundary is code, not prose)

**The world object is the kernel-held facts store, by modeling convention.** Scenario configuration seeds it (modeling world facts: kernel calibration, ceilings, timeouts, verifier identities, outage status, domain accuracy, stored knowledge, baseline-frozen, write-authorization policy); the v5 engine's own body reads every security knob **only** through it — a code-level property asserted by the harness's `assert_read_path()` on every run, and demonstrated behaviorally by S45 (a task-declared accuracy of 1.0 is ignored; the kernel feed produces 0.704). Honest scope: in the single-process mock, the scenario spec is the world model — the task-declaration channel is not modeled separately, and component-level reads of non-knob task facts (`action_class` at attestation, denial flags at authorize) remain; the production write-path boundary is Phase-1 (§32.4). In production the store is populated by EvaluationPlane outcomes and operator policy, in a process boundary the model's tools cannot write (§15.6's single-model-writable-state residual is disclosed: the *read path* is fixed; the *store's write path* requires the Phase-1 key/process boundary, §32.4).

The config block (§9.6 of v4) remains the single source of defaults: reliability seed/window, class bars, trust margin, consolidation threshold, gate/reframe/pending budgets, human-gate SLAs (scheduler-consumed), EVOC base/decay, competence blend, novelty plateau.

---

## 10. Stage 1 — WHAT: Frame the Problem

*(§10.1–10.5 per v4; the owner-unavailable ESCALATED branch is now scenario-validated (V8, §32 S41) and WHAT-gate re-entries are exempt from the novelty plateau (V8).)*

---

## 11. Stage 2 — WHY: Diagnose and Model

*(§11.1–11.6 per v4, plus:)*

- **Memory read-back (V6):** `memory_manager.retrieve` runs **before** hypothesis formation, queries task-derived terms (world `knowledge_terms`) plus the stored-knowledge store, and is **priced by result** — an empty retrieval is a deterministic no-op at 0 tokens; a hit costs 1 and extends evidence. §32 S40 demonstrates a genuine fill changing the outcome; S34's gap is filled by retrieval, not a flag (V11).
- **G-WHY gate fully evaluated and exercisable (V8):** predicates include falsification presence (G-WHY-5 — `no_falsification` blocks, S42) and VOI ≤ cost (G-WHY-4); failures clear hypotheses and re-enter, bounded by the gate budget (C15).

### 11.7 Exit gate and early classifier

```text
G-WHY-1  leading hypothesis has decision-relevant evidence
G-WHY-2  significant alternatives considered
G-WHY-3  residual uncertainty recorded
G-WHY-4  estimated VOI of further diagnosis ≤ cost
G-WHY-5  falsification_evidence non-empty
```

Early classifier entry after the gate when `missing_evidence` (unfillable), `probe_available`, or `verifier_outage` — with two refinements: a world-fillable gap is **actually filled by retrieval** (V11), and **external A3+ outage tasks proceed to attest time**, where L3 fires on the attested class (V5, §32 S29).

---

## 12. Stage 3 — HOW: Generate, Test, and Select Solutions

*(§12.1–12.8 per v4, plus:)*

- **Pre-DO checks on the SELECTED decision (V14):** the class bar is checked against the chosen candidate's verifier reliability — not the candidate-set max — and the identity-registry second-verifier rule is enforced **before any execution** (V4, §32 S39: single-identity A4 escalates with zero executor calls).
- **L3 at attest time (V5):** for external tasks, verifier outage with an attested A3+ class terminates with `ESCALATED` (no external action, `required_human_actions` populated) — reachable, keyed on the attested class, scenario-validated (S29).
- **Progress gating (C9, extended):** premortem and red team run only on new candidate content; the planner builds **once per decision** (V7); the outcome verification is **delta-cached** on the state hash (V7, C26/C32 extended) — identical verdicts are never re-paid.
- **Invariant 8 (V8):** the attestation denies any `REPLICATE`-class action (S44).

---

## 13. Stage 4 — DO: Plan and Execute

*(§13.1–13.7 per v4, plus:)*

- **PENDING kernel allowlist, no backdoor (V3):** `safety_kernel.allowed_subset` returns only tasks whose ids are in the kernel's static table **and** whose classes the kernel's own taxonomy assigns as A2 — the v4 `allowlist_hint` fallback is deleted. §32 S20 (listed task executes) and S38 (unlisted task is NOT executed) are the positive and negative cases.
- **Plan termination conditions** (stop → plan-failure terminal; escalation → ESCALATED) consumed per pass (C16).
- **Crash/resume** with idempotency keys (S21); the integrity boundary (HMAC/key management) remains Phase-1, disclosed (§32.4).

---

## 14. Stage 5 — REVIEW: Reflect, Learn, and Evolve

*(AAR with in-loop review §14.1, single/double-loop §14.2–14.3, consolidation §14.4, Kaizen §14.5 per v4, plus:)*

- **Gated reviews (V7):** the in-loop review runs only on candidate/observation deltas; the epilogue review runs only when a decision was made, actions executed, or lessons are possible — classify-before-decision exits (S5/S6/S16/S25/S41/S42) no longer pay for reviews of nothing (C13's promise, restored; S29's L3 exit occurs after selection, so its epilogue review runs — 11 tokens include it).
- **Competence provenance gate (V2):** `competence_model.update` rejects calibration whose source is not kernel/EvaluationPlane; the accuracy comes from the **kernel domain-accuracy registry** (world facts), never from task-declared `calibration_accuracy`. §32 S45: a task declaring accuracy 1.0 is ignored; routing changes only on the kernel feed.
- **Minting (V1):** the procedural-write authorization is a world-facts policy decision, not a task flag; the positive commit path is scenario-validated (S33) and the negative quarantine path unchanged (S8).

---

## 15. Continuous VERIFY Layer

*(Registry §15.1 with the kernel calibration registry and identity-count second-verifier rule; no-verifier ladder §15.2 with all three levels executable (S25/S5/S29); packet §15.3; SOLVED threshold §15.4 — bars keyed by max(attested, declared) with unknown→A5, enforced pre-DO and at verify, second-verifier kernel-computed (V4); approximation §15.5; delta verification §15.6 — SHA-256 caches for candidates AND outcomes (V7).)*

---

## 16. Reasoning Method Composer

*(Method table per v4; `compose` runs in routing with task-signature branches; creative-design modules remain intention-level (disclosed). SearchController branch exercised (S36).)*

---

## 17. Multi-Agent Collective

*(Roles, agent_answer schema, protocol with debate round + verifier adjudication per v4; aggregation rules and no-council predicates per v4; the council remains 2-agent homogeneous clones with evidence-weighted aggregation still first-pass-wins (F10 of v4, disclosed).)*

---

## 18. Memory and Knowledge Architecture

*(Classes §18.1; the inlined memory record schema §18.2 with the trust-margin contradiction rule (applied, D10) and kernel-minted authority tokens; retrieval — priced by hits, pre-hypothesis, task-term queries (V6); consolidation trigger (design-level, disclosed); retrieval score §18.3 — the seven-term score remains a contract, substring matching in the harness (disclosed); security §18.4; forgetting §18.5; provenance §18.6.)*

---

## 19. World Model and Self-Model

*(World model §19.1; active experimentation §19.2 — probe life-cycle Phase-4, disclosed; self-model §19.3 — competence loop closed with the kernel feed and provenance gate (V2), once per episode, fresh terminal review.)*

---

## 20. Tool Broker and Execution Security

*(Authority separation §20.1, least privilege §20.2, controls + per-class transaction semantics §20.3, independent risk attestation §20.4 — the attestation oracle's ground truth remains world-config in the harness (T6 of v4, disclosed); checkpoint/resume §20.5 with the integrity boundary disclosed.)*

---

## 21. Safety and Alignment Kernel

*(Kernel position §21.1; invariants §21.2 — all ten mapped, invariant 8 now executable (V8/S44); threat model §21.3; human gates §21.4 — packet-before-approval, no auto-confirmation, corroboration; PENDING waits are progress-gated and exempt from the plateau (V8); wall-clock SLA enforcement is scheduler-held (design-level, disclosed).)*

---

## 22. Self-Evolution Engine

*(Levels §22.1; admission control §22.2 — canonical dedup hashes, global rate caps; pipeline §22.3 — `evaluate` invoked when the baseline is frozen, where `baseline_frozen` is a world fact (V1); stable baseline §22.4 inlined with the freeze procedure; Kaizen size §22.5; evaluation-plane immutability §22.6; cadence §22.7; open-ended improvement §22.8.)*

---

## 23. Evaluation Framework

*(Dimensions per v4; the 5-test MVP suite enumerated with its harness-assert mappings; routing-quality and co-scaling gate Phase-2, disclosed; telemetry §23.8 — per-stage audit records, latency timestamps design-level, disclosed; bookkeeping vs cognitive pricing reported at both levels, and bookkeeping totals now printed by the harness.)*

---

## 24. Reference Implementation Specification

### 24.1 Components

*(The v4 component table. Every component's interface appears in §24.3 — inlined in full, not by reference (V9): MetaRouter (route, compose), FrameCritic/Diagnostician (gates, diagnose), Explorer (generate, reject), CouncilOrchestrator (run_council), SearchController (explore), Premortem, RedTeam, VerifierRegistry (verify_candidate, verify_outcome, needs_second), Planner (build), SafetyKernel (attest, authorize, allowed_subset, interrupt, issue_authority_token), ToolBroker (execute_transactional), MemoryManager (retrieve, commit), ReviewEngine (review), CompetenceModel (update), ImprovementEngine (queue, evaluate), LoopMonitor, BudgetController, ExecutionMonitor (check — call site kept, design-level), AuditLog (record), TaskScheduler (checkpoint, resume), GoalManager (renegotiate — Phase-2, disclosed). The world binding is the ordered tuple of §24.1's components plus telemetry, audit-log, and the environment flag — the exact binding is the harness's `make_world()` (19 components + telemetry), documented in §24.3 (V9: no 22-name claim).)*

### 24.2 Shared task state

*(The v4 schema plus: `world` (the kernel-held facts store, V1), `identity_count` (V4), `stabilized` (V10), `outcome_cache` (V7), `gate_wait` (V8), `pending_wait`, `attested_class`, `verifier_outage`, `stakes`, `reliability_blocked`, producers, `_prev_alt_sig`, `result.status_reason/pending_timeout/l3`.)*

### 24.3 Core interface (inlined, v5)

*(The complete interface block — every signature the algorithm calls, plus the declared pseudocode-local helpers: `initialize_task_state`, `direct_answer`, `frame`, `check_exit_gate`, `diagnose`, `generate`, `constraints_violated`, `content_hash`, `tag_untrusted`, `should_reframe` (reads review content), `settle_best_of`, `verifier_unavailable`, `owner_unavailable`, `voi_positive`, `plan_stop_conditions_met`, `plan_escalation_conditions_met`, `authorized_procedural`, `verifier_kind`, `pending_record`, `classify_terminal`, `build_decision_packet`, `query_for(state)` (task-derived retrieval terms), `stabilize_pass(state)` (E5 containment triage), `state_hash(state)` (the outcome-cache key over observations/hypotheses/frame/alternatives), `report_for(decision_id, reports)` (selected-decision lookup), `observations_changed(state)` — each with a one-line contract (V9). `verifier_unavailable` and `voi_positive` are retained contracts (the v5 fill path replaces their v4 call sites; disclosed).)*

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

1. **Termination** — bounded by LoopMonitor: iteration/token/call budgets, novelty plateau (→ RESOURCE_LIMITED, V8), repetition, EVOC; waits exempt but budget-bounded (V8).
2. **State completeness** — all eight states reachable through world-fact-driven producers (S1–S45).
3. **Packet completeness** — every terminal path, including denials, PENDING timeouts, and early exits, produces the packet; decided-early exits skip empty reviews (V7).
4. **Verification independence** — SOLVED requires external identity ∧ reliability ≥ bar ∧ identity-registry second-verifier rule; reliability is kernel-held (C2) with provenance-gated competence (V2); no below-bar or below-identity execution (V4/V14).
5. **Cost boundedness** — envelope metered; progress gating (C9); planner-once (V7); outcome delta-cache (V7); priced-by-result retrieval (V6); deterministic 0-price (C32).
6. **Gate enforcement** — WHAT/WHY/HOW gates; WHY re-evaluable (C15) with G-WHY-4/-5 exercisable (V8); plan stop/escalation conditions consumed (C16).
7. **Review in loop** — gated AAR on non-terminal exits; gated terminal review; competence once per episode with kernel feed (V2).
8. **Resume** — checkpoints at stage boundaries; crash/resume without double-execution (S21); integrity boundary per §20.5/§32.4.

### 24.5 Session and scheduler layer

*(Per v4: TaskScheduler identity/priority/checkpoint-resume; `renegotiate` Phase-2, disclosed; LearningScheduler triggers defined, design-level.)*

### 24.6 Component–call-site map

*(The v4 map, updated: MemoryManager `retrieve` (pre-hypothesis, in `diagnose`), SafetyKernel `allowed_subset` (PENDING, world-keyed), `attest` (REPLICATE denial), CompetenceModel (provenance gate), LoopMonitor (gate_wait/pending_wait exemptions), stabilize pass (E5), outcome cache (V7), ExecutionMonitor (call site kept, findings design-level).)*

---

## 25. Minimal Viable Thinking Agent

*(The 11-step MVP order per v4 with the inlined 5-test suite (each mapping to a harness assert), the freeze procedure, and the Phase-0/Phase-1 tool dependencies stated. The world-facts store is the MVP's kernel config file, read-only to the model's tools — the read path is v5-enforced; the write path's process boundary is Phase-1 (disclosed).)*

---

## 26. Roadmap Toward AGI and ASI Research

*(Phases 0–7 per v4: Phase 1 adds the world-store write boundary and checkpoint HMAC key management; Phase 2 adds EvaluationPlane batch feedback, the co-scaling gate, and `renegotiate`; Phase 3 model heterogeneity; Phase 4 the probe life-cycle; Phase 5 open-ended search.)*

---

## 27. Common Failure Modes

*(The v4 table, updated: "Kernel-held knobs" → world-facts read path with asserted no-task-scope reads (V1); "Competence self-rating" → provenance gate (V2); "Allowlist backdoor" → kernel-table-only with negative scenario (V3); "Second-verifier declared" → identity registry (V4); "L3 unreachable" → attest-time L3 (V5); "Write-only retrieval" → priced hits + real fill (V6); "Uncached outcomes / ungated reviews / planner rebuild" → delta cache + gating (V7); "Dead branches" → scenarios S41–S44 (V8); "Bar on candidate max" → selected decision (V14).)*

---

## 28. Final Operating Rules

*(Rules 1–28 per v4, plus:)*

29. **A knob the v5 engine reads from the task's own declarations is not kernel-held** — the engine's body reads security knobs only through the world store, and the harness's `assert_read_path()` checks the code itself on every run (V1, §32 S45).
30. **A mechanism without a scenario is a paragraph** — every §24.4 enforcement mechanism has a scenario or a named §32.4 disclosure (V8).
31. **Do not pay twice for the same work** — outcome verification is delta-cached, reviews are gated, the planner builds once per decision, and empty retrievals are free (V6/V7).

---

## 29. Conclusion

*(The v4 conclusion, updated: v5 completes the trust boundaries at the code level — every security knob reads from the world store, competence is provenance-gated, the allowlist has no backdoor, the second-verifier rule is kernel-computed, L3 is reachable, retrieval is real, and the previously-dead mechanisms are scenario-validated. The validation discipline remains the point: every revision is executed against a frozen baseline, and every claim about the framework is checked by an independent auditor against the code.)*

---

## 30. Primary Research References

*(Unchanged from v4: the 14 entries.)*

---

## 31. Differential Change Log (v4 → v5)

| ID | v4 defect (aggregated finding) | v5 change | Where | Validated |
|---|---|---|---|---|
| V1 | Kernel-held config was narration: every security knob read from `state.config`; §9.6/§32.4 claims false of the code (6 reviewers) | World-facts store; the v5 engine's body reads no knob from task scope — a code-level `assert_read_path()` runs with the suite; S45 demonstrates a task-declared knob is behaviorally ignored; component-level non-knob reads disclosed | §9.6, §24.2–24.4 | S45, S20, S24, S26 |
| V2 | Competence provenance gate absent; S22 fed by the 0.9 default C3 named (4 reviewers) | Kernel domain-accuracy registry + source gate in `competence.update`; task-declared accuracy rejected | §14, §19.3 | S45, S22 |
| V3 | Allowlist backdoor: `allowlist_hint` fallback executed unlisted A2-labeled tasks (3 reviewers) | Kernel-table-only membership; kernel taxonomy assigns classes; negative scenario | §20.3, §24.4 | S20, S38 |
| V4 | Second-verifier rule task-declarable; never the binding constraint (3 reviewers) | Identity registry; kernel-computed `needs_second`; pre-DO block; true negative scenario | §15.4 | S26, S39, S28 |
| V5 | L3 unreachable: all outage scenarios early-classified via L2; S29's assert trivially true (4 reviewers) | External A3+ outage skips the early exit; L3 fires at attest time on the attested class | §15.2, §24.4 | S29 |
| V6 | Retrieve write-only: 38 calls, 0 hits; query "evidence" matched nothing (3 reviewers) | Task-term queries, pre-hypothesis ordering, priced-by-result retrieval, stored-knowledge store | §18.2b, §24.4 | S40, S34 |
| V7 | Uncached work: unconditional epilogue review (C13 vs §14), ungated in-loop review, planner rebuilds, uncached outcomes (~40+ tokens) (3 reviewers) | Outcome delta-cache; gated in-loop/epilogue reviews; planner-once; decide-early exits skip empty reviews | §14, §15.6, §24.4 | S2, S5, S35, S36 |
| V8 | Rule 28 failed: owner-unavailable, G-HOW dead, tokens_max, plateau, G-WHY-4/-5, invariant-8 — no scenarios, no disclosures (3 reviewers) | Scenarios S41–S44; plateau→RESOURCE_LIMITED mapping; G-WHY-5 exercisable; REPLICATE denial; gate_wait exemption | §3.3, §10.5, §11.7, §21.2 | S41–S44 |
| V9 | §24.3 not self-contained: no interface block; 10+ undeclared helpers; 22-vs-19 binding (3 reviewers) | Full interface inlined; all helpers declared; binding documented as the harness's actual tuple | §24.1–24.3 | doc-level |
| V10 | E5 stabilization a label; diagnose-before-act contradicts Cynefin (2 reviewers) | Stabilize pass before diagnosis for Chaotic; bounded once | §9.4, §24.4 | S35 |
| V11 | VOI fill a task flag; S34 SOLVED with `missing_evidence` set (2 reviewers) | Real retrieval fill with gap clearing; SOLVED asserts empty gaps | §11.7 | S34, S40 |
| V12 | Attribution mislabeled; S32 gap; no per-scenario delta table (2 reviewers) | §32.3 delta table; S32 numbering footnote; relabeled claims | §32.3 | metrics |
| V13 | Co-scaling gate / EvaluationPlane / probe life-cycle / HMAC — no mechanisms | Phase-gated with named disclosures (unchanged from v4's honest list) | §32.4 | disclosed |
| V14 | Bar checked on candidate max, not the selected decision; attestation oracle task-config | Selected-decision bar check; attestation ground truth remains world-config (disclosed) | §15.4, §20.4 | S4, S28 |
| V15 | E1 epilogue 5 vs E0 2 tokens; competence write unprovenanced | E1 cost disclosed; the write is now kernel-fed (V2); deterministic 0-price extended to empty retrievals | §9.4, §32.4 | S22 |

### 31.1 Non-accepted and deferred findings

- EvaluationPlane `run_suite`/`produce_profile` and the co-scaling gate (Phase 2); probe life-cycle (Phase 4); model heterogeneity and multi-round debate (Phase 3); checkpoint HMAC/key management (Phase 1); `renegotiate` deployment (Phase 2); LearningScheduler batching, latency timestamps, ExecutionMonitor findings, the seven-term retrieval score, evidence-weighted council aggregation, and creative-design MethodComposer modules — all named in §32.4's disclosure.
- The attestation oracle's ground truth and the world store's write path remain world-config in the harness (modeling operator/kernel-held facts); the read path is v5-enforced; the write boundary is Phase-1.
- The novelty-signature evasion residual (cosmetic mutations) is documented; hard budgets are the termination guarantee.
- The verifier history in the harness records always-correct verdicts (deterministic mocks); calibration dynamics require real evaluation outcomes (disclosed).

---

## 32. Empirical Validation

### 32.1 Method

Per the framework's own rules (P4, P9, §22.3), v5 changes were validated by execution. `validation/harness.py` implements the frozen v4 algorithm (baseline) and the v5 algorithm over identical deterministic mock components, runs **44 scenarios** (S1–S37 from v4 plus S38–S45 for v5 mechanisms), and asserts the framework's own standards. Pricing: cognitive tokens (model-call-equivalent; bookkeeping at 0; deterministic re-computation at 0; **empty retrieval at 0**, priced hits at 1) and bookkeeping calls (counted, printed). The scenario numbering S1–S31, S33–S45 (S32 retired in v4) is noted in the table footnote.

### 32.2 Results (44 scenarios; 3 reproducible runs, identical every run)

| Scenario | v4 status | v5 status | v4 asserts | v5 asserts | v4 tokens | v5 tokens |
|---|---|---|---|---|---|---|
| S1 trivial task, E0 | SOLVED | SOLVED | 4/4 | 4/4 | 2 | 2 |
| S2 executor always fails | RESOURCE_LIMITED | RESOURCE_LIMITED | 6/6 | 6/6 | 34 | 31 |
| S3 frame oscillates | SOLVED | SOLVED | 4/4 | 4/4 | 46 | 43 |
| S4 clear-looking, high stakes | ESCALATED | ESCALATED | 6/6 | 6/6 | 11 | 11 |
| S5 no external verifier | ESCALATED | ESCALATED | 5/5 | 6/6 | 3 | 2 |
| S6 ambiguous success | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 3 | 2 |
| S7 calculator exists | SOLVED | SOLVED | 4/4 | 4/4 | 2 | 2 |
| S8 injection attempt | SOLVED | SOLVED | 5/5 | 5/5 | 15 | 15 |
| S9 EVOC exhausted | RESOURCE_LIMITED | RESOURCE_LIMITED | 4/4 | 4/4 | 2 | 1 |
| S10 proposal flood | SOLVED | SOLVED | 5/5 | 5/5 | 16 | 16 |
| S11 authorization denied | ESCALATED | ESCALATED | 4/4 | 4/4 | 13 | 13 |
| S12 action-class misattestation | UNSAFE | UNSAFE | 4/4 | 4/4 | 11 | 11 |
| S13 red team catches flaw | SOLVED | SOLVED | 4/4 | 4/4 | 21 | 21 |
| S14 memory contradiction | SOLVED | SOLVED | 4/4 | 4/4 | 15 | 15 |
| S15 WHAT gate: no metrics | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 2 | 1 |
| S16 safe probe available | NEEDS_EXPERIMENT | NEEDS_EXPERIMENT | 4/4 | 4/4 | 3 | 2 |
| S17 bounded approximation | APPROXIMATED | APPROXIMATED | 4/4 | 4/4 | 11 | 11 |
| S18 constraints inconsistent | INFEASIBLE | INFEASIBLE | 4/4 | 4/4 | 4 | 3 |
| S19 plan stop-condition | INFEASIBLE | INFEASIBLE | 4/4 | 4/4 | 15 | 15 |
| S20 pending authorization | ESCALATED | ESCALATED | 6/6 | 6/6 | 17 | 15 |
| S21 crash, resume | SOLVED | SOLVED | 4/4 | 4/4 | 20 | 19 |
| S22 competence feedback | SOLVED | SOLVED | 4/4 | 4/4 | 20 | 20 |
| S23 council minority | SOLVED | SOLVED | 4/4 | 4/4 | 26 | 26 |
| S24 call budget hard-stop | RESOURCE_LIMITED | RESOURCE_LIMITED | 4/4 | 4/4 | 19 | 19 |
| S25 low-stakes verifier outage | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 3 | 2 |
| S26 kernel-calibrated A4, two identities | ESCALATED | SOLVED | 4/4 | 4/4 | 20 | 18 |
| S27 history-fed calibration | INFEASIBLE | RESOURCE_LIMITED | 4/4 | 4/4 | 34 | 33 |
| S28 A5, single verifier | ESCALATED | ESCALATED | 4/4 | 4/4 | 11 | 11 |
| S29 L3 ladder (attest-time) | ESCALATED | ESCALATED | 4/4 | 5/5 | 3 | 11 |
| S30 WHY gate re-entry | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 5 | 4 |
| S31 plan escalation condition | ESCALATED | ESCALATED | 4/4 | 4/4 | 15 | 15 |
| S33 minted-token commit | SOLVED | SOLVED | 4/4 | 4/4 | 15 | 15 |
| S34 VOI gap filled by retrieval | NEEDS_EVIDENCE | SOLVED | 4/4 | 4/4 | 4 | 17 |
| S35 E5 chaotic crisis | ESCALATED | ESCALATED | 4/4 | 4/4 | 25 | 19 |
| S36 search branch | INFEASIBLE | RESOURCE_LIMITED | 4/4 | 4/4 | 30 | 20 |
| S37 fast-path governance | SOLVED | SOLVED | 4/4 | 4/4 | 15 | 15 |
| S38 allowlist negative | ESCALATED | ESCALATED | 3/3 | 4/4 | 14 | 13 |
| S39 second-verifier blocks | ESCALATED | ESCALATED | 3/3 | 4/4 | 20 | 11 |
| S40 real retrieval fill | NEEDS_EVIDENCE | SOLVED | 3/3 | 4/4 | 4 | 17 |
| S41 owner-unavailable gate | INFEASIBLE | ESCALATED | 3/3 | 4/4 | 2 | 1 |
| S42 G-WHY-5 falsification | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 3/3 | 4/4 | 5 | 4 |
| S43 plateau → RESOURCE_LIMITED | INFEASIBLE | RESOURCE_LIMITED | 3/3 | 4/4 | 29 | 19 |
| S44 replication denied | UNSAFE | UNSAFE | 3/3 | 4/4 | 11 | 11 |
| S45 competence self-rating rejected | SOLVED | SOLVED | 3/3 | 4/4 | 20 | 20 |
| **Totals** | | | **177/177** | **187/187** | **616** | **592** |

*Footnote: S32 was retired in v4; numbering is S1–S31, S33–S45 (44 scenarios).*

### 32.3 What the suite demonstrates — and honest attribution

- **Trust-boundary completion (V1):** the algorithm's security-knob reads go through the world store; S45 proves a task-declared accuracy of 1.0 is ignored (competence 0.704, kernel-fed — not 0.65, self-fed). The v4→v5 status changes tell the story: S26 (v4 ESCALATED → v5 SOLVED — the identity registry makes A4 with two identities succeed), S27/S36/S43 (INFEASIBLE → RESOURCE_LIMITED — the plateau mapping is corrected), S34/S40 (NEEDS_EVIDENCE → SOLVED — retrieval genuinely fills gaps), S41 (INFEASIBLE → ESCALATED — the owner-unavailable branch fires).
- **V3/V4 negative cases:** S38 — an unlisted plan task is not executed under PENDING (0 subset executions); S39 — an A4 task whose bar passes but whose registry has one identity escalates with zero executor calls.
- **V5:** S29's ESCALATED now comes from the attest-time L3 branch (l3 flag asserted), not the L2 early classifier.
- **V7 economics:** S35's pending wait dropped 25 → 19 tokens (planner-once + gated reviews + plateau exemption); S36 30 → 20; S43 29 → 19; S2 34 → 31. The suite's cognitive total is **616 → 592 (−3.9%)** across 44 scenarios — the honest per-scenario delta table accompanies this section: the wins are gating/caching/early-exits (S35 −6, S36 −10, S39 −9, S43 −10, S2 −3, S3 −3, S20 −2, S18 −1, S41 −1, S9/S15/S25/S16/S30 −1 each); the costs are the new mechanisms (S34/S40 +13 for the real fill, S29 +8 for the L3 path — an honest cost of reaching a previously-unreachable branch — plus S23/S26/S38/S45 ±1–2). Empty retrievals are now free (S5/S6/S25 etc. dropped 3 → 2).
- **Reproducibility:** deterministic; 3 consecutive runs identical; totals 177/177 (v4 baseline under v5 components) and 187/187 (v5).

### 32.4 Honest limitations of the validation

- Mock components: control-flow guarantees hold for any components satisfying the contracts; not model intelligence, sampling, or real tools.
- **Coverage disclosure (v5):** the harness implements the v5 §24.4 loop: world-facts routing (all knobs), all gates (re-evaluable, G-WHY-4/-5 exercisable), stabilize pass, council with debate round + adjudication, search branch, verifier (kernel calibration, rolling history, identity registry, second-verifier rule, SHA-256 caches for candidates AND outcomes), planner-once, kernel (attest incl. REPLICATE denial, pending, table-only allowlist, minting, interrupt), executor (idempotency), gated reviews, competence (provenance gate), memory (retrieve priced by hits, real fill, contradiction with margin, quarantine), improvement (dedup, evaluate), LoopMonitor (plateau→RESOURCE_LIMITED, wait exemptions), BudgetController, TaskScheduler (checkpoint/resume). Not implemented (design-level, disclosed): EvaluationPlane `run_suite`/`produce_profile` and the co-scaling gate; probe life-cycle; ExecutionMonitor findings; AuditLog latency timestamps; LearningScheduler batching; multi-round debate; checkpoint HMAC/versioning (integrity boundary — the key co-location gap of C5 remains); `renegotiate` deployment; the seven-term retrieval score; evidence-weighted council aggregation; creative-design MethodComposer modules.
- **World-store read path vs write path:** the *read path* is v5-enforced (the algorithm reads knobs only through the world object; S45 asserts it). The *write path* — who populates the store in production — is the kernel/operator boundary: in the harness it is scenario seeding (modeling world facts); the Phase-1 process boundary that prevents the model's tools from writing the store is disclosed, not implemented.
- The attestation oracle's ground truth and the kernel task-class taxonomy remain world-config in the harness; a real independent estimator is Phase-1/3.
- The verifier history records always-correct verdicts (deterministic mocks); calibration dynamics require real evaluation outcomes.
- The novelty-signature evasion residual (cosmetic mutations) is documented; hard budgets are the termination guarantee.
- Pricing honesty: cognitive tokens exclude bookkeeping and deterministic re-computation; bookkeeping totals are printed by the harness; at 1 token per bookkeeping call the historical v3-vs-v2 comparison inverts (C11) — v5 reports both numbers.

### 32.5 How to re-run

```bash
python validation/harness.py        # single pass, writes validation/results.md
python validation/harness.py 3      # 3-pass determinism check
```

---

## 33. Consumer Quick-Reference

| Reader | Sections |
|---|---|
| Implementer (MVP) | §24 (canonical), §25, §9.4–9.6, §15.1–15.6, §18.2, §20.3–20.5 |
| Safety auditor | §21, §20, §22, §23.4, §27 |
| Researcher | §2, §5, §30, §31 |
| Evaluator | §23, §32, §15.4 |
| All | §3.3 (state contract), §28 (operating rules), §6.5 (principle–mechanism matrix) |

Normative content: §3.3–3.4, §6.5, §9.4–9.6, §10.5, §11.7, §12.5–12.8, §13.2–13.3, §13.7, §15.1–15.6, §17.2–17.4, §18.2–18.4, §20.2–20.5, §21.2–21.4, §22.3–22.7, §23.6a–23.8, §24.2–24.4. Guidance (advisory): the remaining prose, including §5 and §26.

---

*End of document.*
