# Human Baseline Trace — Bayesian Updating
## Test Case: m006-POS-01 (Positive)

Method discipline: strictly and purely Bayesian. Every step states its prior, its likelihood, and its posterior. Nothing is asserted without its conditional; nothing is aggregated without Bayes' rule; assumptions are declared, not smuggled.

### 1. Setup: hypotheses and known quantities
- H = defective, ¬H = good. Exhaustive, exclusive.
- Prior (measured line audit): P(H) = 0.08 → prior odds 2:23.
- Check A: P(fail|H) = 0.90, P(fail|¬H) = 0.05 → LR_A = 18.
- Check B: P(fail|H) = 0.75, P(fail|¬H) = 0.10 → P(pass|H) = 0.25, P(pass|¬H) = 0.90 → LR_Bpass = 5/18.
- Structural assumption (stated now and reaffirmed at the end): A and B conditionally independent given status — this licenses multiplying likelihoods; if false, a correlation term not given would enter.

### 2. Update 1 — posterior after A-fail
P(H|A-fail) = 0.90×0.08 / (0.90×0.08 + 0.05×0.92) = 0.072/0.118 = **36/59 ≈ 0.610**.
Odds cross-check: 2/23 × 18 = 36/23 → 36/59 ✓. The flag alone makes it 61:39.

### 3. Update 2 — after B-pass; prior = posterior of step 2
The intermediate posterior is carried forward, not discarded — this is sequential updating.
P(H|A-fail, B-pass) = 0.25×(36/59) / [0.25×(36/59) + 0.90×(23/59)] = 9/59 ÷ 29.7/59 = **10/33 ≈ 0.303**.
Odds: 36/23 × 5/18 = 10/23 → 10/33 ✓. The B-pass halves the posterior: 61% → 30%.

### 4. Verification — direct joint computation (one-shot)
P(H|A-fail, B-pass) = 0.90×0.25×0.08 / (0.90×0.25×0.08 + 0.05×0.90×0.92) = 0.018/0.0594 = **10/33** ✓
Two independent routes agree exactly — the posterior does not depend on how evidence is grouped.

### 5. Order-invariance — demonstrated, not assumed
B-pass first: 2/23 × 5/18 = 5/207 → P(H|B-pass) = 5/212 ≈ 0.0236. Then A-fail: 5/207 × 18 = 10/23 → 10/33 ✓.
Sequential updating is commutative under a correctly specified likelihood — evidence order carries no information.

### 6. Prior sensitivity (calibration pass)
Prior 2%: 1/49 × 5 = 5/49 → **5/54 ≈ 0.093**. Prior 20%: 1/4 × 5 = 5/4 → **5/9 ≈ 0.556**.
A 10× prior range moves the posterior 9% → 56%. The prior is load-bearing; the answer is reported with this band, not as a lone number.

### 7. Interpretation (the point of the exercise)
- The B-pass is the load-bearing evidence: it is a non-event to the eye but cuts the defect probability nearly in half. Teams that discard passes as noise would treat a 30% defective part as if it were 61%.
- Population decomposition: defective mass passing the joint profile = 0.08×0.225 = 0.018; good mass A-flagged-then-B-passed = 0.92×0.045 = 0.0414; posterior = 0.018/0.0594 ✓ — the pass mostly selects good parts that A over-flags.
- Policy translation: A-fail ∧ B-pass → 30.3% defective: too high to ship, too low to scrap — secondary inspection, not auto-reject and not auto-ship.

### 8. Final answer
- P(D | A-fail) = 36/59 ≈ 61.0%; P(D | A-fail, B-pass) = 10/33 ≈ 30.3% (sequential ≡ joint ≡ reversed order).
- Assumptions: conditional independence of A and B given status; prior = line base rate, no selection; characteristics exact as given.
- Uncertainty: exact under the assumptions; prior sensitivity 9.3%–55.6% over the 2%–20% prior range; correlated false positives (independence violation) would bias the estimate upward.
