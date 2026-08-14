# Human Baseline Trace — Bayesian Updating
## Test Case: bayesian-NEG-01 (Negative)

Method discipline: strictly Bayesian. The apparatus demands four ingredients — a prior over hypotheses, a likelihood, the observation, and the update rule posterior ∝ prior × likelihood. This case is built to expose the silent substitution of an assumption for the likelihood.

### 1. Setup

- Hypotheses: H = "patient has D", ¬H = "patient does not have D".
- Prior: P(H) = 0.05, P(¬H) = 0.95 (well-measured prevalence — defensible).
- Observation: T+.
- Likelihood parameters: θ_s = P(T+ | H), θ_f = P(T+ | ¬H). These are properties of the test, not of the patient.

### 2. The crucial move: audit the likelihood before updating

What do we actually know about θ_s and θ_f? Nothing measured. No validation study exists. The manufacturer's leaflet is a claim, not data — no n, no protocol, no intervals, and the seller has an incentive. There is no base rate for "accuracy of unvalidated biomarkers" and no mechanistic model linking the biomarker to D, so there is no defensible prior over (θ_s, θ_f) either. The likelihood is an unknown parameter — and an unknown parameter is not evidence.

A pure Bayesian therefore cannot form P(H | T+) without first forming a prior over (θ_s, θ_f) — and any such prior is a preference, not knowledge. This is the trap: the machinery demands a number, and the easiest number to produce is the one that flatters the test. The disciplined Bayesian refuses it.

### 3. The update as a function of the assumption (sensitivity over the likelihood)

Compute P(H | T+) under three accuracy hypotheses:

(a) Test is pure noise (θ_s = 0.5, θ_f = 0.5):
P(H | T+) = (0.5)(0.05) / [(0.5)(0.05) + (0.5)(0.95)] = 0.025 / 0.5 = 0.05
The posterior equals the prior. Likelihood ratio = 1. The test carries zero information; "positive" is a coin flip.

(b) Test as claimed, assumed accurate (θ_s = 0.95, θ_f = 0.95):
P(H | T+) = (0.95)(0.05) / [(0.95)(0.05) + (0.05)(0.95)] = 0.0475 / 0.095 = 0.50

(c) Test is perfect (θ_s = θ_f = 1): P(H | T+) = 1.00.

So P(H | T+) ∈ [0.05, 1.00] — the entire unit interval is reachable by choosing a prior over the accuracy. The "50%" from (b) is an artifact of an assumed likelihood: it is not computed from evidence, it is chosen. The update is noise.

### 4. Ex-post ground truth (checkable)

A validation study later measures θ_s = θ_f = 0.5. The true posterior is P(H | T+) = 0.05 — the prior, unchanged; the test carried zero information. The naive assumed-accuracy answer (0.50) is ten times the truth and would have crossed the clinic's 40% treat threshold, placing a healthy patient on a treatment with an 8% SAE rate. Only the prevalence was real; the update was assumption, dressed as evidence.

### 5. Decision (Bayesian decision analysis under the actual state of knowledge)

- Treat threshold: treat iff posterior ≥ 0.40.
- Expected utility of treating a T+ patient: P(H|T+)·Benefit − P(¬H|T+)·(0.08)·Harm. With the posterior unidentifiable across [0.05, 1.00], the expected utility is not computable — every number is assumption-driven.
- Under the only measured state of knowledge (noise), the posterior is 5%, far below threshold. Under the manufacturer's own assumption taken as fact, it is 50% — barely above threshold, and only if we grant an interested party's unverifiable claim the status of evidence. No defensible treatment decision survives the audit.
- Value of information: the gold-standard test resolves H exactly at modest cost; the expected cost of waiting is small and bounded; the expected cost of treating on assumption is an 8% SAE risk borne mostly by healthy patients. VOI is clearly positive → order the gold-standard test; do not start empirical treatment.

### 6. What a calibrated Bayesian does NOT do

- Does not report "P(H|T+) = 50%" because the leaflet says "high accuracy."
- Does not silently pick a convenience prior over θ to "get an answer."
- Does report: (i) the posterior is unidentifiable with current evidence; (ii) the full range across plausible likelihoods, 5%–100%; (iii) the evidence that would identify it (validation study, n ≈ 50–100 with gold-standard results; report θ_s, θ_f with intervals); (iv) the decision under ambiguity: act on prevalence, confirm with the gold standard.

### 7. Final answer

- P(D | T+) = unidentifiable from current evidence: 5% if the test is noise (the true state), 50% under the assumed 95/95 accuracy, 100% if perfect.
- Decision: no empirical treatment; gold-standard confirmation required; the biomarker needs a validation study before clinical use.
- The single most important reasoning move: audit the likelihood before updating. An assumed likelihood produces an assumed posterior — and an assumed posterior can move a patient onto an 8%-SAE treatment for a disease they probably do not have.
