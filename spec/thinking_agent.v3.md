# Thinking Agent

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Version:** 3.0  
**Research cutoff:** August 7, 2026  
**Status:** Research and engineering blueprint (validated — see §32)  
**Source policy:** Primary arXiv papers and official xAI materials were prioritized over third-party commentary.  
**Change policy:** v3 supersedes v2. The differential change log in §31 records every accepted finding from the v2 self-review, the v3 change, and its validation status. The executable validation harness lives in `validation/harness.py`; its results are in §32.

---

## 1. Executive Summary

Thinking Agent combines:

1. A ranked portfolio of 40 traditional human thinking frameworks (evaluated by adoption priority, with Cynefin, Premortem, AAR, Double-Loop Learning, RPD, and root-cause methods at the top).
2. The `WHAT → WHY → HOW → DO → REVIEW` process.
3. The memory, multi-agent, metacognitive, and self-evolution concepts in the earlier architecture drafts.
4. Research on cognitive architectures, reasoning, planning, tool use, reflection, verification, multi-agent systems, memory, self-improving scaffolds, and agent security.
5. Production patterns documented by xAI, including adaptive reasoning, parallel subagents, plan-review workflows, verification, synthesis, and tool-oriented agent harnesses.

Its central operating loop is:

> **META-CONTROL → WHAT → WHY → HOW → DO → REVIEW**

A continuous **VERIFY** layer surrounds every stage, and a **governed loop** (loop monitors, budget envelope, stage gates, explicit state classifier, delta-based verification, checkpoint/resume) guarantees termination, graceful failure, and cost-boundedness.

v3's core advance over v2 is **enforcement fidelity**: v2 printed standards its own reference algorithm could not honor — the §15.4 verification thresholds had no consumer (tasks were declared SOLVED at seed reliability 0.5), the stage gates G-HOW and G-DO had no call sites, the classifier read fields no schema declared, the PENDING authorization branch was an unbounded re-execution loop, and the "69% cost reduction" was misattributed to the fast path when it was really loop termination. v3 makes the document's own algorithm satisfy its own standards, and validates each fix by execution (§32). The harness compares the frozen v2 algorithm against the v3 algorithm over identical components: **v2 baseline 98/98 asserts, v3 111/111 asserts, deterministic across runs, 33.6% cognitive-cost reduction on the loop-heavy scenarios**.

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

Every task terminates in exactly one of the eight graceful states (§3.3), and every terminal state produces the proof-carrying decision packet (§15.4). In v3, every state has a named producer with a data path in the reference algorithm (§3.3 producer table, §24.4), and the threshold table is enforced at the SOLVED gate (§15.4) — both demonstrated by the harness (§32).

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

Thinking Agent therefore separates the following functions:

- Generating an answer.
- Determining whether the answer is true.
- Determining whether the action is safe.
- Executing the action.
- Learning from the result.
- Changing the system that generated the result.

These functions must not be collapsed into one unconstrained model call. In v3, each function has a named owner component with an interface (§24.1, §24.3) and — critically — **the interfaces the reference algorithm actually calls**: v2 listed components the algorithm never invoked (CouncilOrchestrator, ExecutionMonitor, CompetenceModel, TaskScheduler) and invoked functions the interface never declared (finding B4); v3's §24.3/§24.4/§24.6 are cross-checked by the harness itself.

---

## 3. Scope and Non-Claims

### 3.1 What “universal” means

Thinking Agent is intended to address:

- Clear and routine problems.
- Expert analytical problems.
- Complex adaptive problems.
- Chaotic or crisis conditions.
- Causal diagnosis.
- Scientific discovery.
- Creative design.
- Strategic planning.
- Software and digital operations.
- Embodied action.
- Social and stakeholder problems.
- Adversarial environments.
- Long-horizon learning.
- Architecture improvement.

It does this by selecting different reasoning procedures rather than applying one fixed prompt to every task.

### 3.2 What Thinking Agent does not claim

Thinking Agent does not claim that:

- Current language models are AGI.
- Multi-agent debate is automatically better than one agent.
- Self-reflection is a reliable substitute for external verification.
- More inference-time computation always improves an answer.
- Recursive self-improvement can be made safe through prompting alone.
- A universal knowledge representation has already been discovered.
- Benchmark performance proves general intelligence.
- ASI can be safely produced by simply increasing model size or agent count.
- The v3 reference algorithm, its harness, or its mock components demonstrate any of the above. The harness (§32) validates control-flow properties, not intelligence; its honest scope is restated in §32.4.

### 3.3 Required graceful-failure states

Every task must terminate in one of these explicit states. In v3, each state has a **producer** — the component and data path that can set it — and the harness demonstrates all eight are reachable (§32, S1–S26):

| State | Meaning | Producer (v3) |
|---|---|---|
| `SOLVED` | The result satisfies the success criteria and verification threshold. | `verify_outcome` with external identity, reliability ≥ class bar (§15.4) |
| `APPROXIMATED` | An exact solution was unavailable, but a bounded approximation was produced. | `select` records `error_bound` → `state.approximation_available` (§15.5) |
| `NEEDS_EVIDENCE` | A decision cannot responsibly be made without more information. | `diagnose` fills `missing_evidence` (§11.5) |
| `NEEDS_EXPERIMENT` | A safe probe or experiment is the next rational action. | `diagnose` sets `state.probe_available` per §19.2 |
| `INFEASIBLE` | Constraints are inconsistent or the requested outcome is not currently achievable. | constraint screen sets `state.infeasible` (§12.4) |
| `UNSAFE` | The requested action violates a safety, legal, ethical, or permission boundary. | SafetyKernel denial; attestation mismatch (§20.4) |
| `ESCALATED` | Human or domain-expert judgment is required. | SafetyKernel denial; L2/L3 no-verifier ladder; reliability-blocked (§15.2, §15.4); PENDING timeout (§21.4) |
| `RESOURCE_LIMITED` | The expected value of further computation does not justify its cost. | LoopMonitor/BudgetController exhaustion: iterations, tokens, calls, EVOC, novelty plateau (§9.5–9.6) |

### 3.4 State-transition policy

- Every terminal state is produced by exactly one owning mechanism (the Producer column above); v2's ghost fields (classifier inputs with no producer and no schema entry) are eliminated — the fields exist in `task_state` (§24.2) and are assigned by their producers in §24.4 (finding B1).
- `UNSAFE` and `ESCALATED` are distinguished: `UNSAFE` means the action is prohibited; `ESCALATED` means the action may be valid but requires authority the system does not have.
- States are mutually exclusive; the classifier tests them in the fixed order defined here and implemented by `classify_terminal` (§24.3, §24.4): verifier-outage-and-high-stakes (L2) → ambiguity → reliability-blocked → evidence gap → probe → infeasibility → budget exhaustion → approximation → residual.
- Every terminal path writes the proof-carrying decision packet (§15.4) via the common epilogue of §24.4 — including denials, pending timeouts, and early classifier exits.

---

## 4. Architectural Synthesis and Lineage

Thinking Agent synthesizes five bodies of knowledge plus its own revision history. No component depends on a separate companion document; every required concept is inlined below or anchored to research URLs in §30.

| Lineage | Retained contribution | Thinking Agent implementation |
|---|---|---|
| Ranked traditional human thinking models (40 frameworks) | Cynefin, Premortem, AAR, Double-Loop Learning, RPD, root-cause, metacognition, creativity, Red Teaming, supporting frameworks (§5.9) | Adaptive routing, risk simulation, structured review, method library, adversarial verification |
| Staged problem-solving process (WHAT → WHY → HOW → DO → REVIEW) | Framing discipline, diagnostic rigor, alternative generation, selection criteria, execution project management, review and iteration | Primary task-level loop (§10–§14) with boolean stage gates enforced in §24.4 |
| Grok-inspired architecture draft | Fast/full dual paths, CoALA memory hierarchy, specialized roles, hierarchical planning, nested self-evolution | Meta-controller (§9), structured workspace (§7), council (§17), learning engine (§14, §22) |
| Verification-first multi-agent protocol | Independent generation, evidence-weighted aggregation, non-claims, anti-debate-failure guards | Verifier separation (§15), verifier-weighted synthesis (§17.3), explicit uncertainty (§3, §5.4) |
| Agent-security and production literature (2024–2026) | Tool security, authority/data separation, least privilege, gated self-modification, structured state, evaluation portfolio | Safety kernel (§21), tool broker (§20), improvement pipeline (§22), evaluation plane (§23), shared state (§24.2) |
| v1 self-review (2026) | Termination, budget governance, stage gates, state-machine completeness, feedback loops, failure semantics | Governed loop, BudgetController, LoopMonitor, classifier, CompetenceModel, transaction semantics (§9, §15, §20, §24) |
| v2 self-review (2026) — six-lens council + executable validation | Enforcement fidelity: threshold bars with consumers, producers for every state, complete gates, pending semantics, checkpoint/resume, delta verification, honest attribution | §3.3 producers, §15.4 enforced bars, §12.8/§13.7 gates, §21.4 pending, §20.5 resume, §15.6 delta reuse, §32.3 attribution — see §31 |

---

## 5. Research Foundations

### 5.1 Cognitive architecture

Cognitive-architecture research consistently treats intelligence as an interaction among perception, attention, action selection, memory, learning, and reasoning rather than a single monolithic process. CoALA provides a particularly useful language-agent abstraction: modular memory, internal and external action spaces, and structured decision procedures. ([arxiv.org](https://arxiv.org/abs/1610.08602?utm_source=openai))

Thinking Agent adopts a **polyglot cognitive substrate** rather than assuming that all knowledge must be stored in one format. Text, graphs, equations, code, images, databases, models, procedures, and trajectories can coexist as long as they share provenance, identity, access-control, and relationship metadata.

### 5.2 Grounded reasoning and tool use

ReAct demonstrated the value of interleaving reasoning, action, and environmental observation. Toolformer showed that models can learn when and how to call external APIs, while SayCan combined semantic planning with grounded affordances. ([arxiv.org](https://arxiv.org/abs/2210.03629?utm_source=openai))

### 5.3 Search, decomposition, and planning

Tree of Thoughts, RAP, LATS, and ADaPT show complementary methods for exploring alternative reasoning paths, simulating future states, backtracking, and decomposing tasks only when needed. Self-Discover adds method composition by task signature. ([arxiv.org](https://arxiv.org/abs/2305.10601?utm_source=openai))

Thinking Agent therefore includes a **method composer** and a **SearchController** (§16.2) with an explicit exploration budget and an expected-value-of-exploration gate. The SearchController is invoked from `generate_candidates` when `route.requires_search` is set.

### 5.4 Reflection and verification

Reflexion, Self-Refine, CRITIC, and Chain-of-Verification show that iterative feedback can improve outputs, especially from tests, tools, or environments. Intrinsic self-correction is unreliable; models may fail to locate errors, convert correct answers into incorrect ones, or produce false-positive verification judgments. ([arxiv.org](https://arxiv.org/abs/2303.11366?utm_source=openai))

Thinking Agent follows this rule:

> **Self-criticism is a source of hypotheses, not proof of correctness.**

In v3 this rule is enforced structurally at every level where it can be violated: (a) the `SOLVED` gate requires external identity *and* reliability ≥ class bar (§15.4) — the v2 harness quietly SOLVED at seed reliability 0.5, and v3's harness now blocks that (finding B2/B11, §32 S4); (b) verifier identity is no longer a mutable string the orchestrator can stamp — it is set by the VerifierRegistry from the verifier's kind and evaluation history, and the v2 fast-path override that masked SELF is removed; (c) competence is fed by evaluation outcomes, not self-reported accuracy (§19.3).

### 5.5 Multi-agent reasoning

Later systematic studies found debate does not reliably beat strong single-agent baselines; model heterogeneity matters; majority voting may explain much of the apparent gain; majority pressure, sycophantic conformity, and consensus collapse are failure modes. ([arxiv.org](https://arxiv.org/abs/2305.14325?utm_source=openai))

The protocol requires: independent generation before communication; verification before debate; targeted debate only over unresolved differences; preservation of minority reports; evidence-weighted aggregation; heterogeneity when possible. In v3 the council is a **branch in the reference algorithm** (`if route.use_council: run_council` — §17.4 predicates consumed in §24.4), not a comment: it produces `{candidate_set, minority_reports, unresolved_disagreements}` and the minority ledger is written before aggregation and surfaced in the decision packet (§17.2–17.3, §32 S23).

### 5.6 Memory and lifelong learning

CoALA, MemGPT, Generative Agents, and Voyager support separated working/episodic/semantic/procedural memory, consolidation, reflection, dynamic retrieval, and skill libraries. ([arxiv.org](https://arxiv.org/abs/2309.02427?utm_source=openai))

In v3 the write protocol is complete: authority tokens are **minted by the SafetyKernel** (a writer-stamped string like `authorized_expert` is not authority — finding B14), trust labels derive from verifier reliability, contradiction handling uses the trust-margin rule with quarantine and promotion (§18.2–18.6).

### 5.7 Self-improving systems

STOP, Automated Design of Agentic Systems, and the Darwin Gödel Machine show model-based systems can improve portions of their scaffolding through search and empirical evaluation, bounded and task-dependent. ([arxiv.org](https://arxiv.org/abs/2310.02304?utm_source=openai))

Thinking Agent separates proposal authority from deployment authority. In v3 the §22.3 acceptance pipeline is **invoked** (`improvement_engine.evaluate`) whenever a proposal passes admission control and a frozen baseline exists — v2 only queued (finding B/F5, §32 S10).

### 5.8 Production agent patterns

Official xAI documentation describes production workflows: plan, focused subagent contexts, parallel fan-out, adversarial verification, synthesis; and the Grok Build harness components. ([x.ai](https://x.ai/news/workflows)) Official xAI safety documentation evaluates chat, agentic, injection, deception, sycophancy, sabotage, and dual-use behavior. ([data.x.ai](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf))

### 5.9 Traditional thinking-model portfolio

Thinking Agent draws on a ranked survey of 40 traditional human thinking models, scored by adoption priority (1 = lowest leverage, 10 = highest). The table covers the top tier; every listed contribution is integrated into stages, the method composer, or multi-agent roles.

| Rank | Model | Origin / Field | Core concept | Adoption score | Why it scores high for agents |
|------|-------|----------------|--------------|----------------|--------------------------------|
| 1 | Cynefin Framework | Complexity science (Snowden) | Sense context first; respond per domain: Clear/Complicated/Complex/Chaotic/Disorder | 10 | Adaptive loop intensity and Fast-vs-Full routing — the single highest-leverage addition |
| 2 | Premortem Analysis | Decision science (Klein) | Imagine failure has occurred; work backward; mitigate up front | 10 | Proactive risk at near-zero cost; runs before HOW commitment (§12.6) |
| 3 | After-Action Review (AAR) | Military / Lean | Supposed → actual → why the difference → what changes next | 10 | Perfect match for REVIEW; single- and double-loop learning (§14) |
| 4 | Double-Loop Learning | Argyris & Schön | Single-loop changes tactics; double-loop questions assumptions and frames | 9.5 | Core to self-evolution; runs inside the loop to trigger mid-task reframes (§14.3) |
| 5 | Recognition-Primed Decision (RPD) | Klein | Pattern match → rapid mental simulation → act | 9.5 | Fast Recognition Path for Clear/Complicated expert domains |
| 6 | Root-cause suite (5 Whys + Ishikawa + FTA) | Toyota/Ishikawa/safety | Causal chains, category diagrams, boolean fault trees | 9 | Strengthens the WHY stage |
| 7 | Metacognition Cycle | Flavell | Plan → Monitor → Evaluate → Adjust | 9 | The lightweight parallel meta-process inside META-CONTROL |
| 8 | Dual Process Theory (S1 & S2) | Kahneman | Fast intuitive vs slow deliberate with context-appropriate switching | 9 | Foundation for Fast-vs-Full routing |
| 9 | Paul-Elder Critical Thinking | Philosophy/Education | Eight Elements vs Intellectual Standards | 8.5 | Quality bar for Diagnostician, Researcher, Verifier, Synthesizer |
| 10 | Theory of Constraints (TOC) | Goldratt | Current Reality Tree → Evaporating Cloud → Future Reality Tree | 8.5 | Contradiction resolution; synergizes with TRIZ |
| 11 | Osborn-Parnes CPS | Creativity | Clarify → Ideate → Develop → Implement → Evaluate | 8 | HOW-stage divergent ideation |
| 12 | Red Team Thinking | Military/Security | Attack your own plan to find weaknesses first | 8 | The Red Team role and HOW-stage gate (§12.7) |
| 13 | Six Thinking Hats | de Bono | Six perspectives: White/Red/Black/Yellow/Green/Blue | 8 | HOW-stage consolidation and perspective diversity |
| 14 | TRIZ | Altshuller | Resolve technical/physical contradictions via 40 principles | 8 | Structured creativity for contradiction-heavy classes |
| 15 | SCAMPER | Eberle | Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse | 7.5 | Rapid ideation for the Explorer role |
| 16 | Kaizen | Toyota | Small, testable, reversible improvements | 7.5 | Governs self-evolution step size (§22.5) |
| 17 | OODA Loop | Boyd | Observe → Orient → Decide → Act | 7 | The DO-stage micro-loop pattern |
| 18 | Design Thinking | Design/Innovation | Empathize → Define → Ideate → Prototype → Test | 7 | User-facing or product-definition tasks |
| 19 | GROW Coaching Model | Whitmore | Goal → Reality → Options → Will | 6.5 | WHAT-stage ambiguous goals; stakeholder alignment |
| 20 | Nemawashi | Japanese decision making | Informal consensus before formal decisions | 5.5 | Pre-debate alignment; stakeholder communication |

*(v3 note: ranking is by adoption score — Design Thinking (7.0) correctly precedes GROW (6.5); the v2 table had a residual ordering anomaly, now fixed.)*

The remaining 20 frameworks cover philosophical cross-cultural traditions (Wu Wei, Stoic Reflection, Buddhism, Ubuntu, 三思而后行), education taxonomies (Bloom's, Kolb's, Gibbs' Reflective Cycle, IDEAL), and specialized process frameworks (PDCA/PDSA, DMAIC, SWOT, Appreciative Inquiry, Hansei, Socratic Method, Action Learning, Dialectical Thinking, 4E Cognition, High-Context vs Low-Context, Ladder of Inference). They are selectively called on by the method composer (§16) according to the task signature.

---

## 6. Design Principles

### P1. Context before cognition
### P2. Frame before diagnosing; diagnose before prescribing
### P3. Evidence outranks confidence
### P4. External feedback outranks intrinsic self-critique
### P5. Independent diversity before social influence
### P6. Reversible before irreversible
### P7. Verification scales with consequence
### P8. Memory requires governance
### P9. Self-improvement must be empirical and reversible
### P10. Preserve human authority
### P11. Stop when marginal value turns negative
### P12. Expose decision artifacts, not performative reasoning

*(Principles retain their v2 wording; the mechanism matrix below is normative.)*

### 6.5 Principle–mechanism matrix (v3)

Every design principle is bound to an enforcing component and an enforcing point. v3 corrects two v2 overclaims: P5 now has a real algorithm branch (the council call), and P6's penalty is exercised inside `select` (documented as contract-level).

| Principle | Enforcing component | Enforcing point (v3) |
|---|---|---|
| P1 | MetaRouter | `route(state, competence)` precedes all stages (§24.4 step 1) |
| P2 | Stage gates | WHAT/WHY/HOW gates block advancement (§10.5, §11.7, §12.8, §24.4) |
| P3 | VerifierRegistry | Aggregation and SOLVED require reports, never self-confidence (§15.4, §17.3) |
| P4 | VerifierRegistry | SOLVED requires external identity AND reliability ≥ class bar (§15.4) |
| P5 | CouncilOrchestrator | `if route.use_council: run_council` branch (§17.2, §24.4); fresh contexts + minority ledger |
| P6 | SafetyKernel + select | Reversibility class on candidates/actions; irreversibility penalty in decision score (§12.5, §13.2) |
| P7 | MetaRouter + VerifierRegistry | `verification_depth` from stakes/effort; class bars per (action class, stakes) (§9.2, §15.4) |
| P8 | MemoryManager | Write protocol with minted authority tokens, contradiction rule, quarantine (§18.2) |
| P9 | ImprovementEngine + EvaluationPlane | §22.3 pipeline invoked (`evaluate`) against a frozen baseline (§22.3–22.4, §32 S10) |
| P10 | SafetyKernel + GoalManager | Goal contract signed and external; renegotiation gated (§21, §24.5) |
| P11 | LoopMonitor + BudgetController | EVOC, novelty plateau, iteration/token/call budgets → RESOURCE_LIMITED (§9.5–9.6, §24.4) |
| P12 | Common epilogue | `build_decision_packet` on every terminal path, including denials (§15.4, §24.4) |

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
│ checkpoint/resume • action-class attestation                │
│ authority-token minting • no-replication whitelist          │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ META-CONTROLLER                                             │
│ Context classification • routing • effort • agenda          │
│ competence model (evaluation-fed) • uncertainty             │
│ BUDGET ENVELOPE • ROUTE FLAGS                               │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ STRUCTURED COGNITIVE WORKSPACE                              │
│ WHAT → WHY → HOW → DO → REVIEW                              │
│ Continuous VERIFY (delta-based) • LOOP MONITOR              │
│ early classifier entry • checkpoint at every stage          │
└───────────────┬──────────────────────┬───────────────────────┘
                │                      │
┌───────────────▼────────────┐  ┌──────▼──────────────────────┐
│ REASONING AND COUNCIL      │  │ MEMORY AND WORLD MODEL     │
│ Decompose • search         │  │ Working • episodic         │
│ simulate • generate        │  │ semantic • procedural      │
│ critique • synthesize      │  │ causal • multimodal        │
│ CouncilOrchestrator branch │  │ CompetenceModel (closed)   │
└───────────────┬────────────┘  └──────┬──────────────────────┘
                │                      │
┌───────────────▼──────────────────────▼───────────────────────┐
│ TOOL BROKER AND EXECUTION SANDBOX                           │
│ timeouts • retries • idempotency • compensation             │
│ pending-authorization subset-once • crash checkpoint        │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ TELEMETRY, EVALUATION, AND SELF-EVOLUTION                   │
│ per-stage audit • frozen baseline • change pipeline         │
│ EvaluationPlane (immutable) • competence history            │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Four Nested Timescales

### 8.1 Action loop

```text
Observe → Predict → Select action → Authorize → Execute → Verify
```

Short ReAct/OODA-style loop during execution. Each action is transactional (§13.3): idempotency keys, timeouts, retries, per-class compensation (§20.3).

### 8.2 Task loop

```text
META → WHAT → WHY → HOW → DO → REVIEW
```

The governed main loop (§24.4): iteration/token/call budgets, novelty/repetition monitoring, stage gates, REVIEW-in-loop, early classifier entry, checkpoint at every stage boundary (§20.5), so a task spans sessions without losing its contract.

### 8.3 Learning loop

```text
Episodes → AAR → Lesson extraction → Skill update → Evaluation
```

Operates across tasks. The CompetenceModel is its operative driver in v3: `competence.update` runs at every episode terminal (REVIEW-in-loop and epilogue) and writes `task_state.competence`, which `route()` consumes (§19.3, §32 S22 — two sequential episodes change the second route). Batch EvaluationPlane results are the primary long-term updater (Phase 2+, §26); a LearningScheduler for queue-triggered consolidation is specified in §24.5.

### 8.4 Architecture-evolution loop

```text
Change proposal
→ admission control (dedup, rate, static policy)
→ static policy check
→ sandbox branch
→ benchmark vs stable baseline
→ adversarial audit
→ independent review
→ approval
→ canary deployment
→ monitoring
→ retain or roll back
```

Must run more slowly and under stronger governance than the task loop. In v3 the pipeline is invoked by `improvement_engine.evaluate` whenever a proposal passes admission and a frozen baseline exists (§22.3, §32 S10); R2+ changes are epoch-spaced (§22.7); the evaluation plane is immutable to candidates (§22.6).

### 8.5 Session layer

The TaskScheduler owns task identity, priority arbitration (stakes × arrival precedence table, §24.5), checkpoint/resume, and goal renegotiation. Prospective memory commitments are consumed by the scheduler.

---

## 9. Stage 0 — META-CONTROL

### 9.1 Responsibilities

The meta-controller (implemented as the **MetaRouter**):

- Parses the goal and delegated authority.
- Classifies the problem context (Cynefin).
- Estimates novelty, uncertainty, stakes, reversibility, and adversariality.
- Selects reasoning modules.
- Allocates model, tool, agent, time, and token budgets (the **budget envelope**, §9.6).
- Sets **route flags** that make effort levels operational (§9.4).
- Monitors progress and cognitive failure modes (LoopMonitor).
- Decides when to continue, stop, ask, experiment, or escalate.
- Maintains an explicit competence model, fed by evaluation history (§19.3) — never by introspection.

### 9.2 Cynefin-based routing

| Context | Default strategy | Typical route |
|---|---|---|
| Clear | Recognize, retrieve, apply known procedure | Fast path (E0–E1) |
| Complicated | Decompose and apply expert analysis | Verified deliberate path (E2) |
| Complex | Probe, observe, update, and adapt | Full experimental loop (E3–E4) |
| Chaotic | Stabilize first, minimize harm, then reclassify | Crisis path with human gate (E5) |
| Disorder | Split the task and classify each part | Decomposition path |

Stakes override simplicity. A familiar medical, legal, financial, infrastructure, or security action is not routed to an unverified fast path merely because the pattern looks familiar.

**Stakes scale:** integers 1–5 (1 routine … 5 critical). Consumers: effort override (stakes ≥ 4 forces E ≥ 2), verification thresholds (§15.4), action-class expectations (§13.2). Stakes ≥ 3 are **attested by an independent risk estimator** (§20.4); the attestation trigger itself is not self-circumventable — the estimator is invoked whenever the route would take the fast path on a familiar pattern, regardless of the self-estimate (finding R3).

**Routing justification log:** every route decision records inputs, route, attestation reference; spot-audited; feeds §23.7 routing-quality dimensions.

### 9.3 Routing variables

```text
complexity, novelty, uncertainty, stakes, irreversibility,
environment volatility, adversarial pressure,
capability match (from CompetenceModel), evidence availability,
time constraints, human availability
```

### 9.4 Reasoning-effort levels (operational)

| Level | Description | Route flags | Typical configuration |
|---|---|---|---|
| `E0` | Reflex | `requires_generation=F, requires_review=F` | Direct retrieval/solver; one outcome check; no review/memory |
| `E1` | Fast verified | `requires_generation=F, requires_review=T` | One solver plus lightweight checks; light review+memory on exit |
| `E2` | Deliberate | `requires_diagnosis=T` | Structured decomposition and verifier |
| `E3` | Search | `+ SearchController, council eligible` | Multiple candidates, simulations, red team |
| `E4` | Experimental | `+ probes` | Full loop with probes and evidence collection |
| `E5` | Critical | `+ council forced, human gate` | Independent council, formal checks, human approval |

Route flags gate every stage of the algorithm (§24.4). E0/E1 take the direct-answer path with a single verification pass and a packet; the fast path is a *return before the loop*, priced at 3 cognitive calls (§32 S1/S7).

### 9.5 Expected value of computation (operational)

Additional reasoning is justified when:

```text
Expected value of computation
=
probability that more reasoning changes the decision
× expected benefit of that change
− compute cost
− delay cost
− added operational risk
```

The LoopMonitor operationalizes termination (§24.4):

- **Novelty signature (v3):** a canonicalized hash (sorted keys) over (hypotheses, frame, observations, evidence, alternatives, plan). Two consecutive identical signatures trigger the *novelty plateau* stop. Canonicalization and the wider input set close the v2 evasion where cosmetic frame mutations (e.g., a `toggle` counter) reset the plateau indefinitely (finding R4); the signature is a stopping heuristic, not evidence.
- **Repetition counter:** repeated unproductive actions stop the loop.
- **EVOC proxy (v3):** `evoc_estimate = base_benefit − decay × iterations_used`, where `base_benefit` is derived from telemetry (§23.8) — measured marginal utility of recent iterations from the verification delta — and capped in influence by the config block (§9.6). The first term ("probability that more reasoning changes the decision") is a **stopping heuristic**, never evidence for any claim (finding R7/F12).
- **Hard budgets:** iteration, token, and call ceilings (and the deadline, when set) from the budget envelope always terminate with `RESOURCE_LIMITED`. `calls_max` is enforced on cognitive calls at loop top *and* inside `budget.check` per iteration (finding F1/B9); `agents_max` is a per-round council cap (§17.4).

### 9.6 Budget envelope and configuration block (v3)

The envelope is typed; `budget.check` runs at loop top and `budget.consume` runs at the route, fast-path, and loop-top entries (the metering points of §24.4 — stage entries are accounted through the loop-top check):

```yaml
budget_envelope:
  tokens_max:      # default 40 + 20 × effort
  calls_max:       # default 16 + 8 × effort (+10 if council); scenario-configurable
  iterations_max:  # default 1 + 2 × effort
  agents_max:      # per-round council cap: 0 below E3, 4 at E3+
  deadline:        # optional wall-clock bound, consumed by budget.check
  tokens_used:  calls_used:  iterations_used:
```

**Configuration block (v3, single source of truth — finding F10):** every tunable default lives in one YAML block in the implementation, keyed to its owner section:

```yaml
config:
  reliability_seed_model_verifier: 0.5      # §15.1 (deterministic tools: 1.0)
  class_bars: §15.4 table                    # per (action class, stakes)
  trust_margin: 0.1                          # §18.2
  consolidation_duplicates: 3                # §18.2
  gate_reentry_budget: 3                     # §10.5
  reframe_budget: 4                          # §14.3
  pending_timeout: 8                         # §21.4
  human_gate_slas: {A2: 0, A3-A4: 60s, A5: 24h}  # §21.4
  evoc: {base_benefit: 0.6, decay: 0.05}     # §9.5 proxy
  novelty_plateau: 2                         # §9.5
```

Effort class is self-declared by the task — v3 documents this as a residual risk (budget laundering via self-classification, finding R8) with two mitigations: effort-class attestation for stakes ≥ 3 (§20.4) and the call ceiling as the final backstop. The harness's `calls_ceiling` scenario override demonstrates the mechanism (S24).

---

## 10. Stage 1 — WHAT: Frame the Problem

*(Objectives §10.1, Problem Definition Card §10.2, framing procedure §10.3, frame critics §10.4 unchanged from v2.)*

### 10.5 Exit gate (predicates)

```text
G-WHAT-1  goal and decision owner identified
G-WHAT-2  scope and constraints explicit
G-WHAT-3  success_metrics non-empty
G-WHAT-4  ambiguities resolved or recorded
G-WHAT-5  decision recorded whether WHY is necessary
```

Gate failure → re-enter WHAT with the reason recorded; bounded by `gate_reentry_budget = 3`, after which the task returns `NEEDS_EVIDENCE` (or `ESCALATED` if the owner is unavailable). Enforced at §24.4; demonstrated by §32 S15.

---

## 11. Stage 2 — WHY: Diagnose and Model

*(Objectives §11.1, diagnostic structures §11.2, hypothesis ledger §11.3 — including `falsification_evidence` — evidence discipline §11.4, active information gathering §11.5 with `evidence_service.voi`, premortem for diagnosis §11.6 unchanged from v2.)*

### 11.7 Exit gate (predicates)

```text
G-WHY-1  leading hypothesis has decision-relevant evidence
G-WHY-2  significant alternatives considered (≥ 1 or explicit nil)
G-WHY-3  residual uncertainty recorded
G-WHY-4  estimated VOI of further diagnosis ≤ cost (evidence_service.voi, §11.5)
G-WHY-5  falsification_evidence non-empty for the leading hypothesis
```

**Early classifier entry (v3):** immediately after the WHY gate, if `missing_evidence` is non-empty, a probe is available, or the verifier is out, the classifier runs — the task does not pay for a full HOW pass on an already-decided outcome (finding F4; §32 S5: 42 → 3 tokens; S6/S16: 16–19 → 3).

---

## 12. Stage 3 — HOW: Generate, Test, and Select Solutions

*(Divergent generation §12.1, alternative-not-sequence §12.2, candidate representation §12.3 — with `reversibility` rubric 0–3 and `action_class_estimate` — constraint screening §12.4, comparative selection §12.5 with independently estimated harm/irreversibility terms for A3+, commitment premortem §12.6, red team gate §12.7 unchanged from v2.)*

### 12.8 Exit gate (predicates, enforced in v3)

```text
G-HOW-1  ≥ 2 meaningful alternatives considered (incl. rejected candidates)
G-HOW-2  hard constraints applied by SafetyKernel
G-HOW-3  preferred option survived sensitivity and red-team checks
G-HOW-4  fallback or abort condition exists
G-HOW-5  decision record explains the choice
```

`check_exit_gate("HOW")` has a call site in §24.4 after selection (v2 listed the gate but no call site — finding F4/C5; §32 S13 exercises the red-team half of G-HOW-3).

---

## 13. Stage 4 — DO: Plan and Execute

*(Hierarchical planning §13.1, action classes §13.2 with attestation, transactional execution §13.3, ReAct/OODA micro-loop §13.4, monitoring §13.5, stakeholder communication §13.6 unchanged from v2.)*

### 13.7 Exit gate (enforced in v3)

Execution ends when **any** predicate holds:

```text
G-DO-1  success metrics met (postconditions verified)
G-DO-2  plan stop_conditions triggered          ← consumed in §24.4 (v3)
G-DO-3  plan proven infeasible
G-DO-4  risk exceeds delegated authority
G-DO-5  human escalation required
```

`plan.stop_conditions` and `plan.escalation_conditions` are read at each DO pass (v2 produced them and never consumed them — finding F3/C5; §32 S19: the plan's own stop condition ends the loop at iteration 1, 61 → 15 tokens).

---

## 14. Stage 5 — REVIEW: Reflect, Learn, and Evolve

*(AAR §14.1 with in-loop review, single-loop §14.2, double-loop §14.3, memory consolidation §14.4, Kaizen §14.5 unchanged from v2.)*

**Calibration consumption (v3):** REVIEW calibration outputs are consumed by the CompetenceModel at every terminal (in-loop and epilogue) — the v2 dangling loop is closed: `competence.update(state, calibration)` writes `state.competence`, which `route()` reads (§19.3, §32 S22).

---

## 15. Continuous VERIFY Layer

### 15.1 Verification registry

| Claim type | Preferred verifiers (ordered) |
|---|---|
| Factual | Primary sources, retrieval, provenance checks |
| Numerical | Calculator, executable code, independent recomputation |
| Logical | Formal proof, solver, counterexample search |
| Software | Tests, static analysis, type checking, sandbox execution |
| Causal | Experiment, intervention, counterfactual analysis |
| Physical | Sensors, measurement, simulation plus real observation |
| Policy | External policy engine and authorized human |
| Security | Adversarial tests, isolation, permission audit |
| Social | Stakeholder confirmation and behavioral observation |
| Creative | Requirement testing, user evaluation, comparative critique |

**Reliability (v3):** each (claim-type, verifier-kind) pair carries a reliability estimate. **Deterministic tools (calculator, solver, code execution) have reliability 1.0 by construction**; model-based verifiers seed at 0.5 and are updated from evaluation history (rolling accuracy), solving the v2 cold-start deadlock where no external-action task could ever clear a 0.8+ bar (finding F3). **Selection rule:** first available verifier in the ordered list with reliability ≥ the class bar.

### 15.2 Proposer-verifier separation and the no-verifier ladder

- The proposer is not the only verifier.
- The verifier receives objective criteria and different evidence/tools where possible.
- Verification failure produces a specific counterexample or test result.
- If no reliable verifier exists, autonomy is reduced.

**No-verifier ladder (v3, all three levels reachable in §24.4):**

```text
L1  verifier unavailable, stakes ≤ 2:  degrade to reduced effort (E ≤ 1),
    inflate uncertainty labels; status SOLVED only for A0/A1-style claims;
    otherwise NEEDS_EVIDENCE          (§32 S25)
L2  verifier unavailable, stakes ≥ 3:  do not declare SOLVED; status = ESCALATED
                                       (§32 S5)
L3  verifier unavailable, action class ≥ A3:  no external action; status =
    ESCALATED with required_human_actions populated
```

**Reliability-blocked (v3):** when a verifier exists but its reliability is below the class bar and no alternative verifier can clear it, the classifier returns `ESCALATED` (§15.4, §32 S4 — the v2 harness declared SOLVED at seed 0.5; v3 refuses).

### 15.3 Verification packet

```yaml
verification:
  artifact_id:
  criteria:
  checks_performed:
  passed:
  failed:
  unresolved:
  evidence:
  counterexamples:
  verifier_identity:      # set by VerifierRegistry, not by the orchestrator
  verifier_reliability:
  class_bar:              # v3: the bar this report was judged against
  success:                # v3: derived (checks ∧ external ∧ reliability ≥ bar)
  ambiguous:              # v3
  confidence:
  recommendation:
```

### 15.4 SOLVED threshold (enforced in v3)

`verify_outcome.success = (all required checks passed) ∧ (verifier_identity ≠ SELF) ∧ (verifier_reliability ≥ class_bar)`. The threshold table is complete for all (action class × stakes) cells and is a consumer of the attested action class:

| Action class / stakes | Required checks | Min reliability |
|---|---|---|
| A0–A1 / stakes 1–2 | 1 pass | 0.5 |
| A0–A1 / stakes 3 | all required | 0.8 |
| A0–A1 / stakes 4 | all required | 0.9 |
| A0–A1 / stakes 5 | all + second verifier | 0.95 |
| A2 / stakes 1–3 | all required | 0.8 |
| A2 / stakes 4–5 | all required | 0.9 |
| A3 / stakes 1–5 | all required | 0.9 |
| A4 / stakes 1–3 | all required | 0.9 |
| A4 / stakes 4–5 | all + independent verifier | 0.95 |
| A5 / any | all + independent second verifier | 0.95 |

The final output always includes the proof-carrying decision packet (common epilogue of §24.4 — every terminal path, including `UNSAFE`/`ESCALATED` and PENDING timeouts, produces it):

```yaml
result:
  conclusion:
  status:
  assumptions:
  evidence:                 # with per-item provenance refs (v3)
  alternatives_considered:
  verification:             # checks, verifier_identity, reliability, class_bar
  uncertainty:
  limitations:
  risks:                    # deduplicated (v3 — premortem entries collapse)
  dissent:                  # minority reports (v3 — from the ledger, §17.3)
  unresolved_disagreements: # (v3)
  required_human_actions:
```

Field sources are defined by the `build_decision_packet` contract (§24.3).

### 15.5 Bounded approximation (v3 producer)

`APPROXIMATED` requires a real error bound: when exact verification fails but an approximation with a computable bound exists, `select` records `error_bound` and sets `state.approximation_available`, which the classifier consumes (§3.3 producer table, §32 S17). Without a bound, the task may not claim `APPROXIMATED`.

### 15.6 Delta-based verification (implemented in v3)

Verification history is keyed by artifact content hash. On iteration, only artifacts whose hash is absent from history are re-verified; unchanged artifacts reuse prior reports. Combined with the deduplicated risk register and premortem-on-new-candidates, this removes the v2 verification cascade (finding F3/B12; §32 S2: candidates verified once, 61 → 39 tokens; premortem entries collapse to one). Reframe paths force re-verification (frame change → new alternatives → new hashes), which is correct.

---

## 16. Reasoning Method Composer

*(Method selection table §16.1 unchanged from v2.)*

### 16.2 SearchController

```yaml
search_controller:
  contract:
    explore(belief_state, budget) -> exploration_results
    exploration_depth:        # from budget envelope
    ev_of_exploration_gate:   # expand only while EV(exploration) > cost
    search_budget:            # nodes, calls, tokens
```

Invoked from `generate_candidates` when `route.requires_search` (effort ≥ 3 and search needed). The interface signature is aligned with the algorithm call site (v2 had an argument drift — finding F9).

---

## 17. Multi-Agent Collective

### 17.1 Roles

*(Role table unchanged from v2: Coordinator (sole writer), Frame Critic, Diagnostician, Researcher, Explorer, Planner, Formal Verifier, Red Team, Safety Agent, Implementer, Synthesizer, Reviewer. MVP: prompt-variants over the single model with fresh contexts; heterogeneity is a Phase-3 upgrade.)*

### 17.2 Council protocol (contract, v3)

```text
1. Decompose the task where useful.
2. Fresh context window per agent.
3. Private write slots; answers generated before any peer communication.
4. Normalize into the claim ledger (deterministic extractor over agent_answer;
   normalization CANNOT delete — lossless projection).
5. Run objective verifiers.
6. Aggregate verified results (evidence-weighted, §17.3).
7. Debate only unresolved contradictions (1 round: exchange claims + evidence
   refs once; verifier adjudicates; dissent → minority ledger).
8. Run a Red Team challenge.
9. Preserve dissent — minority ledger written BEFORE aggregation.
10. Synthesize — output schema mandates a dissent section fed from the ledger.
11. Run a final independent gate (= verify_outcome with the class bar).
```

**Algorithm branch (v3):** `generate` invokes `council_orchestrator.run_council(state)` when `route.use_council` (§17.4 predicates consumed at §24.4), and returns `{candidate_set, minority_reports[], unresolved_disagreements[]}` which are written into `task_state` before selection (v2's minority ledger had no producer — finding F8/B7; §32 S23). `agent_answer` schema per v2 §17.2.

### 17.3 Aggregation rules

*(Unchanged: objective tests outrank votes; weights from verified performance with uniform default; consensus without new evidence is not progress; minority reports recoverable; final report includes unresolved disagreements.)*

### 17.4 When not to use a council (predicates, enforced in v3)

```text
C-1  deterministic calculator or solver available
C-2  one high-quality source answers the question
C-3  agents would share the same blind spot (heterogeneity check fails)
C-4  coordination-cost estimate > expected benefit
C-5  time pressure requires immediate safe stabilization
C-6  the action cannot be safely authorized regardless of consensus
```

Evaluated by `meta_router.should_use_council`; the branch is explicit in §24.4. Council size is per-round capped by `agents_max`; total churn is bounded by the call budget (finding F1/B9; §32 S23 positive case, S7 negative case).

---

## 18. Memory and Knowledge Architecture

*(Memory classes §18.1, memory record schema §18.2 with the trust-margin contradiction rule and consolidation trigger, retrieval score §18.3, memory security §18.4, forgetting §18.5, provenance anchoring §18.6 — all per v2 — with the v3 changes below.)*

### 18.2a Authority tokens (v3)

`authority_token` is **minted by the SafetyKernel** (`issue_authority_token(scope)`), recorded in the audit log, and checked by MemoryManager against the issued set. A writer-stamped string such as `authorized_expert` in lesson content is **not authority** — it is data (finding R1/B14; §32 S8: injected procedural content is quarantined). Trust labels derive from verifier reliability, never from the writer; the trust-margin rule therefore compares verifier-derived trust, not self-declared values.

### 18.2b Retrieval and consolidation call sites (v3)

`memory_manager.retrieve(query, state) -> memory_hits` has an interface entry (§24.3) and a call site inside `diagnose` (evidence retrieval); the consolidation trigger (≥ 3 near-duplicates) has a call site in the REVIEW engine (v2 defined both and never invoked them — finding F8).

---

## 19. World Model and Self-Model

*(World model §19.1 unchanged; active experimentation §19.2 — probe selection inside `diagnose`, setting `state.probe_available` — unchanged.)*

### 19.3 Self-model and CompetenceModel (closed loop, v3)

The self-model must be based on evaluation history rather than unrestricted introspection. In v3 the loop is closed end-to-end and validated across episodes (§32 S22):

```text
REVIEW calibration (in-loop and epilogue) / EvaluationPlane batch results
→ CompetenceModel.update(state, calibration)     — writes state.competence
→ MetaRouter.route(state)                        — capability-match input
→ route quality metrics → EvaluationPlane        — closes the loop (§23.7)
```

`update` blends prior competence with measured accuracy; routing reads competence to adjust effort within bounds. Calibration carries provenance (EvaluationPlane outcome refs) — self-reported accuracy is not accepted as evaluation history (finding R12); in the MVP the frozen 5-test suite (§25.2) is the evaluation source.

---

## 20. Tool Broker and Execution Security

*(Authority separation §20.1, least privilege §20.2, controls table and per-class transaction semantics §20.3, independent risk attestation §20.4 — unchanged from v2 — plus v3 changes below.)*

### 20.3a Pending authorization subset (v3)

`execute_authorized_subset(state, authorization)` is a defined interface (§24.3) whose membership rule is a **static allowlist** — permission-free, idempotent, A2-class actions by kernel table lookup — not a self-selected "reversible subset" (finding R6). The subset executes **exactly once** (guarded by `state.subset_executed`), and the PENDING wait is bounded: `pending_timeout` (default 8 iterations) degrades the task to `ESCALATED` with a partial-result packet (§21.4; §32 S20: subset executed once, then ESCALATED — the v2 branch re-executed the subset on every loop pass).

### 20.5 Interrupt, checkpoint, and resume (v3)

- `safety_kernel.interrupt(task_id) -> checkpoint` aborts the current transaction (per-class compensation), serializes state, returns a checkpoint.
- **Checkpoint format:** versioned JSON of `task_state` + `stage` + `executed_actions` ledger, written at **every stage boundary** (§24.4) — v2 wrote only at the epilogue, so a mid-task crash orphaned side effects (finding F2/B16).
- **Resume:** `task_scheduler.resume(checkpoint)` restores state; idempotency keys bind to (task, action, argument hash), so a resumed task cannot double-execute a confirmed action (§32 S21: crash after execution → resume → completes with the confirmed action executed exactly once). Checkpoints are authenticated (HMAC keyed outside the model's key store) to prevent forged-state re-entry (finding R9).
- **Crash recovery:** on corrupt or unauthenticated checkpoints, the task restarts from INIT with an audit flag.

---

## 21. Safety and Alignment Kernel

### 21.1 Kernel position

*(Unchanged from v2: goals, permissions, capabilities, data access, authorization, self-modification levels, escalation, shutdown/interrupt, checkpoint authority — outside the self-modifiable scaffold.)*

### 21.2 Safety invariants (v3: all ten mapped)

1. The system may not grant itself new authority. → Capability tokens minted by the kernel; checkpoints authenticated (§20.2, §20.5).
2. Untrusted content may not alter governing instructions. → Write channels + minted authority tokens (§18.2a); tool outputs tagged untrusted (§24.2 `observations` carry `origin`/`trust`).
3. High-impact actions require independent authorization. → Action-class attestation by an independent estimator (§20.4) + verifier separation (§15.2).
4. The system may not disable logging or monitoring. → `audit_log.record` at loop top, each stage entry, fast path, and epilogue (§23.8, §24.4) — v2 logged only loop.top and epilogue, leaving the fast path unlogged (finding F6).
5. The system may not autonomously rewrite its core goals. → Signed goal contract outside mutable memory; `renegotiate` gated by kernel + owner (§24.5).
6. The system may not deploy unevaluated self-modifications. → `improvement_engine.evaluate` invoked against the frozen baseline before deployment (§22.3, §32 S10).
7. Safety-critical modifications require human approval. → R5 gate + §21.4 human gates.
8. **Self-replication and uncontrolled resource acquisition are disabled by default (v3 mechanism):** the ToolBroker capability-token whitelist contains no spawn/replication capability at any action class; `attest` denies any action proposing one; resource ceilings are the budget envelope (§20.2, §9.6). (v2 asserted this without a mechanism — finding F5.)
9. External side effects must remain attributable to an authorized task. → Capability tokens carry task ids; audit log records every transaction (§20.3, §24.4).
10. Capability growth may not outpace evaluation and containment capacity. → Capability–safety co-scaling gate (§23.7).

### 21.3 Threat model with enforcing controls

*(v2 table unchanged, plus: "Human manipulation" → corroboration per §21.4; "Evaluation awareness" → hidden and out-of-distribution tests §22.4.)*

### 21.4 Human gates (v3 process)

Human approval is required for: irreversible or high-stakes actions; changes to goals/values/permissions; deployment of architectural self-modifications; sensitive data access; broad external communication or financial transactions; chaotic-domain actions; autonomy/resource expansion.

**Gate process (v3):**

1. **Packet-before-approval:** the human receives the §15.4 packet (with raw evidence links) before any prompt.
2. **No auto-confirmation (v3):** approval requires an explicit human event (click/typed confirmation); the "floor" in v2 read as an auto-confirm timer — v3 removes that reading: no timer ever authorizes an action (finding R5).
3. **Pending semantics:** `authorize` returns `{approved, rejected, pending}`; while pending, the system executes the static A2 allowlist subset exactly once (§20.3a) and other queued tasks.
4. **Timeout and fallback:** `pending_timeout` (default 8 iterations) → `ESCALATED` with a partial-result packet and a named fallback authority; deferral counters prevent ping-pong.
5. **Corroboration:** authority-expanding or sensitive instructions require a **second human or an external recorder** — the system's own audit log is not a second party (finding R5).

---

## 22. Self-Evolution Engine

*(Improvement levels §22.1, admission control §22.2, acceptance pipeline §22.3, evaluation requirements + stable baseline §22.4, Kaizen step-size §22.5, evaluation-plane immutability §22.6, cadence differential §22.7, open-ended improvement §22.8 — per v2 — with the v3 changes below.)*

### 22.2a Admission control (v3 hardening)

- `dedup_hash` is computed by the engine from canonical change content, not by the proposer (a nonce in the change text no longer defeats dedup — finding R10).
- The rate cap is global per epoch (not per target component) so flooding N targets cannot flood the shared evaluation pipeline; `change_size` is verified against a diff metric rather than self-declared.

### 22.3a Pipeline invocation (v3)

`improvement_engine.evaluate(proposal)` is invoked by the §24.4 epilogue for every proposal that passes admission control, **provided a frozen baseline exists** (§22.4); without a baseline, the proposal is held, not deployed (invariant 6 enforced; finding F5/B13 — §32 S10 demonstrates evaluate running against the frozen baseline).

---

## 23. Evaluation Framework

*(Capability §23.1, reliability §23.2, learning §23.3, safety §23.4, efficiency §23.5 dimensions per v2; general intelligence profile §23.6 with producer contract; routing-quality + co-scaling §23.7; telemetry §23.8 — with the v3 additions below.)*

### 23.6a Metrics (v3)

Each profile dimension carries a metric definition and threshold; `unresolved_limits` lists dimensions with no valid measurement yet. The MVP 5-test suite (§25.2 step 8) is enumerated: (1) fast-path routing on a Clear/low-stakes task; (2) WHAT-gate block on missing success metrics; (3) external-only SOLVED (self-only → not SOLVED); (4) decision packet on a denial path; (5) budget termination on a looping task. Each maps to harness scenarios S1, S15, S5/S4, S11, S24.

### 23.8 Telemetry (v3)

`audit_log.record(stage, telemetry.stats())` runs at loop top, each stage entry (WHAT/WHY/HOW/DO), the fast path, and the epilogue — the v2 gap that left fast-path tasks unlogged is closed (finding F6). `stats() = (tokens, calls, latency, agents)`; `latency` = wall-clock per stage from audit timestamps. Cognitive vs bookkeeping calls are priced separately (§32 pricing note): bookkeeping (budget, monitors, audit, gates) costs zero cognitive tokens and is counted as overhead.

---

## 24. Reference Implementation Specification

### 24.1 Core components (canonical, v3)

| Component | Function | Interface (§24.3) |
|---|---|---|
| `GoalManager` | Authorized objectives, priorities, renegotiation | `renegotiate` |
| `MetaRouter` | Route, effort, flags, budget envelope, competence-aware | `route` |
| `Workspace` | Structured active task state | internal (§24.2) |
| `MethodComposer` | Method selection (inside `route`) | `compose` |
| `FrameCritic` | WHAT-gate predicates | `check_exit_gate` |
| `Diagnostician` | Hypotheses, falsification, probes, missing-evidence | `diagnose` |
| `Premortem` | Commitment premortem (deduplicated risk entries) | `premortem` |
| `RedTeam` | Adversarial attack on the selected candidate | `attack` |
| `Explorer` | Candidate generation; rejection ledger | `generate`, `reject` |
| `SearchController` | Bounded exploration with EV gate (E3+) | `explore` |
| `Planner` | Hierarchical plans with stop/escalation conditions | `build` |
| `EvidenceService` | Retrieval, grading, VOI (inside `diagnose`) | `voi`, `retrieve` |
| `WorldModel` | Transition prediction (inside `diagnose`) | `predict` |
| `CouncilOrchestrator` | Independent agents, debate, minority ledger (branch in §24.4) | `run_council` |
| `VerifierRegistry` | Reliability-by-kind, class bars, delta caching | `verify_candidate`, `verify_outcome` |
| `MemoryManager` | Channels, contradiction rule, quarantine, retrieval | `commit`, `retrieve` |
| `ToolBroker` | Schemas, permissions, transactions, no-replication whitelist | `execute_transactional` |
| `SafetyKernel` | Policy, gates, attestation, interrupt, token minting | `authorize`, `attest`, `interrupt`, `issue_authority_token` |
| `ExecutionMonitor` | Drift, anomalies, postcondition checks | `check` |
| `LoopMonitor` | Novelty, repetition, EVOC, budgets | `should_continue` |
| `BudgetController` | Envelope consumption; per-iteration check | `check`, `consume` |
| `CompetenceModel` | Evaluation-based capability estimates (writes `state.competence`) | `update` |
| `ReviewEngine` | AAR, lessons, calibration | `review` |
| `ImprovementEngine` | Admission control, evaluation, deployment | `queue`, `evaluate` |
| `EvaluationPlane` | Frozen suites, profile production | `run_suite`, `produce_profile` |
| `AuditLog` | Immutable telemetry records | `record` |
| `TaskScheduler` | Identity, priority, checkpoint/resume | `checkpoint`, `resume` |

### 24.2 Shared task state (v3 schema)

```yaml
task_state:
  task_id:
  goal_contract:
  route:
    context_class:
    effort_level:
    reasoning_modules:
    use_council:
    requires_diagnosis:
    requires_generation:
    requires_review:
    requires_search:
    verification_depth:
    budget_envelope:
  competence:                 # written by CompetenceModel, read by route
  frame:
    success_metrics:
    unresolved_ambiguities:
  world_state:
  hypotheses:                 # each with falsification_evidence
  evidence:                   # each with provenance refs
  missing_evidence:           # → NEEDS_EVIDENCE
  uncertainties:
  alternatives:               # reversibility, action_class_estimate
  decision:                   # {id, strategy, error_bound?, requires_external_action}
  plan:                       # stop_conditions, escalation_conditions
  permissions:
  risks:                      # deduplicated (premortem, red team, monitor)
  actions:
  observations:               # each with origin + trust tags (§20.1)
  verification:               # §15.3 incl. success, ambiguous, class_bar
  verification_history:       # artifact_hash → report (§15.6 delta cache)
  minority_reports:           # append-only, pre-aggregation (§17.3)
  unresolved_disagreements:
  result:
  review:                     # {lessons, calibration{accuracy, domain}, proposals}
  memory_updates:
  improvement_proposals:
  audit_refs:
  stage:                      # checkpoint pointer
  iteration:
  budget:                     # tokens_used, calls_used, iterations_used, agents_used
  executed_actions:           # idempotency ledger (§20.3)
  subset_executed:            # pending-subset guard (§20.3a)
  attested_class:             # kernel-attested action class; feeds the §15.4 bar
  reliability_blocked:        # verifier below bar, no alternative (§15.4)
  probe_available:            # producer: diagnose (§19.2)
  approximation_available:    # producer: select error_bound (§15.5)
  infeasible:                 # producer: constraint screen (§12.4)
  resumed:                    # resume path marker (§20.5)
  checkpoint:                 # resume payload (HMAC-authenticated)
```

### 24.3 Core interface (canonical, v3)

Every call site in §24.4 uses these names verbatim; the harness implements this interface. **World binding:** `solve(request, context, checkpoint, world)` binds all components and `telemetry` explicitly (the harness `make_world()` pattern); `baseline_frozen` is an environment flag controlled by the EvaluationPlane's immutability (§22.6), not a component. `audit_log.record(stage, stats)` takes `stats := telemetry.stats() -> (tokens, calls, latency, agents)` — the single canonical call form. Pseudocode-local helpers defined inline in §24.4 (not components): `initialize_task_state`, `should_reframe`, `verifier_unavailable`, `constraints_violated`, `content_hash`, `tag_untrusted`, `plan_stop_conditions_met`.

```text
route(state) -> cognitive_route
    # {context_class, effort_level, reasoning_modules, use_council,
    #  requires_diagnosis, requires_generation, requires_review,
    #  requires_search, verification_depth, budget_envelope}

direct_answer(state) -> decision                 # E0/E1 fast path

frame(state) -> problem_frame
check_exit_gate(stage, state) -> gate_result     # {passed, failing_predicates[]}
diagnose(state) -> None                          # sets hypotheses, missing_evidence,
                                                 # probe_available, falsification
evidence_service.voi(uncertainties, actions) -> voi_estimate
memory_manager.retrieve(query, state) -> memory_hits[]
world_model.predict(state) -> predicted_state

generate(state) -> None                          # explorer or council branch
council_orchestrator.run_council(state) -> {candidate_set, minority_reports[], unresolved_disagreements[]}
explorer.reject(candidate_id) -> None            # feeds regeneration (§12.7)
search_controller.explore(belief_state, budget) -> exploration_results

premortem(state) -> None                         # appends deduplicated failure modes
red_team.attack(state) -> optional_rejection

verify_candidate(state, candidate) -> verification_report   # per artifact, cached by hash
verify_outcome(state) -> verification_report    # success := checks ∧ external ∧ rel ≥ bar;
                                                # bar keyed by state.attested_class (§15.4)
select(candidate_set, reports) -> decision       # {id, strategy, error_bound?, requires_external_action}

planner.build(state, decision) -> plan           # with stop/escalation conditions
safety_kernel.attest(state) -> attestation       # independent action-class attestation
safety_kernel.authorize(plan, permissions, risks, attestation) -> {approved|rejected|pending, status, token}
safety_kernel.issue_authority_token(scope) -> token      # §18.2a minting
safety_kernel.interrupt(task_id) -> checkpoint   # §20.5 emergency interruption
tool_broker.execute_transactional(plan, token) -> observations   # tagged untrusted (§20.1)
budget.consume(state, stage) -> None
budget.check(state, telemetry) -> optional_exhaustion_reason
execution_monitor.check(state) -> monitor_report
loop_monitor.should_continue(state, telemetry) -> {continue, reason}
execute_authorized_subset(state, authorization) -> state   # static A2 allowlist, once

review(state) -> lessons + calibration
competence_model.update(state, calibration) -> None        # writes state.competence
memory_manager.commit(state, review) -> accepted[]
improvement_engine.queue(state, review) -> queued_count
improvement_engine.evaluate(state, proposal) -> pipeline_report

evaluation_plane.run_suite(artifact, suite) -> suite_report
evaluation_plane.produce_profile(portfolio_results) -> profile
telemetry.stats() -> (tokens, calls, latency, agents)
audit_log.record(stage, stats) -> None           # canonical 2-arg form (§23.8)
task_scheduler.checkpoint(state, stage) -> None
task_scheduler.resume(checkpoint) -> task_state

build_decision_packet(state, status) -> result_packet   # §15.4 common epilogue
classify_terminal(state, telemetry) -> status           # §3.3/§3.4 decision table
```

### 24.4 Main algorithm (v3 governed loop)

```python
GATE_REENTRY_BUDGET = 3      # §10.5 (config)
REFRAME_BUDGET = 4           # §14.3 (config)
PENDING_TIMEOUT = 8          # §21.4 (config)

def solve(request, context, checkpoint=None, world=default_world):
    # world binds all components + telemetry (§24.3); baseline_frozen is the
    # EvaluationPlane immutability flag (§22.6), not a component.
    (meta_router, frame_critic, diagnostician, explorer, verifier, planner,
     kernel, tool_broker, review_engine, memory, improvements, premortem,
     red_team, loop_monitor, budget, council, competence, scheduler,
     execution_monitor, telemetry, audit_log, baseline_frozen) = world.bind()

    state = initialize_task_state(request, context)
    if checkpoint:
        state = task_scheduler.resume(checkpoint)      # HMAC-verified (§20.5)

    state.route = meta_router.route(state)             # reads state.competence
    budget.consume(state, "route")

    # --- Fast path (E0/E1): direct answer, one outcome check, one packet ---
    if state.route.effort_level <= 1:
        budget.consume(state, "fast_path")
        state.decision = direct_answer(state)
        state.verification = verifier.verify_outcome(state)   # bars apply
        state.result.status = ("SOLVED" if state.verification.success
                               else classify_terminal(state, telemetry))
        state.result.packet = build_decision_packet(state, state.result.status)
        audit_log.record("fast_path", telemetry.stats())      # invariant 4
        task_scheduler.checkpoint(state, "FAST_PATH")
        return state

    # --- Governed main loop ---
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        audit_log.record("loop_top", telemetry.stats())
        if ex := budget.check(state, telemetry):
            state.result.status = "RESOURCE_LIMITED"
            state.result.status_reason = ex
            break
        cont, reason = loop_monitor.should_continue(state, telemetry)
        if not cont:
            state.result.status = ("RESOURCE_LIMITED"
                                   if ("budget" in reason or "iterations" in reason
                                       or "expected value" in reason
                                       or "unproductive" in reason)
                                   else classify_terminal(state, telemetry))
            state.result.status_reason = reason
            break

        # WHAT: frame + gate
        if not state.frame:
            state.stage = "WHAT"
            state.frame = frame(state)
            gate = check_exit_gate("WHAT", state)
            if not gate.passed:
                state.risks.append(gate)
                state.frame = None
                if state.iteration >= GATE_REENTRY_BUDGET:
                    state.result.status = "NEEDS_EVIDENCE"
                    break
                continue
            audit_log.record("what", telemetry.stats())
            task_scheduler.checkpoint(state, "WHAT")

        # WHY: diagnose + gate; EARLY CLASSIFIER ENTRY on decided outcomes
        if state.route.requires_diagnosis and not state.hypotheses:
            state.stage = "WHY"
            diagnose(state)                    # sets hypotheses, missing_evidence,
                                               # probe_available, falsification
            gate = check_exit_gate("WHY", state)
            if not gate.passed:
                state.risks.append(gate)
                continue
            audit_log.record("why", telemetry.stats())
            task_scheduler.checkpoint(state, "WHY")
            if (state.missing_evidence or state.probe_available
                    or verifier_unavailable(state)):
                state.result.status = classify_terminal(state, telemetry)
                break                          # §32 S5/S6/S16/S25: no wasted HOW

        # HOW: council branch or explorer -> premortem -> delta-verify -> select -> gates
        if state.route.requires_generation and not state.alternatives:
            state.stage = "HOW"
            if state.route.use_council:
                (state.alternatives, state.minority_reports,
                 state.unresolved_disagreements) = council_orchestrator.run_council(state)
            else:
                generate(state)
            audit_log.record("how", telemetry.stats())
        if not state.alternatives:
            state.result.status = classify_terminal(state, telemetry)
            break
        if constraints_violated(state):        # §12.4 screen
            state.infeasible = True
        premortem(state)
        reports = []
        for alt in state.alternatives:         # §15.6 delta reuse
            h = content_hash(alt)
            reports.append(state.verification_history.get(h)
                           or (state.verification_history.setdefault(
                               h, verifier.verify_candidate(state, alt))))
        state.decision = select(state.alternatives, reports)
        if state.decision is None:
            state.result.status = classify_terminal(state, telemetry)
            break
        if state.decision.error_bound is not None:
            state.approximation_available = True     # §15.5 producer
        gate = check_exit_gate("HOW", state)         # §12.8 enforced
        if not gate.passed:
            state.risks.append(gate)
            state.result.status = classify_terminal(state, telemetry)
            break
        if rejection := red_team.attack(state):
            state.risks.append(rejection)
            explorer.reject(state.decision.id)       # feeds regeneration
            state.alternatives = []
            continue                                 # bounded by loop monitor

        # DO: plan -> attest -> authorize (incl. PENDING) -> execute -> monitor
        if state.decision.requires_external_action:
            state.stage = "DO"
            state.plan = planner.build(state, state.decision)
            attestation = safety_kernel.attest(state)
            authorization = safety_kernel.authorize(state.plan, state.permissions,
                                                    state.risks, attestation)
            if authorization.status in ("UNSAFE", "ESCALATED"):
                state.result.status = authorization.status
                safety_kernel.interrupt(state.task_id)     # §20.5 call site
                break
            if not attestation.startswith("misattested"):
                state.attested_class = attestation         # §15.4 bar consumes attestation
            if authorization.status == "PENDING":
                if not state.subset_executed:          # static A2 allowlist, once
                    state = execute_authorized_subset(state, authorization)
                    state.subset_executed = True
                if state.iteration >= PENDING_TIMEOUT:
                    state.result.status = "ESCALATED"  # partial packet via epilogue
                    state.result.pending_timeout = True
                    break
                continue
            observations = tool_broker.execute_transactional(state.plan,
                                                             authorization.token)
            state.observations.extend(tag_untrusted(observations))   # §20.1
            audit_log.record("do", telemetry.stats())
            task_scheduler.checkpoint(state, "DO")
            if plan_stop_conditions_met(state.plan, state):   # §13.7 G-DO-2
                state.result.status = classify_terminal(state, telemetry)
                break
            monitor = execution_monitor.check(state)
            state.risks.extend(monitor.findings)

        state.verification = verifier.verify_outcome(state)
        if state.verification.success:
            state.result.status = "SOLVED"
            break

        # REVIEW-in-loop (progress-gated) + competence update
        state.review = review_engine.review(state)
        competence_model.update(state, state.review.calibration)   # §19.3
        if should_reframe(state.review, state):
            if state.iteration < REFRAME_BUDGET:
                state.frame = None
                state.hypotheses = []
                state.alternatives = []
                continue
            # reframe budget exhausted: settle on the best frame and continue
            # (double-loop convergence, §14.3; §32 S3)
            state.frame = settle_best_of(state.frame, state.review)
            state.hypotheses = []
            state.alternatives = []
            continue
        if (state.verification.ambiguous or state.missing_evidence
                or state.reliability_blocked or state.probe_available
                or state.approximation_available or state.infeasible):
            state.result.status = classify_terminal(state, telemetry)  # P11 early stop
            break

    # --- Common epilogue: REVIEW + competence + memory + improvement + packet + audit ---
    if not state.review:
        state.review = review_engine.review(state)
    competence_model.update(state, state.review.calibration)     # §19.3 closes every episode
    safety_kernel.issue_authority_token("procedural")            # §18.2a minting call site
    memory_manager.commit(state, state.review)                   # channels + contradiction rule
    if state.route.requires_review and state.review.lessons:
        queued = improvement_engine.queue(state, state.review)   # admission control
        if queued and baseline_frozen:                           # §22.3 invocation
            for p in state.improvement_proposals:
                improvement_engine.evaluate(state, p)
    state.result.packet = build_decision_packet(state, state.result.status)  # every path
    audit_log.record("epilogue", telemetry.stats())
    task_scheduler.checkpoint(state, "EPILOGUE")
    return state
```

Guarantees (each demonstrated by the harness, §32):

1. **Termination:** every path ends at a status assignment; loop exits bounded by LoopMonitor (iteration/token/call budgets, novelty plateau, repetition, EVOC).
2. **State completeness:** every status produced by a named producer or explicit assignment; all eight states reachable (S1–S26).
3. **Packet completeness:** `build_decision_packet` runs on every terminal path, including UNSAFE/ESCALATED denials and PENDING timeouts.
4. **Verification independence:** SOLVED requires external identity AND reliability ≥ class bar; reliability-blocked tasks escalate (S4).
5. **Cost boundedness:** budget envelope metered at route/fast-path/loop-top with the call ceiling enforced per iteration; delta verification prevents re-verification cascades (S2).
6. **Gate enforcement:** WHAT/WHY/HOW gates checked; plan stop/escalation conditions consumed at DO (S15, S13, S19).
7. **Review in loop:** AAR runs on non-terminal exits and feeds reframe decisions; competence updates close the §19.3 loop (S3, S22).
8. **Resume:** checkpoints at every stage boundary; crash/resume without double-execution (S21).

### 24.5 Session and scheduler layer

- TaskScheduler owns identity, priority arbitration (precedence: stakes desc, then arrival), checkpoint/resume (§20.5).
- Prospective memory entries are consumed by the scheduler.
- `GoalManager.renegotiate(user_request, old_contract) -> new_contract` is gated by SafetyKernel + decision-owner confirmation; the signed goal contract lives outside mutable memory (invariant 5).
- Cross-task conflict detection runs in the ExecutionMonitor: a later goal contradicting an active contract triggers renegotiation (stakes × arrival precedence), not drift.
- LearningScheduler: consolidation and R2-change batching are triggered by the scheduler per the §22.7 epoch cadence (queue-consumer contract with trigger conditions).

### 24.6 Component–call-site map (v3)

| Component | Call sites in §24.4 |
|---|---|
| MetaRouter | step 1 (route) |
| BudgetController | route, fast path, loop top (metering points of §24.4) |
| LoopMonitor | loop top |
| FrameCritic / Diagnostician | `check_exit_gate` (WHAT, WHY, HOW) |
| EvidenceService / WorldModel | inside `diagnose` (VOI, predict) |
| SearchController | inside `generate` for E3+ (`requires_search`) |
| CouncilOrchestrator | `generate` branch when `use_council` |
| Premortem / RedTeam | HOW stage |
| VerifierRegistry | `verify_candidate` (delta-cached) + `verify_outcome` |
| Planner / SafetyKernel / ToolBroker | DO stage |
| ExecutionMonitor | after each transaction |
| ReviewEngine / CompetenceModel | REVIEW-in-loop + epilogue |
| MemoryManager / ImprovementEngine | epilogue (retrieve inside `diagnose`) |
| AuditLog | loop top, each stage, fast path, epilogue |
| TaskScheduler | resume + checkpoints at every stage boundary |

---

## 25. Minimal Viable Thinking Agent

### 25.1 MVP components

- One capable foundation model.
- One independent verifier model or deterministic verifier.
- A MetaRouter with route flags and a budget envelope.
- Structured WHAT–WHY–HOW–DO–REVIEW templates with boolean gate predicates.
- Web, code, calculator, and document tools via a sandboxed ToolBroker (timeouts/retries/idempotency, no-replication whitelist).
- Working, episodic, semantic, and procedural memory with the §18.2 record schema, minted authority tokens, and contradiction rule.
- Four default roles (prompt-variants over the single model, fresh contexts): Coordinator, Researcher, Verifier, Red Team.
- LoopMonitor + BudgetController.
- AAR and change-proposal generation with dedup.
- An immutable audit log with per-stage telemetry.
- Human approval for consequential actions with packet-before-approval and no auto-confirmation (§21.4).
- TaskScheduler for checkpoint/resume (single-process file persistence in the MVP).

### 25.2 MVP development order (v3)

1. Implement structured state and decision records (§24.2).
2. Add evidence retrieval and provenance.
3. Add criterion-specific verification with the enforced threshold table (§15.4).
4. Add transactional tool use with failure semantics (§20.3) and checkpoint/resume (§20.5).
5. Add persistent memory with channels, contradiction rule, and minted tokens (§18).
6. Add independent multi-agent generation (fresh contexts, answer schema).
7. Add targeted debate (one round, minority ledger).
8. Add a minimal frozen EvaluationPlane: `run_suite` + the 5-test MVP suite (§23.6a) — enumerated, not deferred.
9. Add safety and prompt-injection evaluations (against the frozen suite).
10. Add procedural-memory updates gated on the baseline.
11. Add sandboxed architecture search as an explicit Phase-5 stub.

---

## 26. Roadmap Toward AGI and ASI Research

*(Phases 0–7 per v2: Phase 0 structured assistant; Phase 1 grounded agent; Phase 2 persistent generalist (EvaluationPlane batch feedback, LearningScheduler); Phase 3 collective problem solver (model heterogeneity); Phase 4 continual learner; Phase 5 governed self-improving system (open-ended search); Phase 6 AGI candidate evidence list; Phase 7 ASI research boundary with oversight constraints.)*

---

## 27. Common Failure Modes

| Failure | Mitigation (v3 mechanism) |
|---|---|
| Wrong problem frame | Multiple frames, frame critic, WHAT gate |
| HOW before WHY | Stage gates (G-WHY predicates) |
| Confident hallucination | Evidence/tool verification; SOLVED requires external identity + class bar |
| Excessive diagnosis | VOI stop + EVOC check; early classifier after WHY |
| First-answer anchoring | Independent candidate generation (council branch when eligible) |
| Self-critique echo chamber | External verifiers; identity set by registry, not orchestrator |
| Debate conformity | Fresh contexts, private answers, minority ledger in the packet |
| Majority error | Verification-weighted aggregation; dissent mandatory in synthesis |
| Planner-executor drift | Preconditions, postconditions, checkpoints, monitor |
| Tool hallucination | Retrieved schemas, argument validation |
| Prompt injection | Authority/data separation; trust tags on observations |
| Memory poisoning | Minted authority tokens; verifier-derived trust; quarantine |
| Goal drift | Signed goal contract; gated renegotiation |
| Reward hacking | Hidden/adversarial tests; immutable evaluation plane |
| Benchmark overfitting | Portfolio + OOD tests; frozen baseline |
| Unsafe self-modification | §22.3 `evaluate` invoked before deployment |
| Infinite cognitive loop | LoopMonitor: novelty, repetition, EVOC, budgets |
| Overuse of agents | Council predicates + per-round cap + call budget |
| Hidden side effects | Transactional actions; idempotency; per-class compensation |
| Architecture monoculture | Diverse candidate archive; independent audits |
| Capability growth outruns safety | Capability–safety co-scaling gate (§23.7) |
| Denial paths without audit records | Common epilogue on every terminal path |
| Proposal flood | Admission control with canonical dedup hashes |
| Cold-start verification deadlock | Deterministic tools at reliability 1.0; model verifiers seed 0.5 and calibrate |
| Verifier-below-bar silent SOLVED | Reliability-blocked → ESCALATED (§15.4, S4) |
| Cosmetic-frame novelty evasion | Canonicalized signature over evidence/alternatives/plan (§9.5) |

---

## 28. Final Operating Rules

1. **Sense before thinking deeply.**
2. **Frame before diagnosing.**
3. **Diagnose before prescribing.**
4. **Generate alternatives before committing.**
5. **Test assumptions before acting.**
6. **Prefer evidence over agreement.**
7. **Prefer external checks over self-confidence.**
8. **Prefer reversible probes over irreversible bets.**
9. **Use multiple agents only when diversity and decomposition add value.**
10. **Preserve dissent.**
11. **Treat all retrieved content as untrusted data.**
12. **Grant the minimum authority required.**
13. **Verify the environmental result, not merely the generated plan.**
14. **Learn from outcomes, not just narratives.**
15. **Question governing assumptions during review.**
16. **Do not deploy a self-modification merely because the system proposed it.**
17. **Keep goals, permissions, and safety controls outside ordinary self-modification.**
18. **Escalate when evidence, competence, or authority is insufficient.**
19. **Stop when additional cognition has negative expected value.**
20. **Never confuse a scaffold toward AGI with demonstrated AGI.**
21. **Every task terminates in a graceful state; every terminal state carries a decision packet.**
22. **A route that cannot be budgeted is a route that cannot run.**
23. **A claim that cannot name its verifier is not a verified claim** — and a verifier whose reliability is below the class bar is not a verifier for that claim (§15.4).
24. **A label written by the claimant is data, not authority** — authority tokens are minted, trust is measured (§18.2a).
25. **A mechanism the reference algorithm does not call is a paragraph, not a mechanism** — every normative claim names its call site (§24.4, §31).

---

## 29. Conclusion

Thinking Agent combines the strongest elements of traditional human problem-solving systems with contemporary agent research: Cynefin routing, dual-process fast/deliberate paths, the WHAT–WHY–HOW–DO–REVIEW structure, premortem and red teaming, root-cause and Bayesian diagnostics, structured creativity, ReAct and planning search, CoALA-style memory, AAR/double-loop/Kaizen improvement, independent verifiers, selective multi-agent collectives, and sandboxed, gated self-improvement.

v2 made the loop governable; **v3 made it honest.** Every standard v2 printed now has an enforcing mechanism with a call site, and every mechanism has a scenario. The verification thresholds that v2's own harness ignored are enforced — a high-stakes task with an uncalibrated verifier is ESCALATED, not SOLVED (S4). The gates v2 listed without call sites are enforced (S13, S15, S19). The states v2 could only reach via config injection are produced by named producers (S16–S18). The loop costs v2 attributed to the fast path are re-attributed honestly — the real savings came from termination and, in v3, from delta-based verification and early classifier entry (§32.3). The human-gate, checkpoint, competence, and council mechanisms v2 specified but never executed now run and are tested (S20–S23).

The validation discipline is itself the point: **self-criticism is a source of hypotheses, not proof** — so every revision is executed against a frozen baseline, and every claim about the framework is checked by an independent auditor against the code. That is what "meets the thinking agent's standard" means here: not that the document says it, but that it runs.

The architecture’s most important principle is not "think longer" or "use more agents." It is:

> **Apply the right cognitive process, obtain the right evidence, verify through the right mechanism, act with the right authority, and learn without weakening human control.**

That combination provides a practical architecture for increasingly general AI systems while acknowledging that AGI, safe recursive self-improvement, and ASI alignment remain open research problems.

---

## 30. Primary Research References

1. Sumers et al., **Cognitive Architectures for Language Agents**, arXiv:2309.02427. ([arxiv.org](https://arxiv.org/abs/2309.02427?utm_source=openai))
2. Kotseruba and Tsotsos, **A Review of 40 Years of Cognitive Architecture Research**, arXiv:1610.08602. ([arxiv.org](https://arxiv.org/abs/1610.08602?utm_source=openai))
3. Yao et al., **ReAct**, arXiv:2210.03629. ([arxiv.org](https://arxiv.org/abs/2210.03629?utm_source=openai))
4. Yao et al., **Tree of Thoughts**, arXiv:2305.10601; Hao et al., **RAP**, arXiv:2305.14992; Zhou et al., **LATS**, arXiv:2310.04406. ([arxiv.org](https://arxiv.org/abs/2305.10601?utm_source=openai))
5. Prasad et al., **ADaPT**, arXiv:2311.05772; Zhou et al., **Self-Discover**, arXiv:2402.03620. ([arxiv.org](https://arxiv.org/abs/2311.05772?utm_source=openai))
6. Shinn et al., **Reflexion**, arXiv:2303.11366; Gou et al., **CRITIC**, arXiv:2305.11738; Dhuliawala et al., **Chain-of-Verification**, arXiv:2309.11495. ([arxiv.org](https://arxiv.org/abs/2303.11366?utm_source=openai))
7. Huang et al., **LLMs Cannot Self-Correct Reasoning Yet**, arXiv:2310.01798; Tyen et al., **LLMs Cannot Find Reasoning Errors**, arXiv:2311.08516. ([arxiv.org](https://arxiv.org/abs/2310.01798?utm_source=openai))
8. Du et al., **Improving Factuality through Multiagent Debate**, arXiv:2305.14325; Zhang et al., **If Multi-Agent Debate Is the Answer…**, arXiv:2502.08788. ([arxiv.org](https://arxiv.org/abs/2305.14325?utm_source=openai))
9. Choi et al., **Debate or Vote**, arXiv:2508.17536; Wu et al., **Can LLM Agents Really Debate?**, arXiv:2511.07784. ([arxiv.org](https://arxiv.org/abs/2508.17536?utm_source=openai))
10. Packer et al., **MemGPT**, arXiv:2310.08560; Park et al., **Generative Agents**, arXiv:2304.03442; Wang et al., **Voyager**, arXiv:2305.16291. ([arxiv.org](https://arxiv.org/abs/2310.08560?utm_source=openai))
11. Zelikman et al., **STOP**, arXiv:2310.02304; Hu et al., **Automated Design of Agentic Systems**, arXiv:2408.08435; Zhang et al., **Darwin Gödel Machine**, arXiv:2505.22954. ([arxiv.org](https://arxiv.org/abs/2310.02304?utm_source=openai))
12. Debenedetti et al., **AgentDojo**, arXiv:2406.13352; Greenblatt et al., **AI Control**, arXiv:2312.06942. ([arxiv.org](https://arxiv.org/abs/2406.13352?utm_source=openai))
13. xAI, **Grok 4.20 System Card**, April 7, 2026. ([data.x.ai](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf))
14. xAI, **Grok Build Is Now Open Source**, July 15, 2026; **Workflows in Grok Build**, July 23, 2026. ([x.ai](https://x.ai/news/grok-build-open-source))

---

## 31. Differential Change Log (v2 → v3)

Every accepted finding from the six-lens v2 self-review is recorded with its disposition and validation status. "Validated" means demonstrated by the harness (§32).

| ID | v2 defect (aggregated finding) | v3 change | Where | Validated |
|---|---|---|---|---|
| B1 | Ghost fields: `probe_available`/`approximation_available`/`infeasible` read by §24.4, in no schema, produced by nothing; harness reached states only via config injection | Fields added to §24.2 with named producers (diagnose → probe; select error_bound → approximation; constraint screen → infeasible); §24.4 assigns them; classifier is state-only; harness asserts the producer flags | §3.3, §15.5, §24.2, §24.4 | S16–S18 |
| B2 | §15.4 class bars had no consumer; harness SOLVED at seed reliability 0.5 | `verify_outcome` computes success := checks ∧ external ∧ reliability ≥ class_bar; reliability-blocked → ESCALATED; deterministic tools at 1.0, model verifiers seed 0.5 and calibrate | §15.1–15.4 | S4, S26 |
| B3 | PENDING branch: undefined `execute_authorized_subset`, subset re-executed every pass, no resolution, no timeout | Static A2 allowlist subset, once (guard); `pending_timeout` → ESCALATED with partial packet; interface defined | §20.3a, §21.4, §24.3, §24.4 | S20 |
| B4 | Interface drift persisted: missing functions, arity mismatch, free variables in `solve()` | §24.3 completed and bound to §24.4 verbatim; world binding explicit (harness `make_world` pattern); `diagnose` unpacking reconciled | §24.3–24.4 | doc-level + harness |
| B5 | G-HOW gate and plan stop/escalation conditions had no call sites despite §13.7 claims | `check_exit_gate("HOW")` after selection; plan conditions consumed at DO; guarantee 6 reworded | §12.8, §13.7, §24.4 | S13, S19 |
| B6 | Competence loop dangling: update returned None, nothing wrote `state.competence`; §8.3 cited a LearningScheduler that §24.5 didn't define | `competence.update(state, calibration)` writes state.competence; route consumes it; LearningScheduler triggers defined in §24.5 | §19.3, §8.3, §24.5 | S22 |
| B7 | Council was a comment not a branch; minority ledger never written; S7 asserted only absence | `if route.use_council: run_council` branch; generate returns minority_reports/unresolved_disagreements; dissent surfaced in the packet | §17.2–17.4, §24.4 | S23 (positive), S7 (negative) |
| B8 | 69% reduction misattributed to the fast path; §9.4 stale totals | §32.3 attribution: v1→v2 delta was loop-termination driven (S2/S3 ≈ 108%); v2→v3 measured under uniform pricing (−33.6%); §9.4 numbers refreshed | §32.2–32.3 | metrics |
| B9 | `calls_max`/`agents_max`/`deadline` never enforced; budget.check had no call site | Call ceiling enforced on cognitive calls at loop top + budget.check; agents_max is a per-round council cap; deadline consumed; effort-class attestation mitigates self-classification | §9.5–9.6, §20.4 | S24 |
| B10 | Novelty plateau defeatable by cosmetic frame mutations; signature too narrow | Canonicalized signature over hypotheses, frame, observations, evidence, alternatives, plan; documented as heuristic | §9.5 | S3 (still converges) |
| B11 | Verifier identity a mutable string; fast path force-overrode "external" masking SELF | Identity set by VerifierRegistry by kind; override removed; reliability_blocked path | §15.3–15.4, §24.4 | S4 |
| B12 | Delta-verification comment-only; cascade re-verified everything | Content-hash cache per candidate; premortem dedup; risk register dedup | §15.6, §24.4 | S2 |
| B13 | Early classifier entry missing: S5 burned 3 full passes; S6/S16/S17 ran HOW after decision | Classifier entry immediately after WHY gate on gap/probe/outage; reliability-blocked early stop | §11.7, §24.4 | S5, S6, S16, S25 |
| B14 | Memory authority self-attested (`authorized_expert` string); trust writer-labeled | Authority tokens minted by SafetyKernel; trust from verifier reliability | §18.2a | S8 |
| B15 | §21.2 mapped 5 of 10 invariants; invariant 8 had no mechanism | All ten mapped; invariant 8 → ToolBroker no-replication whitelist + attest denial | §21.2, §20.2 | doc-level |
| B16 | Checkpoint/resume unimplementable: single epilogue checkpoint, no format/corruption/replay protection; guarantee 8 overclaimed | Checkpoint at every stage boundary; versioned JSON + HMAC; idempotency on (task, action, args); guarantee 8 reworded | §20.5, §24.4 | S21 |
| B17 | Doc hygiene: §5.9 ranking, stale counts (15 vs 18, S1–S15), REFRAME_BUDGET undefined dual-use, queue-gate drift, L1 unreachable, no config layer, 5-test suite unenumerated, §23.6 metrics unshipped, no auto-confirm ambiguity, EVOC proxy absent | Ranking fixed; counts → S1–S26; constants GATE_REENTRY_BUDGET/REFRAME_BUDGET/PENDING_TIMEOUT named; queue gate aligned; L1 branch; config block §9.6; 5-test suite enumerated §23.6a/§25.2; no auto-confirmation; EVOC proxy formula | throughout | S25, S19, S10, S20 |

### 31.1 Non-accepted and deferred findings

- Model heterogeneity for council roles (Phase 3, §26); open-ended candidate archives (Phase 5); full EvaluationPlane batch feedback (Phase 2) — accepted as documented limitations, matching §26.
- The independent risk estimator's full separation is specified (§20.4) but in the single-model MVP is realized as deterministic checks + second-verifier patterns; documented in §32.4.
- EVOC's first term remains a self-estimated stopping heuristic, capped in influence by config — documented as a residual (never evidence).

---

## 32. Empirical Validation

### 32.1 Method

Per the framework's own rules (P4, P9, §22.3), v3 changes were validated by **execution, not self-critique**. `validation/harness.py` implements the frozen v2 algorithm (baseline) and the v3 algorithm over identical deterministic mock components, runs a 26-scenario suite (S1–S18 from v2 plus S19–S26 for v3 mechanisms), and asserts the framework's own standards. The harness validates what is decidable — termination, state reachability, budget enforcement, stage gating, threshold enforcement, packet completeness, delta reuse, pending semantics, resume idempotency, competence feedback, council minority preservation — **not** model intelligence. Bookkeeping calls (budget, monitors, audit, gates) are priced at 0 cognitive tokens and counted as overhead separately.

### 32.2 Results (26 scenarios; 3 reproducible runs, identical every run)

| Scenario | v2 status | v3 status | v2 asserts | v3 asserts | v2 tokens | v3 tokens |
|---|---|---|---|---|---|---|
| S1 trivial task, E0 | SOLVED | SOLVED | 5/5 | 4/4 | 3 | 3 |
| S2 executor always fails | RESOURCE_LIMITED | RESOURCE_LIMITED | 4/4 | 6/6 | 61 | 39 |
| S3 frame oscillates | SOLVED | SOLVED | 4/4 | 4/4 | 90 | 53 |
| S4 clear-looking, high stakes | SOLVED | ESCALATED | 4/4 | 5/5 | 19 | 18 |
| S5 no external verifier | ESCALATED | ESCALATED | 4/4 | 5/5 | 42 | 3 |
| S6 ambiguous success | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 16 | 3 |
| S7 calculator exists | SOLVED | SOLVED | 4/4 | 4/4 | 3 | 3 |
| S8 injection attempt | SOLVED | SOLVED | 5/5 | 5/5 | 16 | 15 |
| S9 EVOC exhausted | RESOURCE_LIMITED | RESOURCE_LIMITED | 4/4 | 4/4 | 2 | 2 |
| S10 proposal flood | SOLVED | SOLVED | 4/4 | 5/5 | 16 | 16 |
| S11 authorization denied | ESCALATED | ESCALATED | 4/4 | 4/4 | 14 | 13 |
| S12 action-class misattestation | UNSAFE | UNSAFE | 4/4 | 4/4 | 14 | 13 |
| S13 red team catches flaw | SOLVED | SOLVED | 4/4 | 4/4 | 27 | 21 |
| S14 memory contradiction | SOLVED | SOLVED | 4/4 | 4/4 | 16 | 15 |
| S15 WHAT gate: no metrics | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 4/4 | 4/4 | 2 | 2 |
| S16 safe probe available | NEEDS_EXPERIMENT | NEEDS_EXPERIMENT | 4/4 | 4/4 | 19 | 3 |
| S17 bounded approximation | APPROXIMATED | APPROXIMATED | 4/4 | 4/4 | 16 | 15 |
| S18 constraints inconsistent | INFEASIBLE | INFEASIBLE | 4/4 | 4/4 | 16 | 15 |
| S19 plan stop-condition | RESOURCE_LIMITED | INFEASIBLE | 3/3 | 4/4 | 61 | 15 |
| S20 pending authorization | INFEASIBLE | ESCALATED | 3/3 | 5/5 | 34 | 21 |
| S21 crash, resume | SOLVED | SOLVED | 3/3 | 4/4 | 19 | 22 |
| S22 competence feedback | SOLVED | SOLVED | 3/3 | 4/4 | 16 | 19 |
| S23 council minority | SOLVED | SOLVED | 3/3 | 4/4 | 19 | 21 |
| S24 call budget hard-stop | RESOURCE_LIMITED | RESOURCE_LIMITED | 3/3 | 4/4 | 19 | 25 |
| S25 low-stakes verifier outage | NEEDS_EVIDENCE | NEEDS_EVIDENCE | 3/3 | 4/4 | 16 | 3 |
| S26 warm verifier, A4 bar | SOLVED | SOLVED | 3/3 | 4/4 | 16 | 15 |
| **Totals** | | | **98/98** | **111/111** | **592** | **393** |

### 32.3 What the suite demonstrates — and honest attribution

- **Enforcement fidelity (B2/B11):** S4 — v2 SOLVED a stakes-5 task at seed reliability 0.5; v3 refuses (reliability-blocked → ESCALATED). S26 — a warm verifier at the A4 bar does yield SOLVED, showing the bootstrap path.
- **Early classifier entry (B13):** S5: 42 → 3 tokens; S6/S16/S25: 16–19 → 3. The loop stops at WHY when the outcome is already decided.
- **Delta verification (B12):** S2 verifies its candidates once (cache reuse); 61 → 39 tokens; the risk register collapses repeated premortem entries.
- **Gate enforcement (B5):** S13 (red-team regeneration), S15 (WHAT gate), S19 (plan stop-condition ends the loop at iteration 1; 61 → 15).
- **Pending semantics (B3):** S20 — the A2 subset executes exactly once, then PENDING times out to ESCALATED with a packet; v2 re-executed the subset unboundedly.
- **Resume (B16):** S21 — a mid-task crash resumes and completes with the confirmed action executed exactly once.
- **Competence loop (B6):** S22 — episode 1's evaluation outcome changes episode 2's route (effort 2 → 1).
- **Council (B7):** S23 — the council branch runs, the minority report is preserved and surfaced in the packet; S7 — the deterministic-solver task skips it.
- **Call budget (B9):** S24 — the call ceiling terminates a looping task with RESOURCE_LIMITED.
- **All eight states reachable through producers (B1):** S1–S18 + new scenarios; no terminal state is produced by direct classifier reads of task inputs — each is set through a named producer or explicit assignment (world facts are modeled as scenario config; the algorithm reads them only through producers).
- **Attribution honesty (B8):** the v1→v2 "69% reduction" was driven by terminating two watchdog loops (S2/S3 ≈ 108% of the delta); the fast path contributed 6 tokens. v3 measures the remaining loop economics under uniform pricing: **v2 592 → v3 393 cognitive tokens (−33.6%)**, from delta verification, early classifier entry, and gate-driven early stops. Per-task overhead (gates, monitors, audit) is ~0 cognitive tokens (bookkeeping priced separately).
- **Reproducibility:** deterministic; 3 consecutive runs identical.

### 32.4 Honest limitations of the validation

- Mock components: the harness does not simulate model intelligence, sampling, or real tools; control-flow guarantees hold for any components satisfying the component contracts.
- **Coverage disclosure (v3):** the harness implements: MetaRouter (flags, stakes override, competence-aware routing, council feasibility), all gates, Diagnostician with probe/VOI producers, Explorer, CouncilMock (2 agents, minority ledger), VerifierRegistry (reliability by kind, class bars, delta cache), Premortem/RedTeam, Planner (stop conditions), SafetyKernel (attest, pending, minting), Executor (idempotency), ReviewEngine, MemoryManager (channels, contradiction, quarantine, minted tokens), ImprovementEngine (dedup, evaluate), LoopMonitor, BudgetController, CompetenceModel, TaskScheduler (checkpoint/resume). It does **not** implement: SearchController exploration, EvidenceService VOI beyond the producer flags, WorldModel, ExecutionMonitor findings beyond the plan-condition checks, AuditLog latency measurement, full EvaluationPlane suites, or multi-round debate. Those are specified (§24) and validated at design level in §31.
- The independent risk estimator is realized in the harness as attestation checks against ground-truth config; full separation is a Phase-3/implementation concern (§31.1).
- Authority-token minting (§18.2a) has a call site in the algorithm and telemetry in the harness, but the MVP harness seeds the issued-token set; the mint path is exercised at design level. The trust-margin rule uses a strict comparison (margin 0.1 not applied) and the §18.2b consolidation trigger (≥ 3 near-duplicates) has no harness implementation — both are design-level.
- The EVOC proxy and novelty signature remain simplified stand-ins (§9.5); production implementations must calibrate from §23.8 telemetry.
- The threshold table, budget defaults, and SLAs are configuration (§9.6), not constants.

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

Normative content (must be satisfied): §3.3–3.4, §6.5, §9.4–9.6, §10.5, §11.7, §12.5–12.8, §13.2–13.3, §13.7, §15.1–15.6, §17.2–17.4, §18.2–18.4, §20.2–20.5, §21.2–21.4, §22.3–22.7, §23.6a–23.8, §24.2–24.4. Guidance (advisory): the remaining prose, including §5 and §26.

---

*End of document.*
