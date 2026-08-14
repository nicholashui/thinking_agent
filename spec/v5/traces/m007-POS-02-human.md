# Human Baseline — expectedvalue-POS-01
## Style: Expected Value Thinking (pure) — visible reasoning trace

**Problem restatement.** Three candidate strategies: (A) abandon — $0; (B) launch directly; (C) run the $0.1M test, then decide. Demand is binary: High (p = 0.40, net +$3.0M) or Low (p = 0.60, net −$0.5M). Test accuracy: P("High" | High) = 0.80, P("Low" | Low) = 0.80.

**Step 1 — Enumerate outcomes, probabilities, payoffs.**

| Strategy | State | P(state) | Net payoff | EV contribution |
|---|---|---|---|---|
| A. Abandon | — | 1.00 | $0 | $0 |
| B. Launch directly | High | 0.40 | +$3.0M | +$1.20M |
| B. Launch directly | Low | 0.60 | −$0.5M | −$0.30M |
| C. Test, then decide | (tree, below) | — | — | — |

**Step 2 — Strategy B.** EV(B) = 0.40 × 3.0 + 0.60 × (−0.5) = 1.20 − 0.30 = **$0.9M**.

**Step 3 — Strategy C: decision tree with Bayes.**

Joint probabilities of signal and demand:
- P(High ∩ "High") = 0.40 × 0.80 = 0.32
- P(Low ∩ "High") = 0.60 × 0.20 = 0.12 → P("High") = 0.32 + 0.12 = **0.44**
- P(High ∩ "Low") = 0.40 × 0.20 = 0.08
- P(Low ∩ "Low") = 0.60 × 0.80 = 0.48 → P("Low") = 0.08 + 0.48 = **0.56**

Posterior given "High": P(High | "High") = 0.32 / 0.44 = **8/11 ≈ 0.727**; P(Low | "High") = 3/11 ≈ 0.273.
Posterior given "Low": P(High | "Low") = 0.08 / 0.56 = **1/7 ≈ 0.143**; P(Low | "Low") = 6/7 ≈ 0.857.

EV of launching after each signal:
- EV(launch | "High") = (8/11)(3.0M) + (3/11)(−0.5M) = (24 − 1.5)/11 M = **≈ $2.045M** > 0 → launch.
- EV(launch | "Low") = (1/7)(3.0M) + (6/7)(−0.5M) = (3 − 3)/7 M = **$0.0M exactly** → indifferent; either action worth $0.

Decision rule for C: launch iff the test says "High". EV(C) = −0.1M (test cost) + 0.44 × 2.045M + 0.56 × 0 = −0.1M + 0.9M = **$0.8M**.

**Step 4 — Select.** EV: A = $0, B = **$0.9M**, C = $0.8M. **Choose B: launch directly.**

**Step 5 — Sensitivity.**
- EV(C) = EV(B) − price for any price: 0.44 × 2.045M = 0.9M exactly. Breakeven test price = **$0**. The test is never worth paying for; at price 0 it merely ties.
- Check: EV(launch iff "High") = P(High ∩ "High") × 3.0M + P(Low ∩ "High") × (−0.5M) = 0.32 × 3.0 − 0.12 × 0.5 = 0.96 − 0.06 = 0.9M — identical to always-launch. The signal selects no better bet.
- If the test were perfect (accuracy 1.0): EV(C) = −0.1 + 0.40 × 3.0 + 0.60 × 0 = 1.1M > 0.9M — then it would pay. Value of the test comes only from accuracy above 80%; at the stated 80% it is zero.

**Trace summary box.** EV(A) = $0; EV(B) = $0.9M ← **decision**; EV(C) = $0.8M; breakeven test price = $0; EV(launch | "Low") = $0 exactly; EV(launch iff "High") = EV(always launch) = $0.9M.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning above is deliberately confined to the Expected Value style — outcomes × probabilities × payoffs, summed, compared, with sensitivity on the one free parameter (test price/accuracy). No non-EV frameworks (utility, regret, real options) were consulted, per protocol. In this positive case the pure style performs excellently: the answer is exact and checkable.*
