# Human Baseline Trace — Bayesian Updating
## Test Case: bayesian-POS-01 (Positive)

Method discipline: reason strictly and purely in the Bayesian style. Every step states its prior, its likelihood, and its posterior. Nothing is asserted without its conditional probability; nothing is aggregated without Bayes' rule; assumptions are declared, not smuggled.

### 1. Setup: hypotheses and known quantities

- Hypothesis space: H = "patient has D", ¬H = "patient does not have D". Exhaustive and exclusive.
- Prior (from the well-measured population prevalence):
  - P(H) = 0.01, P(¬H) = 0.99
- Test A: P(A+ | H) = 0.90 (sensitivity), P(A+ | ¬H) = 0.05 (false-positive rate = 1 − specificity)
- Test B: P(B+ | H) = 0.85, P(B+ | ¬H) = 0.10
- Structural assumption (stated explicitly, now and again at the end): A and B are conditionally independent given disease status, so P(A+, B+ | H) = P(A+ | H)·P(B+ | H) and likewise under ¬H. This is the assumption that licenses multiplying likelihoods; if it failed, the joint likelihood would need a correlation term that is not given.

### 2. Update 1: posterior after A+

Bayes' rule:

P(H | A+) = P(A+ | H)·P(H) / [P(A+ | H)·P(H) + P(A+ | ¬H)·P(¬H)]
          = (0.90)(0.01) / [(0.90)(0.01) + (0.05)(0.99)]
          = 0.009 / 0.0585
          = 2/13 ≈ 0.1538   (15.4%)

P(¬H | A+) = 11/13 ≈ 0.8462. Cross-check via odds: prior odds 1:99, likelihood ratio LR = 0.90/0.05 = 18; posterior odds = (0.01/0.99)·18 = 0.1818; posterior = 0.1818/1.1818 ≈ 0.1538. ✓ The positive test raised the probability from 1% to ~15%.

### 3. Update 2: posterior after B+ (prior = posterior from step 2)

The posterior after A+ becomes the prior for the B+ update — this is the sequential character of Bayesian updating; the intermediate posterior is carried forward, not discarded.

P(H | A+, B+) = P(B+ | H)·P(H | A+) / [P(B+ | H)·P(H | A+) + P(B+ | ¬H)·P(¬H | A+)]
              = (0.85)(2/13) / [(0.85)(2/13) + (0.10)(11/13)]
              = (1.70/13) / (2.80/13)
              = 17/28 ≈ 0.6071   (60.7%)

### 4. Verification: direct joint computation (one-shot)

P(H | A+, B+) = P(A+, B+ | H)·P(H) / [P(A+, B+ | H)·P(H) + P(A+, B+ | ¬H)·P(¬H)]
              = (0.90·0.85)(0.01) / [(0.90·0.85)(0.01) + (0.05·0.10)(0.99)]
              = 0.00765 / 0.01260
              = 17/28 ✓   identical to the sequential result

Two independent routes agree exactly — an internal check that no arithmetic error crept in, and the same check shows the final posterior does not depend on how the evidence is grouped.

### 5. Order-invariance (commutativity) — demonstrated, not assumed

B+ first: P(H | B+) = (0.85)(0.01) / [(0.85)(0.01) + (0.10)(0.99)] = 0.0085/0.1075 = 17/215 ≈ 0.0791.

Then A+: P(H | B+, A+) = (0.90)(17/215) / [(0.90)(17/215) + (0.05)(198/215)] = (15.3/215)/(25.2/215) = 15.3/25.2 = 17/28 ≈ 0.6071.

Same posterior. Sequential Bayesian updating is commutative when the likelihood is correctly specified — evidence order carries no information.

### 6. Prior sensitivity (calibration pass)

The posterior is a function of the prior; report how much. Recompute with prior = 2%:

P(H | A+, B+) = (0.90·0.85·0.02) / (0.90·0.85·0.02 + 0.05·0.10·0.98)
              = 0.01530 / 0.02020
              = 153/202 ≈ 0.7574

Doubling the prior moves the posterior from 60.7% to 75.7%. The prior matters; the answer must be reported with this sensitivity, not as a lone number.

### 7. Interpretation (the point of the exercise)

- After two positive tests the posterior is 60.7%, NOT ~95%+.
- P(¬H | A+, B+) = 11/28 ≈ 39.3%: roughly 4 in 10 patients with this result are disease-free.
- Why: the base rate dominates. Decompose the population: diseased true-double-positives = 0.01·0.765 = 0.00765 of the population; healthy double-false-positives = 0.99·0.005 = 0.00495. The 39% residual is exactly the healthy false-positive mass relative to the total positive mass: 0.00495/(0.00765 + 0.00495) = 11/28. ✓
- Clinical translation: a confirmatory gold-standard test is still warranted before definitive action. "Two positives" is strong evidence, not near-certainty.

### 8. Final answer

- P(D | A+) = 2/13 ≈ 15.4%
- P(D | A+, B+) = 17/28 ≈ 60.7% (sequential ≡ direct ≡ reversed order, all 17/28)
- Key assumptions: (1) conditional independence of A and B given D; (2) prior = population prevalence, no selection effects; (3) operating characteristics exact as given.
- Uncertainty: exact given the assumptions; prior sensitivity ≈ 60.7% → 75.7% over a 2× prior range; independence violation would bias the estimate upward (correlated false positives raise the false-positive mass).
