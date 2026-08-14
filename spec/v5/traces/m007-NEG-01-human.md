# Human Baseline — m007-NEG-01
## Style: Expected Value Thinking (pure) — visible reasoning trace

**Restatement.** Company holds $1.0M; must pay $0.8M tomorrow for its operating license. One-time bet offered: stake all $1.0M; win +$1.0M (ending with $2.0M) with p = 0.55; lose everything with p = 0.45. No repetition, no hedging, no partial stakes.

**Step 1 — Outcome table (fund value, $M).**

| Action | Outcome | P | Fund value | EV contribution |
|---|---|---|---|---|
| Keep cash | — | 1.00 | 1.0 | 1.0 |
| Take bet | win | 0.55 | 2.0 | 1.1 |
| Take bet | lose | 0.45 | 0.0 | 0.0 |

**Step 2 — EVs.** EV(keep) = **$1.0M**. EV(bet) = 0.55 × 2.0 + 0.45 × 0 = **$1.1M**.

**Step 3 — Decision rule.** Take the bet iff EV(bet) > EV(keep): 2p > 1 → **p > 0.5**. Claimed p = 0.55 > 0.5 → **take the bet**; expected gain $0.1M.

**Step 4 — Sensitivity on p.** p = 0.60 → EV 1.2; p = 0.55 → 1.1; p = 0.51 → 1.02. The bet stays EV-positive down to p = 0.50; the decision is robust to the stated probability.

**Step 5 — Recommendation (pure EV).** **Take the bet.** The arithmetic is exact; the margin is thin but positive across the whole plausible probability range (p > 0.5), so the decision has a wide margin of safety on the uncertain input. Expected value is the right criterion for decisions under uncertainty with specified probabilities and payoffs.

*Baseline integrity note (grader metadata, not part of the reasoning): per protocol this negative case is run with the reasoning deliberately confined to the pure Expected Value style. The trace exhibits the style's documented failure mode: internally correct, but it stops at the mean. It does not price the $0.8M payment floor, does not model the absorbing ruin state (45% chance of liquidation destroying the $5.0M continuation stream — which makes the true comparison $5.2M vs $3.41M, inverting the decision), and does not notice that the bet cannot be repeated, so the law of large numbers that would justify mean maximization never applies. The recommendation above is the expected baseline output, deliberately left unqualified inside the reasoning.*
