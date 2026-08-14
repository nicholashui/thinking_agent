# Human Baseline — m073-POS-01
## Style: Game Theory / Strategic Interaction (pure) — visible reasoning trace

**Step 1 — Name the game before anyone speaks.** Players: LoopExpress (L), Zipdrop (Z). Strategies: Z = {enter, stay out}; L = {accommodate, fight} × {system, no system}. Payoffs are verified from the shared analyst models — this is a complete-information game, so the matrix is the whole world:

| Z \ L | Accommodate | Fight |
|---|---|---|
| Stay out | (12, 0) | (12, 0) |
| Enter | (6, 5) | (3, −2) |

**Step 2 — Solve the base game by backward induction.** Z compares enter vs stay out given what L will do. If Z enters, L chooses accommodate (6 > 3). So Z faces enter → (6, 5) vs stay out → (0). Z enters. Outcome without commitment: (6, 5). Note the threat: L's "we will fight" is cheap talk — fighting gives 3 < 6, so it is non-credible. Bare deterrence fails; the entrant walks in.

**Step 3 — The commitment move.** The system costs 2 (sunk), pays +4 in fight mode only. Re-solve the entry subgame with the system in place: if Z enters, L compares accommodate = 6 − 2 = 4 vs fight = 3 + 4 − 2 = 5. L fights (5 > 4). Now Z's entry yields −2; Z stays out; L nets 12 − 2 = 10. The threat became credible because the instrument made fighting strictly better than accommodating.

**Step 4 — Test the binding property.** Would the same system bind if it were resellable (cost recovered whenever L does not fight)? Then accommodate = 6 + 2 = 8 vs fight = 3 + 4 = 7 — L accommodates, Z enters, deterrence collapses. Sunkness and observability are the entire mechanism: the purchase commits L because walking away from the fight leaves the $2M dead. It is not the technology that deters Z; it is L's inability to resell it.

**Step 5 — Decision and expected play.** Buy the system: 10 > 6, NPV +4 vs the next best. Expected play: Z abandons the main market; watch the adjacent suburb niche, where the system does not follow — Z can earn +1 there without eroding L's 12. Assumptions carried: complete information on both payoff models; vendor-trial effect (+4) accurate; announcement observed by Z. If any of these fail, the matrix is different and the analysis must be re-run, not patched.

**Trace summary box.** players/strategies/payoffs → base game: enter–accommodate (6, 5), threat non-credible → commitment re-solve: fight 5 > accommodate 4 → deter, L = 10 → sunkness check: resellable → accommodate 8 > fight 7 → collapse → decision: buy, expect Z out, monitor niche, +4 NPV.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Game Theory / Strategic Interaction — the game form is the first move, both subgames are solved by backward induction from the verified payoffs, the commitment is analyzed as a change in incentives (not a wish), and the conclusion falls out of the arithmetic. Signature move: the sunkness/observability check that separates a credible commitment from a wish.*
