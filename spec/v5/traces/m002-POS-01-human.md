# Human Baseline Trace — Second-Order Consequences Thinking
## Test Case: m002-POS-01

The question is not "will people catch rats?" The question is: after this decision produces its intended result, what happens next? And after that? And after that?

**Round 1 — the intended result.** Citizens catch rats; the city pays per tail. So far the mayor is right: payment incentivizes catching.

**Round 2 — the effects of the effect.** A bounty on tails is a price signal, and price signals meet supply. Raising a rat in captivity costs $2.00; the bounty pays $5.00. Any payment program where the reward exceeds the cost of producing the deliverable doesn't just buy catches — it buys a production industry. The cap: $6,000/month ÷ $5 = 1,200 tails. Citizens genuinely trapping wild rats will deliver maybe 200. The remaining 1,000 tails/month will come from cages. A cage tail and a wild tail are indistinguishable.

**Round 3 — the effect we forgot first.** We cancelled the contractor. The contractor was not a cost line; it was the only thing removing 600 rats/month. The naive plan quietly assumes citizens replace those 600. They cannot — trapping skill and effort ceiling at 200. Net wild removal after cancellation: 200, not 600.

**Round 4 — arithmetic.** Wild population, +30%/month breeding, minus 200 amateur removal:
W(m) = 1.3·W(m−1) − 200.
W(1) = 2,600 − 200 = **2,400**.
W(2) = 3,120 − 200 = 2,920.
W(3) = 3,796 − 200 = **3,596**.
W(12) = 2,000·1.3¹² − 200·(1.3¹² − 1)/0.3 ≈ **31,700**.
"Population falls to near zero" is wrong by a factor of sixteen.

**Round 5 — after the policy succeeds, what then?** Suppose it worked and tails grew scarce. Then the bounty stops paying (nothing to catch), the contractor is gone, and the city re-hires at a premium — a rebound built into the design. And the metric itself is gameable: cut the tail, release the rat, collect $5, keep the breeding stock. If 30% of amateur captures go that way, effective removal is 140/month → W(12) ≈ 36,200. The payment metric and the goal have quietly diverged.

**Round 6 — the fix.** Pay for outcomes, not inputs: contract for a *measured population reduction* (census before/after), or keep the contractor who already holds equilibrium and add the bounty only as a bounded, per-citizen supplement.

**Conclusion.** The bounty backfires: W 2,000 → 2,400 (month 1) → ≈3,596 (month 3) → ≈31,700 (month 12), at $6,000/month — the same money that previously held the population stable. Advise the mayor: do not cancel the contract; pay per measured reduction, never per tail.

---
## Comparison
