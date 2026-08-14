# AI Thinking Agent — Trace — m097-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = plan-of-record (duration, budget, contract structure) for a 9-month/$1.5M migration estimate; external action = none (decision brief).

## Stage 0 — META-CONTROL
- **Context:** letter of intent signed; bottom-up plan 9 months/$1.5M/14 engineers; firm's post-mortem database of 60 comparable migrations available. **Stakes:** high (client contract number next quarter, $1.5M+ commitment). **Effort:** E3. **Route:** complicated (estimate risk; empirical calibration data exists). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** deliverable = a defensible forecast (duration + budget) plus a contract structure. The forecast must combine two sources: the detailed plan and the firm's 60-project post-mortem history. Success metric: a plan whose numbers survive the historical evidence. **Gate:** both sources in hand; no missing evidence. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: bottom-up estimate vs empirical prior.** The plan is a sum of task-level commitments (vendor promises, lead-time assumptions) — historically optimistic for multi-integration migrations. The database is the firm's own calibration record: an average 1.8× estimate-to-actual overrun and only 2 of 60 completions under 12 months. **G-WHY:** the load-bearing question is how to combine — the database is the calibration data, the plan is the anchor to calibrate. No evidence gap. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — accept the plan as-is (9 mo, $1.5M) · B — calibrate the plan with the firm's own 1.8× overrun factor: ≈16 months, ≈$2.7M, presented as a range (14–19 mo, $2.7–3.2M) · C — distributional forecast: locate the project in the database (median 21 mo, 80% band 14–31), budget at class burn (≈$3.5–3.8M), staged contract with a hard month-14 gate · D — commission an external review of the detailed plan.
- **Verification + selection:** A fails — ignores the database. D fails — it re-audits the same genre of evidence (a bottom-up plan) at real cost. B and C both use the database; B applies the firm's measured factor to the plan, C replaces the plan with the distribution. C is structurally the strongest, but the client needs a commitment number next quarter and the database's spread (σ 7.5) makes a single-point commitment indefensible — the defensible plan is a calibrated band with the firm's own factor as the floor: quote 14–19 months, budget $2.7–3.2M, with a checkpoint at month 14. **Select B-with-range.**
- **Premortem:** if the plan is wrong, the cause is the anchor surviving calibration — mitigated by the 1.8× floor; a tail outcome like Aurora (8 months) is possible but not planable.

## Stage 4 — DO
- External action: none; deliverable = plan-of-record. Verification: calibrated figure sits inside the database's realized range; range-banded pricing avoids a point commitment; the 1.8× factor is the firm's own measured history.

## Stage 5 — REVIEW
- **AAR + calibration:** the move I made was multiplier-on-anchor; the stronger move — locating the plan inside the distribution (9 months ≈ 3rd percentile; 2/60 empirical) — was sitting in the data and I did not lead with it; the month-14 gate came from alternative C, not from my own selection. Confidence: medium-high on the range, low on the center — the center is still the anchor wearing a factor.

## Decision Packet
- **Conclusion:** plan-of-record 14–19 months (floor 16), budget $2.7–3.2M, range-banded contract with a checkpoint at month 14; flag the 9-month plan as outside the firm's own historical envelope. **Status:** SOLVED (decision brief; no external execution).
- **Assumptions:** database representative of Comet's scope family; burn ≈$167K/mo constant; client accepts a range.
- **Evidence:** inside plan 9 mo/$1.5M; database n=60: median 21, mean 22.5, σ 7.5, 10/90 = 14/31; 1.8× estimate-to-actual; 2/60 sub-12-month (incl. Aurora, 8 mo).
- **Alternatives:** A accept (rejected — ignores data) · C distributional (partially adopted: range + gate) · D external review (rejected — same evidence genre) · B factor-calibrated band (selected).
- **Uncertainty:** the 9-month anchor's residual credibility is the main risk; the class tail is real (Aurora); team quality vs class average unmeasured.
- **Risks:** true center is 21 months → under-commitment (mitigated: month-14 gate forces re-plan) · client rejects a range (mitigated: floor 16 defensible) · scope creep (the class already prices it in).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 3 | Human | Human: median 21, 80% 14–31, budget $3.5–3.8M, month-14 gate — inside the class band. AI: 14–19 (floor 16), $2.7–3.2M — ~25% below the class center |
| Logical Validity | 5 | 3 | Human | Human: estimate placed as a percentile of the distribution. AI: factor (1.8×) applied to a biased anchor — the anchor's structure survives the calibration |
| Coherence & Structure | 4 | 5 | AI | Human: linear first-pass. AI: staged trace + packet |
| Depth of Reasoning | 5 | 3 | Human | Human: P(≤9 mo) ≈ 3–5%, Aurora reclassified as 2-of-60 tail, adjustment bounded by the team's own ceiling. AI: none of the percentile/tail analysis |
| Efficiency | 5 | 4 | Human | Human: one move — the class. AI: four alternatives before landing near the class |
| Handling of Uncertainty | 5 | 4 | Human | AI gives a range but it is miscentered; human gives distribution-derived percentiles |
| Insight / Non-obviousness | 5 | 3 | Human | "The one success story is the worst data point in the room" — the AI never sees the precedent trap |
| **Overall Quality** | **4.9** | **3.6** | **Human** | The outside view IS the answer here, and the human executes it; the AI adjusts the inside estimate instead of replacing it |

**Overall judgment:** Human clearly better. The pure style lands the distributional forecast first-pass; the AI's factor-calibrated band is defensible but systematically under the class center. Learning extraction: (1) human move the AI missed: placing the inside estimate as a percentile of the historical distribution and classifying the success-story precedent against the base rate (2/60 tail); (2) adopt: the forecast basis must be the distribution (median + interval), not a multiplier on the anchor; (3) AI failure mode: factor calibration of a single-point anchor — the anchor survives; (4) process change: WHY should record the inside plan's percentile placement before HOW generates alternatives.
