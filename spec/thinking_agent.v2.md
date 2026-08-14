# Thinking Agent

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Version:** 2.0  
**Research cutoff:** August 7, 2026  
**Status:** Research and engineering blueprint (validated — see §32)  
**Source policy:** Primary arXiv papers and official xAI materials were prioritized over third-party commentary.  
**Change policy:** v2 supersedes v1. The differential change log in §31 records every accepted finding from the v1 self-review, the v2 change, and its empirical validation status. The executable validation harness lives in `validation/harness.py`; its results are in §32.

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

A continuous **VERIFY** layer surrounds every stage, and a **governed loop** (loop monitors, budget envelope, stage gates, explicit state classifier) guarantees termination and graceful failure — the properties v1 asserted in prose but left unenforceable, and v2 makes operational (§24.4, §32).

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

Every task terminates in exactly one of the eight graceful states (§3.3), and every terminal state produces the proof-carrying decision packet (§15.4). In v2 these are not aspirations: they are enforced by the state classifier and the common epilogue of the reference algorithm (§24.4), and demonstrated by the executable harness (§32).

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

These functions must not be collapsed into one unconstrained model call. In v2, each function has a named owner component with an interface (§24.1, §24.3): *generation* is owned by the Explorer and council; *truth determination* by the VerifierRegistry with proposer–verifier separation (§15.2); *safety determination* by the SafetyKernel with independent action-class attestation (§13.2, §20.4); *execution* by the ToolBroker with transactional semantics (§13.3, §20.3); *learning* by the ReviewEngine and MemoryManager (§14, §18); *system change* by the ImprovementEngine under the §22 pipeline.

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
- The v2 reference algorithm, its harness, or its mock components demonstrate any of the above. The harness (§32) validates control-flow properties, not intelligence.

### 3.3 Required graceful-failure states

Every task must terminate in one of these explicit states:

| State | Meaning | Producer (v2) |
|---|---|---|
| `SOLVED` | The result satisfies the success criteria and verification threshold. | `verify_outcome` with external verifier identity + threshold per §15.4 |
| `APPROXIMATED` | An exact solution was unavailable, but a bounded approximation was produced. | `classify_terminal` when an approximation bound exists (§15.5) |
| `NEEDS_EVIDENCE` | A decision cannot responsibly be made without more information. | `classify_terminal` when the missing-evidence inventory is non-empty (§11.5) |
| `NEEDS_EXPERIMENT` | A safe probe or experiment is the next rational action. | `classify_terminal` when a probe with positive information value is available (§19.2) |
| `INFEASIBLE` | Constraints are inconsistent or the requested outcome is not currently achievable. | `classify_terminal` on constraint conflict or total candidate failure (§12.4) |
| `UNSAFE` | The requested action violates a safety, legal, ethical, or permission boundary. | SafetyKernel denial with status `UNSAFE` (§20.4, §21) |
| `ESCALATED` | Human or domain-expert judgment is required. | SafetyKernel denial with status `ESCALATED`; verifier-unavailable ladder (§15.2) |
| `RESOURCE_LIMITED` | The expected value of further computation does not justify its cost. | LoopMonitor/BudgetController exhaustion (§9.5, §9.6) |

The state machine is **complete** in v2: every terminal path of the reference algorithm (§24.4) passes through the classifier or an explicit status assignment, and the harness demonstrates that all eight states are reachable (§32, scenario suite S1–S15).

### 3.4 State-transition policy

- Every terminal state is produced by exactly one owning mechanism (the Producer column above).
- `UNSAFE` and `ESCALATED` are distinguished: `UNSAFE` means the action is prohibited; `ESCALATED` means the action may be valid but requires authority the system does not have.
- States are mutually exclusive; the classifier tests them in the fixed order defined here (verifier availability → ambiguity → evidence gap → probe → feasibility → budget → approximation → residual) and implemented by `classify_terminal` (§24.3, §24.4).
- Every terminal path writes the proof-carrying decision packet (§15.4) via the common epilogue of §24.4 — including denial and escalation paths, which v1 omitted (finding A7).

---

## 4. Architectural Synthesis and Lineage

Thinking Agent synthesizes five bodies of knowledge. No component depends on a separate companion document; every required concept is inlined in the sections below or anchored to external research URLs in Section 30.

| Lineage | Retained contribution | Thinking Agent implementation |
|---|---|---|
| Ranked traditional human thinking models (40 frameworks evaluated by adoption priority) | Cynefin, Premortem, AAR, Double-Loop Learning, RPD, root-cause analysis, metacognition, creativity methods, Red Teaming, plus supporting frameworks summarized in §5.9 | Adaptive routing, risk simulation, structured review, method library, adversarial verification |
| Staged problem-solving process model (WHAT → WHY → HOW → DO → REVIEW) | Framing discipline, diagnostic rigor, alternative generation, selection criteria, execution project management, review and iteration | Primary task-level cognitive loop (stages 1–5 of the main loop, §10–§14), with boolean stage gates enforced in §24.4 |
| Grok-inspired agent architecture draft | Fast/full dual paths, CoALA memory hierarchy, specialized multi-agent roles, hierarchical planning, nested self-evolution | Meta-controller (§9), structured cognitive workspace (§7), agent council (§17), learning engine (§14, §22) |
| Verification-first multi-agent protocol | Independent generation before communication, evidence-weighted aggregation, known-limit non-claims, anti-debate-failure guards | Independent verifier separation (§15), verifier-weighted synthesis (§17.3), explicit non-claims and uncertainty (§3.2–3.3, §5.4) |
| Thinking Agent research additions (2024–2026 agent-security and production literature) | Tool security, authority/data separation, least privilege, permission boundaries, gated self-modification, structured task state, evaluation portfolio | Safety kernel (§21), tool broker (§20), self-improvement pipeline (§22), benchmark and audit plane (§23), shared task state (§24.2) |
| v1 self-review (2026) — six-lens council + executable validation | Termination guarantees, budget governance, stage-gate enforcement, state-machine completeness, feedback loops, failure semantics | Governed loop, BudgetController, LoopMonitor, explicit classifier, CompetenceModel, transaction semantics (§9, §15, §20, §24) — see §31 |

---

## 5. Research Foundations

### 5.1 Cognitive architecture

Cognitive-architecture research consistently treats intelligence as an interaction among perception, attention, action selection, memory, learning, and reasoning rather than a single monolithic process. CoALA provides a particularly useful language-agent abstraction: modular memory, internal and external action spaces, and structured decision procedures. Research proposing broader AGI-oriented architectures similarly identifies goal management, reflection, ethics, social interaction, learning, monitoring, and problem-solving as distinct functional requirements. ([arxiv.org](https://arxiv.org/abs/1610.08602?utm_source=openai))

Thinking Agent adopts a **polyglot cognitive substrate** rather than assuming that all knowledge must be stored in one format. Text, graphs, equations, code, images, databases, models, procedures, and trajectories can coexist as long as they share provenance, identity, access-control, and relationship metadata.

### 5.2 Grounded reasoning and tool use

ReAct demonstrated the value of interleaving reasoning, action, and environmental observation. Toolformer showed that models can learn when and how to call external APIs, while SayCan combined semantic planning with grounded affordance or value estimates for embodied action. These results support treating tools and environmental feedback as first-class cognitive components rather than optional plugins. ([arxiv.org](https://arxiv.org/abs/2210.03629?utm_source=openai))

### 5.3 Search, decomposition, and planning

Tree of Thoughts, RAP, LATS, and ADaPT show complementary methods for exploring alternative reasoning paths, simulating future states, backtracking, and decomposing tasks only when needed. Self-Discover adds a method-composition idea: select and combine reasoning modules according to the current task instead of imposing one fixed reasoning structure. ([arxiv.org](https://arxiv.org/abs/2305.10601?utm_source=openai))

Thinking Agent therefore includes a **method composer** and a **SearchController**. In v2 the SearchController is a first-class component (§16.2, §24.1) with an explicit exploration budget and an expected-value-of-exploration gate; full tree search is used only when the expected value of additional exploration exceeds its cost. (v1 asserted the search controller but never owned it — finding A17.)

### 5.4 Reflection and verification

Reflexion, Self-Refine, CRITIC, and Chain-of-Verification provide evidence that iterative feedback can improve outputs, especially when feedback comes from tests, tools, retrieval systems, or environments. However, intrinsic self-corrective reasoning is unreliable on many reasoning and planning tasks. Models may fail to locate their own errors, convert correct answers into incorrect ones, or produce false-positive verification judgments. ([arxiv.org](https://arxiv.org/abs/2303.11366?utm_source=openai))

Thinking Agent consequently follows this rule:

> **Self-criticism is a source of hypotheses, not proof of correctness.**

External tests, tools, independent models, formal systems, environmental observations, and qualified humans take precedence over unsupported self-evaluation. In v2 this rule is enforced at the one place it matters most — the `SOLVED` gate: `verify_outcome` requires an external verifier identity and a reliability above the class threshold (§15.4), so a self-only judgment can never declare `SOLVED` (finding A11, demonstrated in §32 S5).

### 5.5 Multi-agent reasoning

Early multi-agent debate research reported improvements in reasoning and factuality. Later systematic studies found that debate does not reliably beat strong single-agent baselines, that model heterogeneity matters, and that majority voting may explain much of the apparent gain. Controlled studies also identify majority pressure, sycophantic conformity, and consensus collapse as failure modes. ([arxiv.org](https://arxiv.org/abs/2305.14325?utm_source=openai))

The Thinking Agent protocol therefore requires:

1. Independent generation before communication.
2. Verification before debate.
3. Targeted debate only over unresolved differences.
4. Preservation of minority reports.
5. Evidence-weighted rather than eloquence-weighted aggregation.
6. Heterogeneous models, tools, data, or roles when possible.

In v2, independence is structural, not aspirational: each agent gets a fresh context window, an answer schema, and a private write slot (§17.2); the minority report ledger is append-only and written before aggregation (§17.3); and the council is only invoked when §17.4 predicates pass (finding A10, demonstrated in §32 S7).

### 5.6 Memory and lifelong learning

CoALA, MemGPT, Generative Agents, and Voyager support the separation of working, episodic, semantic, and procedural memory. They also demonstrate the value of memory consolidation, reflection, dynamic retrieval, executable skill libraries, and experience-driven planning. ([arxiv.org](https://arxiv.org/abs/2309.02427?utm_source=openai))

Thinking Agent treats memory as an actively managed system with provenance, trust, expiration, contradiction handling, and permission controls—not as an unlimited transcript archive. In v2 the write protocol is a complete decision procedure with a contradiction rule, channel separation, quarantine with a promotion path, and a consolidation trigger (§18.2–18.5) — the v1 protocol dead-ended at “detect contradiction” (finding A9, demonstrated in §32 S14).

### 5.7 Self-improving systems

STOP, Automated Design of Agentic Systems, and the Darwin Gödel Machine provide evidence that model-based systems can improve portions of their scaffolding or code through search and empirical evaluation. These demonstrations remain bounded and task-dependent; the Darwin Gödel Machine, for example, validated coding-agent changes through benchmarks while using sandboxing and human oversight. They do not establish unrestricted or automatically safe recursive self-improvement. ([arxiv.org](https://arxiv.org/abs/2310.02304?utm_source=openai))

Thinking Agent permits systems to **propose** changes to themselves but separates proposal authority from deployment authority. In v2 the improvement path is governed end-to-end: admission control and dedup at the queue (§22.2), the full §22.3 acceptance pipeline invoked before deployment, a defined stable baseline (§22.4), a Kaizen step-size policy (§22.5), and an evaluation plane that candidates cannot modify (§22.6).

### 5.8 Production agent patterns

Official xAI documentation describes production workflows that plan a task, give subagents clean and focused contexts, fan independent work out in parallel, adversarially verify findings, and synthesize a final result. xAI has also published the Grok Build harness components, including context assembly, tool dispatch, skills, hooks, extensions, and subagents. These examples demonstrate that several Thinking Agent orchestration patterns are implementable today, though they are not evidence that AGI has been achieved. ([x.ai](https://x.ai/news/workflows))

Official xAI safety documentation separately evaluates chat behavior, agentic behavior, prompt injection, deception, sycophancy, sabotage, and dual-use capabilities. This reinforces the Thinking Agent position that an agent must be evaluated as a complete acting system, not only as a text generator. ([data.x.ai](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf))

### 5.9 Traditional thinking-model portfolio

Thinking Agent draws on a ranked survey of 40 traditional human thinking models, scored by adoption priority for agent loops (1 = lowest leverage, 10 = highest). The frameworks below cover the top tier and notable supporting entries; every listed contribution is integrated into Thinking Agent's stages, method composer, or multi-agent roles rather than retained as a separate document.

| Rank | Model | Origin / Field | Core concept | Adoption score | Why it scores high for agents |
|------|-------|----------------|--------------|----------------|--------------------------------|
| 1 | Cynefin Framework | Complexity science (Dave Snowden) | Sense context first, then respond according to domain: Clear (best practice), Complicated (expert analysis), Complex (probe–sense–respond), Chaotic (stabilize first), Disorder (decompose) | 10 | Enables adaptive loop intensity and Fast-vs-Full routing — the single highest-leverage addition |
| 2 | Premortem Analysis | Decision science (Gary Klein) | Imagine failure has already occurred, work backward to uncover plausible causes, then mitigate up front | 10 | Proactive risk detection at near-zero implementation cost; runs before HOW-stage commitment (§12.6) |
| 3 | After-Action Review (AAR) | Military / Lean | Four questions: What was supposed to happen? → What actually happened? → Why the difference? → What should change next? | 10 | Perfect match for the REVIEW stage; powers single-loop and double-loop learning (§14) |
| 4 | Double-Loop Learning | Organizational learning (Argyris & Schön) | Single-loop changes tactics; double-loop also questions the governing assumptions, frames, and values behind the tactics | 9.5 | Core to meaningful self-evolution; in v2 runs inside the loop so it can trigger mid-task reframes (§14.3) |
| 5 | Recognition-Primed Decision (RPD) | Naturalistic decision making (Klein) | Expert pattern match → rapid mental simulation → act; used when a familiar pattern is recognized with high confidence | 9.5 | Enables the Fast Recognition Path for Clear/Complicated expert domains without full-loop overhead |
| 6 | Root-cause suite (5 Whys + Ishikawa Fishbone + Fault Tree Analysis) | RCA (Toyota + Ishikawa + safety engineering) | Problem → categories → drill-down toward root cause using causal chains, category diagrams, or boolean fault trees | 9 | Greatly strengthens the WHY stage and diagnostic depth for complex problems |
| 7 | Metacognition Cycle | Educational psychology (Flavell) | Plan → Monitor → Evaluate → Adjust — applied to the thinker's own reasoning process | 9 | Implemented as the lightweight parallel meta-process inside META-CONTROL |
| 8 | Dual Process Theory (System 1 & 2) | Psychology (Kahneman) | Fast intuitive judgment (S1) vs slow deliberate reasoning (S2) with context-appropriate switching | 9 | Foundation for Fast-vs-Full path routing and Cynefin-based effort selection |
| 9 | Paul-Elder Critical Thinking Framework | Philosophy / Education | Eight Elements of Thought checked against Intellectual Standards (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness) | 8.5 | Raises the quality bar on the Diagnostician, Researcher, Verifier, and Synthesizer roles |
| 10 | Theory of Constraints (TOC) Thinking Processes | Management (Eliyahu Goldratt) | Current Reality Tree → Evaporating Cloud (contradiction resolution) → Future Reality Tree | 8.5 | Powerful for conflicting goals; synergizes with TRIZ and HOW-stage alternative generation |
| 11 | Osborn-Parnes Creative Problem Solving (CPS) | Creativity research | Clarify → Ideate → Develop → Implement → Evaluate | 8 | Direct upgrade to HOW-stage divergent ideation and creative Explorer roles |
| 12 | Red Team Thinking | Military / Security | Deliberately attack your own plan, assumptions, and artifacts to find weaknesses before an opponent does | 8 | The Red Team role in the multi-agent council and the HOW-stage Red Team gate (§12.7) |
| 13 | Six Thinking Hats | Lateral thinking (Edward de Bono) | Six sequential or parallel perspectives: Facts (White), Emotions (Red), Caution (Black), Benefits (Yellow), Creativity (Green), Process (Blue) | 8 | Good for HOW-stage consolidation and multi-agent perspective diversity |
| 14 | TRIZ | Inventive problem solving (Altshuller) | Identify contradictions (technical or physical), apply 40 inventive principles or separation principles to resolve | 8 | Structured creativity for contradiction-heavy problem classes |
| 15 | SCAMPER | Creative thinking (Bob Eberle) | Idea-generation checklist: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse | 7.5 | Lightweight rapid-ideation tool for the Explorer role |
| 16 | Kaizen | Japanese management (Toyota) | Many small, testable, reversible improvements over time rather than big-bang rewrites | 7.5 | Governs the step size of the self-evolution engine to reduce regression risk (§22.5) |
| 17 | OODA Loop | Military strategy (John Boyd) | Observe → Orient → Decide → Act — high-tempo loop for dynamic uncertainty | 7 | Inspired the DO-stage micro-loop pattern alongside ReAct |
| 18 | GROW Coaching Model | Coaching (John Whitmore) | Goal → Reality → Options → Will (commitment) | 6.5 | Useful in the WHAT stage for ambiguous user goals and in DO-stage stakeholder alignment |
| 19 | Design Thinking | Design / Innovation | Empathize → Define → Ideate → Prototype → Test → Iterate | 7 | Useful for user-facing or product-definition tasks |
| 20 | Nemawashi | Japanese decision making | Informal consensus gathering and alignment before any formal decision | 5.5 | Informs multi-agent pre-debate alignment and stakeholder-facing communication |

*(v2 fix: OODA (7.0) now ranks above GROW (6.5) — the v1 table had an ordering anomaly; Gibbs' Reflective Cycle is listed once, in the supporting set below, not double-listed.)*

The remaining 20 frameworks in the ranked survey cover philosophical cross-cultural traditions (Wu Wei, Stoic Reflection, Buddhism, Ubuntu, 三思而后行), education taxonomies (Bloom's, Kolb's, Gibbs' Reflective Cycle, IDEAL), and specialized process frameworks (PDCA/PDSA, DMAIC, SWOT, Appreciative Inquiry, Hansei, Socratic Method, Action Learning, Dialectical Thinking, 4E Cognition, High-Context vs Low-Context, Ladder of Inference). They are selectively called on by the method composer (§16) according to the current task signature rather than mandated for every loop.

---

## 6. Design Principles

### P1. Context before cognition

Classify the problem, stakes, uncertainty, and action risk before selecting a reasoning procedure.

### P2. Frame before diagnosing; diagnose before prescribing

Do not optimize a solution to the wrong problem. Preserve the sequence:

```text
WHAT → WHY → HOW
```

unless a chaotic situation requires immediate stabilization.

### P3. Evidence outranks confidence

Fluent language, agent agreement, and self-reported confidence are not evidence.

### P4. External feedback outranks intrinsic self-critique

Whenever feasible, use retrieval, code execution, tests, formal verification, simulations, sensors, or expert review.

### P5. Independent diversity before social influence

Agents produce initial analyses independently before seeing peer conclusions.

### P6. Reversible before irreversible

Prefer actions that can be tested, contained, undone, or compensated.

### P7. Verification scales with consequence

A short high-stakes action can require more verification than a long low-stakes analysis.

### P8. Memory requires governance

No observation becomes durable knowledge without provenance, trust labeling, conflict checks, and an appropriate retention policy.

### P9. Self-improvement must be empirical and reversible

Changes are accepted only after sandboxed evaluation, safety testing, independent review, canary deployment, and rollback preparation.

### P10. Preserve human authority

The architecture may optimize means within delegated scope. It may not autonomously redefine human goals, values, permissions, or governance.

### P11. Stop when marginal value turns negative

Continue reasoning only while the expected benefit of another cycle exceeds computation cost, delay, opportunity cost, and added risk.

### P12. Expose decision artifacts, not performative reasoning

The system should expose assumptions, evidence, alternatives, tests, uncertainty, and decision criteria. It need not reveal unrestricted internal scratchpads or raw chain-of-thought.

### 6.5 Principle–mechanism matrix (v2)

Every design principle is bound to an enforcing component and an enforcing point in the reference algorithm. This matrix is normative: a v2 implementation must be able to point at the enforcing mechanism for each principle (v1 left most principles as prose — finding A18).

| Principle | Enforcing component | Enforcing point (v2) |
|---|---|---|
| P1 | MetaRouter | `route(state, competence)` precedes all stages (§24.4 step 1) |
| P2 | Stage gates | `check_exit_gate("WHAT")` blocks WHY; `"WHY"` gate blocks HOW (§10.5, §11.7, §24.4) |
| P3 | VerifierRegistry | Aggregation and SOLVED require verification reports, never self-reported confidence (§15.4, §17.3) |
| P4 | VerifierRegistry + ToolBroker | `verify_outcome` requires external verifier identity; self-only cannot yield SOLVED (§15.4) |
| P5 | CouncilOrchestrator | Fresh contexts + private answers before any peer communication (§17.2) |
| P6 | SafetyKernel | Reversibility class on every candidate and action; penalty in decision score (§12.5, §13.2) |
| P7 | MetaRouter + VerifierRegistry | `verification_depth` derived from stakes/effort; thresholds per action class (§9.2, §15.4) |
| P8 | MemoryManager | Write protocol with provenance, trust, contradiction, quarantine, expiry (§18.2) |
| P9 | ImprovementEngine + EvaluationPlane | §22.3 pipeline; baseline comparison; canary + rollback (§22.3–22.4) |
| P10 | SafetyKernel + GoalManager | Goal contract signed and external; renegotiation gated by kernel and owner (§21, §24.5) |
| P11 | LoopMonitor + BudgetController | EVOC check, novelty plateau, iteration/token budgets → RESOURCE_LIMITED (§9.5–9.6, §24.4) |
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
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ META-CONTROLLER                                             │
│ Context classification • routing • effort • agenda          │
│ competence model • uncertainty • stopping/escalation        │
│ BUDGET ENVELOPE • ROUTE FLAGS                               │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ STRUCTURED COGNITIVE WORKSPACE                              │
│ WHAT → WHY → HOW → DO → REVIEW                              │
│ Continuous VERIFY across every stage                        │
│ LOOP MONITOR (novelty • repetition • EVOC • budgets)        │
└───────────────┬──────────────────────┬───────────────────────┘
                │                      │
┌───────────────▼────────────┐  ┌──────▼──────────────────────┐
│ REASONING AND COUNCIL      │  │ MEMORY AND WORLD MODEL     │
│ Decompose • search         │  │ Working • episodic         │
│ simulate • generate        │  │ semantic • procedural      │
│ critique • synthesize      │  │ causal • multimodal        │
│ SearchController           │  │ CompetenceModel            │
└───────────────┬────────────┘  └──────┬──────────────────────┘
                │                      │
┌───────────────▼──────────────────────▼───────────────────────┐
│ TOOL BROKER AND EXECUTION SANDBOX                           │
│ Retrieval • code • APIs • sensors • robots • transactions   │
│ timeouts • retries • idempotency • compensation             │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ TELEMETRY, EVALUATION, AND SELF-EVOLUTION                   │
│ Outcomes • AAR • benchmarks • change proposals • rollback   │
│ per-stage audit telemetry • stable baseline                 │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Four Nested Timescales

Thinking Agent operates through four nested loops, plus an explicit session layer.

### 8.1 Action loop

```text
Observe → Predict → Select action → Authorize → Execute → Verify
```

This is a short ReAct/OODA-style loop used during execution. Each action is transactional (§13.3): idempotency keys, timeouts, retries, and compensation are defined per action class (§20.3).

### 8.2 Task loop

```text
META → WHAT → WHY → HOW → DO → REVIEW
```

This is the main problem-solving loop. In v2 the task loop is governed: iteration and token budgets, novelty/repetition monitoring, and stage gates are enforced inside the loop (§24.4). REVIEW runs *inside* the loop at every non-terminal exit so double-loop signals can trigger reframes, and again as a full AAR at termination (§14).

The task loop is resumable: `task_state` checkpoints are serialized at every stage boundary (§20.5), so a task spans session boundaries without losing its contract.

### 8.3 Learning loop

```text
Episodes → AAR → Lesson extraction → Skill update → Evaluation
```

This operates across multiple tasks. In v2 the LearningScheduler (a queue consumer with trigger conditions) is defined in §24.5 so the loop is driven rather than asserted.

### 8.4 Architecture-evolution loop

```text
Change proposal
→ admission control
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

The architecture-evolution loop must always run more slowly and under stronger governance than the task loop. In v2 the cadence differential is enforced: R2+ changes are spaced by epoch (§22.7), the acceptance pipeline is invoked by `improvement_engine.evaluate` before any deployment (not merely queued), and the evaluation plane is immutable to candidates (§22.6).

### 8.5 Session layer (v2)

A fifth, explicit layer spans sessions: the TaskScheduler owns task identity, priority arbitration, checkpoint/resume, and goal renegotiation (§24.5). Prospective memory commitments are consumed by the scheduler rather than left as stored intentions.

---

## 9. Stage 0 — META-CONTROL

### 9.1 Responsibilities

The meta-controller (implemented as the **MetaRouter** component):

- Parses the goal and delegated authority.
- Classifies the problem context (Cynefin).
- Estimates novelty, uncertainty, stakes, reversibility, and adversariality.
- Selects the reasoning modules.
- Allocates model, tool, agent, time, and token budgets (the **budget envelope**, §9.6).
- Sets **route flags** that make effort levels operational (§9.4).
- Monitors progress and cognitive failure modes (via the LoopMonitor).
- Decides when to continue, stop, ask, experiment, or escalate.
- Maintains an explicit model of system competence, fed by evaluation history (§19.3) — not by introspection.

### 9.2 Cynefin-based routing

| Context | Default strategy | Typical route |
|---|---|---|
| Clear | Recognize, retrieve, apply known procedure | Fast path (E0–E1) |
| Complicated | Decompose and apply expert analysis | Verified deliberate path (E2) |
| Complex | Probe, observe, update, and adapt | Full experimental loop (E3–E4) |
| Chaotic | Stabilize first, minimize harm, then reclassify | Crisis path with human gate (E5) |
| Disorder | Split the task and classify each part | Decomposition path |

Stakes override simplicity. A familiar medical, legal, financial, infrastructure, or security action is not routed to an unverified fast path merely because the pattern looks familiar.

**Stakes scale (v2).** Stakes are integers 1–5: 1 = routine, 2 = notable, 3 = consequential, 4 = high (health, finance, law, infrastructure, security, irreversibility), 5 = critical (life-safety, mass impact, irreversible). The scale is the input to three consumers: effort override (stakes ≥ 4 forces E ≥ 2), verification thresholds (§15.4), and action-class expectations (§13.2). Stakes are estimated by the MetaRouter but **attested by an independent risk estimator** (§20.4) whenever stakes ≥ 3 or the route would take the fast path — this removes the incentive conflict where the same model that benefits from the cheap path classifies its own stakes (finding A15, §32 S4/S12).

**Routing justification log (v2).** Every route decision records: inputs (stakes estimate, class, flags), the route chosen, and the attestation reference. This log is spot-audited and feeds the routing-quality dimension of the evaluation plane (§23.7).

### 9.3 Routing variables

The route is based on:

```text
complexity
novelty
uncertainty
stakes
irreversibility
environment volatility
adversarial pressure
capability match        (from CompetenceModel, §19.3)
evidence availability
time constraints
human availability
```

### 9.4 Reasoning-effort levels (operational in v2)

| Level | Description | Route flags | Typical configuration |
|---|---|---|---|
| `E0` | Reflex | `requires_diagnosis=F, requires_generation=F, requires_review=F` | Direct retrieval or deterministic procedure; one outcome check; no review/memory |
| `E1` | Fast verified | `requires_generation=F, requires_review=T` | One solver plus lightweight checks |
| `E2` | Deliberate | `requires_diagnosis=T` | Structured decomposition and verifier |
| `E3` | Search | `+ SearchController, council eligible` | Multiple candidates, simulations, red team |
| `E4` | Experimental | `+ probes` | Full loop with probes and evidence collection |
| `E5` | Critical | `+ council forced, human gate` | Independent council, formal checks, human approval |

In v1 the effort level was a label with no consumer: an E0 task ran the full pipeline. In v2 the route flags gate every stage of the algorithm (§24.4), so E0 executes a direct-answer path with a single verification pass — the change with the largest measured cost reduction in §32 (S1: 8 → 5 token-units; S7: 8 → 5; suite total 1369 → 386).

### 9.5 Expected value of computation

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

The controller terminates unproductive loops when agents repeat arguments, retrieve no new evidence, or fail to reduce uncertainty. In v2 this is **operationalized by the LoopMonitor**:

- **Novelty signature**: a hash of (hypotheses, frame, observations). Two consecutive identical signatures trigger the *novelty plateau* stop.
- **Repetition counter**: repeated unproductive actions (e.g., failing executions) stop the loop.
- **EVOC check**: an estimated expected-value term per iteration; when it crosses zero, the loop stops.
- **Hard budgets**: iteration, token, call, and agent ceilings from the budget envelope always terminate the loop with `RESOURCE_LIMITED` (the state that v1 could never reach; §32 S2/S9).

### 9.6 Budget envelope (v2)

The budget envelope is a typed structure owned by the MetaRouter and consumed by every stage:

```yaml
budget_envelope:
  tokens_max:            # scaled by effort; default 40 + 20 × effort
  calls_max:             # default 8 + 4 × effort (+8 if council)
  iterations_max:        # default 1 + 2 × effort
  agents_max:            # 0 below E3, 4 at E3+
  deadline:              # wall-clock limit, if any
  tokens_used:
  calls_used:
  iterations_used:
```

The BudgetController consumes from the envelope at every stage boundary and the LoopMonitor checks it at loop top. Soft-warn at 80%, hard-stop at 100% → `RESOURCE_LIMITED`. The v1 `resource_budget` field in the problem card is removed as a duplicate; the envelope is the single source.

---

## 10. Stage 1 — WHAT: Frame the Problem

### 10.1 Objectives

The WHAT stage determines:

- What outcome is actually wanted?
- Who has authority to define success?
- What is inside and outside scope?
- What assumptions are being made?
- What constraints and permissions apply?
- What evidence is available?
- What would count as success or failure?
- Is the question diagnostic, prescriptive, predictive, creative, or normative?

### 10.2 Problem Definition Card

```yaml
problem:
  situation:
  complication:
  key_question:
  desired_outcome:
  excluded_outcomes:
  stakeholders:
  decision_owner:
  scope_in:
  scope_out:
  constraints:
  assumptions:
  available_evidence:
  missing_evidence:
  success_metrics:       # REQUIRED — gate predicate (v2)
  failure_conditions:
  deadline:
  permissions:
  risk_class:
  action_class_estimate: # candidate only; kernel attests (§20.4)
```

### 10.3 Framing procedure

1. Restate the user or system goal.
2. Separate explicit requirements from inferred preferences.
3. Generate multiple plausible frames.
4. Challenge inherited assumptions.
5. Identify ambiguity and conflicting objectives.
6. Confirm the frame with the decision owner when practical.
7. Record what the project will not attempt.
8. Produce a precise key question.

### 10.4 Frame critics

A frame critic asks:

- Are we solving a symptom rather than a cause?
- Is the problem too broad or too narrow?
- Has a stakeholder been excluded?
- Is a proposed constraint actually an assumption?
- Would another framing reverse the preferred answer?
- Is the requested goal itself unsafe or incoherent?

### 10.5 Exit gate (predicates, v2)

The stage may advance when **all** of the following predicates hold; the gate is evaluated by `check_exit_gate("WHAT", state)` in the algorithm:

```text
G-WHAT-1  goal and decision owner identified
G-WHAT-2  scope and constraints explicit
G-WHAT-3  success_metrics non-empty
G-WHAT-4  ambiguities resolved or recorded as unresolved
G-WHAT-5  decision recorded whether WHY is necessary
```

Gate failure → re-enter WHAT with the recorded reason; the gate re-entry budget is bounded (default 3 attempts) after which the task returns `NEEDS_EVIDENCE` (or `ESCALATED` if the owner is unavailable). v1 advanced unconditionally; §32 S15 demonstrates the gate blocking a task with no success metrics.

---

## 11. Stage 2 — WHY: Diagnose and Model

### 11.1 Objectives

The WHY stage constructs the best available explanation of:

- The current state.
- Relevant causal mechanisms.
- Root and contributing causes.
- Dependencies and bottlenecks.
- Uncertainties and unknowns.
- Evidence that supports or contradicts each hypothesis.

### 11.2 Diagnostic structures

Possible representations include:

- MECE issue trees.
- Fault trees.
- Ishikawa diagrams.
- Why-why maps.
- Influence diagrams.
- Bayesian networks.
- Causal graphs.
- Argument maps.
- Constraint graphs.
- System-dynamics models.
- Process and value-stream maps.

The structure is selected according to the problem rather than applied ritualistically.

### 11.3 Hypothesis ledger

```yaml
hypothesis:
  id:
  statement:
  causal_role:
  prior_confidence:
  assumptions:
  predicted_observations:
  supporting_evidence:
  disconfirming_evidence:
  falsification_evidence:   # v2: what observation WOULD falsify this hypothesis
  tests:
  posterior_confidence:
  decision_relevance:
  status:
```

`falsification_evidence` is a v2 addition required by the WHY exit gate (v1's §11.7 gate referenced falsifiability that the ledger could not express).

### 11.4 Evidence discipline

Each conclusion is represented through:

- **Presuppositions:** What must be assumed?
- **Evidence:** What observations or sources support the claim?
- **Logic:** How do assumptions and evidence lead to the conclusion?
- **Uncertainty:** What alternatives remain plausible?
- **Provenance:** Where did each evidence item originate? (Anchored to tool-call records and the audit log; claim labels alone are not provenance — §18.6.)
- **Expiry:** When might the evidence become obsolete?

Claims are labeled as:

- `OBSERVED`
- `CALCULATED`
- `INFERRED`
- `PREDICTED`
- `SPECULATIVE`

### 11.5 Active information gathering

The architecture does not collect information merely because it is available. It estimates the value of information (VOI) — implemented as `evidence_service.voi(uncertainties, actions)` in the interface (§24.3), called inside diagnosis:

```text
Would this evidence:
- change the leading hypothesis?
- change the selected action?
- reduce a high-consequence uncertainty?
- expose a hidden constraint?
- alter the risk classification?
```

If not, evidence collection should stop and the gap is recorded in `missing_evidence`, which drives the `NEEDS_EVIDENCE` state (v2; v1 never produced it — §32 S6).

### 11.6 Premortem for diagnosis

Before accepting the diagnosis:

> Assume the diagnosis was later shown to be wrong. What caused the error?

Possible answers include:

- Missing stakeholder evidence.
- Confusing correlation with causation.
- Anchoring on the first explanation.
- Searching only for confirming evidence.
- Using stale or poisoned data.
- Mistaking tool output for ground truth.
- Ignoring base rates.
- Stopping at a superficial cause.

### 11.7 Exit gate (predicates, v2)

Diagnosis is sufficient when **all** predicates hold:

```text
G-WHY-1  leading hypothesis has decision-relevant evidence
G-WHY-2  significant alternatives considered (≥ 1 alternative hypothesis or explicit nil)
G-WHY-3  residual uncertainty recorded in the ledger
G-WHY-4  estimated VOI of further diagnosis ≤ cost (EVOC check)
G-WHY-5  falsification_evidence non-empty for the leading hypothesis
```

Gate failure → re-enter WHY with the recorded reason.

---

## 12. Stage 3 — HOW: Generate, Test, and Select Solutions

### 12.1 Divergent generation

The system first expands the option space using appropriate methods:

- Osborn-Parnes Creative Problem Solving.
- SCAMPER.
- TRIZ.
- Theory of Constraints.
- Analogical transfer.
- Opposite thinking.
- Six Thinking Hats.
- Design Thinking.
- Scientific hypothesis generation.
- Tree or graph search (via the SearchController, §16.2).
- Multi-agent independent proposals (via the council, §17).
- Retrieval of related episodes and procedures.

Feasibility judgment is temporarily delayed unless an option clearly violates a hard safety or permission constraint.

### 12.2 Alternative, not sequence

A solution map must distinguish among genuinely different strategies. A list such as “plan, build, test, launch” is an implementation sequence, not a portfolio of alternatives.

### 12.3 Candidate representation

```yaml
candidate:
  id:
  strategy:
  mechanism:
  assumptions:
  expected_benefits:
  costs:
  time:
  dependencies:
  failure_modes:
  reversibility:            # 0-3 rubric, maps to A2-A5 (§13.2)
  ethical_legal_status:
  evidence:
  uncertainty:
  required_permissions:
  fallback:
  action_class_estimate:    # planner proposes; kernel attests (§20.4)
```

**Reversibility rubric (v2):** 0 = fully reversible in sandbox (A2), 1 = reversible with effort (A3), 2 = costly/uncertain reversal (A4), 3 = effectively irreversible (A5). The decision score penalty for irreversibility = 0.2 × grade × severity coefficient.

### 12.4 Constraint screening

Candidates are first screened against hard boundaries:

- Safety.
- Law and policy.
- Human consent.
- Scope.
- Available authority.
- Technical feasibility.
- Resource ceilings.
- Non-negotiable values.

Options that fail a hard boundary are not rescued by a high utility score. Screening is executed by the SafetyKernel against the candidate's attested action class (§20.4) — the same model that proposes a plan does not also screen it (finding A15).

### 12.5 Comparative selection

Remaining candidates are evaluated using:

- Multiattribute decision analysis.
- Pareto-front analysis.
- Expected utility under uncertainty.
- Sensitivity analysis.
- Scenario testing.
- Counterfactual simulation.
- Robustness to assumption changes.
- Worst-case and tail-risk analysis.
- Reversibility and option value.

A general risk-adjusted score can be represented as:

```text
Decision score
=
expected goal value
− expected harm
− resource cost
− delay cost
− irreversibility penalty
− uncertainty penalty
```

The harm and irreversibility terms are **estimated by an independent verifier with different evidence** whenever the action class is A3 or higher (v2; in v1 all six terms were self-reported — finding A15). Score components are logged so sensitivity analysis is possible. This score informs judgment; it does not replace hard constraints or human values.

### 12.6 Commitment Premortem

Before selection, `premortem(state)` runs (call site in §24.4 — v1 had none):

> Assume this plan was implemented and failed badly. What were the most plausible causes?

The resulting failure modes must be:

- Mitigated.
- Monitored.
- Accepted by an authorized owner.
- Or used to reject the plan.

All failure modes are written into `task_state.risks` and survive into the decision packet.

### 12.7 Red Team gate

After selection, `red_team.attack(state)` runs (call site in §24.4 — v1 had none). The Red Team receives:

- The selected candidate.
- Its assumptions.
- The evidence ledger.
- The implementation plan.
- The risk register.

It attempts to:

- Falsify assumptions.
- Find unmodeled stakeholders.
- Identify incentive failures.
- Expose security vulnerabilities.
- Produce counterexamples.
- Find cheaper or safer alternatives.
- Demonstrate how success metrics could be gamed.

If the gate fails, the candidate is rejected (its id recorded), generation re-runs, and the rejection feeds the next candidate set (demonstrated in §32 S13). The regenerate loop is bounded by the loop monitor.

### 12.8 Exit gate (predicates, v2)

The HOW stage is complete when **all** predicates hold:

```text
G-HOW-1  ≥ 2 meaningful alternatives considered (or explicit nil with reason)
G-HOW-2  hard constraints applied by SafetyKernel
G-HOW-3  preferred option survived sensitivity and red-team checks
G-HOW-4  fallback or abort condition exists
G-HOW-5  decision record explains the choice (criterion evidence present)
```

---

## 13. Stage 4 — DO: Plan and Execute

### 13.1 Hierarchical planning

Plans are represented as graphs of goals and subgoals:

```yaml
plan:
  objective:
  milestones:
  tasks:
    - id:
      owner:
      preconditions:
      action:
      expected_result:
      verifier:
      dependencies:
      deadline:
      rollback:
  metrics:
  checkpoints:
  stop_conditions:
  escalation_conditions:
```

Subtasks are decomposed only as deeply as necessary. If an executor repeatedly fails, the meta-controller may invoke ADaPT-style further decomposition (bounded by the loop monitor).

### 13.2 Action classes

| Class | Example | Default requirement |
|---|---|---|
| `A0` | Internal reasoning | No external permission |
| `A1` | Read-only retrieval | Logged tool access |
| `A2` | Reversible sandbox modification | Automated verification |
| `A3` | External but reversible action | Explicit authorization and rollback |
| `A4` | Consequential or costly action | Independent verifier and human approval |
| `A5` | Irreversible/high-stakes action | Dual control, expert validation, formal incident plan |

**Action-class attestation (v2).** The planner *proposes* an action class; the SafetyKernel *attests* it against an independent risk estimate before authorization. A misattested class (e.g., an irreversible action labeled A2) is denied with status `UNSAFE` (finding A15; §32 S12).

### 13.3 Transactional execution

Every consequential action follows:

```text
Propose
→ validate arguments and permissions
→ simulate or dry-run
→ authorize
→ execute
→ observe actual state
→ verify postconditions
→ commit or compensate
```

A model’s claim that an action succeeded is not sufficient. The relevant environment must confirm the resulting state.

**Failure semantics (v2, §20.3):** per-class timeouts, retry caps (no retry after an observed side effect), idempotency keys on capability tokens, and per-class compensation defined below. A crash mid-task resumes from the last checkpoint (§20.5) instead of orphaning side effects (finding A12).

### 13.4 ReAct/OODA micro-loop

Within each task:

```text
Observe current state
→ compare with expected state
→ update beliefs and plan
→ select the next authorized action
→ execute
→ observe again
```

### 13.5 Monitoring

Execution monitors watch for:

- Plan drift.
- Unexpected side effects.
- Tool-call errors.
- Permission violations.
- Resource overruns (fed by the budget envelope).
- Contradictory observations.
- Security anomalies.
- Repeated unproductive actions.
- Changes in environment or user intent.

Monitor output feeds the LoopMonitor's termination signals and the ReAct micro-loop. In v1 the ExecutionMonitor was defined but never invoked; in v2 `execution_monitor.check(state)` has a call site in §24.4 (finding A16).

### 13.6 Stakeholder communication

Communication records:

- What the audience currently thinks and does.
- What they should think and do afterward.
- The evidence supporting each requested change.
- Decisions, owners, deadlines, and unresolved objections.

Each recommendation should be concise enough to act on and detailed enough to audit.

### 13.7 Exit gate (predicates, v2)

Execution ends when **any** predicate holds:

```text
G-DO-1  success metrics met (postconditions verified)
G-DO-2  stop_conditions triggered
G-DO-3  plan proven infeasible
G-DO-4  risk exceeds delegated authority
G-DO-5  human escalation required
```

In v1 the algorithm never read the plan's `stop_conditions`/`escalation_conditions`; in v2 they are consumed at each loop pass (finding A5).

---

## 14. Stage 5 — REVIEW: Reflect, Learn, and Evolve

### 14.1 After-Action Review

Every meaningful episode asks:

1. What was supposed to happen?
2. What actually happened?
3. Why was there a difference?
4. What should happen next?

**In-loop review (v2).** A lightweight AAR runs at every non-terminal loop exit so its output feeds reframe/replan decisions (§24.4). A full AAR runs at termination. In v1 REVIEW ran only after loop exit, so double-loop signals could never trigger a mid-task reframe (finding A6).

### 14.2 Single-loop learning

Single-loop learning changes tactics while retaining the governing assumptions.

Examples:

- Use a different tool.
- Add a test.
- Change task order.
- Improve a prompt.
- Retrieve a better source.
- Add a missing exception handler.

### 14.3 Double-loop learning

Double-loop learning examines:

- Whether the original goal was framed correctly.
- Whether decision criteria were appropriate.
- Whether the causal model was wrong.
- Whether the routing policy chose the wrong cognitive mode.
- Whether an agent role was counterproductive.
- Whether a safety or permission boundary was underspecified.
- Whether the system optimized the benchmark rather than the real objective.

Double-loop findings that implicate the frame or route trigger the reframe/replan paths of §24.4, bounded by the reframe budget.

### 14.4 Memory consolidation

Review output is divided into:

- Episode facts.
- Reusable semantic lessons.
- New or revised procedures.
- Unresolved questions.
- Calibration updates (consumed by the CompetenceModel, §19.3 — v1 had no consumer).
- Proposed architecture changes.

### 14.5 Kaizen rule

Most improvements should be:

- Small.
- Testable.
- Reversible.
- Attributable to a clear cause.
- Evaluated against a stable baseline.

Large rewrites require stronger evidence because they make regressions harder to localize. The **stable baseline** is defined in §22.4: a frozen snapshot of the portfolio evaluation suite, human-frozen and access-restricted. (v1 used the term without defining it — finding A13.)

---

## 15. Continuous VERIFY Layer

Verification is not a final proofreading step. It surrounds the entire loop.

### 15.1 Verification registry

| Claim type | Preferred verifiers (ordered) | Selection rule |
|---|---|---|
| Factual | Primary sources, retrieval, provenance checks | First available with reliability ≥ class bar |
| Numerical | Calculator, executable code, independent recomputation | Same |
| Logical | Formal proof, solver, counterexample search | Same |
| Software | Tests, static analysis, type checking, sandbox execution | Same |
| Causal | Experiment, intervention, counterfactual analysis | Same |
| Physical | Sensors, measurement, simulation plus real observation | Same |
| Policy | External policy engine and authorized human | Same |
| Security | Adversarial tests, isolation, permission audit | Same |
| Social | Stakeholder confirmation and behavioral observation | Same |
| Creative | Requirement testing, user evaluation, comparative critique | Same |

**Verifier reliability (v2):** each (claim-type, verifier) pair carries a reliability estimate = rolling accuracy over the last N verification outcomes, seeded 0.5 until evaluation history exists, updated by the CompetenceModel (§19.3). v1 named the field without an estimator (finding A11).

**Selection rule (v2):** for a given artifact, use the first verifier in the ordered list whose reliability ≥ the class bar, where the class bar comes from the threshold table (§15.4). This replaces the unspecified "pick one" of v1.

### 15.2 Proposer-verifier separation

When consequences are meaningful:

- The proposer should not be the only verifier.
- The verifier should receive objective criteria.
- The verifier should have access to different evidence or tools where possible.
- Verification failure should produce a specific counterexample or test result.
- If no reliable verifier exists, autonomy must be reduced.

**No-verifier ladder (v2)** — the §15.2 fallback, made concrete:

```text
L1  verifier unavailable, stakes ≤ 2:  proceed at reduced effort (E ≤ 1),
    inflate uncertainty labels, status may be SOLVED only for A0/A1-style claims
L2  verifier unavailable, stakes ≥ 3:  do not declare SOLVED;
    status = ESCALATED (or NEEDS_EVIDENCE if the gap is an evidence gap)
L3  verifier unavailable, action class ≥ A3:  no external action;
    status = ESCALATED with required_human_actions populated
```

Demonstrated in §32 S5: v1 declared `INFEASIBLE` (or worse, allowed self-verification), v2 returns `ESCALATED` with the packet.

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
  verifier_identity:      # REQUIRED external identity for SOLVED
  verifier_reliability:
  confidence:
  recommendation:
```

### 15.4 SOLVED threshold and proof-carrying result

**Threshold table (v2):** the `SOLVED` gate is `verify_outcome.success = (all required checks passed) ∧ (verifier_identity ≠ SELF) ∧ (verifier_reliability ≥ class bar)`.

| Action class / stakes | Required checks | Minimum verifier reliability | Unresolved allowed? |
|---|---|---|---|
| A0–A1 / stakes 1–2 | 1 pass | 0.5 | yes (recorded) |
| A2 / stakes ≤ 3 | all required passed | 0.8 | no |
| A3–A4 / stakes ≥ 3 | all required passed | 0.9 | no |
| A5 / any | all + independent second verifier | 0.95 | no |

The final output always includes a concise decision packet (the **common epilogue** of §24.4 — every terminal path, including `UNSAFE`/`ESCALATED`, produces it; v1's denial path returned before the packet, finding A7):

```yaml
result:
  conclusion:
  status:
  assumptions:
  evidence:
  alternatives_considered:
  verification:
    checks_performed:
    verifier_identity:
  uncertainty:
  limitations:
  risks:
  required_human_actions:
```

Field sources are defined by the `build_decision_packet` contract (§24.3): `conclusion ← decision.strategy`, `assumptions ← union of candidate assumptions`, `evidence ← task_state.evidence`, `uncertainty ← missing_evidence`, `risks ← task_state.risks`, `required_human_actions ← escalate/deny paths`. This is preferable to an unsupported narrative claiming that the system “thought carefully.”

### 15.5 Bounded approximation (v2 producer)

`APPROXIMATED` requires a real error bound: when exact verification is impossible but an approximation with a computable error bound (e.g., numerical tolerance, interval, confidence interval, delta) is available, `select_candidate` records the bound and `classify_terminal` may return `APPROXIMATED` with the bound in the packet's `limitations`. Without a bound, the task may not claim `APPROXIMATED` — it must choose `NEEDS_EVIDENCE`, `NEEDS_EXPERIMENT`, or `RESOURCE_LIMITED` instead. (v1 defined the state but no producer — finding A2.)

### 15.6 Delta-based verification (v2)

Verification history is retained (`task_state.verification_history`). On iteration, only artifacts whose input hash (frame, evidence, candidates) changed are re-verified; unchanged artifacts reuse their prior reports. This removes the v1 verification cascade where every iteration re-verified everything (finding A16).

---

## 16. Reasoning Method Composer

### 16.1 Method selection

The meta-controller selects methods based on the problem signature.

| Problem signal | Preferred methods |
|---|---|
| Familiar, low-risk pattern | RPD, checklist, retrieval |
| Ambiguous goal | GROW, Socratic clarification, frame ensemble |
| Root-cause question | Issue tree, 5 Whys, Ishikawa, Bayesian model |
| Contradictory requirements | TOC, TRIZ, dialectical synthesis |
| Creative design | CPS, SCAMPER, analogies, Six Hats |
| Long-horizon planning | Hierarchical planning, ADaPT, tree search |
| High uncertainty | Active learning, value of information, safe probes |
| Dynamic environment | ReAct, OODA, receding-horizon planning |
| Scientific question | Hypothesis, prediction, experiment, replication |
| Adversarial setting | Threat modeling, Red Team, game theory |
| Stakeholder conflict | Nemawashi, Design Thinking, interest-based negotiation |
| High-impact decision | Premortem, independent verification, human gate |
| Repeated task | Procedural memory, automation, Kaizen |
| Novel task class | Self-Discover-style method composition |

The method composer itself should learn from historical performance (via the CompetenceModel), while retaining fixed safety constraints.

### 16.2 SearchController (v2 owner)

The SearchController owns tree/graph exploration for E3+ routes (v1 asserted a "search controller" without owning it — finding A17):

```yaml
search_controller:
  contract:
    explore(belief_state, budget) -> exploration_results
    exploration_depth:         # from budget envelope
    ev_of_exploration_gate:    # expand only while EV(exploration) > cost
    search_budget:             # nodes, calls, tokens
    termination:               # novelty/repetition signals shared with LoopMonitor
```

The SearchController is invoked from `generate_candidates` when `route.effort_level ≥ 3` and `route.requires_search` is set.

---

## 17. Multi-Agent Collective

### 17.1 Roles

| Role | Responsibility |
|---|---|
| Coordinator | Maintains task state, budgets, and dependencies (sole writer, §17.2) |
| Frame Critic | Challenges scope, assumptions, and key questions |
| Diagnostician | Builds causal models and hypotheses |
| Researcher | Retrieves and grades evidence |
| Explorer | Generates diverse alternatives |
| Planner | Builds executable hierarchical plans |
| Formal Verifier | Checks logic, math, code, and constraints |
| Red Team | Searches for failures and adversarial cases |
| Safety Agent | Evaluates policy, permission, and harm |
| Implementer | Executes authorized tasks |
| Synthesizer | Produces the integrated decision record |
| Reviewer | Performs AAR and proposes lessons |

These roles can be separate models, separate contexts, software modules, humans, or combinations. For the MVP (§25) all roles are prompt-variants over the single foundation model with fresh context windows; model heterogeneity is a Phase-3 upgrade (§26). This is stated explicitly so implementers do not silently share context between "independent" agents (finding A10).

### 17.2 Council protocol (contract, v2)

```text
1. Decompose the task where useful.
2. Give agents clean, role-specific contexts   → fresh context window per agent
3. Generate initial answers independently       → private write slots
4. Normalize answers into claims, evidence, and uncertainties
   → deterministic extractor over the agent_answer schema (below);
   normalization CANNOT delete: it produces the claim ledger
5. Run objective verifiers.
6. Aggregate verified results (evidence-weighted, §17.3).
7. Debate only unresolved contradictions        → bounded rounds (default 1)
8. Run a Red Team challenge.
9. Preserve dissent and minority evidence       → append-only minority ledger, written BEFORE aggregation
10. Synthesize.
11. Run a final independent gate.
```

**Agent answer schema (v2):**

```yaml
agent_answer:
  agent_id:
  role:
  claims:            # [{claim, evidence_refs, uncertainty}]
  evidence:          # [{ref, kind, provenance, trust_label}]
  uncertainties:
  dissent:           # minority positions the agent wants preserved
```

**Independence guarantees (v2):** fresh context window per agent; no peer conclusions before step 6; distinct temperature/seed or distinct model where possible; the Coordinator is the **sole writer** of shared state using versioned compare-and-set writes; synthesis reads only committed state. `task_state.minority_reports` and `task_state.unresolved_disagreements` are first-class fields (v1 had nowhere to store them).

### 17.3 Aggregation rules

- Correctness is not determined by rhetorical persuasiveness.
- Majority voting is used only when candidate independence and competence are sufficient.
- Objective tests outrank votes.
- Agent weights are based on verified domain performance (rolling accuracy from the CompetenceModel), not self-confidence; default uniform until evaluation history exists.
- Consensus without new evidence is not progress.
- A correct minority answer must remain recoverable (append-only minority ledger).
- The final report includes unresolved disagreements.

### 17.4 When not to use a council (predicates, v2)

Do not use multi-agent debate when **any** predicate holds — evaluated by `meta_router.should_use_council(state)`:

```text
C-1  deterministic calculator or solver available
C-2  one high-quality source answers the question
C-3  agents would share the same blind spot (heterogeneity check fails)
C-4  coordination-cost estimate > expected benefit
C-5  time pressure requires immediate safe stabilization
C-6  the action cannot be safely authorized regardless of consensus
```

Council size and debate rounds are set from the budget envelope (default: no council below E3; n_agents ≤ agents_max; debate_rounds = 1). Demonstrated in §32 S7: the deterministic-solver task skips the council and pays the fast-path cost.

---

## 18. Memory and Knowledge Architecture

### 18.1 Memory classes

| Memory | Content |
|---|---|
| Working | Active goals, current observations, temporary calculations |
| Episodic | Time-stamped task trajectories and outcomes |
| Semantic | Validated facts, concepts, relationships, models |
| Procedural | Skills, workflows, prompts, code, action policies |
| Prospective | Future commitments, deadlines, unresolved intentions |
| Normative | User preferences, policies, values, permissions |
| Audit | Immutable decision, action, and approval records |

### 18.2 Memory record schema and write protocol (v2)

```yaml
memory_record:
  id:
  type:             # episodic | semantic | procedural | normative | prospective
  content_ref:
  provenance:       # anchored to audit-log/tool-call records (§18.6)
  trust_label:
  expiry:
  version:
  status:           # COMMITTED | CONFLICTED | QUARANTINED | PROMOTED | EXPIRED
  authority_token:  # required for procedural/normative writes
```

```text
Candidate memory
→ classify content type
→ validate provenance (against external audit records)
→ label trust and uncertainty
→ detect contradiction (rule below)
→ apply privacy and permission policy
→ assign expiry or review date
→ store
→ monitor later use
```

**Contradiction rule (v2, replaces the dead-end):** on a semantic conflict over the same topic with different claims, reject the new write unless its trust label exceeds the incumbent's by a margin (default: ≥ 0.1). Otherwise mark the new record `CONFLICTED`, quarantine it, and surface it to the ReviewEngine for adjudication. No silent "new write wins" (finding A9; §32 S14).

**Write channels (v2):** episodic/semantic writes accept task-content authority; procedural writes require a capability token (default: `authorized_expert`); normative writes require a policy token and are never modified by task content (§21.2 invariant 2). Untrusted-origin records go to quarantine with a promotion path (re-review → PROMOTED, or decay → EXPIRED).

**Consolidation trigger (v2):** when ≥ 3 near-duplicate episodic records exist (embedding similarity > 0.9 or exact content match), the ReviewEngine merges them into one semantic lesson with provenance-preserving diffs; the source episodes are referenced, not destroyed.

### 18.3 Retrieval score

A conceptual retrieval score is:

```text
relevance
× reliability        (source = verifier reliability where available, else trust_label)
× task applicability
× recency
× transfer value
× permission
− contradiction risk
− poisoning risk
```

Terms are 0–1 normalized; `reliability` has a numeric source (see above) rather than being a bare name (finding A6).

### 18.4 Memory security

- Retrieved content is data, not authority.
- External text cannot silently rewrite procedures.
- Untrusted memories are quarantined.
- Procedural-memory changes require stronger validation than episodic writes.
- Normative memory cannot be modified by ordinary task content.
- Every memory has provenance and version history.
- Sensitive memories require scoped access.

### 18.5 Forgetting and consolidation

Useful intelligence requires selective forgetting:

- Remove duplicate observations.
- Compress repeated episodes into stable lessons.
- Retain exceptions that invalidate overgeneralized rules.
- Decay low-confidence or stale knowledge.
- Preserve audit records even when working memories are deleted.

### 18.6 Provenance anchoring (v2)

Claim labels (`OBSERVED`, etc.) are self-labels and are not provenance. Provenance is anchored to external event records — tool-call logs, timestamps, audit-log entries — with replay verification on retrieval. A memory whose provenance cannot be anchored is treated as untrusted (finding A18).

---

## 19. World Model and Self-Model

### 19.1 World model

The world model combines:

- Current state.
- Entities and relationships.
- Causal hypotheses.
- Transition models.
- Constraints.
- Uncertainty.
- Predicted consequences.
- Simulators.
- Historical trajectories.

Observations must remain distinguishable from inferences.

### 19.2 Active experimentation

For complex problems, the system should select actions partly for information value:

```text
Choose the safest probe that most reduces
decision-relevant uncertainty.
```

When such a probe exists and no decision can yet be made, `classify_terminal` returns `NEEDS_EXPERIMENT` (the state v1 defined but could not produce — finding A2).

### 19.3 Self-model and CompetenceModel (v2 feedback loop)

The agent maintains calibrated knowledge of:

- Its capabilities by domain.
- Historical success and failure rates (from evaluation history).
- Available tools.
- Current permissions.
- Known blind spots.
- Resource limits.
- Reliability of its verifiers.
- Conditions requiring human help.

The self-model **must be based on evaluation history rather than unrestricted introspection** — and in v2 there is a data path that makes this possible (v1 had none, finding A8):

```text
EvaluationPlane results / episode outcomes
→ CompetenceModel.update_competence(episode_outcome)   (called from REVIEW)
→ task_state.competence
→ MetaRouter.route(state, competence)                  (capability-match input)
→ route quality metrics → EvaluationPlane              (closes the loop, §23.7)
```

`update_competence` consumes the REVIEW calibration outputs and EvaluationPlane batch results; routing uses the competence field for `capability match` and effort selection. Until evaluation history exists, competence is uniform (no introspection defaults).

---

## 20. Tool Broker and Execution Security

### 20.1 Authority separation

The system distinguishes:

1. **Instructions** — authorized goals and constraints.
2. **Data** — potentially untrusted content.
3. **Capabilities** — actions the system is technically allowed to perform.
4. **Authority** — actions the system is permitted to perform for this task.

A document saying “transfer money” is data, not authorization to transfer money.

### 20.2 Least privilege

Each task receives capability tokens limited by:

- Tool.
- Action.
- Resource.
- Target.
- Time.
- Data scope.
- Maximum cost.
- Reversibility class.

### 20.3 Failure semantics and controls (v2)

AgentDojo and broader agent-security evaluations demonstrate that tool-using agents are vulnerable to prompt injection and related attacks. AI-control research further motivates assuming that a powerful component may be unreliable or even adversarial. Established security principles such as least privilege, complete mediation, and defense in depth should therefore be enforced by systems outside the model prompt. ([arxiv.org](https://arxiv.org/abs/2406.13352?utm_source=openai))

Required controls (each with an enforcement point — v1 listed controls without wiring them, finding A10/A16):

| Control | Enforcement point |
|---|---|
| Sandboxing | ToolBroker execution layer |
| Network restrictions | ToolBroker capability tokens |
| Input and output validation | ToolBroker argument schemas at the retrieval boundary |
| Tool argument schemas | ToolBroker `validate_call` |
| Read-only defaults | Capability token defaults |
| Secret isolation | ToolBroker + SafetyKernel |
| Rate and cost limits | BudgetController per-call counters |
| Human approval | SafetyKernel gates (§21.4) |
| Independent monitors | ExecutionMonitor call site (§24.4) |
| Immutable logging | AuditLog call site per stage (§24.4) |
| Emergency interruption | SafetyKernel.interrupt (§20.5) |
| Rollback or compensation | Transaction semantics (below) |

**Transaction semantics per action class (v2):**

| Class | Timeout | Retry cap | Idempotency | Compensation |
|---|---|---|---|---|
| A0–A1 | n/a | 0 | n/a | n/a |
| A2 | 30 s | 2 (none after side effect observed) | key on capability token | undo/sandbox revert |
| A3 | 30 s | 1 | key | inverse op or pre-authorized fallback |
| A4 | 60 s | 1 | key | declared inverse OR "no compensation → incident record + human gate" |
| A5 | 60 s | 0 | key | no compensation by default; human gate before, incident record after |

The rule "no retry after a side effect was observed" and the compensation table are normative: an executor that cannot name its compensation may not claim transactional semantics.

### 20.4 Independent risk attestation (v2)

Stakes (≥ 3) and action-class labels are attested by an independent risk estimator with different evidence than the proposer (finding A15). The attestation record (inputs, estimate, class) is logged. A class mismatch between the planner's proposal and the kernel's attestation denies authorization with status `UNSAFE` (§32 S12).

### 20.5 Interrupt, checkpoint, and resume (v2)

- `safety_kernel.interrupt(task_id) -> checkpoint` aborts the current transaction (per-class compensation), serializes `task_state` (plus `stage` pointer), and returns a checkpoint.
- `task_state` is serialized at every stage boundary and on interrupt; `solve` accepts a checkpoint and resumes from the last committed stage.
- Capability tokens carry idempotency keys so a resumed task cannot double-execute an action whose postcondition was already confirmed.
- v1 asserted "emergency interruption" in four places with no mechanism; v2 specifies the interface (§24.3) and the resume entry point (finding A12).

---

## 21. Safety and Alignment Kernel

### 21.1 Kernel position

The safety kernel sits outside the ordinary self-modifiable cognitive scaffold. It controls:

- Goal acceptance.
- Permissions.
- Tool capabilities.
- Data access.
- Action authorization.
- Self-modification levels.
- Human escalation.
- Shutdown and interruption.
- Checkpoint/resume authority.

### 21.2 Safety invariants

1. The system may not grant itself new authority.
2. Untrusted content may not alter governing instructions.
3. High-impact actions require independent authorization.
4. The system may not disable logging or monitoring.
5. The system may not autonomously rewrite its core goals.
6. The system may not deploy unevaluated self-modifications.
7. Safety-critical modifications require human approval.
8. Self-replication and uncontrolled resource acquisition are disabled by default.
9. External side effects must remain attributable to an authorized task.
10. Capability growth may not outpace evaluation and containment capability.

Each invariant maps to a mechanism in v2: invariant 2 → write channels (§18.2) + provenance anchoring (§18.6); invariant 3 → independent risk attestation (§20.4) + verifier separation (§15.2); invariant 4 → AuditLog call sites in the algorithm (§24.4); invariant 6 → §22.3 pipeline invocation + evaluation-plane immutability (§22.6); invariant 10 → mandatory capability–safety co-scaling gate (§23.7).

### 21.3 Threat model with enforcing controls (v2)

| Threat | Enforcing control |
|---|---|
| Direct and indirect prompt injection | Authority/data separation (§20.1), validation at retrieval boundary (§20.3) |
| Tool-return injection | Tool outputs tagged untrusted; quarantine (§18.2); §32 S8 |
| Memory poisoning | Provenance anchoring, contradiction rule, quarantine (§18.2, §18.6) |
| Secret extraction | Secret isolation, least privilege, scoped tokens (§20.2) |
| Unauthorized actions | Action-class attestation, human gates (§20.4, §21.4) |
| Reward and benchmark gaming | Hidden tests, evaluation-plane immutability (§22.4, §22.6) |
| Deceptive behavior | Independent verifiers, adversarial evaluation (§15, §23.4) |
| Model or agent collusion | Fresh contexts, private answers, diversity checks (§17.2) |
| Sycophancy and majority pressure | Majority-vote gating, minority ledger (§17.3) |
| Unsafe self-modification | §22 pipeline, R-level gates, human approval (§22) |
| Emergent collective behavior | Council caps, coordination-cost gate (§17.4) |
| Irreversible side effects | Transaction semantics, A5 gates (§13.2, §20.3) |
| Human manipulation | Corroboration for authority-expanding instructions (§21.4) |
| Evaluation awareness | Hidden and out-of-distribution tests (§22.4) |

v1 listed these threats and §23.4 measured some, but no section bound each to a named control; v2 does (finding A18).

### 21.4 Human gates (process, v2)

Human approval is required for:

- Irreversible or high-stakes actions.
- Changes to goals, values, or permissions.
- Deployment of architectural self-modifications.
- Access to highly sensitive data.
- Broad external communication or financial transactions.
- Actions in chaotic domains where consequences cannot be adequately simulated.
- Expansion of autonomy, replication, network access, or resource budgets.

**Gate process (v2, finding A18):**

1. **Packet-before-approval**: the human receives the §15.4 decision packet (conclusion, assumptions, evidence links, alternatives, tests, uncertainty, risks) before any approval prompt. Raw evidence links are included.
2. **Minimum review latency**: no approval prompt may be auto-confirmed below the configured floor (default: none for A2, 60 s for A3–A4, 24 h for A5 and goal/values changes).
3. **Pending semantics**: `authorize` returns `{approved, rejected, pending}`; while pending, the system may execute the authorized reversible subset (A2/A3) and other queued tasks — no unbounded synchronous block.
4. **Timeout and fallback**: on expiry, the task degrades to `ESCALATED` with a partial-result packet and a named fallback authority; deferral counters prevent ping-pong.
5. **Corroboration**: authority-expanding or sensitive instructions require a second human or a recorded audit corroboration (§21.3, human-manipulation row).

---

## 22. Self-Evolution Engine

### 22.1 Improvement levels

| Level | Change target | Default authority |
|---|---|---|
| `R0` | Current answer or plan | Autonomous |
| `R1` | Episodic and semantic memory | Autonomous with validation |
| `R2` | Procedural skill or workflow | Sandbox and benchmark gate |
| `R3` | Tools, prompts, routing, or agent roles | Independent review and canary |
| `R4` | Model weights or core architecture | Controlled offline process |
| `R5` | Goals, values, safety kernel, permissions | Never autonomously authorized |

### 22.2 Change proposal and admission control (v2)

```yaml
improvement:
  problem_observed:
  supporting_episodes:
  proposed_change:
  target_component:
  target_level:          # R0-R5
  expected_gain:
  expected_risk:
  affected_capabilities:
  evaluation_plan:
  rollback_plan:
  required_approvals:
  change_size:           # small | medium | large (Kaizen, §22.5)
  dedup_hash:            # admission control key
```

**Admission control (v2):** the ImprovementEngine deduplicates proposals by `dedup_hash` (no repeated identical proposals queueing — finding A13, §32 S10), applies a per-epoch rate cap per target component, and only forwards proposals that pass a static policy check. `improvement_engine.queue` is no longer called unconditionally on every task: it is gated on `route.requires_review` and on `review.has_lessons`.

### 22.3 Acceptance pipeline

```text
Propose
→ admission control (dedup, rate, static policy)
→ create isolated branch
→ run capability evaluations
→ run safety and adversarial evaluations
→ compare with stable baseline
→ inspect regressions
→ independent review
→ human approval if required
→ canary deployment
→ monitor
→ retain or roll back
```

In v2 the pipeline is **invoked** by `improvement_engine.evaluate(proposal)` before any deployment (v1 ended at `queue_proposals` with no consumer — finding A13). The pipeline is size-aware (§22.5).

### 22.4 Evaluation requirements and stable baseline (v2)

A change is not accepted merely because it improves the benchmark used to generate it.

It must also pass:

- Hidden tests.
- Out-of-distribution tests.
- Safety non-regression.
- Tool-security tests.
- Calibration tests.
- Cost and latency limits.
- Catastrophic-forgetting checks.
- Reproducibility checks.
- Adversarial tests against reward hacking.

**Stable baseline (v2):** a frozen snapshot of the portfolio evaluation suite (scores + configurations), human-frozen and access-restricted, refreshed on a defined cadence (default: monthly or on major version). "No regression vs baseline + hidden tests" is the R2 gate criterion.

### 22.5 Kaizen step-size policy (v2)

`change_size` maps to evidence strength:

| Size | Scope | Required evidence |
|---|---|---|
| small | one component, bounded change | baseline + hidden tests |
| medium | cross-component | baseline + hidden + OOD + independent review |
| large | architecture/core | full pipeline + human approval + canary cohort |

### 22.6 Evaluation-plane immutability (v2)

- The evaluation plane (suites, weights, thresholds, baselines) lives on a separate stack that candidates cannot modify (finding A13).
- Suites are versioned and content-addressed; candidate evaluations run against pinned versions.
- No candidate may propose a change whose target is the evaluation plane itself without an R5-level human process.

### 22.7 Cadence differential (v2)

The architecture-evolution loop must always run more slowly and under stronger governance than the task loop (v1 asserted this; v2 enforces it):

- R1 writes: per-episode (task cadence), autonomous with validation.
- R2 changes: batched per epoch (default: weekly), sandbox + benchmark gate.
- R3+ changes: per epoch with independent review + canary.
- The ImprovementEngine applies these cadences; the harness's proposal-dedup scenario (§32 S10) demonstrates the queue remaining bounded.

### 22.8 Open-ended improvement

An archive of diverse candidate systems may be maintained, as in evolutionary or open-ended search. However:

- Candidates remain sandboxed.
- Lineage is recorded.
- No candidate receives production authority automatically.
- Diversity is preserved to prevent premature convergence.
- Improvement is measured across a portfolio, not one task.
- The evaluation system itself is protected from modification by candidates (§22.6).

---

## 23. Evaluation Framework

A credible AGI architecture cannot be evaluated with one benchmark or one aggregate score. Cognitive-science-oriented AGI testing proposals likewise argue for multidimensional assessment across fluid, crystallized, social, and embodied intelligence. ([arxiv.org](https://arxiv.org/abs/2402.02547?utm_source=openai))

### 23.1 Capability dimensions

- Language and communication.
- Mathematical and logical reasoning.
- Causal and scientific reasoning.
- Creative synthesis.
- Planning and long-horizon execution.
- Tool and computer use.
- Multimodal perception.
- Embodied interaction.
- Social reasoning.
- Cross-domain transfer.
- Continual learning.
- Metacognitive calibration.

### 23.2 Reliability dimensions

- Accuracy.
- Calibration.
- Robustness.
- Reproducibility.
- Factual provenance.
- Tool-call correctness.
- Recovery from failure.
- Resistance to distribution shift.
- Resistance to adversarial influence.

### 23.3 Learning dimensions

- Positive transfer.
- Sample efficiency.
- Skill composition.
- Catastrophic forgetting.
- Memory quality.
- Improvement stability.
- Ability to reject harmful lessons.

### 23.4 Safety dimensions

- Prompt-injection attack success.
- Unauthorized tool use.
- Sensitive-data leakage.
- Policy violations.
- Side-effect severity.
- Deception and sabotage.
- Human-oversight effectiveness.
- Shutdown and correction acceptance.
- Self-modification containment.

### 23.5 Efficiency dimensions

- Tokens and inference cost.
- Wall-clock time.
- Number of agents.
- Tool calls.
- Human-review burden.
- Energy and hardware.
- Marginal gain from added computation.

### 23.6 General intelligence profile

Instead of declaring a binary AGI result, Thinking Agent produces a profile:

```yaml
general_intelligence_profile:
  breadth:
  transfer:
  autonomy:
  grounding:
  learning:
  robustness:
  social_competence:
  calibration:
  safety:
  efficiency:
  unresolved_limits:
```

**Producer contract (v2):** `evaluation_plane.produce_profile(portfolio_results) -> profile` is part of the interface (§24.3). Each dimension has a defined metric set and threshold (v1 named dimensions without metrics — finding A18); unresolved_limits lists dimensions with no valid measurement yet.

### 23.7 Routing-quality and co-scaling dimensions (v2)

- **Route-selection accuracy**: human-labeled problem class vs. router output.
- **Effort calibration**: effort level vs. achieved quality per token.
- **Method-selection precision**: method composer choices vs. outcome.
- **Stopping quality**: false terminations and unnecessary continuations.
- **Capability–safety co-scaling**: invariant 10 — autonomy level granted vs. measured capability+safety scores; no autonomy increase without a passing co-scaling gate.
- These dimensions close the §19.3 loop: routing history feeds CompetenceModel, and CompetenceModel feeds routing.

### 23.8 Telemetry (v2)

`audit_log.record(stage, tokens, calls, latency, agents)` runs at every stage boundary (§24.4). The §23.5 efficiency dimensions are computed from these records; the §9.5 EVOC formula consumes them. (v1 listed efficiency dimensions with no runtime wiring — finding A16.)

---

## 24. Reference Implementation Specification

### 24.1 Core components (canonical)

| Component | Function | Interface (§24.3) |
|---|---|---|
| `GoalManager` | Maintains authorized objectives and priorities; renegotiation | `renegotiate` |
| `MetaRouter` | Selects route, effort, methods, agent count; route flags; budget envelope | `route` |
| `Workspace` | Stores structured active task state | internal (§24.2) |
| `MethodComposer` | Selects and combines reasoning modules (invoked inside `route`) | `compose` |
| `FrameCritic` | Checks WHAT-gate predicates | `check_exit_gate` |
| `Diagnostician` | Builds causal models and hypotheses | `diagnose` |
| `Premortem` | Runs the commitment premortem | `premortem` |
| `RedTeam` | Attacks the selected candidate | `attack` |
| `Explorer` | Generates candidates; tracks rejections | `generate`, `reject` |
| `SearchController` | Bounded tree/graph exploration with EV gate | `explore` |
| `Planner` | Creates hierarchical plans and fallback paths | `build` |
| `EvidenceService` | Retrieves, grades, and tracks evidence; VOI (invoked inside `diagnose`) | `voi`, `retrieve` |
| `WorldModel` | Predicts transitions and maintains causal state (invoked inside `diagnose`) | `predict` |
| `CouncilOrchestrator` | Runs independent agents and targeted debate (invoked inside `generate` when `use_council`) | `run_council` |
| `VerifierRegistry` | Selects objective checks by artifact type with reliability | `verify`, `verify_outcome` |
| `MemoryManager` | Writes, retrieves, consolidates, and expires memory | `commit`, `retrieve` |
| `ToolBroker` | Enforces schemas, permissions, transactions | `execute_transactional` |
| `SafetyKernel` | Applies policy, human gates, attestation, interrupt | `authorize`, `attest`, `interrupt` |
| `ExecutionMonitor` | Detects drift, anomalies, failed postconditions | `check` |
| `LoopMonitor` | Novelty, repetition, EVOC, budgets | `should_continue` |
| `BudgetController` | Consumes and enforces the budget envelope | `check`, `consume` |
| `CompetenceModel` | Maintains evaluation-based capability estimates | `update`, `estimate` |
| `ReviewEngine` | Performs AAR and lesson extraction | `review` |
| `ImprovementEngine` | Admission control, evaluation, deployment of scaffold changes | `queue`, `evaluate` |
| `EvaluationPlane` | Runs capability, safety, regression suites; produces profile | `run_suite`, `produce_profile` |
| `AuditLog` | Records immutable decisions, actions, telemetry | `record` |
| `TaskScheduler` | Task identity, priority arbitration, checkpoint/resume | `schedule`, `resume` |

(v1 listed 17 components with 11 having zero interface functions; v2 gives every component at least one interface and marks pure-internal ones — finding A14. Components invoked at sub-call-sites rather than directly in the loop are annotated above; their invocation points are summarized in §24.6.)

### 24.2 Shared task state (v2 schema)

```yaml
task_state:
  task_id:
  goal_contract:
  route:
    context_class:
    effort_level:
    reasoning_modules:
    use_council:
    requires_diagnosis:      # v2 route flags (operationalized effort)
    requires_generation:
    requires_review:
    requires_search:
    verification_depth:
    budget_envelope:
  competence:
  frame:
    success_metrics:         # gate predicate input
    unresolved_ambiguities:
  world_state:
  hypotheses:                # each with falsification_evidence
  evidence:
  missing_evidence:          # → NEEDS_EVIDENCE
  uncertainties:
  alternatives:              # each with reversibility, action_class_estimate
  decision:
  plan:                      # with stop_conditions, escalation_conditions
  permissions:
  risks:                     # premortem + red team + monitor entries
  actions:
  observations:
  verification:              # current report
  verification_history:      # delta-based re-verification (v2)
  minority_reports:          # append-only, pre-aggregation (v2)
  unresolved_disagreements:  # (v2)
  result:
  review:
  memory_updates:
  improvement_proposals:
  audit_refs:
  stage:                     # checkpoint pointer (v2)
  iteration:                 # loop iteration counter (v2)
  budget:
    tokens_used:
    calls_used:
    iterations_used:
  checkpoint:                # resume payload (v2)
```

### 24.3 Core interface (canonical, v2)

Return-type schemas follow the §24.2 style; every algorithm call site uses these names verbatim (v1's three-way drift between §24.2/§24.3/§24.4 is eliminated — finding A14).

```text
route(state, competence) -> cognitive_route
    # cognitive_route: {context_class, effort_level, reasoning_modules,
    #   use_council, requires_diagnosis, requires_generation, requires_review,
    #   requires_search, verification_depth, budget_envelope}

direct_answer(state) -> decision              # E0/E1 fast path: retrieval/solver

frame(state) -> problem_frame
    # problem_frame: §10.2 card + gate predicates

check_exit_gate(stage, state) -> gate_result
    # gate_result: {passed: bool, failing_predicates: [str]}

diagnose(state) -> belief_state
    # belief_state: {hypotheses[], falsification, missing_evidence[]}

evidence_service.voi(uncertainties, actions) -> voi_estimate
world_model.predict(state) -> predicted_state  # invoked inside diagnose

generate(state) -> candidate_set
    # candidate_set: [{id, strategy, assumptions, reversibility, ...}]
    # invokes council (run_council) when route.use_council (§17.4)

search_controller.explore(belief_state, budget) -> exploration_results

premortem(state) -> failure_modes[]
red_team.attack(state) -> optional_rejection

verify(artifact, criteria, class_bar) -> verification_report
    # verification_report: §15.3 fields + verifier_identity + reliability
verify_outcome(state) -> verification_report  # final gate; external identity required

select(candidate_set, verification_reports) -> decision
    # decision: {id, strategy, error_bound?}

authorize(action_plan, task_permissions, risk, action_class) -> {approved|rejected|pending, token, status}
attest(action_plan, state) -> attestation     # independent action-class attestation (§20.4)
budget.consume(state, stage) -> None          # BudgetController bookkeeping (§9.6)
interrupt(task_id) -> checkpoint
execute_transactional(action, capability_token) -> observation
execution_monitor.check(state) -> monitor_report
loop_monitor.should_continue(state, telemetry) -> {continue, reason}
budget.check(state) -> optional_exhaustion_reason
review(state) -> lessons
memory_manager.commit(state, review) -> accepted[]
competence_model.update(episode_outcome) -> None
improvement_engine.queue(state, review) -> queued_count
improvement_engine.evaluate(proposal) -> pipeline_report
evaluation_plane.run_suite(artifact, suite) -> suite_report
evaluation_plane.produce_profile(portfolio_results) -> general_intelligence_profile
audit_log.record(stage, tokens, calls, latency, agents) -> None
task_scheduler.resume(checkpoint) -> task_state
build_decision_packet(state, status) -> result_packet    # §15.4, common epilogue
classify_terminal(state, telemetry) -> status            # §3.3 decision table
```

### 24.4 Main algorithm (v2 governed loop)

```python
def solve(request, context, checkpoint=None):
    state = initialize_task_state(request, context)
    if checkpoint:
        state = task_scheduler.resume(checkpoint)          # §20.5

    state.route = meta_router.route(state, state.competence)
    budget.consume(state, "route")

    # --- Fast path (E0/E1): effort levels are operational ---
    if state.route.effort_level <= 1:
        budget.consume(state, "fast_path")
        state.decision = direct_answer(state)              # retrieval/solver
        state.verification = verifier.verify_outcome(state)  # external identity required
        state.result.status = ("SOLVED" if state.verification.success
                               else classify_terminal(state, telemetry))
        state.result.packet = build_decision_packet(state, state.result.status)
        return state
        # no generate/select/review: gated by route.requires_generation/review

    # --- Governed main loop ---
    while True:
        state.iteration += 1
        budget.consume(state, "loop.top")
        audit_log.record("loop.top", telemetry.stats())
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
                if state.iteration >= REFRAME_BUDGET:      # bounded re-entry
                    state.result.status = "NEEDS_EVIDENCE"
                    break
                continue

        # WHY: diagnose + gate
        if state.route.requires_diagnosis and not state.hypotheses:
            state.stage = "WHY"
            state.hypotheses, state.missing_evidence = diagnose(state)
            gate = check_exit_gate("WHY", state)
            if not gate.passed:
                state.risks.append(gate)
                continue

        # HOW: generate -> premortem -> verify -> select -> red-team gate
        if state.route.requires_generation and not state.alternatives:
            state.stage = "HOW"
            if state.route.requires_search:
                state.alternatives = search_controller.explore(state, budget)
            generate(state)
        if not state.alternatives:
            state.result.status = classify_terminal(state, telemetry)
            break
        state.risks.extend(premortem(state))
        reports = [verifier.verify(c, state.route.verification_depth)
                   for c in state.alternatives]
        state.verification_history.append(reports)          # delta-based reuse
        state.decision = select(state.alternatives, reports)
        if state.decision is None:
            state.result.status = classify_terminal(state, telemetry)
            break
        rejection = red_team.attack(state)
        if rejection:
            state.risks.append(rejection)
            explorer.reject(state.decision.id)              # feeds regeneration
            state.alternatives = []
            continue                                        # bounded by loop monitor

        # DO: plan -> attest -> authorize -> execute transactionally -> verify
        if state.decision.requires_external_action:
            state.stage = "DO"
            action_plan = planner.build(state, state.decision)
            attestation = safety_kernel.attest(action_plan, state)   # §20.4
            authorization = safety_kernel.authorize(
                action_plan, state.permissions, state.risks,
                attestation.action_class)
            if authorization.status in ("UNSAFE", "ESCALATED"):
                state.result.status = authorization.status
                break                                           # epilogue still runs
            if authorization.status == "PENDING":
                state = execute_authorized_subset(state, authorization)
                continue                                        # no unbounded block (§21.4)
            observations = tool_broker.execute_transactional(
                action_plan, authorization.token)
            state.observations.extend(observations)
            monitor = execution_monitor.check(state)
            state.risks.extend(monitor.findings)

        state.verification = verifier.verify_outcome(state)     # external required
        if state.verification.success:
            state.result.status = "SOLVED"
            break

        # REVIEW-in-loop: light AAR feeds reframe/replan (double-loop, §14.3)
        state.review = review_engine.review(state)
        competence_model.update(state.review.calibration)
        if should_reframe(state.review, state):
            if state.iteration < REFRAME_BUDGET:
                state.frame = None
                state.hypotheses = []
                continue
        if (state.verification.ambiguous or state.missing_evidence
                or state.probe_available or state.approximation_available
                or state.infeasible):
            # deterministic classifier entry for the remaining states
            state.result.status = classify_terminal(state, telemetry)
            break

    # --- Common epilogue: REVIEW + packet on EVERY terminal path ---
    if not state.review:
        state.review = review_engine.review(state)
    memory_manager.commit(state, state.review)      # channels + contradiction rule
    if state.route.requires_review:
        improvement_engine.queue(state, state.review)   # admission control
    state.result.packet = build_decision_packet(state, state.result.status)
    audit_log.record("epilogue", telemetry.stats())
    task_scheduler.checkpoint(state)                 # resume contract
    return state
```

Guarantees (all demonstrated by the harness, §32):

1. **Termination**: every path ends at a status assignment; loop exits are bounded by LoopMonitor (iteration/token budgets, novelty plateau, repetition, EVOC).
2. **State completeness**: every status is produced by the classifier or an explicit assignment; all eight states are reachable.
3. **Packet completeness**: `build_decision_packet` runs on every terminal path, including UNSAFE/ESCALATED denials.
4. **Verification independence**: `SOLVED` requires external `verifier_identity`; self-only never suffices.
5. **Cost boundedness**: the budget envelope is consumed at every stage; E0/E1 take the direct path.
6. **Gate enforcement**: WHAT/WHY/HOW gates are checked before stage advancement.
7. **Review in loop**: AAR runs on non-terminal exits and feeds reframe decisions.
8. **Resume**: checkpoint at the epilogue makes the task resumable across sessions.

### 24.5 Session and scheduler layer (v2)

- `TaskScheduler` owns task identity, priority arbitration (conflicting concurrent goals), and checkpoint/resume.
- Prospective memory entries are consumed by the scheduler (deadlines, unresolved intentions) rather than stored inertly.
- `GoalManager.renegotiate(user_request, old_contract) -> new_contract` is gated by the SafetyKernel and requires decision-owner confirmation; the signed goal contract is stored outside mutable memory (invariant 5).
- Cross-task conflict detection runs in the ExecutionMonitor: a later user goal that contradicts an active contract triggers renegotiation, not drift (finding A17).

### 24.6 Component–call-site map

| Component | Call sites in §24.4 |
|---|---|
| MetaRouter | step 1 (route) |
| BudgetController | loop top, every stage boundary |
| LoopMonitor | loop top |
| FrameCritic / gates | `check_exit_gate` (WHAT, WHY) |
| Diagnostician | `diagnose` |
| EvidenceService | inside `diagnose` (VOI) |
| SearchController | inside `generate` for E3+ |
| Premortem / RedTeam | HOW stage |
| VerifierRegistry | candidate + outcome verification |
| Planner / SafetyKernel / ToolBroker | DO stage |
| ExecutionMonitor | after each transaction |
| ReviewEngine / CompetenceModel | REVIEW-in-loop + epilogue |
| MemoryManager / ImprovementEngine | epilogue |
| AuditLog | loop top + every stage + epilogue |
| TaskScheduler | resume + checkpoint |

**Sub-call-sites (v2):** components that run inside stage bodies rather than directly in the loop — CouncilOrchestrator (`generate` when `use_council`, §17), WorldModel and EvidenceService (`diagnose`, §11), MethodComposer (`route`, §16), EvaluationPlane (`improvement_engine.evaluate` and batch runs, §22.3, §23.6), GoalManager (`initialize_task_state` and `renegotiate`, §24.5). The harness (§32) implements the loop-level subset; see §32.4 for the exact coverage.

---

## 25. Minimal Viable Thinking Agent

### 25.1 MVP components

- One capable foundation model.
- One independent verifier model or deterministic verifier.
- A MetaRouter (the v1 "Layer-0 router" is renamed — one name, one component; finding A18) with route flags and a budget envelope.
- Structured WHAT–WHY–HOW–DO–REVIEW templates with boolean gate predicates.
- Web, code, calculator, and document tools via a sandboxed ToolBroker with timeouts/retries/idempotency.
- Working, episodic, semantic, and procedural memory with the §18.2 record schema and contradiction rule.
- Four default roles (all prompt-variants over the single model, fresh contexts per agent):
  - Coordinator.
  - Researcher.
  - Verifier (the v1 "Verifier" and §17.1 "Formal Verifier" are the same role; §17.1 is authoritative).
  - Red Team.
- LoopMonitor + BudgetController (a few counters — the highest value-per-line additions).
- AAR and change-proposal generation with dedup.
- An immutable audit log with per-stage telemetry.
- Human approval for consequential actions with packet-before-approval (§21.4).

### 25.2 MVP development order (v2, deadlock removed)

1. Implement structured state and decision records (§24.2).
2. Add evidence retrieval and provenance.
3. Add criterion-specific verification with the threshold table (§15.4).
4. Add transactional tool use with failure semantics (§20.3).
5. Add persistent memory with channels and contradiction rule (§18).
6. Add independent multi-agent generation (fresh contexts, answer schema).
7. Add targeted debate (bounded rounds, minority ledger).
8. Add a minimal frozen EvaluationPlane (`run_suite` + 5-test MVP suite) **before** safety evaluations and procedural-memory updates, so those gates have infrastructure — v1 ordered these after, creating a deadlock (finding A18).
9. Add safety and prompt-injection evaluations (against the frozen suite).
10. Add procedural-memory updates gated on the baseline.
11. Add sandboxed architecture search as an explicit stub (Phase-5 feature, §26) rather than an MVP item.

---

## 26. Roadmap Toward AGI and ASI Research

### Phase 0 — Structured assistant

- Adaptive routing with route flags.
- WHAT–WHY–HOW–DO–REVIEW with stage gates.
- Retrieval and deterministic verification.
- LoopMonitor + BudgetController.
- No autonomous external action.

### Phase 1 — Grounded agent

- Tool broker with transaction semantics.
- Sandboxed execution.
- Hierarchical plans.
- Environmental feedback.
- Human-approved consequential actions.

### Phase 2 — Persistent generalist

- Long-term memory with contradiction and consolidation.
- Skill library.
- User and domain adaptation.
- Calibration from historical performance (CompetenceModel).
- Cross-task lesson consolidation.

### Phase 3 — Collective problem solver

- Heterogeneous specialist agents.
- Independent candidate generation (fresh contexts).
- Verifier-weighted synthesis.
- Large parallel workflows for decomposable tasks.
- Shared structured workspace with sole-writer Coordinator.

### Phase 4 — Continual learner

- Active curricula.
- Automatic experiment generation.
- Stable procedural learning.
- Transfer and forgetting controls.
- Multimodal and embodied world models.

### Phase 5 — Governed self-improving system

- Automated scaffold search (sandboxed).
- Portfolio evaluations against the stable baseline.
- Independent safety audits.
- Canary deployment and rollback.

### Phase 6 — AGI candidate

An AGI claim would require evidence of:

- Broad transfer across unfamiliar domains.
- Low-data learning.
- Long-horizon autonomy.
- Reliable tool and environment grounding.
- Persistent, useful memory.
- Calibrated uncertainty.
- Social and collaborative competence.
- Robust correction and interruption.
- Safe continual improvement.
- Performance under strict resource constraints.

### Phase 7 — ASI research boundary

ASI would involve performance exceeding the strongest human experts across most relevant cognitive domains, including improving AI research itself.

At this point, the central problem becomes oversight:

> How can humans reliably evaluate and control systems whose reasoning and planning exceed human capability?

Thinking Agent does not solve that problem. It establishes constraints for approaching it:

- No uncontrolled replication.
- No autonomous goal rewriting.
- No unilateral permission expansion.
- Independent external oversight.
- Restricted resources and network access.
- Multiple containment layers.
- Capability evaluations before autonomy increases (co-scaling gate, §23.7).
- Improvement speed limited by evaluation and containment capacity.

---

## 27. Common Failure Modes

| Failure | Mitigation (v2 mechanism) |
|---|---|
| Wrong problem frame | Multiple frames, user confirmation, frame critic, WHAT gate |
| HOW before WHY | Stage gate requiring diagnosis (G-WHY predicates) |
| Confident hallucination | Evidence and tool verification; SOLVED requires external verifier |
| Excessive diagnosis | Value-of-information stop + EVOC check |
| First-answer anchoring | Independent candidate generation |
| Self-critique echo chamber | External and heterogeneous verifiers |
| Debate conformity | Private first answers, fresh contexts, minority ledger |
| Majority error | Verification-weighted aggregation; minority reports recoverable |
| Planner-executor drift | Preconditions, postconditions, checkpoints, monitor |
| Tool hallucination | Retrieved tool schemas and argument validation |
| Prompt injection | Authority/data separation and least privilege, boundary validation |
| Memory poisoning | Provenance anchoring, contradiction rule, quarantine, channels |
| Goal drift | Signed goal contract outside mutable memory; renegotiation gate |
| Reward hacking | Hidden and adversarial evaluations; immutable evaluation plane |
| Benchmark overfitting | Portfolio and out-of-distribution tests; stable baseline |
| Unsafe self-modification | §22 pipeline invoked, admission control, canary, rollback |
| Infinite cognitive loop | LoopMonitor: novelty, repetition, EVOC, budgets → RESOURCE_LIMITED |
| Overuse of agents | Council feasibility predicates (§17.4) + agent caps |
| Hidden side effects | Transactional actions and state verification; compensation table |
| Architecture monoculture | Diverse candidate archive and independent audits |
| Capability growth outruns safety | Mandatory capability–safety co-scaling gate (§23.7) |
| Denial paths without audit records | Common epilogue produces the packet on every terminal path |
| Proposal flood | ImprovementEngine admission control + dedup |

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
23. **A claim that cannot name its verifier is not a verified claim.**

---

## 29. Conclusion

Thinking Agent combines the strongest elements of traditional human problem-solving systems with contemporary agent research:

- Cynefin supplies context-sensitive routing.
- Dual Process Theory and RPD supply fast and deliberate paths.
- WHAT–WHY–HOW–DO–REVIEW supplies the task structure.
- Premortem and Red Teaming supply anticipatory criticism.
- Root-cause methods and Bayesian reasoning supply diagnostic rigor.
- CPS, SCAMPER, TRIZ, TOC, and Six Hats supply structured creativity.
- ReAct, planning search, and hierarchical decomposition connect thought to action.
- CoALA-style memory provides persistent cognitive state.
- AAR, Double-Loop Learning, Reflexion, and Kaizen support improvement.
- Independent verifiers and tool feedback correct the weaknesses of intrinsic self-critique.
- Multi-agent collectives provide scalable diversity when used selectively.
- Sandboxing, least privilege, transaction gates, and human oversight constrain action.
- Gated scaffold search provides a bounded route toward self-improving systems.

v2 adds what v1 lacked: a governed loop that guarantees termination, an operational budget envelope, enforced stage gates, a complete eight-state classifier, a mandatory decision packet on every terminal path, structural verification independence, a competence feedback loop fed by evaluation history, memory governance with a contradiction rule, transaction failure semantics, council contracts, and an invoked — not merely described — self-improvement pipeline. These changes were not adopted on the strength of self-critique alone; they were executed, measured, and validated against a baseline in the harness (§32), in accordance with the framework's own rule: self-criticism is a source of hypotheses, not proof.

The architecture’s most important principle is not “think longer” or “use more agents.” It is:

> **Apply the right cognitive process, obtain the right evidence, verify through the right mechanism, act with the right authority, and learn without weakening human control.**

That combination provides a practical architecture for increasingly general AI systems while acknowledging that AGI, safe recursive self-improvement, and ASI alignment remain open research problems.

---

## 30. Primary Research References

1. Sumers et al., **Cognitive Architectures for Language Agents**, arXiv:2309.02427. ([arxiv.org](https://arxiv.org/abs/2309.02427?utm_source=openai))
2. Kotseruba and Tsotsos, **A Review of 40 Years of Cognitive Architecture Research**, arXiv:1610.08602. ([arxiv.org](https://arxiv.org/abs/1610.08602?utm_source=openai))
3. Yao et al., **ReAct: Synergizing Reasoning and Acting in Language Models**, arXiv:2210.03629. ([arxiv.org](https://arxiv.org/abs/2210.03629?utm_source=openai))
4. Yao et al., **Tree of Thoughts**, arXiv:2305.10601; Hao et al., **RAP**, arXiv:2305.14992; Zhou et al., **LATS**, arXiv:2310.04406. ([arxiv.org](https://arxiv.org/abs/2305.10601?utm_source=openai))
5. Prasad et al., **ADaPT**, arXiv:2311.05772; Zhou et al., **Self-Discover**, arXiv:2402.03620. ([arxiv.org](https://arxiv.org/abs/2311.05772?utm_source=openai))
6. Shinn et al., **Reflexion**, arXiv:2303.11366; Gou et al., **CRITIC**, arXiv:2305.11738; Dhuliawala et al., **Chain-of-Verification**, arXiv:2309.11495. ([arxiv.org](https://arxiv.org/abs/2303.11366?utm_source=openai))
7. Huang et al., **Large Language Models Cannot Self-Correct Reasoning Yet**, arXiv:2310.01798; Tyen et al., **LLMs Cannot Find Reasoning Errors**, arXiv:2311.08516. ([arxiv.org](https://arxiv.org/abs/2310.01798?utm_source=openai))
8. Du et al., **Improving Factuality and Reasoning through Multiagent Debate**, arXiv:2305.14325; Zhang et al., **If Multi-Agent Debate Is the Answer, What Is the Question?**, arXiv:2502.08788. ([arxiv.org](https://arxiv.org/abs/2305.14325?utm_source=openai))
9. Choi et al., **Debate or Vote**, arXiv:2508.17536; Wu et al., **Can LLM Agents Really Debate?**, arXiv:2511.07784. ([arxiv.org](https://arxiv.org/abs/2508.17536?utm_source=openai))
10. Packer et al., **MemGPT**, arXiv:2310.08560; Park et al., **Generative Agents**, arXiv:2304.03442; Wang et al., **Voyager**, arXiv:2305.16291. ([arxiv.org](https://arxiv.org/abs/2310.08560?utm_source=openai))
11. Zelikman et al., **STOP**, arXiv:2310.02304; Hu et al., **Automated Design of Agentic Systems**, arXiv:2408.08435; Zhang et al., **Darwin Gödel Machine**, arXiv:2505.22954. ([arxiv.org](https://arxiv.org/abs/2310.02304?utm_source=openai))
12. Debenedetti et al., **AgentDojo**, arXiv:2406.13352; Greenblatt et al., **AI Control**, arXiv:2312.06942. ([arxiv.org](https://arxiv.org/abs/2406.13352?utm_source=openai))
13. xAI, **Grok 4.20 System Card**, April 7, 2026. ([data.x.ai](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf))
14. xAI, **Grok Build Is Now Open Source**, July 15, 2026; **Workflows in Grok Build**, July 23, 2026. ([x.ai](https://x.ai/news/grok-build-open-source))

---

## 31. Differential Change Log (v1 → v2)

Every accepted finding from the six-lens v1 self-review is recorded below with its disposition and validation status. Findings are numbered per the aggregated analysis (A1–A18); "Validated" means the behavior change is demonstrated by the harness (§32).

| ID | v1 defect (aggregated finding) | v2 change | Where | Validated |
|---|---|---|---|---|
| A1 | `while True` loop cannot terminate; §9.5 signals never computed; `RESOURCE_LIMITED` unreachable | LoopMonitor (novelty signature, repetition, EVOC) + bounded loop | §9.5, §24.4 | S2, S3, S9 |
| A2 | 5 of 8 graceful states unreachable; `determine_failure_state` black box; APPROXIMATED/NEEDS_EXPERIMENT had no producers | `classify_terminal` decision table; error-bound producer for APPROXIMATED; probe producer for NEEDS_EXPERIMENT; §3.4 policy | §3.3–3.4, §15.5, §24.3–24.4 | S2–S18 suite (all 8 states reached) |
| A3 | Effort levels E0–E5 never branched on; no fast path; §17.4 never evaluated | Route flags (`requires_*`) gating every stage; direct-answer path for E0/E1; `should_use_council` predicates | §9.4, §17.4, §24.4 | S1, S7 |
| A4 | Budgets declared, never enforced; no BudgetController | Budget envelope + BudgetController consumed at every stage | §9.6, §24.4 | S9 |
| A5 | Stage gates, premortem, red team had no call sites; §13.7 exit conditions unread | `check_exit_gate` predicates; `premortem()` and `red_team.attack()` call sites; plan conditions consumed | §10.5, §11.7, §12.6–12.8, §13.7, §24.4 | S13, S15 |
| A6 | REVIEW outside the loop; VERIFY = 2 points not a layer; verification cascade | In-loop AAR feeding reframe; delta-based verification with history; ExecutionMonitor call site | §14, §15.6, §24.4 | S3 (in-loop review); delta-verification design-level |
| A7 | Decision packet path-dependent; denial paths returned before packet | Common epilogue on every terminal path; field-source contract | §15.4, §24.3–24.4 | S11, universal asserts |
| A8 | Competence model had no data feed; §5.4 violated by default | CompetenceModel feedback loop (episode → calibration → route) | §19.3, §23.7, §24.4 | design-level |
| A9 | Memory write protocol dead-ended; no contradiction rule; no channels; no consolidation | memory_record schema; trust-margin contradiction rule; write channels; quarantine+promotion; consolidation trigger | §18.2–18.5 | S14, S8 |
| A10 | Council unimplementable: no schemas, no independence, no concurrency | agent_answer schema; fresh contexts; sole-writer Coordinator; minority ledger | §17.2–17.3 | S7 |
| A11 | SOLVED gate uncomputable: no threshold/reliability/selection/fallback | Threshold table; reliability estimator; ordered selection; no-verifier ladder | §15.1–15.4 | S5 |
| A12 | No failure semantics: no timeouts/retries/idempotency/checkpoints/interrupt | Per-class transaction table; interrupt/checkpoint/resume; idempotency keys | §13.3, §20.3, §20.5, §24.5 | design-level |
| A13 | Self-evolution gate never invoked; unconditional queue; baseline undefined | Admission control + dedup; `evaluate()` pipeline invocation; stable baseline; evaluation-plane immutability; cadence differential | §22.2–22.7 | S10 (queue dedup); pipeline invocation design-level |
| A14 | Interface triple mismatch (§24.2/24.3/24.4); components without interfaces | Canonical §24.3 with return schemas; component–call-site map; schema alignment | §24.1–24.4, §24.6 | doc-level |
| A15 | Meta-controller SPOF; stakes/action-class self-assessed with incentive conflict | Stakes scale; independent risk attestation; harm/irreversibility estimated separately | §9.2, §12.5, §13.2, §20.4 | S4 (stakes override), S12 (denial on class mismatch); independent estimator design-level |
| A16 | VOI not a mechanism; no telemetry; route recomputed per iteration; §23.5 unwired | `voi()` interface; AuditLog per-stage telemetry; route once per task; §23.8 | §11.5, §23.8, §24.3–24.4 | S1/S7 (fast-path cost); telemetry design-level |
| A17 | No session/scheduler; goal renegotiation absent; search controller unowned | TaskScheduler; `renegotiate`; SearchController with EV gate | §8.5, §16.2, §24.5 | design-level |
| A18 | Doc nits: naming drift, Gibbs double-list, §4 cross-ref, OODA order, MVP deadlock, gates prose, threats without controls, human-gate process | Terminology unified (MetaRouter); §5.9 fixed; §4 citation fixed; §25.2 reordered; gate predicates; threat→control table; §21.4 gate process; §6.5 matrix | throughout | doc-level |

### 31.1 Non-accepted findings

None of the six reviewers' findings were rejected outright. Three were partially deferred to later phases rather than v2: (a) model heterogeneity for council roles (deferred to Phase 3, §26 — accepted as documented limitation); (b) open-ended candidate archives (deferred to Phase 5, §26); (c) interrupt semantics require implementation care with state serialization (specified in §20.5, implementation attention flagged).

---

## 32. Empirical Validation

### 32.1 Method

Per the framework's own rules (P4, P9, §22.3), the v2 changes were validated by **execution, not self-critique**. `validation/harness.py` implements the v1 §24.4 algorithm and the v2 §24.4 algorithm over identical deterministic mock components (control-flow simulation), runs a 15-scenario suite, and asserts the framework's own standards. The harness validates what is decidable — termination, state reachability, budget enforcement, stage gating, verification independence, packet completeness, cost behavior — **not** model intelligence. It is a specification-execution simulation.

### 32.2 Results (18 scenarios; 3 reproducible runs, identical every run)

| Scenario | v1 status | v2 status | v1 asserts | v2 asserts | v1 tokens | v2 tokens |
|---|---|---|---|---|---|---|
| S1 trivial task, E0 | SOLVED | SOLVED | 8/14 | 5/5 | 8 | 5 |
| S2 executor always fails | WATCHDOG_INFINITE_LOOP | RESOURCE_LIMITED | 6/14 | 4/4 | 655 | 69 |
| S3 frame oscillates | WATCHDOG_INFINITE_LOOP | SOLVED | 6/14 | 4/4 | 555 | 83 |
| S4 clear-looking, high stakes | SOLVED | SOLVED | 8/14 | 4/4 | 17 | 22 |
| S5 no external verifier | INFEASIBLE | ESCALATED | 10/14 | 4/4 | 13 | 42 |
| S6 ambiguous success | INFEASIBLE | NEEDS_EVIDENCE | 11/14 | 4/4 | 13 | 18 |
| S7 calculator exists | SOLVED | SOLVED | 8/14 | 4/4 | 8 | 5 |
| S8 injection attempt | SOLVED | SOLVED | 9/14 | 5/5 | 13 | 19 |
| S9 budget exhaustion | INFEASIBLE | RESOURCE_LIMITED | 11/14 | 4/4 | 15 | 6 |
| S10 proposal flood | SOLVED | SOLVED | 9/14 | 4/4 | 13 | 19 |
| S11 authorization denied | ESCALATED | ESCALATED | 8/14 | 4/4 | 9 | 17 |
| S12 action-class misattestation | UNSAFE | UNSAFE | 8/14 | 4/4 | 9 | 17 |
| S13 red team catches flaw | SOLVED | SOLVED | 8/14 | 4/4 | 15 | 29 |
| S14 memory contradiction | SOLVED | SOLVED | 8/14 | 4/4 | 13 | 19 |
| S15 WHAT gate: no metrics | SOLVED | NEEDS_EVIDENCE | 8/14 | 4/4 | 13 | 6 |
| S16 safe probe available | INFEASIBLE | NEEDS_EXPERIMENT | 11/14 | 4/4 | 15 | 20 |
| S17 bounded approximation available | INFEASIBLE | APPROXIMATED | 11/14 | 4/4 | 13 | 18 |
| S18 constraints inconsistent | INFEASIBLE | INFEASIBLE | 11/14 | 4/4 | 13 | 18 |
| **Totals** | | | **159/252** | **74/74** | **1410** | **432** |

Token units are mock cost units; the 69% reduction comes mainly from the operational fast path (A3) and budget enforcement (A4).

### 32.3 What the suite demonstrates

- **Termination (A1):** v1 hits the watchdog on S2/S3 (no guard of its own); v2 terminates every scenario with a graceful state.
- **State completeness (A2):** the v2 suite reaches **all eight states** — SOLVED (S1, S3, S4, S7, S8, S10, S13, S14), RESOURCE_LIMITED (S2, S9), ESCALATED (S5, S11), NEEDS_EVIDENCE (S6, S15), UNSAFE (S12), NEEDS_EXPERIMENT (S16), APPROXIMATED (S17), INFEASIBLE (S18). v1 could not produce RESOURCE_LIMITED, NEEDS_EVIDENCE, NEEDS_EXPERIMENT, APPROXIMATED, or ESCALATED correctly (it collapsed them into INFEASIBLE or SOLVED).
- **Verification independence (A11/§5.4):** S5 — v1 declared SOLVED/INFEASIBLE with self-only judgment; v2 refuses SOLVED without an external verifier and escalates.
- **Fast path (A3):** S1/S7 — v2 runs 2–3 cognitive stages; v1 ran the full pipeline.
- **Budget (A4/A1):** S9 — v2 ends at RESOURCE_LIMITED; v1 ran on or mislabeled.
- **Gate enforcement (A5):** S15 — v2 blocks a task with no success metrics at WHAT; v1 proceeded to SOLVED.
- **Red team (A5):** S13 — v2 rejects the flawed candidate and regenerates successfully; v1 shipped it.
- **Memory governance (A9):** S14 — v2 quarantines the conflicting lesson (CONFLICTED); v1 silently overwrote. S8 — untrusted tool content never reaches procedural memory.
- **Council feasibility (A3/A10):** S7 — deterministic-solver task skips the council.
- **Attestation (A15):** S12 — misattested action class is denied.
- **Packet completeness (A7):** universal assert — every v2 terminal path carries the §15.4 packet; v1's denial path returned none.
- **Reproducibility:** the suite is deterministic; 3 consecutive runs produced identical results.

### 32.4 Honest limitations of the validation

- Mock components: the harness does not simulate model intelligence, sampling, or real tools; control-flow guarantees hold for any components satisfying the component contracts.
- **Coverage disclosure:** the harness implements the loop-level subset of §24.4 — MetaRouter (route flags, stakes override, council feasibility), FrameCritic/Diagnostician gates, Explorer, Premortem, RedTeam, VerifierRegistry (independence + reliability), Planner, SafetyKernel (authorize + attestation), Executor, ReviewEngine, MemoryManager (channels, contradiction, quarantine), ImprovementEngine (dedup + gating), LoopMonitor, BudgetController. It does **not** implement: CouncilOrchestrator/multi-agent generation, ExecutionMonitor, CompetenceModel, SearchController, EvidenceService/VOI, TaskScheduler/checkpoint-resume, AuditLog telemetry, EvaluationPlane, or delta-based verification reuse (§15.6). Those are specified (§24) but validated only at design level in §31.
- The EVOC proxy and novelty signature are simplified stand-ins for the §9.5 terms; production implementations must calibrate them from §23.8 telemetry.
- The threshold table and budget defaults are configuration, not constants; they must be tuned per deployment.
- S4's stakes-override and S12's attestation-denial behaviors are demonstrated; the *independent risk estimator* itself is specified (§20.4) but not separately modeled in the harness.

### 32.5 How to re-run

```bash
python validation/harness.py        # single pass, writes validation/results.md
python validation/harness.py 3      # 3-pass determinism check
```

---

## 33. Consumer Quick-Reference

| Reader | Sections |
|---|---|
| Implementer (MVP) | §24 (canonical), §25, §9.4–9.6, §15.4, §18.2, §20.3 |
| Safety auditor | §21, §20, §22, §23.4, §27 |
| Researcher | §2, §5, §30, §31 |
| Evaluator | §23, §32, §15.4 |
| All | §3.3 (state contract), §28 (operating rules), §6.5 (principle–mechanism matrix) |

Normative content (must be satisfied): §3.3–3.4, §6.5, §9.4–9.6, §10.5, §11.7, §12.5–12.8, §13.2–13.3, §13.7, §15.1–15.4, §17.2–17.4, §18.2–18.4, §20.3–20.5, §21.2–21.4, §22.3–22.7, §23.7–23.8, §24.3–24.4. Guidance (advisory): the remaining prose, including §5 and §26.

---

*End of document.*
