# AI Thinking Agent — Trace — m099-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = decide which driver Meridian's churn strategy should target, showing the belief update; external action = none (decision brief).

## Stage 0 — META-CONTROL
- **Context:** $18M ARR, 600 accounts, ~1.8%/mo churn (~$320K/mo at risk); org policy (<2h SLA as churn lever) built on exit-interview anecdotes; a 6-month measured cohort of 600 accounts with two drivers (first-response speed, onboarding completion). **Stakes:** medium-high. **Effort:** E3. **Route:** complicated (evidence-dependent policy shift). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** deliverable = which driver to invest in, with a quantified belief update from the cohort and the policy change it licenses. Success metric: a posterior-based policy with effect size and re-measurement plan. **Gate:** data is in hand; no missing evidence blocks the frame. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: prior → likelihood → posterior → policy.** Prior: P(speed drives churn) = 0.75, provenance: exit interviews + folklore — a stated prior, updateable, not evidence. Hypotheses with predicted churn rates: H_speed (fast 15% / slow 25%), H_onboarding (completed 10% / not 30%), H0 (20% both). Cohort: 600 accounts, 120 churned; speed: 60/300 vs 60/300 (flat); onboarding: 30/300 vs 90/300 (10% vs 30%). **G-WHY:** two channels disagree — the exit interviews measure what customers SAID, the cohort measures what they DID; on a churn decision the did-channel dominates. No missing evidence. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — keep the SLA policy, treat the cohort as noise · B — full Bayesian update: onboarding wins, redirect CS budget · C — split the difference, half the budget to each driver.
- **Verification + selection:** A fails: the speed cohort is 20%/20% over 600 accounts — the gradient H_speed needed is absent; its full-data likelihood ≈ 0.07× H0. C fails: averaging policies while ignoring a ~10^10 odds ratio is a compromise on the wrong axis. **Select B**: full-data LR = L(H_onboarding)/L(H_speed) = e^24 ≈ 3×10^10; posterior odds = prior odds (1:3) × 3×10^10 ≈ 10^10:1; P(onboarding drives churn) ≈ 1 − 10^-10. Effect size: 30% → 10% churn at completion (≈20pp, a 2/3 reduction); >90% completion is worth ≈0.8pp/mo — half of current churn.
- **Premortem:** if B is wrong, it is because completion is confounded with account size. Mitigated: quarterly cohort re-check + segment regression before the SLA budget is fully cut.

## Stage 4 — DO
- External action: none; deliverable = the decision brief. Verification: update arithmetic re-checked (prior odds 1:3 × LR 3×10^10 → posterior ≈ 1); every policy line traces to the posterior, none to the anecdotes.

## Stage 5 — REVIEW
- **AAR + calibration:** the load-bearing move was treating the anecdote as a stated prior with provenance — updateable, not dismissible — and the said-vs-did channel comparison. Gap: I did not bound the confound risk (account size) until the premortem. Confidence: high on direction; medium on effect size (single cohort, no segment controls).

## Decision Packet
- **Conclusion:** churn is onboarding-driven, not speed-driven. Redirect CS budget from the <2h SLA to an onboarding-completion program (target >90% completion within 30 days); kill SLA-as-churn-lever; re-run the cohort quarterly with a segment control before fully cutting the SLA budget. **Status:** SOLVED (decision brief; no external execution).
- **Assumptions:** the 600-account cohort is representative (no selection); completion is not confounded with account size (checked next quarter); exit-interview statements understate true drivers.
- **Evidence:** speed cohort 20%/20% (60/300 each); onboarding 10% vs 30% (30/300 vs 90/300); LR(H_o|H_s) = e^24 ≈ 3×10^10; posterior odds ≈ 10^10:1; prior 0.75 (anecdote-held).
- **Alternatives:** A keep SLA (rejected — flat speed cohort) · C split budget (rejected — ignores a 10^10 odds ratio) · B onboarding-first (selected).
- **Uncertainty:** effect-size precision (counts 30/300 vs 90/300); confound risk (account size); next-quarter regression to mean.
- **Risks:** SLA degradation hurts NPS (mitigated: SLA stays; only its churn attribution goes) · completion program misses >90% (mitigated: quarterly cohort + segment check before further cuts) · single-cohort correlation ≠ causation (mitigated: pre-registered quarterly re-measurement).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | tie | Identical decision: onboarding-first, SLA-as-churn-lever killed, quarterly re-measure |
| Logical Validity | 5 | 5 | tie | Same checkable update: prior odds 1:3 × LR e^24 → posterior ≈ 1 |
| Coherence & Structure | 4 | 5 | AI | Human linear first-pass; AI staged trace + packet |
| Depth of Reasoning | 5 | 4 | Human | Human lands the channel insight ("churn must be measured, not heard") and the prior's survival ("update, don't discard") in one pass; AI reaches both via machinery |
| Efficiency | 5 | 3 | Human | Human's first move is the prior and the update; AI generates a full alternative set before the update is obvious |
| Handling of Uncertainty | 3 | 4 | AI | AI packet bounds confound risk and effect-size precision; human asserts |
| Insight / Non-obviousness | 5 | 4 | Human | "The measured outcomes did not confirm the anecdotes — they replaced them" is the human's line, said with ownership |
| **Overall Quality** | **4.6** | **4.3** | **Human** | Same decision; the pure style executes the update first-pass and owns the insight; AI matches and adds auditability at scaffolding cost |

**Overall judgment:** Human clearly better (narrow). The pure style IS the answer here and lands it first-pass; the AI reproduces the identical posterior and policy but pays overhead (alternatives generation before the update is obvious) and reaches the said-vs-did insight more cautiously. Learning extraction: (1) human move the AI missed first-pass: the update-as-first-move — elicit the prior with provenance, then let the data speak, before generating alternatives; (2) adopt: the decision packet's evidence line already carries the LR arithmetic (AI strength); (3) AI failure mode: machinery before the obvious Bayesian move; (4) process change: WHAT should elicit "the org's current belief + provenance" as a first-class object for belief-update problems.
