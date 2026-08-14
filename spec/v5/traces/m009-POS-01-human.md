# Human Baseline Trace — Base Rate Neglect Avoidance
## Test Case: m009-POS-01 (Positive)

Method discipline: strict pure base-rate style — anchor on population frequencies FIRST; case evidence enters only after the anchor, only if quantified, and only as an explicit, sized adjustment. Salience is never a quantity.

### 1. Anchor: the base rate, before any case evidence
Reference class: candidates passing the resume screen. Measured base rate of top performers in this class: 5%. Written first, because it is first.
The portfolio review is a measured instrument: sensitivity 80%, false-positive rate 30%.

### 2. The computation: prior → likelihood → posterior
P(top | review+) = (0.80)(0.05) / [(0.80)(0.05) + (0.30)(0.95)] = 0.04 / 0.325 = 8/65 ≈ 12.3%
Odds check: prior odds 5:95 ≈ 1:19; LR = 0.80/0.30 ≈ 2.67; posterior odds ≈ 2.67/19 ≈ 0.141 → P ≈ 12.3% ✓
Population view: of 100 resume-screen passers, 5 are top performers → 4 flagged (0.80·5); 95 are not → 28.5 flagged (0.30·95). Of 32.5 flagged, only 4 are top performers: 4/32.5 ≈ 12.3% ✓ — the base rate does the work; the test mostly adds noise.
Translation: ~88 of 100 review-passers are not top performers. The instrument is weak; the base rate carries the analysis.

### 3. The anecdote: quantify what it is worth
Claim: "strongest portfolio in 15 years." Define information as posterior change: any item that leaves the posterior unchanged has LR = 1 by definition. The endorsement contains no observation beyond "portfolio review passed" — the same test, run once, unaudited, reliability unknown.
Adjustment: ZERO. Salience ≠ information; an unmeasured restatement of the same evidence has LR = 1, so its information value is 1, not "unknown." Posterior stays 12.3%.
Only a NEW, independent, measured signal may adjust — by its measured LR, nothing else.

### 4. Flip-point: what it would take to move the decision
Target P ≥ 50% ⇒ posterior odds ≥ 1. Prior odds = 5/95 ≈ 0.0526 ⇒ required LR ≥ 1/0.0526 ≈ 19.
Anchor against known instruments: a 95%-sensitivity / 5%-FPR work-sample reaches LR 19; unstructured interviews (LR ≈ 2–4 in the validity literature) do not; a restated opinion (LR = 1) does nothing.

### 5. Decision
Do NOT fast-track. The base-rate answer is 12.3% with an LR ≈ 19 bar to clear; recommend measured follow-up signals (structured work sample, pre-committed threshold), not VP enthusiasm.

### 6. Final answer
P(top performer | review+) = 8/65 ≈ 12.3%; the VP anecdote adds exactly 0 (redundant evidence, LR = 1); an independent signal needs LR ≥ ~19 to justify P ≥ 50%. No fast-track on this evidence.
