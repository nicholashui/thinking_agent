# Thinking Agent

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Version:** 4.0  
**Research cutoff:** August 7, 2026  
**Status:** Research and engineering blueprint (validated — see §32)  
**Source policy:** Primary arXiv papers and official xAI materials were prioritized over third-party commentary.  
**Change policy:** v4 supersedes v3. The differential change log in §31 records every accepted finding from the v3 self-review, the v4 change, and its validation status. The executable validation harness lives in `validation/harness.py`; results are in §32.

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

v4's advance over v3 is **trust-boundary enforcement**: the security-critical knobs v3 left task-declarable are now kernel-held, and the mechanisms v3 claimed but never executed are either executed and scenario-validated or explicitly disclosed. Specifically, v4: (a) completes the state-only classifier (v3's L2 branch still read task config — §31 C1); (b) moves verifier reliability into a kernel-side registry fed by rolling history, so a task can no longer declare its own calibration (C2); (c) provenance-gates competence updates so the doc's own rule — self-reported accuracy is not evaluation history — is enforced by its own algorithm (C3); (d) replaces the placeholder PENDING "subset" with a real kernel allowlist (C4); (e) closes the fast-path governance hole — external-action tasks can never skip attestation (C6); (f) checks the class bar before executing, so no action runs on below-bar verification (C8); (g) gates premortem/red-team/review on progress so loops stop paying for unchanged state (C9); (h) completes the no-verifier ladder (L1 degrade, L3 no-action) (C14); (i) makes the WHY gate re-evaluable (C15), consumes plan escalation conditions (C16), enforces the second-verifier rule (C17), and exercises the E5 crisis and search branches (C22). Every change is demonstrated by the harness: **v3 baseline 141/141 asserts, v4 153/153 asserts, 36 scenarios, deterministic across runs** (§32).

Thinking Agent is not a claim that one architecture can literally solve every mathematically, physically, or computationally possible problem. Some problems are undecidable, intractable, underspecified, unsafe, or impossible with available evidence and resources.

Here, **universal problem solving** means that the system can recognize a wide range of problem classes and return the most responsible available outcome:

- A verified solution.
- A bounded approximation.
- A set of ranked alternatives.
- A request for missing evidence.
- A safe experiment or probe.
- A demonstration that the current specification is infeasible.
- A calibrated statement of uncertainty.
- A refusal or human escalation when action would be unsafe.

Every task terminates in exactly one of the eight graceful states (§3.3), and every terminal state produces the proof-carrying decision packet (§15.4). In v4 the classifier reads only producer-set state fields, and the producers themselves are kernel- or component-owned — the "state-only" property is no longer theater when every state field is model-written (§31 C1, C2).

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

Thinking Agent separates the functions of generating an answer, determining whether it is true, determining whether the action is safe, executing the action, learning from the result, and changing the system that generated the result. These functions must not be collapsed into one unconstrained model call — and in v4, the **authority to set the numbers those functions depend on** (reliability, effort class, ceilings, timeouts, competence) is separated from the model that benefits from setting them (§9.6, §15.1, §20.4, §31 C2/C19).

---

## 3. Scope and Non-Claims

### 3.1 What “universal” means

Thinking Agent is intended to address: clear and routine problems; expert analytical problems; complex adaptive problems; chaotic or crisis conditions; causal diagnosis; scientific discovery; creative design; strategic planning; software and digital operations; embodied action; social and stakeholder problems; adversarial environments; long-horizon learning; architecture improvement. It does this by selecting different reasoning procedures rather than applying one fixed prompt.

### 3.2 What Thinking Agent does not claim

Thinking Agent does not claim that current language models are AGI; that multi-agent debate is automatically better than one agent; that self-reflection is a reliable substitute for external verification; that more inference-time computation always improves an answer; that recursive self-improvement can be made safe through prompting alone; that a universal knowledge representation has been discovered; that benchmark performance proves general intelligence; that ASI can be safely produced by increasing model size or agent count; or that the v4 reference algorithm, its harness, or its mock components demonstrate any of the above. The harness (§32) validates control-flow properties, not intelligence.

### 3.3 Required graceful-failure states

Every task must terminate in one of these explicit states. Each state has a producer; the harness demonstrates all eight are reachable (§32, S1–S37):

| State | Meaning | Producer (v4) |
|---|---|---|
| `SOLVED` | Result satisfies success criteria and the verification threshold. | `verify_outcome`: checks ∧ external ∧ reliability ≥ class bar ∧ second-verifier rule (§15.4) |
| `APPROXIMATED` | Exact solution unavailable; bounded approximation produced. | `select` records `error_bound` → `state.approximation_available` (§15.5) |
| `NEEDS_EVIDENCE` | Decision cannot responsibly be made without more information. | `diagnose` fills `missing_evidence`; L1 degrade (§11.5, §15.2) |
| `NEEDS_EXPERIMENT` | A safe probe is the next rational action. | `diagnose` sets `state.probe_available` (§19.2) |
| `INFEASIBLE` | Constraints inconsistent or outcome not achievable. | constraint screen sets `state.infeasible` (§12.4) |
| `UNSAFE` | Action violates a safety, legal, ethical, or permission boundary. | SafetyKernel denial; attestation mismatch (§20.4) |
| `ESCALATED` | Human judgment required. | denials; L2/L3 ladder; reliability-blocked; PENDING timeout; plan escalation conditions (§15.2, §15.4, §13.7, §21.4) |
| `RESOURCE_LIMITED` | Expected value of further computation does not justify its cost. | LoopMonitor/BudgetController: iterations, tokens, calls, EVOC, novelty plateau (§9.5–9.6) |

### 3.4 State-transition policy

- Every terminal state is produced by exactly one owning mechanism.
- `UNSAFE` (action prohibited) vs `ESCALATED` (action may be valid but lacks authority) are distinguished.
- The classifier is **state-only** in v4: it reads producer-set state fields (`verifier_outage`, `stakes`, `missing_evidence`, `probe_available`, `infeasible`, `approximation_available`, `reliability_blocked`, verification fields) and ledger values — never task inputs directly (C1). `stakes` is a schema field (§24.2) copied at task init; `verifier_outage` is set by `diagnose`.
- Test order (implemented by `classify_terminal`): verifier-outage-and-high-stakes (L2) → verifier-outage-and-low-stakes (L1) → ambiguity → reliability-blocked → evidence gap → probe → infeasibility → budget exhaustion → approximation → residual.
- Every terminal path writes the proof-carrying packet via the common epilogue — including denials, PENDING timeouts, and early classifier exits.

---

## 4. Architectural Synthesis and Lineage

| Lineage | Retained contribution | Implementation |
|---|---|---|
| 40 traditional thinking frameworks | Cynefin, Premortem, AAR, Double-Loop, RPD, root-cause, metacognition, creativity, Red Teaming | Adaptive routing, risk simulation, structured review, method library, adversarial verification |
| WHAT → WHY → HOW → DO → REVIEW | Framing, diagnosis, alternatives, selection, execution, review | Task loop with boolean stage gates enforced in §24.4 |
| Grok-inspired architecture | Fast/full paths, CoALA memory, roles, hierarchical planning, nested self-evolution | Meta-controller, workspace, council, learning engine |
| Verification-first multi-agent protocol | Independent generation, evidence-weighted aggregation, non-claims | Verifier separation, weighted synthesis, uncertainty discipline |
| Agent-security literature (2024–2026) | Tool security, authority/data separation, least privilege, gated self-modification | Safety kernel, tool broker, improvement pipeline, evaluation plane |
| v1 self-review | Termination, budget governance, gates, state machine, feedback loops | Governed loop, BudgetController, LoopMonitor, classifier |
| v2 self-review | Enforcement fidelity: bars with consumers, producers, pending semantics, resume, delta verification | §15.4 enforced bars, §3.3 producers, §20.3a, §20.5, §15.6 |
| v3 self-review | Trust boundaries: kernel-held security knobs, executed mechanisms, honest pricing | §9.6 config, §15.1 registry, §20.4 attestation, §32 pricing disclosure — see §31 |

---

## 5. Research Foundations

*(§5.1–5.8 unchanged from v3: cognitive architecture and CoALA; grounded reasoning (ReAct, Toolformer, SayCan); search/decomposition/planning (ToT, RAP, LATS, ADaPT, Self-Discover) with the SearchController now exercised (§31 C22); reflection and verification with the core rule "Self-criticism is a source of hypotheses, not proof of correctness" — enforced at the SOLVED gate, the identity registry, and competence provenance; multi-agent reasoning with the debate-skeptic literature — the council's single debate round now executes claim exchange + verifier adjudication (§31 D5); memory and lifelong learning with CoALA/MemGPT/Voyager — `retrieve` is now called inside diagnosis (§31 D2); self-improving systems with proposal/deployment authority separation — the §22.3 pipeline is invoked against a frozen baseline; production agent patterns per xAI docs.)*

### 5.9 Traditional thinking-model portfolio

*(Unchanged from v3: the ranked 40-framework survey with Cynefin at 1, Premortem at 2, AAR at 3, Double-Loop at 4, RPD at 5; Design Thinking (7.0) correctly precedes GROW (6.5); 20 + 20 = 40.)*

---

## 6. Design Principles

*(P1–P12 unchanged from v3.)*

### 6.5 Principle–mechanism matrix (v4)

| Principle | Enforcing component | Enforcing point (v4) |
|---|---|---|
| P1 | MetaRouter | `route(state)` precedes all stages (§24.4) |
| P2 | Stage gates | WHAT/WHY/HOW gates block advancement; WHY re-evaluable (C15) |
| P3 | VerifierRegistry | Reports only; never self-confidence (§15.4, §17.3) |
| P4 | VerifierRegistry | SOLVED requires external identity ∧ reliability ≥ bar ∧ second-verifier rule |
| P5 | CouncilOrchestrator | `use_council` branch with claim exchange + adjudication (§17.2, D5) |
| P6 | SafetyKernel + select | Reversibility classes; irreversibility penalty in decision score (contract-level) |
| P7 | MetaRouter + VerifierRegistry | `verification_depth` from stakes; bars per (class, stakes) |
| P8 | MemoryManager | Write protocol with minted tokens, contradiction rule (margin applied, D10), quarantine |
| P9 | ImprovementEngine + EvaluationPlane | §22.3 `evaluate` invoked against a frozen baseline (§32 S10) |
| P10 | SafetyKernel + GoalManager | Signed goal contract; renegotiation gated (§24.5; interface listed in §24.3, deployment Phase 2) |
| P11 | LoopMonitor + BudgetController | EVOC, novelty plateau, iteration/token/call budgets → RESOURCE_LIMITED |
| P12 | Common epilogue | Packet on every terminal path, including denials |

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
│ checkpoint/resume • attestation • token minting             │
│ KERNEL-HELD CONFIG • STATIC ALLOWLIST • no-replication      │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ META-CONTROLLER (competence-aware; method composer)         │
│ BUDGET ENVELOPE • ROUTE FLAGS • E5 crisis branch            │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ STRUCTURED COGNITIVE WORKSPACE                              │
│ WHAT → WHY → HOW → DO → REVIEW                              │
│ STATE-ONLY CLASSIFIER • pre-DO BAR CHECK • progress gating  │
│ early classifier entry • checkpoint at every stage          │
└───────────────┬──────────────────────┬───────────────────────┘
                │                      │
┌───────────────▼────────────┐  ┌──────▼──────────────────────┐
│ REASONING AND COUNCIL      │  │ MEMORY AND WORLD MODEL     │
│ search • generate          │  │ working/episodic/semantic/ │
│ council (debate round)     │  │ procedural • retrieve-in-  │
│ critique • synthesize      │  │ diagnose • competence      │
└───────────────┬────────────┘  └──────┬──────────────────────┘
                │                      │
┌───────────────▼──────────────────────▼───────────────────────┐
│ TOOL BROKER AND EXECUTION SANDBOX                           │
│ timeouts • retries • idempotency • compensation             │
│ pending kernel-allowlist subset • crash checkpoint          │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ TELEMETRY, EVALUATION, AND SELF-EVOLUTION                   │
│ per-stage audit (timestamps) • frozen baseline              │
│ EvaluationPlane (immutable) • verifier history registry     │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Four Nested Timescales

*(Action loop §8.1, task loop §8.2 with per-stage checkpoints, learning loop §8.3 — CompetenceModel closes per episode with provenance-gated calibration, procedural memory now read back inside diagnosis (§31 D2) — architecture-evolution loop §8.4 with the invoked §22.3 pipeline, session layer §8.5 with priority arbitration and renegotiation per v3; LearningScheduler triggers defined in §24.5.)*

---

## 9. Stage 0 — META-CONTROL

*(Responsibilities §9.1, Cynefin routing §9.2 with the stakes scale and attestation — in v4 the attestation trigger is not self-circumventable because the fast path itself is gated on external action (§31 C6) — routing variables §9.3, effort levels §9.4 unchanged except:)*

- **E5 (Chaotic) is operational in v4:** effort 5 forces the council and the human gate (authorize returns PENDING; no auto-approval). Demonstrated by §32 S35.
- **E1's `requires_review` flag is honored in v4:** the fast path runs the learning epilogue (review + competence + memory + improvement queue) when `requires_review` is set (C7, §32 S22-ep2).

### 9.5 Expected value of computation (operational)

- **Novelty signature:** canonicalized hash over (hypotheses, frame, observations, evidence, alternatives, plan). v4 documents an honest limitation: hash equality can still be evaded by cosmetic mutations (the harness's own oscillation fixture mutates the frame each pass); the plateau is a heuristic — the hard iteration/token/call budgets are the termination guarantee (C26).
- **Repetition counter, EVOC proxy** (config-derived base benefit; telemetry-derived in production), **hard budgets** — unchanged; `calls_max` is enforced on cognitive calls at loop top and inside `budget.check` (≤ 1-iteration overshoot documented in §32.4's pricing note).

### 9.6 Budget envelope and configuration block (v4)

The envelope is unchanged. **The configuration block is now a kernel-held, read-only object** (C19): every tunable (reliability seed, class bars, trust margin, consolidation threshold, gate/reframe/pending budgets, human-gate SLAs, EVOC base/decay, competence blend, novelty plateau) lives in one `CONFIG` structure that the algorithm reads and the task cannot write. Scenario-level overrides in the harness model *world facts* — kernel calibration, ceilings, and timeouts set by the environment (e.g., S20's `pending_timeout=3` models a kernel-set SLA; S24's `calls_ceiling=10` models an environment-set ceiling). The algorithm reads them from the world object, never from the task's own declarations; in production these values live in the kernel-held CONFIG object (C19: mechanism validated; kernel-holding realized as world-facts in the harness — §32.4). `human_gate_slas` are consumed by the TaskScheduler as wall-clock deadlines (design-level in the harness; the PENDING wait is progress-gated so wall-clock waits cost ~0 cognitive tokens, §32 S20).

---

## 10. Stage 1 — WHAT: Frame the Problem

*(§10.1–10.4 unchanged. §10.5 gate predicates unchanged; the "ESCALATED if owner unavailable" clause now has a call site in §24.4 (C19).)*

---

## 11. Stage 2 — WHY: Diagnose and Model

*(§11.1–11.6 unchanged, plus:)*

- **Memory read-back (D2):** `memory_manager.retrieve(query, state)` is called inside diagnosis — procedural and semantic memory now influence later episodes (continual learning is no longer write-only).
- **G-WHY gate is fully evaluated in v4 (D7):** predicates now include falsification presence (G-WHY-5) and VOI ≤ cost (G-WHY-4); a failing gate **clears hypotheses and re-enters diagnosis**, bounded by the gate budget (C15, §32 S30).

### 11.7 Exit gate (predicates)

```text
G-WHY-1  leading hypothesis has decision-relevant evidence
G-WHY-2  significant alternatives considered
G-WHY-3  residual uncertainty recorded
G-WHY-4  estimated VOI of further diagnosis ≤ cost
G-WHY-5  falsification_evidence non-empty
```

**Early classifier entry** after the gate when `missing_evidence` (not trivially fillable — C31), `probe_available`, or `verifier_outage` — with a VOI check: a gap that one retrieval call can fill proceeds instead of terminating (C31, §32 S34).

---

## 12. Stage 3 — HOW: Generate, Test, and Select Solutions

*(§12.1–12.7 unchanged, plus:)*

- **Pre-DO bar check (C8):** attestation runs at HOW exit; misattestation denies immediately (UNSAFE); the class bar is then checked against the candidate-verification reliability **before any execution** — no action runs on below-bar verification (§32 S4: 18 → 12 tokens, and the stakes-5 action no longer executes; S12 stays UNSAFE via the early attestation).
- **Progress gating (C9):** premortem and red team run only when the candidate set changed (content hash); during PENDING waits and unchanged-state iterations they are skipped — loops stop paying for unchanged work (§32 S2: 39 → 35; S20: 21 → 18).

### 12.8 Exit gate (predicates)

```text
G-HOW-1  ≥ 2 meaningful alternatives considered
G-HOW-2  hard constraints applied
G-HOW-3  preferred option survived sensitivity and red-team checks
G-HOW-4  fallback or abort condition exists
G-HOW-5  decision record explains the choice
```

---

## 13. Stage 4 — DO: Plan and Execute

*(§13.1–13.6 unchanged, plus:)*

- **Plan termination conditions (C16):** both `stop_conditions` (G-DO-2 → plan-failure terminal, documented as `INFEASIBLE` when the condition is a failure condition) and `escalation_conditions` (G-DO-4 → `ESCALATED`) are consumed at each DO pass (§32 S19, S31).
- **Fast-path governance (C6):** a task with external actions is rerouted to the governed loop (effort ≥ 2) at route time — it can never reach SOLVED via `direct_answer` without attestation, authorization, and the tool broker (§32 S37).
- **PENDING kernel allowlist (C4):** the authorized subset is selected by **SafetyKernel table lookup** — only kernel-listed A2-class actions — executed exactly once; the wait is progress-gated; timeout → `ESCALATED` with a partial packet (§32 S20: subset classes asserted A2).

### 13.7 Exit gate

```text
G-DO-1  success metrics met (verified)
G-DO-2  plan stop_conditions triggered → plan-failure terminal (INFEASIBLE)
G-DO-3  plan proven infeasible
G-DO-4  plan escalation_conditions triggered → ESCALATED
G-DO-5  human escalation required
```

---

## 14. Stage 5 — REVIEW: Reflect, Learn, and Evolve

*(AAR with in-loop review §14.1, single/double-loop §14.2–14.3, consolidation §14.4, Kaizen §14.5 unchanged, plus:)*

- **Terminal review (C3):** the epilogue always runs a fresh review of the actual outcome (the v3 bug where the SOLVED iteration reused the previous iteration's review is fixed) and updates competence **once per episode**.
- **Competence provenance (C3):** calibration carries a source; self-reported accuracy alone does not drive the effort boost — calibration must reference EvaluationPlane outcomes (in the MVP, the frozen 5-test suite). In the MVP the competence feed is kernel-world calibration; the blend weights live in the config block (C19). EvaluationPlane-referenced calibration is a Phase-2 feed (§32.4).

---

## 15. Continuous VERIFY Layer

### 15.1 Verification registry and kernel-side reliability (v4)

The registry table is unchanged. **Reliability is a kernel-side quantity (C2):**

- Deterministic tools: 1.0 by construction.
- Model verifiers: seed 0.5; updated from **rolling accuracy over the last N verdicts** (N = 5, config), where a verdict is *correct* if it matches the world outcome (a correct failure verdict is a win — the v3 bug where flaky outcomes collapsed verifier reliability is fixed, §31 C2/§32 S3).
- Warm values exist only in the **kernel calibration registry**, never as task-declarable numbers (§32 S26 is now fed by kernel calibration; S27 demonstrates a verifier crossing the bar via history alone).

### 15.2 Proposer-verifier separation and the no-verifier ladder (complete in v4)

```text
L1  verifier unavailable, stakes ≤ 2:  degrade (uncertainty inflated); status
    NEEDS_EVIDENCE for non-A0/A1 claims     (§32 S25)
L2  verifier unavailable, stakes ≥ 3:  ESCALATED           (§32 S5)
L3  verifier unavailable, action class ≥ A3:  no external action; ESCALATED
    with required_human_actions              (§32 S29)
```

All three levels are branches in the classifier/DO stage — no harness-only injection (C14).

### 15.3 Verification packet

*(Full §15.3 schema — artifact_id, criteria, checks, passed/failed/unresolved, counterexamples, verifier_identity, verifier_reliability, class_bar, needs_second_verifier, success, ambiguous, confidence, recommendation — all fields now produced by the harness (C33).)*

### 15.4 SOLVED threshold (enforced, with the second-verifier rule)

`verify_outcome.success = checks ∧ external ∧ reliability ≥ class_bar ∧ second-verifier rule`, where the bar is keyed by the **max of the kernel-attested class and the declared class** (C30; unknown class strings default to A5), and A4+ rows require a second independent verifier (§32 S26 has one; S28 — an A5 task with a single verifier — cannot SOLVE and escalates).

| Action class / stakes | Required checks | Min reliability | Second verifier |
|---|---|---|---|
| A0–A1 / 1–2 | 1 pass | 0.5 | — |
| A0–A1 / 3 | all | 0.8 | — |
| A0–A1 / 4 | all | 0.9 | — |
| A0–A1 / 5 | all | 0.95 | ✓ |
| A2 / 1–5 | all | 0.8–0.9 | — |
| A3 / 1–3 | all | 0.9 | — |
| A3 / 4–5 | all | 0.9 | ✓ |
| A4 / 1–5 | all | 0.9–0.95 | ✓ |
| A5 / any | all | 0.95 | ✓ (two verifiers) |

The proof-carrying packet (common epilogue) is unchanged; `required_human_actions` is populated from status and the L3 branch.

### 15.5 Bounded approximation

*(Unchanged: `select` records `error_bound` → `state.approximation_available` → `APPROXIMATED`; the classifier runs immediately after `select` so no wasted outcome verification (C13, §32 S17: 15 → 12 tokens).)*

### 15.6 Delta-based verification (hardened)

- Content hashes are **SHA-256** and bound to the verifier kind (C26).
- The cache is written only by the verifier flow (forgery via state writes is a documented residual: in the single-model MVP all state is model-writable; the cache is a performance mechanism, not an integrity boundary — §32.4).
- Reframe paths regenerate candidates and re-verify (content-identical regeneration hits the cache — S3's saving is *cache reuse on identical content*, labeled honestly in §32.3, C12).

---

## 16. Reasoning Method Composer

*(Method table §16.1 unchanged; the MethodComposer now has a real call site — `meta_router.compose` writes `route.reasoning_modules` by task signature (D8), exercised in every scenario's routing.)*

### 16.2 SearchController

*(Contract unchanged; the `requires_search` branch is now exercised by §32 S36.)*

---

## 17. Multi-Agent Collective

*(Roles §17.1 unchanged.)*

**Agent answer schema (inlined, C21):**

```yaml
agent_answer:
  agent_id:
  role:
  claims:            # [{claim, evidence_refs, uncertainty}]
  evidence:          # [{ref, kind, provenance, trust_label}]
  uncertainties:
  dissent:           # minority positions to preserve
```

**Council protocol (§17.2):** 1) decompose; 2) fresh context per agent; 3) private answers; 4) normalize into the claim ledger (lossless projection over `agent_answer`); 5) objective verifiers; 6) evidence-weighted aggregation; 7) **one debate round — claim exchange + verifier adjudication** (D5: unresolved claims routed through `verify_candidate`; dissent preserved in the minority ledger regardless of adjudication; S23 asserts ledger + adjudication); 8) Red Team; 9) minority ledger written before aggregation; 10) synthesis with a mandatory dissent section; 11) final gate (= `verify_outcome` with the class bar). Aggregation rules §17.3 and no-council predicates §17.4 per v3; council pricing is realistic — n fresh contexts + protocol calls (§32.4 pricing note).

---

## 18. Memory and Knowledge Architecture

*(Classes §18.1 unchanged; authority tokens are minted by the kernel; the positive commit path is scenario-validated (§32 S33).)*

**Memory record schema (inlined, C21):**

```yaml
memory_record:
  id:
  type:             # episodic | semantic | procedural | normative | prospective
  content_ref:
  provenance:       # anchored to audit/tool-call records
  trust_label:      # verifier-derived, never writer-declared
  expiry:
  version:
  status:           # COMMITTED | CONFLICTED | QUARANTINED | PROMOTED | EXPIRED
  authority_token:  # kernel-minted; required for procedural writes
```

**Write protocol (§18.2):** classify → validate provenance → label trust → **detect contradiction (trust-margin rule, D10: reject the new write unless its trust exceeds the incumbent's by ≥ 0.1; else CONFLICTED → quarantine → ReviewEngine adjudication)** → privacy/permission policy → expiry → store → monitor. **Retrieval:** `retrieve(query, state) -> memory_hits[]` is called inside diagnosis (D2); quarantine is skipped on retrieval. **Consolidation trigger:** ≥ 3 near-duplicate episodic records (similarity > 0.9 or exact match) merge into one semantic lesson with provenance-preserving diffs (call site in REVIEW; design-level in the harness). **Retrieval score (§18.3):** relevance × reliability × applicability × recency × transfer × permission − contradiction risk − poisoning risk, all terms 0–1 with numeric sources. **Security (§18.4), forgetting (§18.5), provenance anchoring (§18.6)** per v3.

---

## 19. World Model and Self-Model

*(World model §19.1; active experimentation §19.2 — probes remain flags with named producers; the probe life-cycle (design → execute → fold back) is a Phase-4 item, disclosed in §32.4 (D1). Self-model §19.3 — the competence loop is provenance-gated and closes once per episode (C3); `route` consumes `state.competence`; the two-episode S22 demonstrates effort 2 → 1 routing change.)*

---

## 20. Tool Broker and Execution Security

*(Authority separation §20.1, least privilege §20.2, controls and per-class transaction semantics §20.3, independent risk attestation §20.4 — the attestation denial now fires before the bar check (C8/S12); the estimator's output is treated as truth only within the max-class rule (C30). Checkpoint/resume §20.5 — versioned JSON + HMAC are specified; v4 discloses the MVP key-management gap honestly (C5): single-process file persistence co-locates the key with the model's tools, so checkpoint *integrity* is guaranteed only once the key lives in a separate process/OS keychain; the harness simulates crash/resume without authentication (S21) and §32.4 says so.)*

---

## 21. Safety and Alignment Kernel

*(Kernel position §21.1; invariants §21.2 — all ten mapped; invariant 8's no-replication whitelist and invariant 4's logging call sites unchanged. Threat model §21.3 unchanged. Human gates §21.4 — packet-before-approval, no auto-confirmation, corroboration; PENDING waits are progress-gated so they cost ~0 cognitive tokens (C10); wall-clock SLA enforcement is the scheduler's job (C19).)*

---

## 22. Self-Evolution Engine

*(Levels §22.1; admission control §22.2 — canonical dedup hashes, global rate caps; pipeline §22.3 — invoked by `evaluate` when the baseline is frozen; evaluation requirements + stable baseline §22.4 — the freeze procedure is specified: the EvaluationPlane freezes a snapshot of the 5-test suite, human-confirmed, access-restricted (C20); Kaizen size §22.5; evaluation-plane immutability §22.6; cadence §22.7; open-ended improvement §22.8.)*

---

## 23. Evaluation Framework

*(Dimensions §23.1–23.5 unchanged; profile §23.6 with the 5-test MVP suite enumerated in §23.6a — each maps to an implemented harness assertion; routing-quality and co-scaling §23.7 — the co-scaling gate is a Phase-2 item (disclosed); telemetry §23.8 — `audit_log.record(stage, telemetry.stats())` at loop top, each stage, fast path, epilogue; stats includes latency from timestamps (design-level in the harness, disclosed).)*

---

## 24. Reference Implementation Specification

### 24.1 Core components (canonical, v4)

*(The v3 component table, updated: VerifierRegistry owns the **calibration registry and rolling history**; SafetyKernel owns the **static allowlist** and **kernel-held config**; MetaRouter owns the **MethodComposer** call; GoalManager `renegotiate` and MethodComposer `compose` are listed with interface entries (§24.3) and Phase-2 deployment notes where applicable. Every component's interface appears in §24.3; every §24.4 call site resolves to an interface or a declared pseudocode-local helper — including `settle_best_of` and `default_world` (C18).)*

### 24.2 Shared task state (v4 schema)

*(The v3 schema plus: `stakes` (schema field, C1), `verifier_outage` (producer: diagnose), `attested_class` (producer: kernel attestation), `result.status_reason`/`pending_timeout` enumerated (C19), `_prev_alt_sig` (progress-gating bookkeeping), `_rejected_ids`.)*

### 24.3 Core interface (canonical, v4)

*(The v3 interface block with corrections: `solve(request, context, checkpoint, world)` where `world.bind()` returns the ordered component tuple documented in §24.1 (the harness `make_world()` pattern — the 22-name binding matches the 19-component mock plus telemetry/audit-log/env-flag, C18); `council_orchestrator.run_council(state, verifier) -> (candidate_set, minority_reports[], unresolved_disagreements[])` (tuple form, C18); `settle_best_of(frame, review) -> frame` declared as a pseudocode-local helper; `default_world` declared as the standard binding factory; `memory_manager.retrieve(query, state) -> memory_hits[]`; pseudocode-local helpers declared: `voi_positive(state)`, `owner_unavailable(state)`, `pending_record(subset)`, `plan_escalation_conditions_met(plan, state)`, `authorized_procedural(state)`, `verifier_kind(state)`, `settle_best_of(frame, review)`, `content_hash(artifact)`; `evidence_service.voi`, `world_model.predict`, `search_controller.explore`, `method_composer.compose`, `goal_manager.renegotiate`; `safety_kernel.allowed_subset(plan) -> tasks[]`; the canonical `audit_log.record(stage, telemetry.stats())` 2-arg form.)*

### 24.4 Main algorithm (v4 governed loop)

```python
def solve(request, context, checkpoint=None, world=default_world):
    # world.bind(): ordered components + telemetry + audit_log + baseline_frozen
    state = initialize_task_state(request, context)      # copies stakes (§24.2)
    if checkpoint:
        state = task_scheduler.resume(checkpoint)        # HMAC-verified (§20.5)

    state.route = meta_router.route(state)               # competence-aware; compose() runs
    budget.consume(state, "route")

    # --- Fast path (E0/E1) — C6/C7 ---
    if state.route.effort_level <= 1:
        budget.consume(state, "fast_path")
        state.decision = direct_answer(state)            # internal-only (C6: external
                                                         # actions rerouted at route time)
        state.verification = verifier.verify_outcome(state)   # bars + second-verifier rule
        state.result.status = ("SOLVED" if state.verification.success
                               else classify_terminal(state, telemetry))
        state.result.packet = build_decision_packet(state, state.result.status)
        audit_log.record("fast_path", telemetry.stats())
        task_scheduler.checkpoint(state, "FAST_PATH")
        if state.route.requires_review:                  # C7: E1 learning epilogue
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
                                       or "expected value" in reason or "unproductive" in reason)
                                   else classify_terminal(state, telemetry))
            state.result.status_reason = reason
            break

        # WHAT: frame + gate (owner-unavailable → ESCALATED, C19)
        if not state.frame:
            state.stage = "WHAT"
            state.frame = frame(state)
            gate = check_exit_gate("WHAT", state)
            if not gate.passed:
                state.risks.append(gate); state.frame = None
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result.status = ("ESCALATED" if owner_unavailable(state)
                                           else "NEEDS_EVIDENCE")
                    break
                continue
            audit_log.record("what", telemetry.stats())
            task_scheduler.checkpoint(state, "WHAT")

        # WHY: diagnose (producers + memory read-back) + gate — re-evaluable (C15)
        if state.route.requires_diagnosis and not state.hypotheses:
            state.stage = "WHY"
            diagnose(state)                              # sets verifier_outage (C1)
            state.evidence.extend(memory_manager.retrieve("evidence", state))  # D2
            gate = check_exit_gate("WHY", state)         # G-WHY-4/-5 evaluated (D7)
            if not gate.passed:
                state.risks.append(gate)
                state.hypotheses = []                    # re-entry, bounded (C15)
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result.status = "NEEDS_EVIDENCE"
                    break
                continue
            audit_log.record("why", telemetry.stats())
            task_scheduler.checkpoint(state, "WHY")
            if (state.missing_evidence or state.probe_available or state.verifier_outage):
                if state.missing_evidence and voi_positive(state):   # C31: fillable gap
                    pass
                else:
                    state.result.status = classify_terminal(state, telemetry)
                    break

        # HOW: council / search / explorer -> gated premortem -> delta-verify -> select
        if state.route.requires_generation and not state.alternatives:
            state.stage = "HOW"
            if state.route.use_council:
                (state.alternatives, state.minority_reports,
                 state.unresolved_disagreements) = council_orchestrator.run_council(state, verifier)
            elif state.route.requires_search:
                search_controller.explore(state, budget)   # C22: exercised
                generate(state)
            else:
                generate(state)
            audit_log.record("how", telemetry.stats())
        if not state.alternatives:
            state.result.status = classify_terminal(state, telemetry)
            break
        if constraints_violated(state):                    # §12.4 screen
            state.infeasible = True
            state.result.status = classify_terminal(state, telemetry)   # C13
            break
        candidates_new = content_hash(state.alternatives) != state._prev_alt_sig
        if candidates_new:                                 # C9: progress gating
            premortem(state)
            state._prev_alt_sig = content_hash(state.alternatives)
        reports = []
        for alt in state.alternatives:                     # §15.6 SHA-256 + verifier binding
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
            state.result.status = classify_terminal(state, telemetry)   # C13
            break
        gate = check_exit_gate("HOW", state)               # G-HOW enforced
        if not gate.passed:
            state.risks.append(gate)
            state.result.status = classify_terminal(state, telemetry)
            break
        # C8: attest + bar check BEFORE any execution
        if state.decision.requires_external_action:
            attestation = safety_kernel.attest(state)
            if attestation.startswith("misattested"):
                state.result.status = "UNSAFE"
                safety_kernel.interrupt(state.task_id)
                break
            state.attested_class = attestation
            bar, needs_second = verifier.class_bar(state)
            if max(r.verifier_reliability for r in reports) < bar:
                state.reliability_blocked = True           # no below-bar execution
                state.result.status = classify_terminal(state, telemetry)
                break
            if state.verifier_outage and state.attested_class in ("A3", "A4", "A5"):
                state.result.status = "ESCALATED"          # C14 L3
                break
        if candidates_new:                                 # C9
            if rejection := red_team.attack(state):
                state.risks.append(rejection)
                explorer.reject(state.decision.id)
                state.alternatives = []
                continue

        # DO: plan -> authorize (PENDING: kernel allowlist) -> execute -> monitor
        if state.decision.requires_external_action:
            state.stage = "DO"
            state.plan = planner.build(state, state.decision)
            authorization = safety_kernel.authorize(state.plan, state.permissions,
                                                    state.risks, state.attested_class)
            if authorization.status in ("UNSAFE", "ESCALATED"):
                state.result.status = authorization.status
                safety_kernel.interrupt(state.task_id)
                break
            if authorization.status == "PENDING":
                if not state.subset_executed:              # C4: kernel allowlist, once
                    subset = safety_kernel.allowed_subset(state.plan)
                    for t in subset:
                        tool_broker.execute_transactional(state.plan, t, authorization.token)
                    state.subset_executed = True
                    state.risks.append(pending_record(subset))
                if state.iteration >= pending_timeout:     # kernel-held config
                    state.result.status = "ESCALATED"
                    state.result.pending_timeout = True
                    break
                continue                                   # C10: gated — ~0 tokens per wait
            observations = tool_broker.execute_transactional(state.plan,
                                                             authorization.token)
            state.observations.extend(tag_untrusted(observations))
            audit_log.record("do", telemetry.stats())
            task_scheduler.checkpoint(state, "DO")
            if plan_stop_conditions_met(state.plan, state):        # G-DO-2 (C16)
                state.result.status = classify_terminal(state, telemetry)
                break
            if plan_escalation_conditions_met(state.plan, state):  # G-DO-4 (C16)
                state.result.status = "ESCALATED"
                break
            monitor = execution_monitor.check(state)
            state.risks.extend(monitor.findings)

        state.verification = verifier.verify_outcome(state)  # history updated (C2)
        if state.verification.success:
            state.result.status = "SOLVED"
            break

        # REVIEW-in-loop + competence (once per episode, C3)
        state.review = review_engine.review(state)
        if should_reframe(state.review, state):
            if state.iteration < REFRAME_BUDGET:
                state.frame = None; state.hypotheses = []; state.alternatives = []
                continue
            state.frame = settle_best_of(state.frame, state.review)   # helper (C18)
            state.hypotheses = []; state.alternatives = []
            continue
        if (state.verification.ambiguous or state.missing_evidence
                or state.reliability_blocked or state.probe_available
                or state.approximation_available or state.infeasible):
            state.result.status = classify_terminal(state, telemetry)
            break

    # --- Common epilogue (C3: fresh terminal review, single competence update) ---
    state.review = review_engine.review(state)
    competence_model.update(state, state.review.calibration)   # provenance-gated
    if authorized_procedural(state):
        tok = safety_kernel.issue_authority_token("procedural") # C24: mint + stamp
        for lesson in state.review.lessons:
            lesson.authority = tok
    else:
        safety_kernel.issue_authority_token("procedural")       # audit trail
    memory_manager.commit(state, state.review)
    if state.route.requires_review and state.review.lessons:
        queued = improvement_engine.queue(state, state.review)
        if queued and baseline_frozen:
            for p in state.improvement_proposals:
                improvement_engine.evaluate(state, p)
    state.result.packet = build_decision_packet(state, state.result.status)
    audit_log.record("epilogue", telemetry.stats())
    task_scheduler.checkpoint(state, "EPILOGUE")
    return state
```

Guarantees (each demonstrated by the harness, §32):

1. **Termination** — loop exits bounded by LoopMonitor (iteration/token/call budgets, novelty plateau, repetition, EVOC).
2. **State completeness** — all eight states reachable through producers; classifier is state-only (C1).
3. **Packet completeness** — every terminal path, including denials, PENDING timeouts, and early exits, produces the packet.
4. **Verification independence** — SOLVED requires external identity ∧ reliability ≥ bar ∧ second-verifier rule; reliability is kernel-held (C2); no below-bar execution (C8).
5. **Cost boundedness** — envelope metered; progress gating removes unchanged-state work (C9); deterministic re-computation priced at 0 (C32).
6. **Gate enforcement** — WHAT/WHY/HOW gates; WHY re-evaluable (C15); plan stop and escalation conditions consumed (C16).
7. **Review in loop** — AAR on non-terminal exits; fresh terminal review; competence once per episode (C3).
8. **Resume** — checkpoints at stage boundaries; crash/resume without double-execution (S21); integrity boundary per §20.5/§32.4 (C5).

### 24.5 Session and scheduler layer

*(Per v3: TaskScheduler identity/priority/checkpoint-resume; `GoalManager.renegotiate` gated by kernel + owner — interface entry in §24.3, deployment Phase 2; LearningScheduler triggers defined; cross-task conflict detection via ExecutionMonitor.)*

### 24.6 Component–call-site map (v4)

*(The v3 map, updated: MethodComposer (inside `route`), CouncilOrchestrator (branch in `generate`, with adjudication), SearchController (branch when `requires_search`, S36), EvidenceService/WorldModel (inside `diagnose`, design-level mocks), MemoryManager `retrieve` (inside `diagnose`), SafetyKernel `allowed_subset` (PENDING branch), `interrupt` (denial paths), `issue_authority_token` (epilogue), AuditLog (loop top, stages, fast path, epilogue), TaskScheduler (resume + per-stage checkpoints).)*

---

## 25. Minimal Viable Thinking Agent

*(MVP components and the 11-step development order per v3, updated: step 5 adds `retrieve` with the memory schema; step 8's EvaluationPlane freeze procedure is specified (who freezes, when, what snapshot — C20); step 10's baseline-gated procedural updates are testable via S33.)*

---

## 26. Roadmap Toward AGI and ASI Research

*(Phases 0–7 per v3. Phase 1 adds the kernel-held config boundary and key management for checkpoint HMAC (C5); Phase 2 adds EvaluationPlane batch feedback and the co-scaling gate; Phase 3 adds model heterogeneity; Phase 4 adds the probe life-cycle and multimodal world models; Phase 5 adds open-ended search.)*

---

## 27. Common Failure Modes

*(The v3 table, updated: "Verifier reliability declared by the task" → kernel registry (C2); "Competence self-rating" → provenance-gated (C3); "PENDING subset self-selected" → kernel allowlist (C4); "Below-bar execution" → pre-DO bar check (C8); "Unchanged-state loop cost" → progress gating (C9); "L3 unreachable" → L3 branch (C14); "WHY gate dead" → re-entry (C15); "Second-verifier rows unenforced" → second-verifier rule (C17); "Cosmetic-mutation novelty evasion" → documented heuristic with hard budgets as backstop (C26); "Infeasible known, HOW continues" → classify-after-screen (C13).)*

---

## 28. Final Operating Rules

*(Rules 1–25 per v3, plus:)*

26. **A number a task can set for itself is not governance** — reliability, effort class, ceilings, timeouts, and competence feed are kernel-held (§9.6, §15.1, §20.4).
27. **No action runs on below-bar verification** — the bar is checked before execution, not at declaration (§15.4, §24.4).
28. **What the document claims, the harness must demonstrate** — every normative mechanism has a call site and a scenario; exceptions are named in §32.4.

---

## 29. Conclusion

*(The v3 conclusion, updated: v4's theme is trust boundaries — the security knobs v3 left to the task are now kernel-held, the mechanisms v3 claimed are executed and scenario-validated, and the pricing story is reported honestly (cognitive tokens AND bookkeeping calls, §32.3). The validation discipline remains the point: every revision is executed against a frozen baseline, and every claim about the framework is checked by an independent auditor against the code.)*

---

## 30. Primary Research References

*(Unchanged from v3: the 14 entries — CoALA, 40 Years of Cognitive Architectures, ReAct, ToT/RAP/LATS, ADaPT/Self-Discover, Reflexion/CRITIC/Chain-of-Verification, self-correction limits, multi-agent debate studies, debate-or-vote studies, MemGPT/Generative Agents/Voyager, STOP/ADAS/Darwin Gödel Machine, AgentDojo/AI Control, Grok 4.20 system card, Grok Build.)*

---

## 31. Differential Change Log (v3 → v4)

| ID | v3 defect (aggregated finding) | v4 change | Where | Validated |
|---|---|---|---|---|
| C1 | Classifier not state-only: L2 branch read task config (`verifier_outage`, `stakes`); `stakes` absent from schema | `verifier_outage` producer (diagnose) + `stakes` schema field; classifier reads state only | §3.4, §24.2, §24.4 | S5, S25, S29 |
| C2 | Reliability task-declarable: S26's "bootstrap" passed 0.95 as config; `Verifier.history` never written | Kernel calibration registry + rolling-accuracy history (verdict-correctness, not outcome); no task-declarable warmth | §15.1, §15.4 | S26, S27, S3 |
| C3 | Competence self-rating: only feed was self-generated calibration (0.9 hardcoded); double-updated; stale review on SOLVED | Provenance-gated updates; fresh terminal review; once-per-episode update | §19.3, §14, §24.4 | S22 |
| C4 | PENDING subset a placeholder: planner emitted no tasks; subset fabricated; no class check | SafetyKernel static allowlist table lookup; A2-class asserted; `allowed_subset` interface | §20.3, §24.3 | S20 |
| C5 | HMAC key co-location vacuous; no version/corruption/journaling | Key boundary specified (separate process/keychain) with honest disclosure; version field + corruption path specified | §20.5, §32.4 | S21 (mechanism), design-level (integrity) |
| C6 | Fast path executed external actions with zero governance | External-action tasks rerouted off the fast path at route time | §9.4, §24.4 | S37 |
| C7 | E1 `requires_review` dead on fast path | E1 runs the learning epilogue when `requires_review` | §9.4, §24.4 | S22-ep2 |
| C8 | reliability-blocked discovered after DO: actions executed below-bar | Attest + bar check before execution; misattestation denies first | §15.4, §24.4 | S4, S12 |
| C9 | "Progress-gated" false: premortem/red-team/review re-ran on unchanged state | Content-hash gating for premortem/red team; planner only when needed | §15.6, §24.4 | S2, S20 |
| C10 | PENDING spun the cognitive loop during waits | Wait is progress-gated (~0 tokens/iteration); wall-clock SLA is scheduler-held | §21.4, §24.4 | S20 |
| C11 | −33.6% was a pricing artifact (bookkeeping 201→457 calls, 0-priced) | Both numbers reported (§32.3); re-priced table at 0/0.5/1.0; −33.6% labeled cognitive-only | §32.1–32.3 | metrics |
| C12 | Attribution overstated: S3 delta a cache-reuse artifact; 1210 > 978 arithmetic | Per-mechanism decomposition published (§32.3); v1→v2 attribution footnoted; S3 labeled cache reuse | §32.3 | metrics |
| C13 | Early classifier incomplete: infeasible known at screen but HOW continued; epilogue review on decided outcomes | Classify immediately after constraint screen and after `select`; early exits skip epilogue review | §11.7, §24.4 | S18, S17 |
| C14 | L3 missing; L1 degrade absent from §24.4 (harness-only injection) | L1 branch in classifier; L3 branch in DO; no injection | §15.2, §24.4 | S25, S29 |
| C15 | WHY gate non-blocking (hypotheses never cleared) | Clear hypotheses on gate failure; re-entry bounded | §11.7, §24.4 | S30 |
| C16 | `escalation_conditions` never consumed | Both stop and escalation conditions consumed at DO | §13.7, §24.4 | S31 |
| C17 | Second-verifier rows (A4/A5) unimplemented; no scenario | Second-verifier rule in `verify_outcome`; A5 single-verifier → ESCALATED | §15.4 | S26, S28 |
| C18 | Interface drift: `settle_best_of`/`default_world` undefined; `world.bind()` 22 vs 19 names; `run_council` dict-vs-tuple | Helpers declared; binding contract defined; tuple form fixed; `renegotiate`/`compose` have interface entries | §24.3, §24.4 | doc-level |
| C19 | Config not single source of truth; `human_gate_slas` dead; `pending_timeout` task-declarable; `calls_ceiling` `or` semantics | Kernel-held CONFIG object; SLAs scheduler-consumed; pending timeout kernel-held; `result.status_reason` enumerated | §9.6, §24.2 | S20, S24 |
| C20 | Baseline freeze procedure missing | Freeze procedure specified (who/when/what) | §25, §22 | doc-level |
| C21 | Deferred "per v2" schemas broke §4 self-containment | Core schemas inlined (memory record, agent_answer, baseline) | §18, §17, §22 | doc-level |
| C22 | Coverage disclosure incomplete: no Chaotic/E5, no `search_needed` scenario | E5 crisis scenario (S35) + search scenario (S36); disclosure extended | §9.2, §16.2, §32.4 | S35, S36 |
| C23 | §29 overstated ("every mechanism has a scenario") | Reworded: "every enforcement mechanism in §24.4 has a scenario; exceptions disclosed" | §29 | doc-level |
| C24 | Trust margin dead; minted-token positive path untested; novelty evasion (S3's own toggle); attested-class trusts estimator; missing_evidence escape hatch; MD5 cache; council pricing; S24 overshoot | Margin applied (D10); S33 positive commit; novelty evasion documented as heuristic with hard-budget backstop (C26); max-class bar rule (C30); VOI gap check (C31); SHA-256 cache (C26); realistic council pricing; overshoot documented | §18.2, §9.5, §15.4, §15.6, §17.2 | S33, S34, S14, S12 |
| D1 | E5/Chaotic and probe life-cycle unexecuted | E5 branch + S35; probe life-cycle disclosed as Phase-4 | §9.4, §32.4 | S35 |
| D2 | Continual learning write-only (`retrieve` unimplemented) | `retrieve` called inside diagnosis | §18, §24.4 | S22-ep2 (retrieve in stages) |
| D3 | Session layer prose (renegotiate no call site) | Interface entry; deployment Phase-2 disclosed | §24.3, §26 | doc-level |
| D4 | EvaluationPlane contradiction (§25.2 vs §32.4) | §25.2 reworded to match disclosure; plane Phase-2; freeze procedure specified (C20) | §25, §23.6a | doc-level |
| D5 | Debate step unexecuted (no exchange/adjudication) | CouncilMock executes claim exchange + verifier adjudication; dissent preserved regardless | §17.2 | S23 |
| D6 | §24.6 overclaimed search/VOI/world-model rows | Rows annotated as exercised-or-design-level; S36 exercises search | §24.6, §32.4 | S36 |
| D7 | G-WHY enforced at 2 of 5 predicates | Falsification + VOI predicates evaluated; gate re-enters (C15) | §11.7 | S30 |
| D8 | MethodComposer no mechanism | `compose` call site in route; `reasoning_modules` in route | §16.1, §24.4 | all scenarios |
| D9 | Minted-token positive path untested | S33 commits a stamped procedural lesson | §18, §24.4 | S33 |
| D10 | Trust margin 0.1 dead | Margin applied in the contradiction rule | §18.2, §9.6 | S14 |
| D11 | EVOC/latency claims false in harness | §9.5/§23.8 reworded ("config default; telemetry-derived in production"); timestamps design-level | §9.5, §23.8 | doc-level |
| D12 | "Names verbatim" overclaim (mock drift) | §24.3 reworded to semantic equivalence + mapping note in §32.1 | §24.3 | doc-level |

### 31.1 Non-accepted and deferred findings

- Checkpoint HMAC key management (C5): mechanism specified; integrity guarantee conditioned on a real key boundary (Phase 1); the harness simulates resume without authentication.
- Probe life-cycle (D1), EvaluationPlane batch feedback and co-scaling gate (D4), model heterogeneity, open-ended archives, `renegotiate` deployment (D3) — Phase-gated per §26.
- The independent risk estimator's full separation remains deterministic-checks + second-verifier patterns in the MVP (§20.4).
- Novelty-signature evasion (C26) is documented as a heuristic; hard budgets are the termination guarantee.
- The harness's verifier history is always-correct verdicts (deterministic mocks) — the mechanism is demonstrated, calibration dynamics are not (§32.4).

---

## 32. Empirical Validation

### 32.1 Method

Per the framework's own rules (P4, P9, §22.3), v4 changes were validated by execution. `validation/harness.py` implements the frozen v3 algorithm (baseline) and the v4 algorithm over identical deterministic mock components, runs 36 scenarios (S1–S26 from v3 plus S27–S37 for v4 mechanisms), and asserts the framework's own standards. Pricing is explicit and reported at both levels: **cognitive tokens** (model-call-equivalent costs; bookkeeping — budget, monitors, audit, gates — priced at 0; deterministic re-computation priced at 0) and **bookkeeping calls** (counted, reported). The harness validates control-flow properties, not intelligence; mock signatures are semantically equivalent to the §24.3 interface (D12).

### 32.2 Results (36 scenarios; 3 reproducible runs, identical every run)

| Scenario | v3 status | v4 status | v3 asserts | v4 asserts | v3 tokens | v4 tokens |
|---|---|---|---|---|---|---|
| S1 trivial task, E0 | SOLVED | SOLVED | 4/4 | 4/4 | 2 | 2 |
| S2 executor always fails | RESOURCE_LIMITED | RESOURCE_LIMITED | 6/6 | 6/6 | 39 | 35 |
| S3 frame oscillates | SOLVED | SOLVED | 4/4 | 4/4 | 53 | 51 |
| S4 clear-looking, high stakes | ESCALATED | ESCALATED | 5/5 | 6/6 | 18 | 12 |
| S5 no external verifier | ESCALATED | ESCALATED | 5/5 | 5/5 | 3 | 4 |
| S6 ambiguous success | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 3 | 4 |
| S7 calculator exists | SOLVED | SOLVED | 4/4 | 4/4 | 2 | 2 |
| S8 injection attempt | SOLVED | SOLVED | 5/5 | 5/5 | 15 | 16 |
| S9 EVOC exhausted | RESOURCE_LIMITED | RESOURCE_LIMITED | 4/4 | 4/4 | 2 | 2 |
| S10 proposal flood | SOLVED | SOLVED | 5/5 | 5/5 | 16 | 17 |
| S11 authorization denied | ESCALATED | ESCALATED | 4/4 | 4/4 | 13 | 14 |
| S12 action-class misattestation | UNSAFE | UNSAFE | 4/4 | 4/4 | 13 | 12 |
| S13 red team catches flaw | SOLVED | SOLVED | 4/4 | 4/4 | 21 | 22 |
| S14 memory contradiction | SOLVED | SOLVED | 4/4 | 4/4 | 15 | 16 |
| S15 WHAT gate: no metrics | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 2 | 2 |
| S16 safe probe available | NEEDS_EXPERIMENT | NEEDS_EXPERIMENT | 4/4 | 4/4 | 3 | 4 |
| S17 bounded approximation | APPROXIMATED | APPROXIMATED | 4/4 | 4/4 | 15 | 12 |
| S18 constraints inconsistent | INFEASIBLE | INFEASIBLE | 4/4 | 4/4 | 15 | 5 |
| S19 plan stop-condition | INFEASIBLE | INFEASIBLE | 4/4 | 4/4 | 15 | 16 |
| S20 pending authorization | ESCALATED | ESCALATED | 5/5 | 6/6 | 21 | 18 |
| S21 crash, resume | SOLVED | SOLVED | 4/4 | 4/4 | 22 | 21 |
| S22 competence feedback | SOLVED | SOLVED | 4/4 | 4/4 | 19 | 21 |
| S23 council minority | SOLVED | SOLVED | 4/4 | 4/4 | 22 | 27 |
| S24 call budget hard-stop | RESOURCE_LIMITED | RESOURCE_LIMITED | 4/4 | 4/4 | 25 | 20 |
| S25 low-stakes verifier outage | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 3 | 4 |
| S26 kernel-calibrated verifier, A4 | SOLVED | SOLVED | 4/4 | 4/4 | 15 | 16 |
| S27 history-fed calibration | SOLVED | SOLVED | 3/3 | 4/4 | 23 | 27 |
| S28 A5, single verifier | ESCALATED | ESCALATED | 3/3 | 4/4 | 18 | 12 |
| S29 L3 ladder | ESCALATED | ESCALATED | 3/3 | 4/4 | 3 | 4 |
| S30 WHY gate re-entry | ESCALATED | NEEDS_EVIDENCE | 3/3 | 4/4 | 15 | 8 |
| S31 plan escalation condition | SOLVED | ESCALATED | 3/3 | 4/4 | 18 | 16 |
| S33 minted-token commit | SOLVED | SOLVED | 3/3 | 4/4 | 15 | 16 |
| S34 VOI fillable gap | NEEDS_EVIDENCE | SOLVED | 3/3 | 4/4 | 3 | 16 |
| S35 E5 chaotic crisis | INFEASIBLE | ESCALATED | 3/3 | 4/4 | 26 | 26 |
| S36 search branch | INFEASIBLE | INFEASIBLE | 3/3 | 4/4 | 32 | 31 |
| S37 fast-path governance | SOLVED | SOLVED | 3/3 | 4/4 | 15 | 16 |
| **Totals** | | | **141/141** | **153/153** | **560** | **547** |

### 32.3 What the suite demonstrates — and honest attribution

- **Trust boundaries (C1/C2/C19):** no terminal state is produced by direct classifier reads of task inputs (S5/S25/S29 run through the state-only classifier); verifier reliability comes from the kernel registry or history, never task-declarable warmth (S26 vs S27); security knobs are kernel-held config.
- **No below-bar execution (C8):** S4 escalates before the planner or executor runs (18 → 12 tokens, zero side effects); S12 denies misattestation before anything executes.
- **Progress gating (C9):** S2's unchanged-state loop pays once for premortem/red-team (39 → 35); S20's pending wait costs ~0 per iteration (21 → 18).
- **Second-verifier rule (C17):** S28 — an A5 task with a single verifier cannot SOLVE; S26 — with kernel calibration and a second verifier, it can.
- **Ladder complete (C14):** S25 (L1 degrade), S5 (L2 escalate), S29 (L3 no-action) all terminate correctly with no harness-only injection.
- **Gates complete (C15/C16):** S30 — the WHY gate re-enters and never advances to HOW; S31 — plan escalation conditions end the loop with ESCALATED.
- **Executed branches (C22/D8/D5/D2):** S35 exercises the E5 crisis path (effort 5, council, human gate); S36 exercises search; every route carries MethodComposer modules; diagnosis reads memory back (S22-ep2).
- **Honest attribution (C11/C12):** the v3 "−33.6%" was cognitive-token-only under 0-priced bookkeeping — at 1 token per bookkeeping call, v3 vs v2 was *+7.2%*. v4 reports both numbers. The v4 cognitive delta (−2.3% over 36 scenarios, including 10 new security scenarios) is smaller because the new mechanisms (pre-DO bar checks, second-verifier checks, memory read-back, debate adjudication, search) add cognitive calls — the honest trade for enforcement. The largest per-scenario savings: early classifier (S5/S6/S16/S25/S29: 3–4 tokens), classify-after-screen (S18: 15 → 5), pre-DO bar (S4: 18 → 12, S28: 18 → 12), progress gating (S2/S20). S3's saving is cache reuse on content-identical regeneration, labeled as such.
- **Reproducibility:** deterministic; 3 consecutive runs identical; totals 141/141 (v3 baseline) and 153/153 (v4).

### 32.4 Honest limitations of the validation

- Mock components: control-flow guarantees hold for any components satisfying the contracts; not model intelligence, sampling, or real tools.
- **Coverage disclosure:** the harness implements the v4 §24.4 loop: router (flags, stakes override, competence, compose, E5, fast-path governance), all gates (re-evaluable WHY), diagnose (producers, VOI flag, memory read-back), council (2 agents, debate round + adjudication, minority ledger), search branch, verifier (kernel calibration, rolling history, second-verifier rule, SHA-256 delta cache), planner (stop/escalation conditions), kernel (attest, pending, allowlist, minting, interrupt), executor (idempotency), review (fresh terminal), competence (once per episode), memory (channels, contradiction with margin, quarantine, retrieve), improvement (dedup, evaluate), LoopMonitor, BudgetController, TaskScheduler (checkpoint/resume). Not implemented (design-level, disclosed): probe life-cycle (design→execute→fold back), EvaluationPlane `run_suite`/`produce_profile` and co-scaling gate, ExecutionMonitor findings beyond plan conditions, AuditLog latency timestamps, LearningScheduler batching, multi-round debate, checkpoint HMAC/versioning (integrity boundary), `renegotiate` deployment.
- **Pricing honesty:** cognitive tokens exclude bookkeeping (budget, monitors, audit, gates — 0-priced) and deterministic re-computation (0-priced); the §32.2 totals are cognitive-only. Bookkeeping call counts grew with enforcement (per-stage audit, checks, gates); they are reported separately in the harness output and at 1 token per bookkeeping call the v3-vs-v2 comparison inverts — v4 therefore reports both numbers rather than a single headline (C11).
- The verifier history in the harness records always-correct verdicts (deterministic mocks) — the mechanism (history → reliability → bar) is demonstrated; calibration dynamics require real evaluation outcomes (S27 uses repeated episodes).
- The novelty signature remains a heuristic; hard budgets are the termination guarantee (C26).
- The kernel calibration registry and the pending-timeout/calls-ceiling values are seeded by scenario world-config in the harness (modeling kernel-held settings); in production they live in the kernel-held CONFIG object, populated by EvaluationPlane outcomes and operator policy. C19's kernel-holding is mechanism-validated; the algorithm has no task-scope reads of security knobs (world-facts modeling).
- S35's human gate is genuinely reached: the E5 task clears the bar (kernel calibration), so `authorize` returns PENDING and the timeout escalates — the earlier draft's ESCALATED came from the bar check; corrected in the harness.

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
