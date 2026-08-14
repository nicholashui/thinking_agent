<!-- ============================================================
  LP04 — Stage 0/1: META-CONTROL + WHAT (Frame the Problem)
  Source file: thinking_agent.v8.md  (split part 04/12)
  ============================================================ -->
## 9. Stage 0 — META-CONTROL

*(Responsibilities §9.1, Cynefin routing §9.2, routing variables §9.3 per v4. Effort levels §9.4 with E5's stabilize-before-diagnose pass (V10) and E1's honored* *`requires_review`* *epilogue.)*

### 9.5 Expected value of computation (operational)

- **Novelty signature:** canonicalized SHA-256 hash over (hypotheses, frame, observations, evidence, alternatives, plan). The **plateau stop now maps to** **`RESOURCE_LIMITED`** via its reason keyword, matching the §3.3 producer table (V8, §32 S36/S43). The evasion residual (cosmetic mutations) remains documented as a heuristic; hard budgets are the termination guarantee.
- **EVOC proxy:** `base − decay × iterations`, with `base` read from the world store (V1). The first term is a stopping heuristic, never evidence.
- **Hard budgets:** iterations, tokens, calls, agents (per-round cap), deadline — all from the world store; the call ceiling is enforced on cognitive calls at loop top and inside `budget.check` (≤ 1-iteration overshoot documented).
- **Wait exemptions:** PENDING human-gate waits and WHAT-gate re-entries are external waits, not cognitive churn — the plateau/EVOC stops do not apply while `pending_wait` or `gate_wait` is set (V8, §32 S20/S35/S41); only hard budgets and the kernel-held timeout bound them.

### 9.6 World-facts store (v5: the security-knob boundary is code, not prose)

**The world object is the kernel-held facts store, by modeling convention.** Scenario configuration seeds it (modeling world facts: kernel calibration, ceilings, timeouts, verifier identities, outage status, domain accuracy, stored knowledge, baseline-frozen, write-authorization policy); the v5 engine's own body reads every security knob **only** through it — a code-level property asserted by the harness's `assert_read_path()` on every run, and demonstrated behaviorally by S45 (a task-declared accuracy of 1.0 is ignored; the kernel feed produces 0.704). Honest scope: in the single-process mock, the scenario spec is the world model — the task-declaration channel is not modeled separately, and component-level reads of non-knob task facts (`action_class` at attestation, denial flags at authorize) remain; the production write-path boundary is Phase-1 (§32.4). In production the store is populated by EvaluationPlane outcomes and operator policy, in a process boundary the model's tools cannot write (§15.6's single-model-writable-state residual is disclosed: the *read path* is fixed; the *store's write path* requires the Phase-1 key/process boundary, §32.4).

The config block (§9.6 of v4) remains the single source of defaults: reliability seed/window, class bars, trust margin, consolidation threshold, gate/reframe/pending budgets, human-gate SLAs (scheduler-consumed), EVOC base/decay, competence blend, novelty plateau.

***

## 10. Stage 1 — WHAT: Frame the Problem

*(§10.1–10.5 per v4; the owner-unavailable ESCALATED branch is now scenario-validated (V8, §32 S41) and WHAT-gate re-entries are exempt from the novelty plateau (V8).)*

***

