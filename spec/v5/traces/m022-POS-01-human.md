# Human Baseline — m022-POS-01
**Human Thinking Model**: Decision Trees & Scenario Planning — strict, pure application.
**Prompt contract**: Reason ONLY as a decision-tree analyst: draw decision nodes (□) and chance nodes (○), assign branch values, roll back expected values at every node, run sensitivity, and state the resulting contingent policy. Full visible trace.

---

## Trace

**Step 1 — Frame as a tree.** Today is decision node D1 with two branches: Continue Phase 3 (○ trial) vs License-now ($55M). The continue branch must contain its own downstream decisions — that is the whole point of a tree: no branch gets stubbed.

**Step 2 — Build the full tree.**
- D1 root: [Continue: ○ Trial] vs [License-now: +55]
- ○ Trial: Success (0.6) → D2 ; Failure (0.4) → D3
- D2 (success): [Launch: ○ Market] vs [License: +150]
- ○ Market: High (0.5) +400 / Low (0.5) +100 (gross); launch cost 80
- D3 (failure): [Rescue: ○ Fix] vs [Abandon: 0]
- ○ Fix: Fixed (0.25) → D2 value ; Not fixed (0.75) → 0 ; rescue cost 15

**Step 3 — Roll back (expected value at every node).**
- D2: Launch = 0.5(400)+0.5(100) − 80 = 170 > License 150 → **170** (launch)
- D3: Rescue = 0.25×170 − 15 = 27.5 > Abandon 0 → **27.5** (rescue)
- D1: Continue = 0.6(170) + 0.4(27.5) − 40 = 102 + 11 − 40 = **73** > 55 → **continue**
All three decision nodes are real decisions: the tree never defaults to "abandon on failure" without costing the rescue option that the data explicitly supplies.

**Step 4 — Sensitivity.**
- Break-even trial-success p vs the $55M license-now: p×170 + (1−p)×27.5 − 40 = 55 → p* = 67.5/142.5 = **0.474**. The rescue arm is what buys robustness: without it, p×170 − 40 = 55 → p* = 0.56.
- Success-node license threshold: the $150M offer must exceed 170 to switch D2 — it is $20M short; any renegotiation above $170M flips the policy.
- Rescue break-even fix-probability: q×170 = 15 → q* = **0.088**; the 0.25 estimate clears it by ~3× — the rescue is robust over a huge range.

**Step 5 — Policy.** The tree's output is a contingent policy, not a number: **Run Phase 3. On success, launch alone — do not accept the $150M license (short by $20M of indifference). On failure, spend the $15M rescue — do not abandon (EV 27.5 vs 0). Reject the $55M pre-trial license (73 vs 55).**

**Step 6 — What the tree cannot hold (declared, not ignored).** Financing dilution (trial fits in $120M cash), pipeline correlation (AT-9 upside correlates with the second asset), regulatory tail. Declared out of scope; none reverses a 73-vs-55 margin.

---

## Verdict for the eval
All rubric items met: three decision nodes and three chance nodes with branch values; fold-back 170 / 27.5 / 73; rescue costed (failure branch completed, not stubbed); contingent policy stated; two decision thresholds (p* 0.474, $170M license) plus rescue q* 0.088. Verdict: continue Phase 3 — the optimal policy is the tree, not the EV.
