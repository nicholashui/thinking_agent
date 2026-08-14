# AI Thinking Agent — Trace — m035-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = launch decision for a retention feature under deadline; external action = none (recommendation + implementation plan; engineering order is a human step, not executed).

## Stage 0 — META-CONTROL
- **Context:** mobile-app team must decide this quarter whether to ship the "RecFlow" feature. One study (n = 20,000, 8 weeks, client-side telemetry): 6-week retention 31.4% → 31.6% (+0.2 pp, n.s.). A colleague proposes a 12-week, n = 30,000, ≈ $40k confirmatory replication with a second analytics vendor before deciding. Competitor ships a similar feature in ~4 months; seasonal retention dip begins in ~2 months. **Stakes:** medium-high (revenue, competitive window, feature investment). **Effort:** E3. **Route:** evidence-based launch decision (Cynefin: complicated). **Safety:** none. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the decision is "does the feature ship this quarter, on the best evidence obtainable inside the window." The question is not "do we have enough data" but "is the data we have trustworthy, and what would actually repair it?" **Gate:** measurement-validity screen on the study's instrument — client-side telemetry with known platform limits → **gate fails → NEEDS_EVIDENCE** (missing evidence: session coverage / missingness mechanism).

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1 the null is genuine; H2 the null is an artifact of biased instrumentation; H3 a real but small effect is underpowered here.
- **Evidence + falsification:** coverage audit — the client-side heartbeat drops Android 13+ background sessions and ad-blocker sessions: 31% of sessions unmeasured, missingness correlated with light usage (the users most likely to churn). The study's 31.4 / 31.6% was computed on 69% of sessions, and the missing 31% is not missing at random. H2's mechanism is documented and confirmed; H1 is unfounded (the study never measured 31% of its population) and unfalsifiable on biased data. Power: n = 20,000 detects ≥ 0.5 pp at 80% → H3 secondary. Replication check: the second vendor's SDK is the same client-side class with the same platform limits → a replica of a biased instrument is biased identically; replication settles variance, not bias. **Gate passed** (bias established; replication ruled out as a remedy).

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A replicate with the second vendor (rejected: 12 weeks + $40k; inherits the 31% blind spot; decision lands past the seasonal dip and near the rival window) · B repair the measurement layer: wire the licensed server-side pipeline (1 week) and backfill/re-analyze the SAME study from server-side logs (1 week) → decision in ~2 weeks, inside the window (**selected**) · C launch anyway with monitoring (rejected: cannot separate feature effect from measurement bias) · D kill the feature (rejected: no valid measurement exists; premature).
- **Verification + selection:** server-side logs cover the full session stream including the dropped 31% → the corrected retention is computable from data that already exists; B is 1/6 the duration and removes the bias mechanism A would inherit. **Select B. Premortem:** backfill shows a corrected null → switch to C′ (launch with monitoring if the feature is otherwise sound); corrected result shows a real effect → accelerate launch. Both branches land inside the window.

## Stage 4 — DO
- External action: none. Deliverable = decision memo: reject the replication proposal; order server-side instrumentation (1 week) + backfill re-analysis of the existing 20k study (1 week); launch decision at week 2 on the corrected number; C′ and accelerate paths pre-planned.

## Stage 5 — REVIEW
- **AAR + calibration:** decisive move = auditing the measurement layer before the variance layer (bias check before replication check). The proposed replication was not a robustness check of the result — it was a ritual that would faithfully reproduce a known blind spot at triple the cost and outside the decision window. Lesson: when the instrument is biased, more studies are not the remedy; repairing the instrument and re-measuring is. Confidence in B high (mechanism documented); residual uncertainty = backfill data quality (±0.3 pp), handled by pre-registered thresholds.

## Decision Packet
- **Conclusion:** reject the 12-week replication; repair the measurement layer (server-side pipeline, 1 week) and re-analyze the existing experiment from server-side logs (1 week); resolve the launch decision at week 2 with corrected retention, inside the seasonal and competitive windows. **Status:** SOLVED (decision verified: bias mechanism documented; A fails its own goal; B is in-window and removes the bias).
- **Assumptions:** server-side logs retained for the study window (licensed pipeline exists); the 31% missingness rate is stable across the study; corrected thresholds pre-registered.
- **Evidence:** coverage audit (31% unmeasured; Android 13+ / ad-block mechanism), power analysis (≥ 0.5 pp detectable), cost/calendar table (12 w / $40k vs 2 w), vendor-SDK equivalence.
- **Alternatives:** A replicate (rejected) · B instrument repair + backfill (selected) · C launch-with-monitoring now (rejected; reserved as C′ if corrected null holds) · D kill feature (rejected).
- **Uncertainty:** corrected effect size unknown until week 2 (±0.3 pp data-quality risk); missingness rate drift.
- **Risks:** backfill incomplete (fallback: extend 1 week, still in window); corrected null → launch decision falls to other evidence with monitoring (C′); the replication was never a risk reducer here.
## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human's plan misses both windows and reproduces the blind spot; AI's plan resolves the decision in 2 weeks |
| Logical Validity | 3 | 5 | AI | Human is internally consistent but "replicate the biased instrument" is a non-sequitur as a fix; AI separates bias from variance |
| Coherence & Structure | 3 | 5 | AI | Human stops at the replication plan; AI closes with packet, branches, and fallbacks |
| Depth of Reasoning | 2 | 5 | AI | Human never audits coverage or missingness; AI documents the mechanism and its non-randomness |
| Efficiency | 2 | 4 | AI | Human: 12 weeks / $40k for a decision outside the window; AI: 2 weeks in-window (spends passes, but on the winning audit) |
| Handling of Uncertainty | 2 | 5 | AI | Human assumes the replication settles it; AI pre-registers thresholds and pre-plans both corrected outcomes |
| Insight / Non-obviousness | 2 | 5 | AI | "Replication reproduces the blind spot; the fix is the instrument" is the AI's insight; the human's is the ritual itself |
| **Overall Quality** | **2.3** | **4.9** | **AI** | Negative case does its job: pure style falls into replication ritual; the agent's measurement-validity gate escapes it |

**Overall judgment:** AI clearly better. The negative case exposes exactly the registry-listed weakness — "time cost; can become ritual" — and the agent's bias-before-variance gate converts correct framing (the null is unfounded, not confirmed) into a correct, in-window decision.
