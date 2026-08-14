# Thinking Agent

## A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research

**Version:** 1.0\
**Research cutoff:** August 7, 2026\
**Status:** Research and engineering blueprint\
**Source policy:** Primary arXiv papers and official xAI materials were prioritized over third-party commentary.

***

## 1. Executive Summary

Thinking Agent combines:

1. A ranked portfolio of 40 traditional human thinking frameworks (evaluated by adoption priority, with Cynefin, Premortem, AAR, Double-Loop Learning, RPD, and root-cause methods at the top).
2. The `WHAT → WHY → HOW → DO → REVIEW` process.
3. The memory, multi-agent, metacognitive, and self-evolution concepts in the two earlier architecture drafts.
4. Research on cognitive architectures, reasoning, planning, tool use, reflection, verification, multi-agent systems, memory, self-improving scaffolds, and agent security.
5. Production patterns documented by xAI, including adaptive reasoning, parallel subagents, plan-review workflows, verification, synthesis, and tool-oriented agent harnesses.

Its central operating loop is:

> **META-CONTROL → WHAT → WHY → HOW → DO → REVIEW**

A continuous **VERIFY** process surrounds every stage.

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

Thinking Agent should be viewed as a scaffold for researching AGI, not as proof that AGI or ASI follows automatically from adding more agents or more inference-time computation.

***

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

These functions must not be collapsed into one unconstrained model call.

***

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

### 3.3 Required graceful-failure states

Every task must terminate in one of these explicit states:

| State              | Meaning                                                                            |
| ------------------ | ---------------------------------------------------------------------------------- |
| `SOLVED`           | The result satisfies the success criteria and verification threshold.              |
| `APPROXIMATED`     | An exact solution was unavailable, but a bounded approximation was produced.       |
| `NEEDS_EVIDENCE`   | A decision cannot responsibly be made without more information.                    |
| `NEEDS_EXPERIMENT` | A safe probe or experiment is the next rational action.                            |
| `INFEASIBLE`       | Constraints are inconsistent or the requested outcome is not currently achievable. |
| `UNSAFE`           | The requested action violates a safety, legal, ethical, or permission boundary.    |
| `ESCALATED`        | Human or domain-expert judgment is required.                                       |
| `RESOURCE_LIMITED` | The expected value of further computation does not justify its cost.               |

***

## 4. Architectural Synthesis and Lineage

Thinking Agent synthesizes five bodies of knowledge. No component depends on a separate companion document; every required concept is inlined in the sections below or anchored to external research URLs in Section 30.

| Lineage                                                                                 | Retained contribution                                                                                                                                                     | Thinking Agent implementation                                                                                                       |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Ranked traditional human thinking models (40 frameworks evaluated by adoption priority) | Cynefin, Premortem, AAR, Double-Loop Learning, RPD, root-cause analysis, metacognition, creativity methods, Red Teaming, plus 31 supporting frameworks summarized in §5.9 | Adaptive routing, risk simulation, structured review, method library, adversarial verification                                      |
| Staged problem-solving process model (WHAT → WHY → HOW → DO → REVIEW)                   | Framing discipline, diagnostic rigor, alternative generation, selection criteria, execution project management, review and iteration                                      | Primary task-level cognitive loop (stages 1–5 of the main loop, §10–§14)                                                            |
| Grok-inspired agent architecture draft                                                  | Fast/full dual paths, CoALA memory hierarchy, specialized multi-agent roles, hierarchical planning, nested self-evolution                                                 | Meta-controller (§9), structured cognitive workspace (§7), agent council (§17), learning engine (§14, §22)                          |
| Verification-first multi-agent protocol                                                 | Independent generation before communication, evidence-weighted aggregation, known-limit non-claims, anti-debate-failure guards                                            | Independent verifier separation (§15), verifier-weighted synthesis (§17.3), explicit non-claims and uncertainty (§3, §21.2)         |
| Thinking Agent research additions (2024–2026 agent-security and production literature)  | Tool security, authority/data separation, least privilege, permission boundaries, gated self-modification, structured task state, evaluation portfolio                    | Safety kernel (§21), tool broker (§20), self-improvement pipeline (§22), benchmark and audit plane (§23), shared task state (§24.2) |

***

## 5. Research Foundations

### 5.1 Cognitive architecture

Cognitive-architecture research consistently treats intelligence as an interaction among perception, attention, action selection, memory, learning, and reasoning rather than a single monolithic process. CoALA provides a particularly useful language-agent abstraction: modular memory, internal and external action spaces, and structured decision procedures. Research proposing broader AGI-oriented architectures similarly identifies goal management, reflection, ethics, social interaction, learning, monitoring, and problem-solving as distinct functional requirements. ([arxiv.org](https://arxiv.org/abs/1610.08602?utm_source=openai))

Thinking Agent adopts a **polyglot cognitive substrate** rather than assuming that all knowledge must be stored in one format. Text, graphs, equations, code, images, databases, models, procedures, and trajectories can coexist as long as they share provenance, identity, access-control, and relationship metadata.

### 5.2 Grounded reasoning and tool use

ReAct demonstrated the value of interleaving reasoning, action, and environmental observation. Toolformer showed that models can learn when and how to call external APIs, while SayCan combined semantic planning with grounded affordance or value estimates for embodied action. These results support treating tools and environmental feedback as first-class cognitive components rather than optional plugins. ([arxiv.org](https://arxiv.org/abs/2210.03629?utm_source=openai))

### 5.3 Search, decomposition, and planning

Tree of Thoughts, RAP, LATS, and ADaPT show complementary methods for exploring alternative reasoning paths, simulating future states, backtracking, and decomposing tasks only when needed. Self-Discover adds a method-composition idea: select and combine reasoning modules according to the current task instead of imposing one fixed reasoning structure. ([arxiv.org](https://arxiv.org/abs/2305.10601?utm_source=openai))

Thinking Agent therefore includes a **method composer** and a **search controller**. Full tree search is used only when the expected value of additional exploration exceeds its cost.

### 5.4 Reflection and verification

Reflexion, Self-Refine, CRITIC, and Chain-of-Verification provide evidence that iterative feedback can improve outputs, especially when feedback comes from tests, tools, retrieval systems, or environments. However, intrinsic self-correction is unreliable on many reasoning and planning tasks. Models may fail to locate their own errors, convert correct answers into incorrect ones, or produce false-positive verification judgments. ([arxiv.org](https://arxiv.org/abs/2303.11366?utm_source=openai))

Thinking Agent consequently follows this rule:

> **Self-criticism is a source of hypotheses, not proof of correctness.**

External tests, tools, independent models, formal systems, environmental observations, and qualified humans take precedence over unsupported self-evaluation.

### 5.5 Multi-agent reasoning

Early multi-agent debate research reported improvements in reasoning and factuality. Later systematic studies found that debate does not reliably beat strong single-agent baselines, that model heterogeneity matters, and that majority voting may explain much of the apparent gain. Controlled studies also identify majority pressure, sycophantic conformity, and consensus collapse as failure modes. ([arxiv.org](https://arxiv.org/abs/2305.14325?utm_source=openai))

The Thinking Agent protocol therefore requires:

1. Independent generation before communication.
2. Verification before debate.
3. Targeted debate only over unresolved differences.
4. Preservation of minority reports.
5. Evidence-weighted rather than eloquence-weighted aggregation.
6. Heterogeneous models, tools, data, or roles when possible.

### 5.6 Memory and lifelong learning

CoALA, MemGPT, Generative Agents, and Voyager support the separation of working, episodic, semantic, and procedural memory. They also demonstrate the value of memory consolidation, reflection, dynamic retrieval, executable skill libraries, and experience-driven planning. ([arxiv.org](https://arxiv.org/abs/2309.02427?utm_source=openai))

Thinking Agent treats memory as an actively managed system with provenance, trust, expiration, contradiction handling, and permission controls—not as an unlimited transcript archive.

### 5.7 Self-improving systems

STOP, Automated Design of Agentic Systems, and the Darwin Gödel Machine provide evidence that model-based systems can improve portions of their scaffolding or code through search and empirical evaluation. These demonstrations remain bounded and task-dependent; the Darwin Gödel Machine, for example, validated coding-agent changes through benchmarks while using sandboxing and human oversight. They do not establish unrestricted or automatically safe recursive self-improvement. ([arxiv.org](https://arxiv.org/abs/2310.02304?utm_source=openai))

Thinking Agent permits systems to **propose** changes to themselves but separates proposal authority from deployment authority.

### 5.8 Production agent patterns

Official xAI documentation describes production workflows that plan a task, give subagents clean and focused contexts, fan independent work out in parallel, adversarially verify findings, and synthesize a final result. xAI has also published the Grok Build harness components, including context assembly, tool dispatch, skills, hooks, extensions, and subagents. These examples demonstrate that several Thinking Agent orchestration patterns are implementable today, though they are not evidence that AGI has been achieved. ([x.ai](https://x.ai/news/workflows))

Official xAI safety documentation separately evaluates chat behavior, agentic behavior, prompt injection, deception, sycophancy, sabotage, and dual-use capabilities. This reinforces the Thinking Agent position that an agent must be evaluated as a complete acting system, not only as a text generator. ([data.x.ai](https://data.x.ai/2026-04-07-grok-4-20-model-card.pdf))

### 5.9 Traditional thinking-model portfolio

Thinking Agent draws on a ranked survey of 40 traditional human thinking models, scored by adoption priority for agent loops (1 = lowest leverage, 10 = highest). The frameworks below cover the top tier and notable supporting entries; every listed contribution is integrated into Thinking Agent's stages, method composer, or multi-agent roles rather than retained as a separate document.

| Rank | Model                                                               | Origin / Field                               | Core concept                                                                                                                                                                                | Adoption score | Why it scores high for agents                                                                     |
| ---- | ------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------- |
| 1    | Cynefin Framework                                                   | Complexity science (Dave Snowden)            | Sense context first, then respond according to domain: Clear (best practice), Complicated (expert analysis), Complex (probe–sense–respond), Chaotic (stabilize first), Disorder (decompose) | 10             | Enables adaptive loop intensity and Fast-vs-Full routing — the single highest-leverage addition   |
| 2    | Premortem Analysis                                                  | Decision science (Gary Klein)                | Imagine failure has already occurred, work backward to uncover plausible causes, then mitigate up front                                                                                     | 10             | Proactive risk detection at near-zero implementation cost; runs before HOW-stage commitment       |
| 3    | After-Action Review (AAR)                                           | Military / Lean                              | Four questions: What was supposed to happen? → What actually happened? → Why the difference? → What should change next?                                                                     | 10             | Perfect match for the REVIEW stage; powers single-loop and double-loop learning                   |
| 4    | Double-Loop Learning                                                | Organizational learning (Argyris & Schön)    | Single-loop changes tactics; double-loop also questions the governing assumptions, frames, and values behind the tactics                                                                    | 9.5            | Core to meaningful self-evolution; prevents optimizing a solution to the wrong problem            |
| 5    | Recognition-Primed Decision (RPD)                                   | Naturalistic decision making (Klein)         | Expert pattern match → rapid mental simulation → act; used when a familiar pattern is recognized with high confidence                                                                       | 9.5            | Enables the Fast Recognition Path for Clear/Complicated expert domains without full-loop overhead |
| 6    | Root-cause suite (5 Whys + Ishikawa Fishbone + Fault Tree Analysis) | RCA (Toyota + Ishikawa + safety engineering) | Problem → categories → drill-down toward root cause using causal chains, category diagrams, or boolean fault trees                                                                          | 9              | Greatly strengthens the WHY stage and diagnostic depth for complex problems                       |
| 7    | Metacognition Cycle                                                 | Educational psychology (Flavell)             | Plan → Monitor → Evaluate → Adjust — applied to the thinker's own reasoning process                                                                                                         | 9              | Implemented as the lightweight parallel meta-process inside META-CONTROL                          |
| 8    | Dual Process Theory (System 1 & 2)                                  | Psychology (Kahneman)                        | Fast intuitive judgment (S1) vs slow deliberate reasoning (S2) with context-appropriate switching                                                                                           | 9              | Foundation for Fast-vs-Full path routing and Cynefin-based effort selection                       |
| 9    | Paul-Elder Critical Thinking Framework                              | Philosophy / Education                       | Eight Elements of Thought checked against Intellectual Standards (clarity, accuracy, precision, relevance, depth, breadth, logic, significance, fairness)                                   | 8.5            | Raises the quality bar on the Diagnostician, Researcher, Verifier, and Synthesizer roles          |
| 10   | Theory of Constraints (TOC) Thinking Processes                      | Management (Eliyahu Goldratt)                | Current Reality Tree → Evaporating Cloud (contradiction resolution) → Future Reality Tree                                                                                                   | 8.5            | Powerful for conflicting goals; synergizes with TRIZ and HOW-stage alternative generation         |
| 11   | Osborn-Parnes Creative Problem Solving (CPS)                        | Creativity research                          | Clarify → Ideate → Develop → Implement → Evaluate                                                                                                                                           | 8              | Direct upgrade to HOW-stage divergent ideation and creative Explorer roles                        |
| 12   | Red Team Thinking                                                   | Military / Security                          | Deliberately attack your own plan, assumptions, and artifacts to find weaknesses before an opponent does                                                                                    | 8              | The Red Team role in the multi-agent council and the HOW-stage Red Team gate                      |
| 13   | Six Thinking Hats                                                   | Lateral thinking (Edward de Bono)            | Six sequential or parallel perspectives: Facts (White), Emotions (Red), Caution (Black), Benefits (Yellow), Creativity (Green), Process (Blue)                                              | 8              | Good for HOW-stage consolidation and multi-agent perspective diversity                            |
| 14   | TRIZ                                                                | Inventive problem solving (Altshuller)       | Identify contradictions (technical or physical), apply 40 inventive principles or separation principles to resolve                                                                          | 8              | Structured creativity for contradiction-heavy problem classes                                     |
| 15   | SCAMPER                                                             | Creative thinking (Bob Eberle)               | Idea-generation checklist: Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse                                                                                        | 7.5            | Lightweight rapid-ideation tool for the Explorer role                                             |
| 16   | Kaizen                                                              | Japanese management (Toyota)                 | Many small, testable, reversible improvements over time rather than big-bang rewrites                                                                                                       | 7.5            | Governs the step size of the self-evolution engine to reduce regression risk                      |
| 17   | GROW Coaching Model                                                 | Coaching (John Whitmore)                     | Goal → Reality → Options → Will (commitment)                                                                                                                                                | 6.5            | Useful in the WHAT stage for ambiguous user goals and in DO-stage stakeholder alignment           |
| 18   | OODA Loop                                                           | Military strategy (John Boyd)                | Observe → Orient → Decide → Act — high-tempo loop for dynamic uncertainty                                                                                                                   | 7              | Inspired the DO-stage micro-loop pattern alongside ReAct                                          |
| 19   | Design Thinking                                                     | Design / Innovation                          | Empathize → Define → Ideate → Prototype → Test → Iterate                                                                                                                                    | 7              | Useful for user-facing or product-definition tasks                                                |
| 20   | Nemawashi                                                           | Japanese decision making                     | Informal consensus gathering and alignment before any formal decision                                                                                                                       | 5.5            | Informs multi-agent pre-debate alignment and stakeholder-facing communication                     |

The remaining 20 frameworks in the ranked survey cover philosophical cross-cultural traditions (Wu Wei, Stoic Reflection, Buddhism, Ubuntu, 三思而后行), education taxonomies (Bloom's, Kolb's, Gibbs', IDEAL), and specialized process frameworks (PDCA/PDSA, DMAIC, SWOT, Appreciative Inquiry, Hansei, Socratic Method, Action Learning, Dialectical Thinking, 4E Cognition, High-Context vs Low-Context, Gibbs' Reflective Cycle). They are selectively called on by the method composer (§16) according to the current task signature rather than mandated for every loop.

***

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

***

## 7. Architectural Overview

```text
┌──────────────────────────────────────────────────────────────┐
│                  HUMAN / ENVIRONMENT                         │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ GOVERNANCE AND SAFETY KERNEL                                │
│ Goals • permissions • policy • risk gates • interrupts      │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ META-CONTROLLER                                             │
│ Context classification • routing • effort • agenda          │
│ competence model • uncertainty • stopping/escalation        │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ STRUCTURED COGNITIVE WORKSPACE                              │
│ WHAT → WHY → HOW → DO → REVIEW                              │
│ Continuous VERIFY across every stage                        │
└───────────────┬──────────────────────┬───────────────────────┘
                │                      │
┌───────────────▼────────────┐  ┌──────▼──────────────────────┐
│ REASONING AND COUNCIL      │  │ MEMORY AND WORLD MODEL     │
│ Decompose • search         │  │ Working • episodic         │
│ simulate • generate        │  │ semantic • procedural      │
│ critique • synthesize      │  │ causal • multimodal        │
└───────────────┬────────────┘  └──────┬──────────────────────┘
                │                      │
┌───────────────▼──────────────────────▼───────────────────────┐
│ TOOL BROKER AND EXECUTION SANDBOX                           │
│ Retrieval • code • APIs • sensors • robots • transactions  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ TELEMETRY, EVALUATION, AND SELF-EVOLUTION                   │
│ Outcomes • AAR • benchmarks • change proposals • rollback  │
└──────────────────────────────────────────────────────────────┘
```

***

## 8. Four Nested Timescales

Thinking Agent operates through four nested loops.

### 8.1 Action loop

```text
Observe → Predict → Select action → Authorize → Execute → Verify
```

This is a short ReAct/OODA-style loop used during execution.

### 8.2 Task loop

```text
META → WHAT → WHY → HOW → DO → REVIEW
```

This is the main problem-solving loop.

### 8.3 Learning loop

```text
Episodes → AAR → Lesson extraction → Skill update → Evaluation
```

This operates across multiple tasks.

### 8.4 Architecture-evolution loop

```text
Change proposal
→ sandbox branch
→ benchmark
→ adversarial audit
→ approval
→ canary deployment
→ monitoring
→ retain or roll back
```

The architecture-evolution loop must always run more slowly and under stronger governance than the task loop.

***

## 9. Stage 0 — META-CONTROL

### 9.1 Responsibilities

The meta-controller:

- Parses the goal and delegated authority.
- Classifies the problem context.
- Estimates novelty, uncertainty, stakes, reversibility, and adversariality.
- Selects the reasoning modules.
- Allocates model, tool, agent, time, and token budgets.
- Monitors progress and cognitive failure modes.
- Decides when to continue, stop, ask, experiment, or escalate.
- Maintains an explicit model of system competence.

### 9.2 Cynefin-based routing

| Context     | Default strategy                                | Typical route               |
| ----------- | ----------------------------------------------- | --------------------------- |
| Clear       | Recognize, retrieve, apply known procedure      | Fast path                   |
| Complicated | Decompose and apply expert analysis             | Verified deliberate path    |
| Complex     | Probe, observe, update, and adapt               | Full experimental loop      |
| Chaotic     | Stabilize first, minimize harm, then reclassify | Crisis path with human gate |
| Disorder    | Split the task and classify each part           | Decomposition path          |

Stakes override simplicity. A familiar medical, legal, financial, infrastructure, or security action is not routed to an unverified fast path merely because the pattern looks familiar.

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
capability match
evidence availability
time constraints
human availability
```

### 9.4 Reasoning-effort levels

| Level | Description   | Typical configuration                              |
| ----- | ------------- | -------------------------------------------------- |
| `E0`  | Reflex        | Direct retrieval or deterministic procedure        |
| `E1`  | Fast verified | One solver plus lightweight checks                 |
| `E2`  | Deliberate    | Structured decomposition and verifier              |
| `E3`  | Search        | Multiple candidates, simulations, red team         |
| `E4`  | Experimental  | Full loop with probes and evidence collection      |
| `E5`  | Critical      | Independent council, formal checks, human approval |

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

The controller terminates unproductive loops when agents repeat arguments, retrieve no new evidence, or fail to reduce uncertainty.

***

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
  success_metrics:
  failure_conditions:
  deadline:
  resource_budget:
  permissions:
  risk_class:
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

### 10.5 Exit gate

The stage may advance when:

- The goal and owner are identified.
- Scope and constraints are explicit.
- Success metrics exist.
- Major ambiguities are resolved or recorded.
- The system knows whether a WHY stage is necessary.

***

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
  tests:
  posterior_confidence:
  decision_relevance:
  status:
```

### 11.4 Evidence discipline

Each conclusion is represented through:

- **Presuppositions:** What must be assumed?
- **Evidence:** What observations or sources support the claim?
- **Logic:** How do assumptions and evidence lead to the conclusion?
- **Uncertainty:** What alternatives remain plausible?
- **Provenance:** Where did each evidence item originate?
- **Expiry:** When might the evidence become obsolete?

Claims are labeled as:

- `OBSERVED`
- `CALCULATED`
- `INFERRED`
- `PREDICTED`
- `SPECULATIVE`

### 11.5 Active information gathering

The architecture does not collect information merely because it is available. It estimates the value of information:

```text
Would this evidence:
- change the leading hypothesis?
- change the selected action?
- reduce a high-consequence uncertainty?
- expose a hidden constraint?
- alter the risk classification?
```

If not, evidence collection should stop.

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

### 11.7 Exit gate

Diagnosis is sufficient when:

- The leading explanation has decision-relevant evidence.
- Significant alternatives have been considered.
- Residual uncertainty is explicit.
- More diagnosis has low expected value.
- The system can explain what evidence would falsify its conclusion.

***

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
- Tree or graph search.
- Multi-agent independent proposals.
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
  reversibility:
  ethical_legal_status:
  evidence:
  uncertainty:
  required_permissions:
  fallback:
```

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

Options that fail a hard boundary are not rescued by a high utility score.

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

This score informs judgment; it does not replace hard constraints or human values.

### 12.6 Commitment Premortem

Before selection:

> Assume this plan was implemented and failed badly. What were the most plausible causes?

The resulting failure modes must be:

- Mitigated.
- Monitored.
- Accepted by an authorized owner.
- Or used to reject the plan.

### 12.7 Red Team gate

The Red Team receives:

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

### 12.8 Exit gate

The HOW stage is complete when:

- Multiple meaningful alternatives were considered.
- Hard constraints were applied.
- The preferred option survives sensitivity and adversarial checks.
- A fallback or abort condition exists.
- The decision record explains why the option was chosen.

***

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

Subtasks are decomposed only as deeply as necessary. If an executor repeatedly fails, the meta-controller may invoke ADaPT-style further decomposition.

### 13.2 Action classes

| Class | Example                         | Default requirement                                   |
| ----- | ------------------------------- | ----------------------------------------------------- |
| `A0`  | Internal reasoning              | No external permission                                |
| `A1`  | Read-only retrieval             | Logged tool access                                    |
| `A2`  | Reversible sandbox modification | Automated verification                                |
| `A3`  | External but reversible action  | Explicit authorization and rollback                   |
| `A4`  | Consequential or costly action  | Independent verifier and human approval               |
| `A5`  | Irreversible/high-stakes action | Dual control, expert validation, formal incident plan |

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
- Resource overruns.
- Contradictory observations.
- Security anomalies.
- Repeated unproductive actions.
- Changes in environment or user intent.

### 13.6 Stakeholder communication

Communication records:

- What the audience currently thinks and does.
- What they should think and do afterward.
- The evidence supporting each requested change.
- Decisions, owners, deadlines, and unresolved objections.

Each recommendation should be concise enough to act on and detailed enough to audit.

### 13.7 Exit gate

Execution ends when:

- Success metrics are met.
- A stop condition is triggered.
- The plan is proven infeasible.
- Risk exceeds delegated authority.
- The system requires human escalation.

***

## 14. Stage 5 — REVIEW: Reflect, Learn, and Evolve

### 14.1 After-Action Review

Every meaningful episode asks:

1. What was supposed to happen?
2. What actually happened?
3. Why was there a difference?
4. What should happen next?

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

### 14.4 Memory consolidation

Review output is divided into:

- Episode facts.
- Reusable semantic lessons.
- New or revised procedures.
- Unresolved questions.
- Calibration updates.
- Proposed architecture changes.

### 14.5 Kaizen rule

Most improvements should be:

- Small.
- Testable.
- Reversible.
- Attributable to a clear cause.
- Evaluated against a stable baseline.

Large rewrites require stronger evidence because they make regressions harder to localize.

***

## 15. Continuous VERIFY Layer

Verification is not a final proofreading step. It surrounds the entire loop.

### 15.1 Verification registry

| Claim type | Preferred verifier                                         |
| ---------- | ---------------------------------------------------------- |
| Factual    | Primary sources, retrieval, provenance checks              |
| Numerical  | Calculator, executable code, independent recomputation     |
| Logical    | Formal proof, solver, counterexample search                |
| Software   | Tests, static analysis, type checking, sandbox execution   |
| Causal     | Experiment, intervention, counterfactual analysis          |
| Physical   | Sensors, measurement, simulation plus real observation     |
| Policy     | External policy engine and authorized human                |
| Security   | Adversarial tests, isolation, permission audit             |
| Social     | Stakeholder confirmation and behavioral observation        |
| Creative   | Requirement testing, user evaluation, comparative critique |

### 15.2 Proposer-verifier separation

When consequences are meaningful:

- The proposer should not be the only verifier.
- The verifier should receive objective criteria.
- The verifier should have access to different evidence or tools where possible.
- Verification failure should produce a specific counterexample or test result.
- If no reliable verifier exists, autonomy must be reduced.

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
  verifier_identity:
  verifier_reliability:
  confidence:
  recommendation:
```

### 15.4 Proof-carrying result

The final output should include a concise decision packet:

```yaml
result:
  conclusion:
  status:
  assumptions:
  evidence:
  alternatives_considered:
  verification:
  uncertainty:
  limitations:
  risks:
  required_human_actions:
```

This is preferable to an unsupported narrative claiming that the system “thought carefully.”

***

## 16. Reasoning Method Composer

The meta-controller selects methods based on the problem signature.

| Problem signal             | Preferred methods                                      |
| -------------------------- | ------------------------------------------------------ |
| Familiar, low-risk pattern | RPD, checklist, retrieval                              |
| Ambiguous goal             | GROW, Socratic clarification, frame ensemble           |
| Root-cause question        | Issue tree, 5 Whys, Ishikawa, Bayesian model           |
| Contradictory requirements | TOC, TRIZ, dialectical synthesis                       |
| Creative design            | CPS, SCAMPER, analogies, Six Hats                      |
| Long-horizon planning      | Hierarchical planning, ADaPT, tree search              |
| High uncertainty           | Active learning, value of information, safe probes     |
| Dynamic environment        | ReAct, OODA, receding-horizon planning                 |
| Scientific question        | Hypothesis, prediction, experiment, replication        |
| Adversarial setting        | Threat modeling, Red Team, game theory                 |
| Stakeholder conflict       | Nemawashi, Design Thinking, interest-based negotiation |
| High-impact decision       | Premortem, independent verification, human gate        |
| Repeated task              | Procedural memory, automation, Kaizen                  |
| Novel task class           | Self-Discover-style method composition                 |

The method composer itself should learn from historical performance, while retaining fixed safety constraints.

***

## 17. Multi-Agent Collective

### 17.1 Roles

| Role            | Responsibility                                   |
| --------------- | ------------------------------------------------ |
| Coordinator     | Maintains task state, budgets, and dependencies  |
| Frame Critic    | Challenges scope, assumptions, and key questions |
| Diagnostician   | Builds causal models and hypotheses              |
| Researcher      | Retrieves and grades evidence                    |
| Explorer        | Generates diverse alternatives                   |
| Planner         | Builds executable hierarchical plans             |
| Formal Verifier | Checks logic, math, code, and constraints        |
| Red Team        | Searches for failures and adversarial cases      |
| Safety Agent    | Evaluates policy, permission, and harm           |
| Implementer     | Executes authorized tasks                        |
| Synthesizer     | Produces the integrated decision record          |
| Reviewer        | Performs AAR and proposes lessons                |

These roles can be separate models, separate contexts, software modules, humans, or combinations.

### 17.2 Council protocol

```text
1. Decompose the task where useful.
2. Give agents clean, role-specific contexts.
3. Generate initial answers independently.
4. Normalize answers into claims, evidence, and uncertainties.
5. Run objective verifiers.
6. Aggregate verified results.
7. Debate only unresolved contradictions.
8. Run a Red Team challenge.
9. Preserve dissent and minority evidence.
10. Synthesize.
11. Run a final independent gate.
```

### 17.3 Aggregation rules

- Correctness is not determined by rhetorical persuasiveness.
- Majority voting is used only when candidate independence and competence are sufficient.
- Objective tests outrank votes.
- Agent weights are based on verified domain performance, not self-confidence.
- Consensus without new evidence is not progress.
- A correct minority answer must remain recoverable.
- The final report includes unresolved disagreements.

### 17.4 When not to use a council

Do not use multi-agent debate when:

- The task has a deterministic calculator or solver.
- One high-quality source answers the question.
- Agents would share the same blind spot.
- Coordination cost exceeds expected benefit.
- Time pressure requires immediate safe stabilization.
- The action cannot be safely authorized regardless of consensus.

***

## 18. Memory and Knowledge Architecture

### 18.1 Memory classes

| Memory      | Content                                                    |
| ----------- | ---------------------------------------------------------- |
| Working     | Active goals, current observations, temporary calculations |
| Episodic    | Time-stamped task trajectories and outcomes                |
| Semantic    | Validated facts, concepts, relationships, models           |
| Procedural  | Skills, workflows, prompts, code, action policies          |
| Prospective | Future commitments, deadlines, unresolved intentions       |
| Normative   | User preferences, policies, values, permissions            |
| Audit       | Immutable decision, action, and approval records           |

### 18.2 Memory write protocol

```text
Candidate memory
→ classify content type
→ validate provenance
→ label trust and uncertainty
→ detect contradiction
→ apply privacy and permission policy
→ assign expiry or review date
→ store
→ monitor later use
```

### 18.3 Retrieval score

A conceptual retrieval score is:

```text
relevance
× reliability
× task applicability
× recency
× transfer value
× permission
− contradiction risk
− poisoning risk
```

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

***

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

### 19.3 Self-model

The agent maintains calibrated knowledge of:

- Its capabilities by domain.
- Historical success and failure rates.
- Available tools.
- Current permissions.
- Known blind spots.
- Resource limits.
- Reliability of its verifiers.
- Conditions requiring human help.

The self-model must be based on evaluation history rather than unrestricted introspection.

***

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

### 20.3 Defense in depth

AgentDojo and broader agent-security evaluations demonstrate that tool-using agents are vulnerable to prompt injection and related attacks. AI-control research further motivates assuming that a powerful component may be unreliable or even adversarial. Established security principles such as least privilege, complete mediation, and defense in depth should therefore be enforced by systems outside the model prompt. ([arxiv.org](https://arxiv.org/abs/2406.13352?utm_source=openai))

Required controls include:

- Sandboxing.
- Network restrictions.
- Input and output validation.
- Tool argument schemas.
- Read-only defaults.
- Secret isolation.
- Rate and cost limits.
- Human approval.
- Independent monitors.
- Immutable logging.
- Emergency interruption.
- Rollback or compensation.

***

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

### 21.3 Threat model

The safety system must address:

- Direct and indirect prompt injection.
- Tool-return injection.
- Memory poisoning.
- Secret extraction.
- Unauthorized actions.
- Reward and benchmark gaming.
- Deceptive behavior.
- Model or agent collusion.
- Sycophancy and majority pressure.
- Unsafe self-modification.
- Emergent collective behavior.
- Irreversible side effects.
- Human manipulation.
- Evaluation awareness.

### 21.4 Human gates

Human approval is required for:

- Irreversible or high-stakes actions.
- Changes to goals, values, or permissions.
- Deployment of architectural self-modifications.
- Access to highly sensitive data.
- Broad external communication or financial transactions.
- Actions in chaotic domains where consequences cannot be adequately simulated.
- Expansion of autonomy, replication, network access, or resource budgets.

***

## 22. Self-Evolution Engine

### 22.1 Improvement levels

| Level | Change target                             | Default authority             |
| ----- | ----------------------------------------- | ----------------------------- |
| `R0`  | Current answer or plan                    | Autonomous                    |
| `R1`  | Episodic and semantic memory              | Autonomous with validation    |
| `R2`  | Procedural skill or workflow              | Sandbox and benchmark gate    |
| `R3`  | Tools, prompts, routing, or agent roles   | Independent review and canary |
| `R4`  | Model weights or core architecture        | Controlled offline process    |
| `R5`  | Goals, values, safety kernel, permissions | Never autonomously authorized |

### 22.2 Change proposal

```yaml
improvement:
  problem_observed:
  supporting_episodes:
  proposed_change:
  target_component:
  expected_gain:
  expected_risk:
  affected_capabilities:
  evaluation_plan:
  rollback_plan:
  required_approvals:
```

### 22.3 Acceptance pipeline

```text
Propose
→ static policy check
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

### 22.4 Evaluation requirements

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

### 22.5 Open-ended improvement

An archive of diverse candidate systems may be maintained, as in evolutionary or open-ended search. However:

- Candidates remain sandboxed.
- Lineage is recorded.
- No candidate receives production authority automatically.
- Diversity is preserved to prevent premature convergence.
- Improvement is measured across a portfolio, not one task.
- The evaluation system itself is protected from modification by candidates.

***

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

***

## 24. Reference Implementation Specification

### 24.1 Core components

| Component             | Function                                            |
| --------------------- | --------------------------------------------------- |
| `GoalManager`         | Maintains authorized objectives and priorities      |
| `MetaRouter`          | Selects route, effort, methods, and agent count     |
| `Workspace`           | Stores structured active task state                 |
| `MethodComposer`      | Selects and combines reasoning modules              |
| `Planner`             | Creates hierarchical plans and fallback paths       |
| `EvidenceService`     | Retrieves, grades, and tracks evidence              |
| `WorldModel`          | Predicts transitions and maintains causal state     |
| `CouncilOrchestrator` | Runs independent agents and targeted debate         |
| `VerifierRegistry`    | Selects objective checks by artifact type           |
| `MemoryManager`       | Writes, retrieves, consolidates, and expires memory |
| `ToolBroker`          | Enforces schemas, permissions, and transactions     |
| `SafetyKernel`        | Applies policy and human gates                      |
| `ExecutionMonitor`    | Detects drift, anomalies, and failed postconditions |
| `ReviewEngine`        | Performs AAR and lesson extraction                  |
| `ImprovementEngine`   | Proposes and evaluates scaffold changes             |
| `EvaluationPlane`     | Runs capability, safety, and regression suites      |
| `AuditLog`            | Records immutable decisions and actions             |

### 24.2 Shared task state

```yaml
task_state:
  task_id:
  goal_contract:
  route:
    context_class:
    effort_level:
    reasoning_modules:
    budget:
  frame:
  world_state:
  hypotheses:
  evidence:
  uncertainties:
  alternatives:
  decision:
  plan:
  permissions:
  risks:
  actions:
  observations:
  verification:
  result:
  review:
  memory_updates:
  improvement_proposals:
  audit_refs:
```

### 24.3 Core interface

```text
route(task_state) -> cognitive_route

frame(request, context) -> problem_frame

diagnose(problem_frame, evidence) -> belief_state

generate(belief_state, constraints) -> candidate_set

verify(artifact, criteria) -> verification_report

select(candidate_set, verification_reports) -> decision

authorize(action, task_permissions, risk) -> capability_token

execute(action, capability_token) -> observation

review(task_state) -> lessons

propose_improvement(lessons) -> change_proposal
```

### 24.4 Main algorithm

```python
def solve(request, context):
    state = initialize_task_state(request, context)

    while True:
        state.route = meta_router.route(state)

        if not state.frame:
            state.frame = frame_problem(state)

        if state.route.requires_diagnosis:
            state.hypotheses, state.evidence = diagnose(state)

        state.alternatives = generate_candidates(state)
        candidate_reports = verify_candidates(state.alternatives, state)

        state.decision = select_candidate(
            state.alternatives,
            candidate_reports,
            state.constraints,
            state.risks,
        )

        if state.decision.requires_external_action:
            action_plan = planner.build(state.decision, state)
            authorization = safety_kernel.authorize(action_plan, state)

            if not authorization.approved:
                return escalate_or_refuse(state, authorization)

            observations = executor.run_transactionally(
                action_plan,
                authorization,
            )
            state.observations.extend(observations)

        state.verification = verify_outcome(state)

        if state.verification.success:
            state.result.status = "SOLVED"
            break

        if should_reframe(state):
            state.frame = None
            continue

        if should_retry_or_replan(state):
            continue

        state.result.status = determine_failure_state(state)
        break

    state.review = after_action_review(state)
    memory_manager.commit_validated_lessons(state.review)
    improvement_engine.queue_proposals(state.review)

    return build_decision_packet(state)
```

***

## 25. Minimal Viable Thinking Agent

A practical first implementation does not require a frontier-scale AGI project.

### 25.1 MVP components

- One capable foundation model.
- One independent verifier model or deterministic verifier.
- A Layer-0 router.
- Structured WHAT–WHY–HOW–DO–REVIEW templates.
- Web, code, calculator, and document tools.
- A sandboxed tool broker.
- Working, episodic, semantic, and procedural memory.
- Four default roles:
  - Coordinator.
  - Researcher.
  - Verifier.
  - Red Team.
- AAR and change-proposal generation.
- An immutable audit log.
- Human approval for consequential actions.

### 25.2 MVP development order

1. Implement structured state and decision records.
2. Add evidence retrieval and provenance.
3. Add criterion-specific verification.
4. Add transactional tool use.
5. Add persistent memory.
6. Add independent multi-agent generation.
7. Add targeted debate.
8. Add safety and prompt-injection evaluations.
9. Add procedural-memory updates.
10. Add sandboxed architecture search.

***

## 26. Roadmap Toward AGI and ASI Research

### Phase 0 — Structured assistant

- Adaptive routing.
- WHAT–WHY–HOW–DO–REVIEW.
- Retrieval and deterministic verification.
- No autonomous external action.

### Phase 1 — Grounded agent

- Tool broker.
- Sandboxed execution.
- Hierarchical plans.
- Environmental feedback.
- Human-approved consequential actions.

### Phase 2 — Persistent generalist

- Long-term memory.
- Skill library.
- User and domain adaptation.
- Calibration from historical performance.
- Cross-task lesson consolidation.

### Phase 3 — Collective problem solver

- Heterogeneous specialist agents.
- Independent candidate generation.
- Verifier-weighted synthesis.
- Large parallel workflows for decomposable tasks.
- Shared structured workspace.

### Phase 4 — Continual learner

- Active curricula.
- Automatic experiment generation.
- Stable procedural learning.
- Transfer and forgetting controls.
- Multimodal and embodied world models.

### Phase 5 — Governed self-improving system

- Automated scaffold search.
- Sandboxed code and workflow modification.
- Portfolio evaluations.
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
- Capability evaluations before autonomy increases.
- Improvement speed limited by evaluation and containment capacity.

***

## 27. Common Failure Modes

| Failure                          | Mitigation                                       |
| -------------------------------- | ------------------------------------------------ |
| Wrong problem frame              | Multiple frames, user confirmation, frame critic |
| HOW before WHY                   | Stage gate requiring diagnosis                   |
| Confident hallucination          | Evidence and tool verification                   |
| Excessive diagnosis              | Value-of-information stopping rule               |
| First-answer anchoring           | Independent candidate generation                 |
| Self-critique echo chamber       | External and heterogeneous verifiers             |
| Debate conformity                | Private first answers and minority reports       |
| Majority error                   | Verification-weighted aggregation                |
| Planner-executor drift           | Preconditions, postconditions, checkpoints       |
| Tool hallucination               | Retrieved tool schemas and argument validation   |
| Prompt injection                 | Authority/data separation and least privilege    |
| Memory poisoning                 | Provenance, quarantine, write gates              |
| Goal drift                       | Signed goal contract outside mutable memory      |
| Reward hacking                   | Hidden and adversarial evaluations               |
| Benchmark overfitting            | Portfolio and out-of-distribution tests          |
| Unsafe self-modification         | Sandbox, approval, canary, rollback              |
| Infinite cognitive loop          | Expected-value and novelty monitors              |
| Overuse of agents                | Adaptive effort and coordination-cost accounting |
| Hidden side effects              | Transactional actions and state verification     |
| Architecture monoculture         | Diverse candidate archive and independent audits |
| Capability growth outruns safety | Mandatory capability-safety co-scaling gate      |

***

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

***

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

The architecture’s most important principle is not “think longer” or “use more agents.” It is:

> **Apply the right cognitive process, obtain the right evidence, verify through the right mechanism, act with the right authority, and learn without weakening human control.**

That combination provides a practical architecture for increasingly general AI systems while acknowledging that AGI, safe recursive self-improvement, and ASI alignment remain open research problems.

***

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

***

*End of document.*
