<!-- ============================================================
  LP02 — Scope, Lineage & Research Foundations
  Source file: thinking_agent.v8.md  (split part 02/12)
  ============================================================ -->
## 3. Scope and Non-Claims

### 3.1 What "universal" means

Thinking Agent is intended to address: clear and routine problems; expert analytical problems; complex adaptive problems; chaotic or crisis conditions (E5 now with a stabilize-before-diagnose pass, V10); causal diagnosis; scientific discovery (probe life-cycle remains Phase-4, disclosed); creative design (MethodComposer branches per task signature, with creativity modules still intention-level, disclosed); strategic planning; software and digital operations; embodied action; social and stakeholder problems (renegotiate remains Phase-2, disclosed); adversarial environments; long-horizon learning (memory retrieval now genuinely read back, V6); architecture improvement.

### 3.2 What Thinking Agent does not claim

*(Unchanged from v4: no AGI claims, no debate-superiority claims, no self-reflection-as-proof, no benchmark-performance-as-intelligence, and the harness validates control-flow properties, not intelligence.)*

### 3.3 Required graceful-failure states

Every task must terminate in one of these explicit states, each with a producer; the harness demonstrates all eight reachable (§32, S1–S45):

| State              | Producer (v5)                                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `SOLVED`           | `verify_outcome`: checks ∧ external ∧ reliability ≥ bar ∧ identity-registry second-verifier rule (§15.4)                                   |
| `APPROXIMATED`     | `select` records `error_bound` → `state.approximation_available` (§15.5)                                                                   |
| `NEEDS_EVIDENCE`   | `diagnose` fills `missing_evidence`; L1 degrade; G-WHY gate failure (§11.5, §15.2)                                                         |
| `NEEDS_EXPERIMENT` | `diagnose` sets `state.probe_available` (§19.2)                                                                                            |
| `INFEASIBLE`       | constraint screen sets `state.infeasible`; plan stop-conditions (§12.4, §13.7)                                                             |
| `UNSAFE`           | SafetyKernel denial; attestation mismatch; invariant-8 replication denial (V8)                                                             |
| `ESCALATED`        | denials; L2/L3 ladder; reliability-blocked; PENDING timeout; plan escalation conditions; owner-unavailable (V8)                            |
| `RESOURCE_LIMITED` | LoopMonitor/BudgetController: iterations, tokens, calls, EVOC, **novelty plateau** (§9.5–9.6; plateau→RESOURCE\_LIMITED mapping fixed, V8) |

### 3.4 State-transition policy

- Every terminal state is produced by exactly one owning mechanism; producers read **world facts** (V1), so the state-only classifier's inputs are kernel- or component-owned rather than task-copied.
- Test order (implemented by `classify_terminal`): L2 → L1 → ambiguity → reliability-blocked → evidence gap → probe → infeasibility → budget → approximation → residual. The plateau stop now maps to `RESOURCE_LIMITED` via its reason keyword (V8).
- Every terminal path writes the proof-carrying packet via the common epilogue — including denials, PENDING timeouts, and early classifier exits (reviews on decided-early outcomes are gated, V7).

***

## 4. Architectural Synthesis and Lineage

*(The five lineages plus four self-revision rounds: v1 governed the loop; v2 enforced the standards; v3 kernel-held the numbers; v4 executed the branches; v5 completes the trust boundaries and makes the remaining claimed mechanisms executable or explicitly disclosed. The harness now freezes four engines — v2, v3, v4 (baseline), v5 — over identical components.)*

***

## 5. Research Foundations

*(§5.1–5.8 per v4, with the SearchController branch now exercised (S36) and the council's debate round executing claim exchange + verifier adjudication (D5 of v4). §5.9: the 40-framework survey unchanged.)*

***

