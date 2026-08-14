# Thinking Agent

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Book Edition covering Versions 1.0 – 5.0**  
**Research cutoff:** August 7, 2026  
**Source policy:** Primary arXiv papers and official xAI materials prioritized over third-party commentary.

---

## Preface

This book presents the complete evolution and the definitive architecture of **Thinking Agent** — a research and engineering blueprint for a governed cognitive system intended as a scaffold for AGI/ASI research. It is **not** a claim that current language models are AGI, nor that multi-agent debate, longer inference, or recursive self-modification automatically produce general intelligence or safe superintelligence.

The central thesis is multiplicative:

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

A severe weakness in any factor limits the whole. Thinking Agent therefore separates generation, truth determination, safety determination, execution, learning, and system change into distinct owners that cannot be collapsed into a single unconstrained model call.

The documents progressed through five major versions. Each version was subjected to a multi-lens self-review and, from v2 onward, an executable validation harness that freezes the previous algorithm as baseline and asserts the framework’s own standards. The progression is not “more features”; it is successive closure of the gap between what the document asserted and what the reference algorithm actually enforced.

This book:

1. Recounts the changes between each version with the concrete defects that motivated them and the reasons those changes were accepted.
2. Provides a detailed, self-contained explanation of the latest (v5) architecture.
3. Embeds architectural diagrams as SVG illustrations.
4. Collects the operating rules, failure modes, roadmap, and validation results into a single coherent narrative.

---

## Chapter 1 — What Thinking Agent Is

### 1.1 Purpose and Non-Claims

Thinking Agent is designed to handle a wide range of problem classes — clear/routine, complicated/expert, complex adaptive, chaotic/crisis, causal diagnosis, scientific discovery, creative design, strategic planning, software operations, embodied action, social/stakeholder, adversarial, long-horizon learning, and architecture improvement — by selecting different reasoning procedures rather than applying one fixed prompt.

**Universal problem solving**, in this context, means the system can recognize the problem class and return the most responsible available outcome:

- A verified solution (`SOLVED`)
- A bounded approximation (`APPROXIMATED`)
- Ranked alternatives
- A request for missing evidence (`NEEDS_EVIDENCE`)
- A safe experiment/probe (`NEEDS_EXPERIMENT`)
- Demonstration of infeasibility (`INFEASIBLE`)
- Calibrated uncertainty
- Refusal or human escalation when action would be unsafe (`UNSAFE` / `ESCALATED`)
- Explicit resource exhaustion (`RESOURCE_LIMITED`)

Every task must terminate in exactly one of these eight states and must produce a proof-carrying decision packet.

The architecture does **not** claim:

- Current models are AGI.
- Multi-agent debate is automatically superior to a strong single agent.
- Self-reflection substitutes for external verification.
- More inference-time compute always improves answers.
- Recursive self-improvement can be made safe by prompting alone.
- A universal knowledge representation has been discovered.
- Benchmark scores prove general intelligence.
- ASI can be safely obtained by scaling model size or agent count.
- The reference algorithm or its harness demonstrates any of the above. The harness validates control-flow properties only.

### 1.2 The Central Operating Loop

```text
META-CONTROL → WHAT → WHY → HOW → DO → REVIEW
```

A continuous **VERIFY** layer surrounds every stage. A **governed loop** (LoopMonitor, BudgetController, stage gates, state-only classifier, delta verification, checkpoint/resume, progress gating) guarantees termination, graceful failure, and cost-boundedness.

![Operating Loop](svg/operating_loop.svg)

*Figure 1. Central operating loop of Thinking Agent v5. The VERIFY layer is continuous; the loop is budgeted and monitored.*

### 1.3 Design Principles (abridged)

| # | Principle | Core idea |
|---|-----------|-----------|
| P1 | Context before cognition | Classify problem, stakes, uncertainty, risk before choosing procedure |
| P2 | Frame → Diagnose → Prescribe | Do not optimize a solution to the wrong problem |
| P3 | Evidence outranks confidence | Fluency, agreement, and self-reported confidence are not evidence |
| P4 | External feedback outranks intrinsic critique | Self-criticism is a source of hypotheses, never proof |
| P5 | Independent diversity before social influence | Agents generate privately before any communication |
| P6 | Reversible before irreversible | Prefer tests, containment, undo, compensation |
| P7 | Verification scales with consequence | High-stakes short actions can require deeper verification |
| P8 | Memory requires governance | Provenance, trust, contradiction handling, permission, expiry |
| P9 | Self-improvement empirical & reversible | Sandbox → evaluate → review → canary → rollback |
| P10 | Preserve human authority | Goals, permissions, safety kernel outside ordinary self-modification |
| P11 | Stop when EV is negative | Novelty plateau, EVOC, hard budgets → `RESOURCE_LIMITED` |
| P12 | Packet on every path | Common epilogue; no silent denials |

These principles are not advisory. In v5 each has a named enforcing component and call site in the reference algorithm.

---

## Chapter 2 — Evolution: Why Each Version Changed

The change logs (§31 of each version) are the primary source. Below is a narrative synthesis of the defects that were found, the changes that were accepted, and the reasons.

### 2.1 Version 1.0 — Research Blueprint (Prose)

**Status:** Research and engineering blueprint. No executable harness.

v1 assembled:

- Ranked portfolio of 40 traditional thinking frameworks (Cynefin highest, then Premortem, AAR, Double-Loop, RPD, root-cause suite…).
- The WHAT → WHY → HOW → DO → REVIEW process.
- Memory, multi-agent, metacognitive, and self-evolution ideas from earlier drafts.
- Contemporary agent research (CoALA, ReAct, Tree-of-Thoughts / RAP / LATS, Reflexion / CRITIC, multi-agent debate literature, STOP / Darwin Gödel Machine, AgentDojo / AI Control).
- Production patterns from xAI (adaptive reasoning, parallel subagents, plan-review, verification, Grok Build harness components).

It already stated the eight graceful states, the separation of generation / truth / safety / execution / learning / change, and the principle that self-criticism is not proof. However, the reference algorithm was a `while True` loop whose termination signals were never computed, five of the eight states were unreachable or collapsed, budgets were declared but never enforced, stage gates and premortem/red-team had no call sites, the decision packet was path-dependent (denial paths returned nothing), and the competence model had no data feed. In short, the document described properties the algorithm did not possess.

**Key limitation recognized:** “Asserted in prose” is not the same as “enforced by the control flow.”

### 2.2 Version 2.0 — Governed Loop

**Theme:** Terminability, state completeness, and an executable validation harness.

Major accepted findings (A1–A18):

| Defect (v1) | Change (v2) | Reason |
|-------------|-------------|--------|
| `while True` with no computed stop | LoopMonitor (novelty, repetition, EVOC) + bounded loop | Termination must be guaranteed, not hoped for |
| 5 of 8 states unreachable | `classify_terminal` decision table with named producers | Every graceful state must have a producer path |
| Effort levels never branched | Route flags (`requires_*`) and fast path for E0/E1 | Adaptive effort must be operational |
| Budgets declared, never enforced | BudgetController consumed at every stage | Cost must be a first-class constraint |
| Gates / premortem / red-team no call sites | Explicit call sites + `check_exit_gate` | Mechanisms without call sites are paragraphs |
| REVIEW outside the loop; VERIFY = two points | In-loop AAR + continuous verification layer | Learning and verification must be continuous |
| Decision packet path-dependent | Common epilogue on every terminal path | No silent denials |
| Council / memory / self-evolution incomplete | Structural independence, contradiction rule, admission control | Make the multi-agent and memory protocols implementable |

**Validation:** First harness. v1 vs v2 over identical mocks. v1 frequently hit a watchdog infinite loop; v2 terminated every scenario with a graceful state. All eight states reached. Token cost dropped dramatically on the pathological cases because the loop could now stop.

**Reason for the jump:** A research blueprint that cannot terminate or produce the states it promises is not yet a reliable engineering object. v2 made the control flow match the stated contract.

### 2.3 Version 3.0 — Enforcement Fidelity

**Theme:** The algorithm must satisfy the document’s own standards.

v2 still contained gaps that the harness itself exposed:

- Class bars (§15.4) had no consumer; tasks were declared `SOLVED` at seed reliability 0.5.
- Ghost fields (`probe_available`, `approximation_available`, `infeasible`) were read by the classifier but never written by any producer and were absent from the schema.
- PENDING authorization was an unbounded re-execution loop.
- Several gates still lacked call sites.
- Competence loop was dangling.
- Council was still a comment, not a branch.
- Cost reduction was mis-attributed (most of the “69 %” came from terminating two infinite loops, not from the fast path).

v3 fixed these (B1–B17). Producers were added for every classifier input; the reliability bar became a real predicate inside `verify_outcome`; PENDING acquired a static allowlist subset, a single-execution guard, and a timeout that escalates; gates and plan conditions received call sites; the council became a true branch that writes a minority ledger; early classifier entry after the WHY gate stopped wasted full passes; delta verification and progress awareness began to appear.

**Validation:** 26 scenarios. v2 baseline 98/98 asserts → v3 111/111. Cognitive tokens 592 → 393 (−33.6 %). Attribution was made honest: the earlier large saving was largely loop-termination; the remaining saving came from early exits and delta reuse.

**Reason:** A document that prints thresholds its own algorithm ignores is not honest. v3 closed the most glaring “print vs execute” gaps.

### 2.4 Version 4.0 — Trust-Boundary Enforcement

**Theme:** Security-critical numbers must not be task-declarable.

Even after v3, several knobs that affect safety and truth remained under the influence of the task (or of a self-assessing model):

- Verifier reliability could still be influenced by task-supplied “warmth.”
- Competence updates were fed by self-generated calibration.
- The PENDING “subset” was still partly planner-fabricated.
- External-action tasks could still take the fast path and skip attestation.
- The class bar was checked after execution on some paths.
- L3 of the no-verifier ladder was unreachable in practice.
- WHY gate could not force re-diagnosis; plan escalation conditions were unread.

v4 moved reliability into a kernel-side registry fed by rolling history, provenance-gated competence, replaced the placeholder allowlist with a real kernel table, forced external-action tasks off the fast path, performed attestation + bar check **before** any execution, completed the L1/L2/L3 ladder, made the WHY gate re-evaluable, consumed plan escalation conditions, enforced the second-verifier rule, and exercised the previously dead E5 (Chaotic) and search branches.

**Validation:** 36 scenarios. v3 141/141 → v4 153/153. Cognitive cost almost flat (560 → 547) because the new checks add work; the honest trade for stronger enforcement.

**Reason:** A system that lets the task (or the model that benefits) set its own reliability, competence, or allowlist is not governed. Trust boundaries must be structural.

### 2.5 Version 5.0 — Trust-Boundary Completion

**Theme:** Kernel-holding is code, not narration; previously dead mechanisms live or are explicitly disclosed.

v4 still left residual trust holes and dead code:

- Security knobs were still readable from task-scope structures in the engine body (narrated as “kernel-held”).
- Competence could still be influenced by task-declared accuracy.
- An `allowlist_hint` fallback permitted unlisted tasks.
- Second-verifier rule was still partly task-flag driven.
- L3 fired only via early classifier, never at attest time on the attested class.
- Memory retrieval was write-only (0 hits).
- Outcome verification, in-loop review, and planner were not progress-gated; unchanged state was re-paid.
- Several claimed branches (owner-unavailable, G-WHY-4/5, novelty-plateau mapping, REPLICATE denial) had no scenarios.

v5 closed them:

- **World-facts store.** Every security knob (`pending_timeout`, `calls_ceiling`, EVOC parameters, calibration, identities, outage, baseline-frozen, write-authorization) is read **only** through the world object. A code-level `assert_read_path()` runs with every harness suite. S45 demonstrates a task-declared accuracy of 1.0 is ignored.
- Competence fed exclusively from a kernel domain-accuracy registry with a provenance gate.
- PENDING subset = kernel-table membership only; negative scenario S38.
- Second-verifier rule computed from the identity registry; pre-DO block; negative scenario S39.
- L3 fires at attest time on the attested class (S29).
- Retrieval is real, priced by hits, queries task-derived terms, and can fill gaps (S34/S40).
- Outcome delta-cache + gated reviews + planner-once (V7).
- Previously dead mechanisms given scenarios (S41–S44); plateau correctly maps to `RESOURCE_LIMITED`; E5 receives a stabilize-before-diagnose pass; bar is checked on the **selected** decision’s verifier, not the candidate max.

**Validation:** 44 scenarios. v4 baseline 177/177 → v5 187/187. Cognitive tokens 616 → 592 (−3.9 %). Savings come from gating/caching/early exits; costs come from the newly live mechanisms (real retrieval, L3 path, etc.). Attribution is published per scenario.

**Reason:** “Kernel-held” that is not enforced by the read path of the engine is still narration. Mechanisms that have never been executed are still paragraphs. v5 makes the remaining claims either true of the code or explicitly disclosed as Phase-N.

![Version Timeline](svg/version_timeline.svg)

*Figure 2. Evolution from prose blueprint (v1) to code-level trust-boundary completion (v5).*

---

## Chapter 3 — Architecture of Thinking Agent v5 (Detailed)

### 3.1 High-Level Structure

![Architecture Overview](svg/architecture_overview.svg)

*Figure 3. Nested architecture of Thinking Agent v5. The Safety Kernel sits outside the ordinary cognitive scaffold and owns the world-facts store.*

The system is organized as four nested timescales:

1. **Action loop** — single tool call / observation with transactional semantics.
2. **Task loop** — the META → WHAT → WHY → HOW → DO → REVIEW cycle with per-stage checkpoints.
3. **Learning loop** — competence update (kernel-fed, provenance-gated), memory consolidation, improvement proposals.
4. **Architecture-evolution loop** — gated scaffold search under the R0–R5 authority levels, always against a frozen baseline.

### 3.2 Stage 0 — META-CONTROL

Responsibilities:

- Cynefin context classification (Clear / Complicated / Complex / Chaotic / Disorder).
- Effort level selection (E0–E5). E5 forces council + human gate and runs a **stabilize-before-diagnose** pass (Cynefin act→sense→respond).
- Route flags: `requires_diagnosis`, `requires_search`, `use_council`, `requires_review`, external-action gate, etc.
- Budget envelope allocation (iterations, tokens, calls, agents-per-round, deadline).
- Competence-aware routing (historical success/failure by domain, kernel-sourced).
- MethodComposer selection of reasoning modules according to task signature.

All security-relevant ceilings and seeds are read from the **world-facts store**, never from task declarations.

### 3.3 Stage 1 — WHAT (Frame)

- Produce a problem frame with success metrics, constraints, stakeholders, and owner.
- Gate predicates (G-WHAT): metrics present, owner available or escalated, frame coherent.
- Owner-unavailable → `ESCALATED` (now scenario-validated).
- Gate re-entries are exempt from the novelty-plateau stop (they are external waits).

### 3.4 Stage 2 — WHY (Diagnose)

- Memory retrieval **before** hypothesis formation (priced by hits; empty = free).
- Hypothesis generation, evidence collection, falsification search, residual uncertainty.
- VOI estimation; a fillable gap is actually filled by retrieval rather than left as a flag.
- G-WHY predicates (all five evaluated):
  1. Leading hypothesis has decision-relevant evidence
  2. Significant alternatives considered
  3. Residual uncertainty recorded
  4. Estimated VOI of further diagnosis ≤ cost
  5. Falsification evidence non-empty
- Gate failure clears hypotheses and re-enters (budgeted).
- Early classifier entry when the outcome is already decided (`missing_evidence` unfillable, `probe_available`, verifier outage on low-stakes, etc.).

### 3.5 Stage 3 — HOW (Generate / Test / Select)

- MethodComposer + optional SearchController (EV of exploration gate).
- Independent candidate generation (fresh contexts when council is used).
- Premortem and Red Team — progress-gated (only on new content).
- VerifierRegistry: external identity, reliability from kernel registry / rolling history, second-verifier rule from identity count.
- **Pre-DO checks on the selected decision:**
  - Attestation (action class, REPLICATE denial, etc.)
  - Class bar against the **chosen** candidate’s verifier (not the set max)
  - Second-verifier requirement
- Constraint screen → `infeasible` producer.
- Selection records `error_bound` when approximation is the best available.

### 3.6 Stage 4 — DO (Plan & Execute)

- Hierarchical plan with stop and escalation conditions (both consumed).
- SafetyKernel authorize:
  - Full approval, denial (`UNSAFE` / `ESCALATED`), or PENDING.
  - PENDING executes **only** the kernel static allowlist subset (A2-class, table membership only — no fallback).
  - PENDING wait is progress-gated (~0 cognitive tokens per iteration) and bounded by kernel-held timeout → `ESCALATED`.
- ToolBroker: schemas, least privilege, transactional semantics, idempotency keys, compensation table, timeouts/retries.
- Crash/resume via versioned checkpoints (integrity boundary Phase-1 disclosed).
- L3 (no-action) fires at attest time for external A3+ tasks under verifier outage.

### 3.7 Stage 5 — REVIEW (Reflect / Learn / Evolve)

- After-Action Review (supposed → actual → difference → change).
- Single-loop (tactics) and double-loop (assumptions/frames) learning; the latter can trigger mid-task reframe.
- Reviews are **gated**: in-loop only on candidate/observation deltas; epilogue only when a decision was made, actions executed, or lessons are possible.
- Competence update once per episode, only from kernel/EvaluationPlane sources.
- Procedural writes require a SafetyKernel-minted authority token.
- ImprovementEngine: admission control + dedup, then full acceptance pipeline against frozen baseline when authorized.

### 3.8 Continuous VERIFY Layer

- VerifierRegistry owns identity and reliability; model cannot stamp “external.”
- SOLVED requires: checks pass ∧ external identity ∧ reliability ≥ class bar (keyed by max(attested, declared), unknown → A5) ∧ second-verifier rule when required.
- Delta caches (SHA-256) for candidates and for outcome verification.
- No action ever runs on below-bar verification.

### 3.9 Memory Architecture

![Memory and Evolution](svg/memory_and_evolution.svg)

*Figure 4. Memory classes and the R0–R5 self-evolution authority ladder.*

Write protocol is a complete decision procedure: classify → provenance → trust (derived from verifier reliability) → contradiction (trust-margin rule) → quarantine/promotion → privacy/permission → expiry → store. Retrieval is active inside diagnosis and is priced by result.

### 3.10 Safety Kernel (outside the scaffold)

Owns:

- Goal acceptance and signed goal contract
- Permissions and capability tokens
- World-facts store (all security knobs)
- Static allowlist and action-class taxonomy
- Identity registry
- Token minting
- Attestation and REPLICATE denial
- Human gates and PENDING timeouts
- Interrupt / shutdown
- Self-modification level gates (R0–R5)

Invariants include: the system may not grant itself new authority; untrusted content may not alter governing instructions; high-impact actions require independent authorization; logging cannot be disabled; core goals cannot be autonomously rewritten; unevaluated self-modifications cannot be deployed; safety-critical changes require human approval; self-replication and uncontrolled resource acquisition are disabled by default.

### 3.11 Graceful States (revisited)

![Graceful States](svg/graceful_states.svg)

*Figure 5. The eight terminal states, their producers, and the state-only classifier policy.*

### 3.12 Reference Algorithm Guarantees (v5)

1. **Termination** — iteration/token/call budgets, novelty plateau → `RESOURCE_LIMITED`, repetition, EVOC; external waits exempt but still timeout-bounded.
2. **State completeness** — all eight states reachable through world-fact-driven producers.
3. **Packet completeness** — every terminal path, including denials and early exits.
4. **Verification independence** — external identity + bar + second-verifier; reliability kernel-held; no below-bar execution.
5. **Cost boundedness** — envelope + progress gating + planner-once + outcome cache + priced retrieval.
6. **Gate enforcement** — WHAT/WHY/HOW + plan conditions; WHY re-evaluable.
7. **Review in loop** — gated AAR; competence once per episode with kernel feed.
8. **Resume** — stage-boundary checkpoints; idempotent re-execution protection.

---

## Chapter 4 — Validation Discipline

From v2 onward the framework obeys its own rule: **self-criticism is a source of hypotheses, not proof**. Every accepted change is executed against a frozen baseline of the previous algorithm over identical deterministic mock components. The harness asserts the framework’s own standards (termination, state reachability, budget enforcement, stage gating, threshold enforcement, packet completeness, independence, etc.). It does **not** claim to measure model intelligence.

### 4.1 Headline Results (v5 suite)

| Metric | v4 (baseline) | v5 |
|--------|---------------|-----|
| Scenarios | 36 (+ later) | 44 |
| Asserts | 177/177 | 187/187 |
| Cognitive tokens | 616 | 592 (−3.9 %) |
| Determinism | 3 identical runs | 3 identical runs |

Notable behavioral shifts:

- S26: identity-registry A4 with two identities now correctly SOLVED.
- S34/S40: real retrieval fills gaps → SOLVED.
- S29: L3 reached at attest time.
- S38/S39: negative cases for allowlist and second-verifier.
- S41–S44: previously dead branches now live.
- S45: task-declared competence accuracy ignored.

### 4.2 Honest Limitations (always restated)

- Mock components only; control-flow guarantees, not intelligence.
- Several Phase-N features remain design-level (EvaluationPlane batch, probe life-cycle, multi-round debate, checkpoint HMAC integrity boundary, `renegotiate` deployment, etc.) and are named in the disclosure.
- World-store **read path** is enforced; the production **write path** (who may populate the store) is the Phase-1 process/key boundary.
- Novelty signature remains a heuristic; hard budgets are the termination backstop.
- Verifier history in the harness uses always-correct verdicts; real calibration dynamics require real evaluation outcomes.

---

## Chapter 5 — Roadmap, MVP, and Operating Rules

### 5.1 Minimal Viable Thinking Agent (order)

1. Structured task state and decision records.
2. Evidence retrieval + provenance.
3. Criterion-specific verification (external + bar).
4. Transactional tool use + least privilege.
5. Persistent memory with retrieve + write protocol.
6. Independent multi-agent generation + minority ledger.
7. Targeted debate / adjudication.
8. Safety + prompt-injection evaluations; world-facts store.
9. Procedural-memory updates gated on baseline.
10. Sandboxed architecture search (stub for Phase 5).
11. Full EvaluationPlane freeze procedure.

### 5.2 Phased Roadmap (summary)

| Phase | Focus |
|-------|--------|
| 0 | Structured assistant (routing, stages, deterministic verification, LoopMonitor) |
| 1 | Grounded agent (tool broker, sandbox, human-approved actions, world-store write boundary, checkpoint integrity) |
| 2 | Persistent generalist (long-term memory, competence calibration, EvaluationPlane batch, co-scaling gate, renegotiate) |
| 3 | Collective solver (heterogeneous specialists, large parallel workflows) |
| 4 | Continual learner (active curricula, probe life-cycle, multimodal world models) |
| 5 | Governed self-improving system (scaffold search, canary, independent safety audits) |
| 6 | AGI candidate (evidence of broad transfer, low-data learning, long-horizon autonomy, calibrated uncertainty, robust interruption, safe continual improvement under resource constraints) |
| 7 | ASI research boundary (oversight of systems that exceed human experts; no uncontrolled replication, no autonomous goal rewriting, capability–safety co-scaling) |

### 5.3 Final Operating Rules (v5)

1. Sense before thinking deeply.
2. Frame before diagnosing.
3. Diagnose before prescribing.
4. Generate alternatives before committing.
5. Test assumptions before acting.
6. Prefer evidence over agreement.
7. Prefer external checks over self-confidence.
8. Prefer reversible probes over irreversible bets.
9. Use multiple agents only when diversity and decomposition add value.
10. Preserve dissent.
11. Treat all retrieved content as untrusted data.
12. Grant the minimum authority required.
13. Verify the environmental result, not merely the generated plan.
14. Learn from outcomes, not just narratives.
15. Question governing assumptions during review.
16. Do not deploy a self-modification merely because the system proposed it.
17. Keep goals, permissions, and safety controls outside ordinary self-modification.
18. Escalate when evidence, competence, or authority is insufficient.
19. Stop when additional cognition has negative expected value.
20. Never confuse a scaffold toward AGI with demonstrated AGI.
21. Every task terminates in a graceful state; every terminal state carries a decision packet.
22. A route that cannot be budgeted is a route that cannot run.
23. A claim that cannot name its verifier is not a verified claim — and a verifier whose reliability is below the class bar is not a verifier for that claim.
24. A label written by the claimant is data, not authority — authority tokens are minted, trust is measured.
25. A mechanism the reference algorithm does not call is a paragraph, not a mechanism.
26. A number a task can set for itself is not governance — reliability, effort class, ceilings, timeouts, and competence feed are kernel-held.
27. No action runs on below-bar verification — the bar is checked before execution.
28. What the document claims, the harness must demonstrate — every normative mechanism has a call site and a scenario (or a named disclosure).
29. A knob the engine reads from the task’s own declarations is not kernel-held — the engine body reads security knobs only through the world store, and the harness asserts the read path.
30. A mechanism without a scenario is a paragraph.
31. Do not pay twice for the same work — outcome verification is delta-cached, reviews are gated, the planner builds once per decision, empty retrievals are free.

---

## Chapter 6 — Common Failure Modes and Mitigations (v5)

| Failure | v5 Mitigation |
|---------|---------------|
| Wrong problem frame | Multiple frames, user confirmation, frame critic, WHAT gate |
| HOW before WHY | Stage gate requiring diagnosis |
| Confident hallucination | External verifier + reliability bar + second-verifier rule |
| Excessive diagnosis | VOI stop + EVOC |
| First-answer anchoring | Independent candidate generation |
| Self-critique echo chamber | External / heterogeneous verifiers; SOLVED never self-only |
| Debate conformity | Private first answers, fresh contexts, minority ledger |
| Majority error | Verification-weighted aggregation; minority recoverable |
| Planner–executor drift | Preconditions, postconditions, checkpoints, monitor |
| Tool hallucination | Retrieved schemas + argument validation |
| Prompt injection | Authority/data separation, least privilege, boundary validation |
| Memory poisoning | Minted tokens, verifier-derived trust, quarantine |
| Goal drift | Signed goal contract outside mutable memory |
| Reward hacking | Hidden / adversarial evaluations; immutable evaluation plane |
| Benchmark overfitting | Portfolio + OOD tests; frozen baseline |
| Unsafe self-modification | Full §22.3 pipeline invoked; R5 never autonomous |
| Infinite cognitive loop | LoopMonitor (novelty → RESOURCE_LIMITED, budgets) |
| Overuse of agents | Council feasibility predicates + per-round cap |
| Hidden side effects | Transactional actions, idempotency, compensation |
| Capability growth outruns safety | Co-scaling gate (Phase 2) |
| Denial paths without audit | Common epilogue on every path |
| Proposal flood | Admission control + canonical dedup |
| Verifier-below-bar silent SOLVED | Reliability-blocked → ESCALATED; pre-DO check |
| Task-declared competence / reliability | World-facts store + provenance gate + assert_read_path |
| Allowlist backdoor | Kernel-table-only membership; negative scenario |
| Cosmetic novelty evasion | Documented heuristic; hard budgets are the guarantee |

---

## Chapter 7 — Conclusion

Thinking Agent is the product of five successive self-corrections. v1 described a rich architecture. v2 made the loop terminable and the state machine complete. v3 forced the reference algorithm to honor the thresholds and producers the document itself required. v4 moved security-critical numbers behind trust boundaries and closed governance holes on the fast path and the bar check. v5 completed the trust boundary at the code level, made retrieval and previously dead branches real, and subjected every remaining claim to either a scenario or an explicit disclosure.

The most important principle is not “think longer” or “use more agents.” It is:

> **Apply the right cognitive process, obtain the right evidence, verify through the right mechanism, act with the right authority, and learn without weakening human control.**

That combination supplies a practical, auditable scaffold for increasingly general AI systems while keeping the central research problems — AGI itself, safe recursive self-improvement, and ASI oversight — explicitly open.

---

## Appendix A — Primary Research References

1. Sumers et al., *Cognitive Architectures for Language Agents*, arXiv:2309.02427  
2. Kotseruba & Tsotsos, *A Review of 40 Years of Cognitive Architecture Research*, arXiv:1610.08602  
3. Yao et al., *ReAct*, arXiv:2210.03629  
4. Yao et al., *Tree of Thoughts*, arXiv:2305.10601; Hao et al., *RAP*; Zhou et al., *LATS*  
5. Prasad et al., *ADaPT*; Zhou et al., *Self-Discover*  
6. Shinn et al., *Reflexion*; Gou et al., *CRITIC*; Dhuliawala et al., *Chain-of-Verification*  
7. Huang et al., *LLMs Cannot Self-Correct Reasoning Yet*; Tyen et al., *LLMs Cannot Find Reasoning Errors*  
8. Du et al., *Improving Factuality through Multiagent Debate*; later debate-skeptic studies  
9. Packer et al., *MemGPT*; Park et al., *Generative Agents*; Wang et al., *Voyager*  
10. Zelikman et al., *STOP*; Hu et al., *Automated Design of Agentic Systems*; Zhang et al., *Darwin Gödel Machine*  
11. Debenedetti et al., *AgentDojo*; Greenblatt et al., *AI Control*  
12. xAI, *Grok 4.20 System Card* (2026-04-07); *Grok Build* open-source and workflow notes (2026)

---

## Appendix B — Consumer Quick-Reference

| Reader | Priority sections |
|--------|-------------------|
| Implementer (MVP) | Chapters 3 & 5, §24-equivalent material, memory write protocol, tool broker |
| Safety auditor | Safety Kernel, tool security, self-evolution levels R0–R5, failure modes |
| Researcher | Core thesis, research foundations lineage, roadmap Phases 6–7 |
| Evaluator | Validation chapter, eight states, packet contract |
| All | Operating rules, design principles, graceful-state table |

---

*End of book.*  
*Generated from Thinking Agent versions 1.0–5.0 (research cutoff 2026-08-07).*  
*SVG diagrams live in the `svg/` directory relative to this document.*
