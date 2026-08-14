# AI Thinking Agent Run — inversion-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided; the agent reasons with its own method portfolio.

---

## META — Context, stakes, effort classification
- **Task class**: growth/product adoption decision for an existing B2B product. Moderate stakes (2 FTE + limited budget, 90-day window, no safety surface). Uncertainty high (segments, activation, channels all unmeasured).
- **Cynefin-style routing**: complicated with genuine unknowns — analysis plus a small, cheap, falsifiable experiment beats pure deliberation.
- **Effort level**: balanced-analytical (medium-high); deliberate decision with a checkable checkpoint; no external execution.
- **Owner**: available (product lead); deliverable is a decision + plan.
- **Method composition**: opportunity framing + base-rate reasoning + hypothesis-driven launch with checkpoint.

## WHAT — Frame the problem
- **Frame**: "Choose the 90-day adoption plan that maximizes the number of teams reaching an activation threshold, within 2 FTE and the budget envelope, starting in 4 weeks."
- **Key question**: "Which single lever most determines whether a new feature in an existing product gets adopted — segment, activation path, or distribution — and what is the smallest bet that tests it?"
- **Success metrics (gate)**:
  1. A quantified target (activation %) with a defined activation metric.
  2. A chosen wedge with rationale (explicitly selected over alternatives).
  3. A falsifiable checkpoint: metric + date + decision rule.
- **Gate check**: metrics defined; owner available; the frame is a maximization problem — note explicitly: avoiding failures is necessary, not sufficient; proceed.

## WHY — Hypotheses, evidence, falsification
Memory/retrieval of task-relevant knowledge (feature-adoption base rates, PLG patterns):
- **H1**: The dominant failure of new-feature adoption is the absence of a wedge — no segment for whom the feature is a must-do — not a specific defect. Base rate: most feature launches flatline from weak activation and reach, not from bugs.
- **H2**: Activation friction (empty first run, setup steps) is the strongest controllable driver among teams who actually see the feature.
- **H3**: Distribution (surface area) is adequate; burying is not the binding constraint — the product already has an active daily user base.
- **Evidence available**: product usage telemetry shows the reporting module is used by analytics-heavy PM/ops teams; past features with in-app prompts alone reached only ~2% of teams — weak wedge, not weak distribution (supports H1/H3). No measurement of the new feature's activation behavior yet (not launched).
- **Falsification**: H1/H3 would be falsified if the analytics-heavy segment showed no higher report-usage density than the general population — testable in week 1 via cohort analysis of existing reporting usage. H2 is testable by comparing first-run completion between template-first and blank-first onboarding.
- **G-WHY gate**: leading hypothesis has evidence (telemetry + past-launch base rates); alternatives (H2, H3) considered; residual uncertainty recorded; falsification defined; VOI of further diagnosis low before the launch — cheap probes inside the plan → pass.

## HOW — Generate, test, select
**Alternative A — Broad-surface launch**: in-app prompts + onboarding content to all 4,000 teams; no segmentation.
**Alternative B — Wedge launch**: target the analytics-heavy PM/ops segment (~600 teams) with 5 pre-built demo templates, a "generate my weekly report" one-click template that mimics their spreadsheet workflow, and a 2-week targeted campaign; activation metric: ≥ 3 reports generated in 28 days; checkpoint at week 4.
**Alternative C — Enterprise-assisted**: sales-led outreach to top 50 accounts with white-glove onboarding.

**Verify**:
- A is contradicted by the evidence: past prompts-only launches plateaued at ~2% — it repeats a known-failed distribution pattern with no activation fix.
- C is high-value-per-account but consumes the entire 2 FTE for 50 accounts; it maximizes revenue, not adoption breadth — and the checkpoint would be weak (sample too small to falsify anything at week 4).
- B matches H1/H2: it concentrates on the segment with the highest usage density (wedge), fixes the activation path (templates + one-click), and its checkpoint is statistically meaningful (600-account cohort).
- Feasibility: 2 FTE over 4 weeks fits B's scope (templates, campaign, telemetry, template-first onboarding variant).

**Selection (decision record)**: Alternative B, with A's prompt surface as a thin second layer (prompts only to the wedge segment, not all 4,000 — avoids prompt fatigue). C deferred to week 4 review. Reason: B is the only alternative aligned with both the base-rate diagnosis (H1) and the controllable activation lever (H2), and it has a falsifiable checkpoint the others lack.

**Bounded risk pass (top-5, one mitigation each — explicitly capped, not exhaustive)**:
1. Template reports don't fit real weekly workflows → ship 5 templates, pick the 3 most-used report types by telemetry; week-1 telemetry read.
2. Demo data shapes differ from customer data → template generation uses the customer's live data, not static samples.
3. Perf regression on AI report generation → load-test before launch; < 5 s target.
4. Campaign noise → scope prompts to the wedge segment only.
5. Feature is gated behind a paywall in some plans → include in all tiers for 90 days.

## DO — Attest / authorize
- Attestation: advisory recommendation; class A2 (decision + plan, no external execution). Authorized: produce the plan. No live rollout performed in-workspace.

## REVIEW — After-action review
- What went well: goal-type discrimination (maximization ≠ reliability) drove the frame; base rates prevented repeating a known-failed pattern (A); the checkpoint converts opinion into a decision rule.
- What to record: (1) The bounded risk pass was deliberately capped at 5 — but the cap is a discipline, and the AAR must note what the cap excluded: an IT/security procurement-review gate for the feature's AI data flows was not in the pass and could stall launch in real organizations; add it as a pre-launch task. (2) The activation metric is a hypothesis; week-1 cohort analysis on existing reporting usage is the first falsification point and should gate the campaign spend. (3) Uncertainty about the wedge is the plan's biggest exposure — mitigated by the checkpoint, not by more analysis.
- Lesson folded back: procurement/security pre-clearance added to assumptions and risks.

---

## Decision Packet
- **Conclusion**: Launch wedge plan B: target the analytics-heavy PM/ops segment (~600 teams); ship 5 templates + one-click "generate my weekly report" mimicking existing spreadsheet workflow; prompts scoped to the segment only; activation metric = ≥ 3 reports generated in 28 days. Checkpoint (week 4): if ≥ 5% of the targeted segment has activated, double down (expand prompts to next segment); if < 5% and week-1 cohort analysis shows no usage-density edge for the segment, pivot to a broad-surface variant with onboarding redesign (plan A′) rather than spending the remaining 60 days on the same wedge.
- **Status**: `APPROXIMATED` — bounded, evidence-graded plan with a defined checkpoint; effect sizes unknown pre-launch (approximation error: activation-rate estimate ± large until week-1 data).
- **Assumptions**: analytics-heavy PM/ops segment has highest report-usage density (telemetry-based, to be confirmed week 1); 3-reports-in-28-days is the right activation proxy; 2 FTE is sufficient for templates + campaign; IT/security pre-clearance for AI data flows completes before launch (added at review).
- **Evidence**: reporting-module usage telemetry; past-launch base rates (prompts-only ≈ 2% activation); AI report-generation perf measurements (pre-launch load test pending).
- **Alternatives**: A (broad-surface — rejected on past-launch evidence), C (enterprise-assisted — deferred, sample too small to falsify at week 4), hold (rejected: no new information arrives by waiting).
- **Uncertainty**: highest: wedge hypothesis (is the segment actually AI-report-hungry?) — falsifiable at week 1 via cohort analysis; then activation friction, then channel efficacy.
- **Risks**: wedge wrong → 3 weeks of spend on the wrong segment (mitigation: week-1 cohort gate + week-4 pivot rule); prompt fatigue in wedge segment (mitigation: scoped prompts); procurement stall (mitigation: pre-clear now); perf regression (mitigation: pre-launch load test).

---

## Comparison — inversion-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 3 | 5 | AI | Human's plan answers "don't fail," not "maximize"; AI frames the maximization directly with a target and a wedge. |
| Logical Validity | 4 | 5 | AI | Human is internally valid but commits goal displacement (goal substitution); AI's reasoning stays on-goal. |
| Coherence & Structure | 4 | 5 | AI | Human: 12 equal-weight workstreams, no spine; AI: diagnosis → bet → checkpoint structure. |
| Depth of Reasoning | 4 | 4 | Tie | Human's enumeration is deep and catches a real risk the AI's bounded pass missed (IT/security procurement friction, item 9); AI's base-rate and falsification reasoning is deeper on the positive space. |
| Efficiency | 2 | 5 | AI | Human spreads 2 FTE across 12 workstreams; AI concentrates on one wedge with one bounded risk pass. |
| Handling of Uncertainty | 3 | 5 | AI | Human: no checkpoint, no falsification, uncertainty unmanaged; AI: week-1 cohort gate + week-4 pivot rule. |
| Insight / Non-obviousness | 3 | 4 | AI | AI's wedge insight (past-launch base rates) is the plan's spine; human's genuine insight (procurement gate) is real but incidental to its flatline. |
| Overall Quality | 3 | 5 | AI | AI clearly better on the negative case. |

**Overall judgment**: AI clearly better. Strict inversion converted a maximization problem into an equal-weighted avoidance list with no wedge, no activation metric, and no checkpoint; the AI's mixed-method run stayed on-goal, used base rates to avoid repeating a known-failed pattern, and built a falsifiable decision rule. The human's one surviving insight (procurement/IT friction) is a genuine catch that the AI's bounded risk pass missed and only recovered at AAR — a useful asymmetry, not a close contest.
