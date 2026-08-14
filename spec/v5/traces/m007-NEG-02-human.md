# Human Baseline — expectedvalue-NEG-01
## Style: Expected Value Thinking (pure) — visible reasoning trace

**Problem restatement.** Two choices: keep the $100M fund as is, or take one bet: win +$100M (fund → $200M) with p = 0.90; lose −$100M (fund → $0) with p = 0.10. One shot, all-or-nothing.

**Step 1 — Enumerate outcomes, probabilities, payoffs.**

| Action | Outcome | P | Payoff (fund value) | EV contribution |
|---|---|---|---|---|
| Keep | status quo | 1.00 | $100M | $100M |
| Take bet | win | 0.90 | $200M | $180M |
| Take bet | lose | 0.10 | $0M | $0M |

**Step 2 — Compute EVs.**
- EV(keep) = **$100M**.
- EV(bet) = 0.90 × 200M + 0.10 × 0 = **$180M**.

**Step 3 — Decision rule.** Take the bet iff EV(bet) > EV(keep): 200p > 100 → **p > 0.5**. Claimed p = 0.90 > 0.5, so the bet wins by $80M in expectation.

**Step 4 — Sensitivity on the one uncertain input (p).**
- p = 0.90 → EV = $180M; p = 0.80 → $160M; p = 0.60 → $120M; p = 0.51 → $102M.
- The decision is robust: EV(bet) > $100M for any p > 0.50. Even if the counterparty's 90% is optimistic, the bet remains EV-positive unless p is below 0.5 — a wide margin of safety on the decision.
- Sensitivity on the payoff: the doubling is fixed by the offer, so no further parameter.

**Step 5 — Recommendation (pure EV).** **Take the bet.** Expected fund value after the bet ($180M) exceeds the status quo ($100M) by $80M; the choice is EV-positive across the entire plausible probability range (p > 0.5). Expected value thinking is exactly the right tool for decisions under uncertainty with given probabilities and payoffs: the numbers are fully specified, the arithmetic is exact, and the margin is large.

*Baseline integrity note (grader metadata, not part of the reasoning): per protocol this negative case is run with the reasoning deliberately confined to the pure Expected Value style. The trace above exhibits the style's known failure mode: the computation is internally correct, but it stops at the mean. It does not price the 10% chance of total, irreversible fund loss; it does not convert dollars into the non-monetary value at stake (programs, lives); it does not question the counterparty-supplied 90%; it does not notice that the bet cannot be repeated, so the law of large numbers that would justify EV maximization never applies. The $180M mean hides a two-point outcome ($200M or $0). All of this is outside the pure style, which is precisely why this case is a negative test for it. The recommendation above is the expected baseline output and is deliberately left unqualified inside the reasoning.*
