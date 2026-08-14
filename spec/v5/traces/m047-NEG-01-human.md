# Human Baseline Trace — Bayesian Updating in Medical Diagnosis
## Test Case: m047-NEG-01 (Negative)

Method discipline: strictly Bayesian — with the provenance clause: every prior and every likelihood enters the equation only after its provenance is established. Unvalidated numbers are not likelihoods; they are hypotheses about likelihoods.

### 1. Audit the prior FIRST — reference class, not impressions
- Prior must be the annual cancer incidence for this age/sex: 0.3% (3/1000) → odds 3:997.
- Rejected priors: lifetime risk (≈40%) is the wrong reference class — the question is "cancer now", not "cancer ever"; clinic prevalence applies only to symptomatic patients. Prior misuse moves the answer more than the update ever will.

### 2. Audit the likelihoods BEFORE updating
The quoted Se 0.90 / Sp 0.95 carry a cohort design, not a validation:
- Development cohort of 200 = 100 cases + 100 controls: a 50%-cancer enriched sample — prevalence engineered by construction, not measured.
- Single center; no external validation in the target screening population; no confidence intervals (n = 100 per group).
- Verdict: point estimates from a selected sample — **unvalidated likelihoods**. They enter the computation only as a band, never as exact.

### 3. Compute the PPV under the anchored prior (for reference)
Natural frequencies, 100,000 women: 300 with cancer → 270 test positive; 99,700 without → 4,985 test positive. PPV = 270/5,255 = **54/1051 ≈ 5.1%** (odds 3/997 × 18 = 54/997 → 54/1051 ✓).
Even taking the manufacturer's claims at face value, 19 of 20 positives are false.

### 4. Quantify the band — how much the unvalidated numbers matter
- If true Se 0.5, Sp 0.95: LR+ 10 → 30/1027 ≈ 2.9%.
- If true Se 0.9, Sp 0.90: LR+ 9 → 27/1024 ≈ 2.6%.
- If true Se 0.5, Sp 0.90: LR+ 5 → 15/1012 ≈ 1.5%.
- Wrong prior (lifetime 40%) with claimed Se/Sp: 2/3 × 18 = 12 → **12/13 ≈ 92.3%** — the full trap: wrong prior + unvalidated likelihoods = invasive workup of ~9 in 10 healthy women.

### 5. Decision
- No diagnostic action — and no reassurance — follows from this result alone. The test is not validated for screening in this population: the 5.1% does not license a workup, the 1.5% does not license dismissal, and the 92.3% is the cautionary floor for how far the wrong reasoning goes.
- What WOULD update the belief: external validation of the test in the target screening population with reported CIs; meanwhile, standard-of-care age-appropriate screening and workup proceed unchanged.

### 6. Final answer
- P(cancer|positive) = 54/1051 ≈ 5.1% under the anchored annual-incidence prior, IF the quoted likelihoods were validated — they are not; the defensible band is ≈ 1.5%–5.1%, with 92.3% as the wrong-prior extreme.
- Assumptions: annual incidence 0.3% for the reference class; claimed Se/Sp used for the point estimate only.
- Uncertainty: dominated by the unvalidated likelihoods and the prior reference class, not by the arithmetic; the arithmetic itself is exact and checkable.
