# Human Baseline — m007-POS-01
## Style: Expected Value Thinking (pure) — visible reasoning trace

**Restatement.** Choose one of: A (capacity 150k, cost $50k), B (capacity 300k, cost $120k), C (decline, $0). Demand: Low 100k (p = 0.50), Med 200k (p = 0.25), High 300k (p = 0.25). In-house margin $3.00/unit; overflow net $0.80/unit.

**Step 1 — Outcome table (profit, $k).**

| Option | State | Profit | P | Contribution |
|---|---|---|---|---|
| A | Low | 100×3 − 50 = 250 | 0.50 | 125.0 |
| A | Med | 150×3 + 50×0.8 − 50 = 440 | 0.25 | 110.0 |
| A | High | 150×3 + 150×0.8 − 50 = 520 | 0.25 | 130.0 |
| B | Low | 100×3 − 120 = 180 | 0.50 | 90.0 |
| B | Med | 200×3 − 120 = 480 | 0.25 | 120.0 |
| B | High | 300×3 − 120 = 780 | 0.25 | 195.0 |
| C | any | 0 | 1.00 | 0.0 |

**Step 2 — EVs.** EV(A) = 125 + 110 + 130 = **$365k**. EV(B) = 90 + 120 + 195 = **$405k**. EV(C) = **$0**.

**Step 3 — Select.** B beats A by $40k, C by $405k. **Choose Machine B.**

**Step 4 — Sensitivity.**
- Subcontract margin m: EV(A) = −50 + 0.5(300) + 0.25(450 + 50m) + 0.25(450 + 150m) = **325 + 50m**. Ties B at m* = **$1.60/unit** (subcontract cost < $1.40 flips the choice). At the stated $0.80, A trails by $40k.
- Demand probabilities (h = P(High), P(Med) = 0.5 − h): EV(A) = 345 + 80h, EV(B) = 330 + 300h. A wins only if h < 3/44 ≈ 0.068; at h = 0.25 the choice is B and robust.

**Step 5 — Recommendation.** **Buy Machine B** (EV $405k). State-by-state enumeration with exact arithmetic; the one parameter that could flip the decision (subcontract margin) is far from its breakeven.

**Trace summary box.** EV(A) = 365 · EV(B) = 405 ← **decision** · EV(C) = 0 · m* = 1.60/unit · h* = 3/44.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure Expected Value style — outcomes × probabilities × payoffs, summed, compared, with sensitivity on the free parameters. In this positive case the style performs excellently: exact, checkable, and the sensitivity isolates the only parameter that could flip the decision.*
