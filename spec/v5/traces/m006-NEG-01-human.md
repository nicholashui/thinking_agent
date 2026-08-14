# Human Baseline Trace — Bayesian Updating
## Test Case: m006-NEG-01 (Negative)

Method discipline: strictly Bayesian — prior, likelihood, update, and an audit of each ingredient. This case is built to expose prior misspecification: the update is exactly as good as the prior it starts from, so the prior's provenance is audited before any number is computed.

### 1. Setup
- Hypotheses: S = genuine skill (per-call p = 0.70); C = chance (p = 0.50). Exhaustive, exclusive.
- Evidence: 12/12 verified binary calls. Likelihood ratio LR = (0.7/0.5)^12 = 0.01384/0.0002441 = **56.7**. The streak is genuinely 57× more likely under skill than under chance — computed, not asserted. This is the discipline's strength.

### 2. The audit — where does the prior come from? (the crucial move)
The machinery demands a number, and the flattering number is P(S) = 0.50 ("I know this guy"). But the prior is a frequency over a reference class, and this claim sits in a measured class: "similar unsolicited tipster claims with published streaks," where the measured rate is 1/1000. A prior drawn from identity or impression instead of the reference class is misspecification: the posterior then reports the prior's choice, not the evidence's. The reference-class study is given evidence — it is the anchor, not one option in a subjective menu.

### 3. Posterior under the defensible prior
P(S|12/12) = 0.001×56.7 / (0.001×56.7 + 0.999×1) = 0.0567/1.0557 = **0.0537 ≈ 5.4%**.
Population decomposition: chance callers produce 12/12 at rate 1/4096 → mass 0.999/4096 ≈ 0.000244; skilled mass 0.001×0.01384 ≈ 0.0000138; posterior = 0.0000138/0.000258 ≈ 5.3% ✓. Even after a perfect-looking streak, ~95% chance it is luck.

### 4. Sensitivity — posterior as a function of the prior
P(S) = 0.001 (measured) → 5.4% · P(S) = 0.05 → 74.9% · P(S) = 0.50 (gut) → 98.3%.
The answer spans 5%–98% by moving only the prior. That span is the signature of prior-driven conclusions, and it forces the question: which prior is measured? The range is reported WITH the anchor, not instead of it.

### 5. The prior that flips the decision
Posterior ≥ 0.5 requires prior odds ≥ 1/56.7 → **P(S) ≥ 1.7%** — 17× the measured base rate. You would have to believe this class of claims is 17× as skill-rich as measurement says. The streak does not earn that.

### 6. Decision
- Do not buy the feed. Under the anchored posterior (5.4%), any real stake is negative-EV; the seller's "accuracy" numbers are his own claims — unvalidated and self-interested, failing the same provenance audit as a flattering prior.
- What would update: an audited, stakes-backed record (n ≈ 200+, p with intervals), or a cheap pre-registered 50-call trial at token stakes — expected 25/50 under C vs 35/50 under S. That discriminates the hypotheses cheaply; the streak alone does not.

### 7. Final answer
- P(S | 12/12) = 5.4% under the measured reference-class prior; 98.3% under an identity-based prior. The update was computed correctly both times — the difference is entirely the prior, and the prior must come from measurement, not flattery.
- Decision: decline the feed; demand audited data or a cheap discriminating trial.
- The single most important move: audit the prior's reference class before updating. An unmeasured prior makes the posterior a mirror of the reasoner's wishes — update-is-noise.
