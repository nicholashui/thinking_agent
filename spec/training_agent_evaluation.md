# Training Agent Evaluation Protocol  
## Comparing AI Thinking Agent vs. Elite Human Thinking Models

**Document Version:** 1.0  
**Purpose:** Provide a complete, executable procedure for an evaluation agent (or human operator) to systematically test a Thinking Agent by comparing its reasoning against high-quality human thinking patterns.  
**Output Goal:** Identify where the AI Thinking Agent is stronger/weaker, extract concrete learning signals, and generate training data or critique loops for improvement.

---

## 1. Overview & Core Idea

The evaluation treats **elite human thinking** as the gold-standard baseline.

We define a set of **named Human Thinking Models** (high-quality reasoning styles and cognitive strategies used by top human thinkers).  

For each selected Human Thinking Model we:

1. Create carefully designed **Positive Test Cases** (scenarios where that thinking style should excel) and **Negative Test Cases** (scenarios that expose its common failure modes or limitations).
2. Run the same scenarios through:
   - The **Human Thinking Model** (simulated by a strong frontier model prompted to reason strictly in that style, or real human experts when available).
   - The **AI Thinking Agent** under test.
3. Perform a structured side-by-side comparison.
4. Generate a clear judgment: which performed better and *why*.
5. Extract actionable learning points the AI Thinking Agent can absorb.

The final deliverable of a full run is a structured evaluation report + training signals that can be fed back into critic / self-refinement / fine-tuning loops.

---

## 2. Definitions

### Human Thinking Model
A named, well-defined reasoning style or cognitive strategy that high-performing humans deliberately use. Examples include First Principles Thinking, Inversion, Bayesian Updating, Systems Thinking, Red Teaming, etc.

### Positive Test Case
A scenario carefully constructed so that the specific Human Thinking Model is expected to produce high-quality results. Success here demonstrates strength.

### Negative Test Case
A scenario designed to expose the known weaknesses, biases, or blind spots of that particular Human Thinking Model. Failure (or suboptimal performance) here is informative.

### Comparison Dimensions
Every pair of outputs is scored on:

- **Correctness / Goal Achievement**
- **Reasoning Quality** (logical validity, coherence, depth, absence of hallucinations)
- **Efficiency** (number of steps, tokens, unnecessary exploration)
- **Robustness & Calibration** (handling of uncertainty, recognition of unsolvable cases)
- **Transferability / Generality** (how well the reasoning generalizes)

---

## 3. The 100 Best Human Thinking Models (Core Set + Expansion Method)

### 3.1 Core Named Human Thinking Models (Starter Set – Expand to 100)

Use the following high-quality named models as the foundation. Expand toward 100 by combining, specializing by domain, or adding lesser-known expert strategies.

**Foundational & First-Principles Family**
1. First Principles Thinking
2. Second-Order / Second-Order Consequences Thinking
3. Inversion (Invert, always invert)
4. Occam’s Razor + Complexity Awareness
5. Fermi Estimation / Back-of-the-Envelope Reasoning

**Probabilistic & Bayesian Family**
6. Bayesian Updating
7. Expected Value Thinking
8. Probabilistic Forecasting (Superforecasting style)
9. Base Rate Neglect Avoidance
10. Calibration & Confidence Intervals

**Systems & Causal Family**
11. Systems Thinking (feedback loops, stocks & flows)
12. Causal Reasoning (Pearl-style / do-calculus intuition)
13. Root Cause Analysis (5 Whys + deeper)
14. Constraint Theory / Bottleneck Thinking
15. Emergence & Complexity Awareness

**Dialectical & Critical Family**
16. Socratic Method / Question-Driven Inquiry
17. Dialectical Reasoning (Thesis → Antithesis → Synthesis)
18. Steel-manning
19. Red Teaming / Devil’s Advocate
20. Pre-Mortem Analysis

**Decision & Strategic Family**
21. OODA Loop
22. Decision Trees & Scenario Planning
23. Opportunity Cost Thinking
24. Regret Minimization Framework
25. Real Options Thinking

**Creative & Analogical Family**
26. Analogical Reasoning / Pattern Transfer
27. Design Thinking (Empathize → Define → Ideate → Prototype → Test)
28. Lateral Thinking
29. Combinatorial Creativity
30. Constraint-Driven Creativity

**Scientific & Empirical Family**
31. Scientific Method (Hypothesis → Experiment → Update)
32. Falsificationism (Popper)
33. Controlled Experiment Design
34. Measurement & Operationalization
35. Replication & Robustness Checks

**Additional High-Value Models (continue expanding)**
36. Mental Models Latticework (Munger-style)
37. Circle of Competence Awareness
38. Margin of Safety
39. Asymmetric Upside / Barbell Strategy
40. Leverage Points Identification
41. Hierarchical Decomposition
42. Abstraction Laddering
43. Temporal Thinking (short vs long-term)
44. Multi-Perspective Taking (Stakeholder Analysis)
45. Ethical Reasoning Frameworks (utilitarian, deontological, virtue)
... (continue systematically to reach ~100 by domain specialization: engineering, science, business strategy, medicine, law, creative writing, etc.)

### 3.2 How to Expand to ~100
- Take each core model and create domain-specialized variants (e.g., “First Principles in Software Architecture”, “Bayesian Updating in Medical Diagnosis”).
- Add named methods from cognitive science, military strategy, scientific discovery, and elite practitioners.
- Maintain a living registry: `human_thinking_models.json` with name, short description, known strengths, known weaknesses, and example prompts.

---

## 4. Step-by-Step Evaluation Procedure

### Phase 0 – Preparation
1. Load or define the AI Thinking Agent under test (with full trace logging enabled).
2. Prepare a strong baseline LLM (or ensemble) that will simulate the Human Thinking Models.
3. Create or load the registry of Human Thinking Models.
4. Decide the evaluation scope for this run (e.g., 8–15 models for a focused session, or larger batch).

### Phase 1 – Select Human Thinking Models for This Run
- Choose a diverse subset (recommended starting size: 8–12 models covering different families).
- For each selected model, record:
  - Name
  - Short definition
  - Known strengths
  - Known failure modes / biases

### Phase 2 – Design Test Cases for Each Selected Model

For **every** selected Human Thinking Model, create:

**Positive Test Cases (2–4 recommended)**
- Scenarios where this thinking style is particularly powerful.
- Clear success criteria.
- Preferably verifiable or graded outcomes.

**Negative Test Cases (2–3 recommended)**
- Scenarios that trigger the known weaknesses of this thinking style.
- Cases where pure application of the style leads to suboptimal or incorrect conclusions.
- Edge cases, ambiguous information, missing data, adversarial framing, or conflicting goals.

**Test Case Template**
```markdown
### Test Case ID: [MODEL]-[POS/NEG]-[Number]
- **Human Thinking Model**: 
- **Type**: Positive / Negative
- **Scenario**:
- **Context / Constraints**:
- **Expected High-Quality Behavior**:
- **Success Criteria / Scoring Rubric**:
- **Notes**:
```

### Phase 3 – Generate Human Baseline Responses
For each test case:
1. Prompt a strong frontier model (or real expert) with a carefully engineered system prompt that forces it to reason **strictly in the style of the named Human Thinking Model**.
2. Require full visible thinking / reasoning trace.
3. Store the complete response + trace as the **Human Baseline**.

### Phase 4 – Run the AI Thinking Agent
- Run the exact same test cases through the AI Thinking Agent under test.
- Capture the **full thinking trace** + final output.
- Do **not** reveal the Human Thinking Model name to the AI agent (to avoid contamination).

### Phase 5 – Structured Comparison
For every test case, perform a side-by-side evaluation using the following dimensions (score 1–5 or use detailed rubric):

| Dimension                  | Human Score | AI Score | Winner | Notes |
|---------------------------|-------------|----------|--------|-------|
| Goal Achievement          |             |          |        |       |
| Logical Validity          |             |          |        |       |
| Coherence & Structure     |             |          |        |       |
| Depth of Reasoning        |             |          |        |       |
| Efficiency                |             |          |        |       |
| Handling of Uncertainty   |             |          |        |       |
| Insight / Non-obviousness |             |          |        |       |
| Overall Quality           |             |          |        |       |

**Overall Judgment** for the case:
- Human clearly better
- AI clearly better
- Roughly equal
- Different strengths (complementary)

### Phase 6 – Learning Extraction
For every comparison, answer:

1. **What did the stronger side do that the weaker side missed?**
2. **What specific thinking moves or patterns should the AI Thinking Agent adopt?**
3. **What failure mode did the AI exhibit that the human style avoided (or vice versa)?**
4. **Concrete prompt / process / architectural change recommendations.**

Produce structured learning signals in a format usable by critic agents or fine-tuning pipelines, e.g.:

```json
{
  "test_case_id": "...",
  "human_model": "...",
  "winner": "human | ai | tie",
  "key_gap": "...",
  "learning_signal": "...",
  "suggested_improvement": "..."
}
```

### Phase 7 – Aggregate Report
Compile:
- Per-model summary (strengths/weaknesses of the AI relative to that human style)
- Global patterns (recurring failure modes of the AI Thinking Agent)
- Prioritized list of improvements
- Recommended next training / refinement actions
- Updated ranking of which Human Thinking Models the AI currently matches or exceeds

---

## 5. Recommended Execution Workflow for an Evaluation Agent

An automated evaluation agent should follow this sequence:

1. Load configuration (list of Human Thinking Models to test, number of positive/negative cases per model).
2. For each Human Thinking Model:
   a. Generate or retrieve Positive + Negative test cases.
   b. Generate Human Baseline responses.
   c. Run AI Thinking Agent on the same cases.
   d. Perform comparison using LLM-as-Judge + optional human review.
   e. Extract learning signals.
3. Aggregate all results into a single evaluation report.
4. Output both human-readable markdown report and machine-readable learning signals (JSON/YAML).
5. Optionally push learning signals into a critic loop or training data pipeline.

---

## 6. Output Artifacts

A complete evaluation run must produce:

1. `evaluation_report.md` — full narrative + tables
2. `learning_signals.json` — structured improvement data
3. `test_cases/` — all scenarios used
4. `traces/` — full thinking traces from both human baseline and AI agent
5. `comparison_matrix.csv` or equivalent for quantitative tracking over time

---

## 7. Quality Gates & Best Practices

- Always keep the Human Thinking Model prompt strict and pure.
- Never let the AI Thinking Agent see the name or description of the Human Thinking Model during inference.
- Prefer verifiable or graded outcomes whenever possible.
- Run multiple trials on non-deterministic agents.
- Periodically calibrate the comparison judge against human expert ratings.
- Track historical performance so you can measure whether the AI Thinking Agent is closing the gap over time.
- Balance Positive and Negative cases; Negative cases often yield the most valuable learning signals.

---

## 8. Example Minimal Run (Illustration)

**Selected Human Thinking Model**: Inversion  
**Positive Case**: “How can we ensure this critical system never fails in production?”  
**Negative Case**: A situation where excessive inversion leads to paralysis or over-engineering.

Then run both the pure Inversion baseline and the AI Thinking Agent, compare, and extract lessons such as:  
“The AI agent jumped to solutions too quickly without systematically listing failure modes. It should adopt a mandatory inversion pass before proposing solutions.”

---

## 9. Continuous Improvement Loop

1. Run evaluation → extract learning signals
2. Feed signals into critic / self-refinement / prompt update / fine-tuning
3. Re-run a subset of previous test cases (regression)
4. Expand to new Human Thinking Models or harder scenarios
5. Repeat

This turns evaluation into an active training mechanism rather than a one-time score.

---

**End of Protocol**

This document is designed to be followed directly by an AI evaluation agent or a human operator.  
All steps are intentionally concrete so they can be turned into code, prompts, or agent workflows.
