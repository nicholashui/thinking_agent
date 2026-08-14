# Human Baseline Trace — Bayesian Updating in Medical Diagnosis
## Test Case: m047-POS-01 (Positive)

Method discipline: strictly and purely Bayesian, clinically framed. Every step states its prior, its likelihood, and its posterior. Every test characteristic is a likelihood with a provenance. Nothing is aggregated without Bayes' rule; assumptions are declared, not smuggled.

### 1. Setup: hypotheses, prior, likelihoods
- H = cancer present, ¬H = absent. Exhaustive, exclusive.
- Prior = registry screening prevalence: P(H) = 0.005 → odds 1:199. (Measured population base rate — not clinical suspicion, not age-adjusted guess.)
- Mammogram: Se 0.87, Sp 0.89 → LR+ = 0.87/0.11 = 87/11 ≈ 7.91.
- Ultrasound: Se 0.82, Sp 0.94 → LR+ = 0.82/0.06 = 41/3 ≈ 13.67.
- MRI: Se 0.94, Sp 0.81 → LR+ = 0.94/0.19 = 94/19 ≈ 4.95.
- Structural assumption (declared): tests conditionally independent given cancer status — licenses multiplying likelihoods; if false, a correlation term not given would enter.

### 2. Update 1 — posterior after the positive screen
P(H|M+) = 0.87×0.005 / (0.87×0.005 + 0.11×0.995) = 0.00435/0.11380 = **87/2276 ≈ 3.8%**.
Odds cross-check: 1/199 × 87/11 = 87/2189 → 87/2276 ✓. A positive screen leaves 96.2% of these women cancer-free.

### 3. Test ordering — information value, not sensitivity
Next test = the one that most increases discrimination = highest LR+:
- Ultrasound LR+ = 13.67; repeat mammogram LR+ = 7.91; MRI LR+ = 4.95.
MRI has the HIGHEST sensitivity (0.94) yet the LOWEST information value: its specificity (0.81) dilutes a positive. **Next test: ULTRASOUND.** (Biopsy, LR+ ≈ 100, is the confirmatory end-stage, not a screening-follow-up option here.)

### 4. Update 2 — after US positive; prior = posterior of step 2
P(H|M+, U+) = 0.82×0.0382 / (0.82×0.0382 + 0.06×0.9618) = 0.03132/0.08903 = **3567/10134 ≈ 35.2%**.
Odds: 87/2189 × 41/3 = 3567/6567 → 3567/10134 ✓. One test quintuples the posterior (3.8% → 35%): the workup decision is now 35:65, not 50:50.

### 5. Verification — order-invariance, demonstrated
US first, then M+: 1/199 × 41/3 = 41/597 (P = 6.4%); then × 87/11 = 3567/6567 → **3567/10134 ✓**.
Sequential updating is commutative under a correctly specified likelihood — test order carries no information; sequencing is purely a cost/harm/urgency decision, never a posterior decision.

### 6. The negative branch (the load-bearing non-event)
After M+, a NEGATIVE ultrasound: LR− = (1−0.82)/0.94 = 9/47 ≈ 0.19 → odds 87/2189 × 9/47 = 783/102,883 → P = 783/103,666 ≈ **0.76%**.
One normal ultrasound returns the patient nearly to her pre-screening risk (0.5%). Negative evidence is decisive in low-prevalence screening; teams that read "US negative" as "test failed to add anything" misjudge risk 5-fold.

### 7. Prior sensitivity (calibration pass)
Prior 1%: 1/99 × 87/11 = 87/1089 → **87/1176 ≈ 7.4%**. Prior 0.1%: 87/11,076 ≈ **0.79%**.
A 10× prior range moves the posterior 0.8% → 7.4%. Prevalence varies by age, density, geography — the answer is reported with this band, not as a lone number.

### 8. Final answer
- P(cancer|M+) = 87/2276 ≈ 3.8%; P(cancer|M+, U+) = 3567/10134 ≈ 35.2%; P(cancer|M+, U−) ≈ 0.76%.
- Next test after M+: ULTRASOUND (LR+ 13.7 > MRI 4.9); test order does not change the posterior (demonstrated both directions).
- Assumptions: prior = registry prevalence; Se/Sp exact and validated as given; conditional independence of M, U, MRI given status.
- Uncertainty: exact under stated inputs; band 0.79%–7.4% over 0.1%–1% priors; correlated test errors (independence violation) would bias estimates upward.
