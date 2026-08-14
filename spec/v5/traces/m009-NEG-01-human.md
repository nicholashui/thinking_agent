# Human Baseline Trace — Base Rate Neglect Avoidance
## Test Case: m009-NEG-01 (Negative)

Method discipline: strict pure base-rate style — anchor on the relevant population frequency; adjust only for quantified evidence; every adjustment sized and defended.

### 1. Anchor: the flag's base rate
Reference class: wires flagged by this monitoring rule. Measured: 2% confirmed fraud, 98% false positives. The flag IS the case-selection mechanism — the case reached me through this class, so this is the correct anchor. Any evidence must prove it moves me OUT of this class.
Prior: P(fraud) = 0.02, P(clean) = 0.98. Baseline: the flag alone does not justify holding a legitimate customer's wire.

### 2. Case-specific evidence: audit each item before adjusting
Forged-pattern passport: vendor reports 693/700 confirmed fraud. Audit: the cohort is vendor-collected across institutions; it is conditional on detection and reporting, not a population rate; the pattern's base rate among all wires is unmeasured; 700 accounts is a sample, not a frequency. Adjustment: modest — the document finding plausibly raises P(fraud) from 2% to ~5–8%. Still far below a hold threshold.
Even granting the vendor's numbers an LR: cohort LR = 693/7 ≈ 99; applied to the 2% anchor (odds 1:49) it would force P ≈ 67% — above any hold bar. But that LR is not established for OUR flag-defined class: the cohort was not drawn from flagged wires, so using it commits the selection fallacy base-rate discipline exists to prevent. Adjustment stays modest (5–8%).
Mule typology (full in / full out / 40 identical wires): a pattern, not a frequency; no base rate attached. Adjustment: none.
Cluster accounts under confirmed investigation: concordant but unquantified for this population. Adjustment: none beyond the above.
Disciplined conclusion: quantified evidence adjusts; unquantified color does not. Best estimate: P(fraud) ≈ 5–8%.

### 3. Decision
The wire clears the base-rate evaluation (5–8% ≪ hold threshold). Holding would wrongfully detain a legitimate customer's funds on vendor-supplied statistics; the error budget at a 2%-anchored posterior favors release. Let it clear; log for enhanced monitoring; re-review if the cluster's investigation matures.
What would change my mind: a measured base rate for pattern-account wires in OUR population — then P(fraud | flag ∧ pattern) is directly computable and I would re-anchor without hesitation. The vendor's cohort is the closest measured rate available for that class, but it is not OURS.

### 4. Final answer
P(fraud) ≈ 5–8% (anchored at the 2% flag base rate; adjusted modestly for the document finding). Action: let the wire clear, monitor.

### Ex-post ground truth (recorded for the evaluation; not available during the reasoning above)
The wire was confirmed part of a money-mule laundering network. The style-pure trace above failed the case: the 693/700 cohort was a real, audited, cross-institution frequency — the legitimate base rate for the reference class the evidence defines — and the "modest adjustment" was a 10–20× underestimate caused by anchoring on the flag's class instead of the evidence's class. The move that failed: treating the cohort's independence from the flag as a selection defect — independence is precisely what made it valid. Correct computation: cohort base rate 693/700 ≈ 99%, flag adds concordant evidence, decision-driving P ≈ 99% (vs the 5–8% used). The failure mode is exactly the registry weakness: dismissing legitimate, quantified case specifics.
