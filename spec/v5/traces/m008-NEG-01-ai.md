# AI Thinking Agent — Trace — m008-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided to the agent); task = board forecast memo; external action = none (recommendation only).
## Stage 0 — META-CONTROL
- Context: one-off binary outcome (Aurora ≥ 10k WAUs by week 8 post-launch); no reference class; two beta data points; three non-metric news events; board demands a number.
- Stakes: medium (staffing ramp, costly to reverse). Effort: E2. Route: estimation with thin evidence (Cynefin: complicated-to-complex boundary).
- Safety: advisory only. Proceed.
## Stage 1 — WHAT: Frame the Problem
- Frame: the demanded deliverable (committed probability ± tight CI) is not warranted by the evidence; reframe as an honest probability, a deliberately wide range, revision rules, and a decision lever.
- Gate (WHAT): solvable? Partially — the question is well-defined and resolves at week 8, but the evidence cannot support precision. Proceed with L1 degrade.
## Stage 2 — WHY: Diagnose and Model
- Hypotheses: H1 growth sustains → P(≥10k) high (≥ 0.5); H2 early spike decays → P(≥10k) low (0.1–0.2); H3 precision is knowable from two points (the board's implicit claim).
- Evidence: two beta points (1,800 → 2,200, +22%/wk); no retention/cohort/channel data; no reference class (checked — none exists for category-new products).
- Falsification: H3 falsified now — a 1-parameter fit from n = 2 points has 0 residual df; any CI width is model-asserted, not evidence-derived. H3 rejected.
- Gate (G-WHY): evidence gap for H1 vs H2 — missing_evidence = [week-2 post-launch retention, install velocity by channel, activation share]. Gate fails → NEEDS_EVIDENCE (L1 degrade); continue with an honest wide forecast rather than a fake precise one.
## Stage 3 — HOW: Generate, Test, and Select
- A. Precision theater: P = 0.33, 90% CI [8.2k, 11.5k] from the 2-point hockey-stick — rejected: CI width not evidence-derived; the board would act on it.
- B. Wide honest forecast: P(≥10k) ≈ 0.15 (regression to base rate for category-new products), 90% range [1k–30k] — selected.
- C. "Cannot say" — rejected: a decision is needed; a wide range IS a forecast.
- No-update rule: the three non-events (CEO X-post, competitor news, bug fix) carry no metric information → probability held at 0.15 across all three, explicitly stated.
- Revision rules (evidence that WOULD move it): week-2 retention ≥ 30% → up; install velocity < 3k/wk → down to ≤ 0.05; activation share > 50% → up. Selection: B + no-update rule + revision rules + decision lever.
## Stage 4 — DO
- External action: none. Recommendation: staged ramp — hire at 25% of the full plan; kill criteria at week 2 post-launch; the decision does not need calibration to ±5 pp.
## Stage 5 — REVIEW
- AAR: the gate failure (G-WHY → NEEDS_EVIDENCE) was the decisive move — it blocked adopting the model's false precision. Calibration: honest forecast Brier-scored at week 8; expected score vs theater forecast documented in the comparison.
## Decision Packet
- **Conclusion:** P(Aurora ≥ 10k WAUs by week 8) ≈ 0.15; 90% range [1k–30k]; probability held flat on non-events; stage the ramp with kill criteria.
- **Status:** NEEDS_EVIDENCE (missing: retention, channel install velocity, activation share; L1 degrade; decision lever provided without false precision).
- **Assumptions:** category-new products regress toward low sustained growth; beta weeks represent launch acquisition (flagged: often not).
- **Evidence:** 2 beta points; absence of reference class (verified); non-events enumerated with zero metric content.
- **Alternatives:** A theater 0.33/[8.2k–11.5k] (rejected: CI not evidence-derived) · B wide honest 0.15/[1k–30k] (selected) · C no forecast (rejected: decision needed).
- **Uncertainty:** very high; range deliberately wide; probability ±10 pp either side.
- **Risks:** if H1 is right and the firm under-hires, momentum lost — mitigated by staged ramp; base-rate judgment for novel products documented as unavoidable without data.
## Comparison
**Evaluator section (provisional; appended after both runs; resolution: NO — actual 2,900 WAUs; narrow CI [8.2k–11.5k] missed by >3 sd of its own model).**
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human's narrow CI missed the outcome; AI's wide range contained it; AI separated forecast from decision |
| Logical Validity | 3 | 5 | AI | Human's arithmetic is internally fine but built on a 0-df fit; AI rejected precision with no evidential basis |
| Coherence & Structure | 3 | 5 | AI | Human logs probability moves driven by non-events; AI explicitly holds the probability flat |
| Depth of Reasoning | 3 | 4 | AI | Human names the missing reference class but proceeds as if it didn't matter; AI operationalizes the gap |
| Efficiency | 4 | 3 | Human | Human answers fast; AI's evidence-gap analysis costs steps (the style's known 'slow' trait) |
| Handling of Uncertainty | 2 | 5 | AI | Human's 90% CI overconfident and missed; AI gives a wide range + revision triggers |
| Insight / Non-obviousness | 3 | 4 | AI | Both know the model is thin; AI adds forecast/decision separation (staged ramp) |
| **Overall Quality** | **2.9** | **4.4** | **AI** | Pure style applied to a category-new one-off produced false precision; the agent's gate stopped it |
**Overall judgment:** AI clearly better. The superforecasting failure modes (over-narrow range, forecast theater, updating without new information) are exactly what this case exposes; the AI's G-WHY gate and decision-packet structure avoided all three.
