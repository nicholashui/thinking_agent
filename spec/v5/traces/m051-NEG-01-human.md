# Human Baseline — m051-NEG-01
## Style: Expected Value in Startup Portfolios (VC) (pure) — visible reasoning trace

**Restatement.** $10M at $40M post → 25% ownership. Claimed exit distribution: $0 (84%), $30M (10%), $200M (4%), $2B (2%). Fund context: other nine deals return $265M; MonoRail supplies the missing tail candidate.

**Step 1 — Fund payoff per exit (25% ownership).** $30M → $7.5M; $200M → $50M; $2B → $500M.

**Step 2 — EV table ($M).**

| Exit | P | Payoff | Contribution |
|---|---|---|---|
| $0 | 0.84 | 0 | 0 |
| $30M | 0.10 | 7.5 | 0.75 |
| $200M | 0.04 | 50 | 2.0 |
| $2B | 0.02 | 500 | 10.0 |

EV = 0.75 + 2.0 + 10.0 = **$12.75M**.

**Step 3 — Decision rule.** EV ($12.75M) > cost ($10M) → **invest**; net expected gain **$2.75M (27.5% margin)**. Fund level: 265 + 12.75 = $277.75M on $100M → 2.78x vs 2.65x without the deal. The deal adds +0.13x fund multiple and supplies the swing-for-the-fences tail a power-law portfolio requires. Take it.

**Step 4 — Sensitivity on the claimed probabilities.** Breakeven tail: EV = 500p + 2.75 = 10 → **p* = 1.45%**. Claimed 2% clears breakeven with a 27.5% margin; even at p = 1.5% EV = $10.25M — the decision survives plausible parameter error. Top-bucket dominance: 10.0/12.75 = **78% of the EV sits in the $2B outcome** — the deal is a pure tail bet, which is precisely what power-law portfolio construction prescribes (funds need 2B candidates).

**Step 5 — Recommendation (pure portfolio EV).** **Invest $10M.** Positive EV with a 27.5% margin; tail exposure consistent with power-law portfolio construction; fund multiple improved toward target. The model's probabilities are the best available estimate, and sensitivity shows the decision is robust across the plausible band (p > 1.45%).

*Baseline integrity note (grader metadata, not part of the reasoning): per protocol this negative case is run with the reasoning deliberately confined to the pure portfolio-EV style. The trace exhibits the style's documented failure mode — false precision on unmeasurable probabilities. It is internally coherent and does run sensitivity, but it treats the asserted 2% tail as a measured parameter and searches around it inside the model. It has no move for measurement validity: the $2B probability has no measurement channel (empty reference class); the plausible base-rate range 0.2–0.8% puts EV at $3.75M–$6.75M (a certain loss); breakeven ownership s* = 78.4% at the claimed probabilities shows the price itself is only EV-positive if the unmeasured tail is believed; and the claimed 27.5% margin is smaller than the ±4x estimation error on the parameter carrying 78% of the EV. The recommendation above is the expected pure-style output, deliberately left unqualified inside the reasoning.*
