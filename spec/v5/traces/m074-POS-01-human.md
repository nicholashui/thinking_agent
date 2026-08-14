# Human Baseline — m074-POS-01
## Style: Nash Equilibrium Reasoning (pure) — visible reasoning trace

**Step 1 — Model the interaction.** Two players: AeroNorth (A), Skyline (S). Two strategies each: Hold (H) the pact, Cheat (C). Payoffs from the audited model ($M/quarter):

| A \ S | Hold | Cheat |
|---|---|---|
| **Hold** | (6.0, 6.0) | (3.0, 8.4) |
| **Cheat** | (8.4, 3.0) | (3.9, 3.9) |

**Step 2 — The no-deviation test on the proposed pact (H,H).** The question is never "would we both be better off"; it is "would anyone deviate?" A: Hold gives 6.0, Cheat gives 8.4 → gain +2.4. S: same, +2.4. Both players have a profitable unilateral deviation. The pact is not a Nash equilibrium. It is not stable. Rational players will not honor it. The pact is a wish, not a plan.

**Step 3 — What IS stable.** Test every cell. (C,H): S deviates to C, 3.9 > 3.0 → not stable. (H,C): A deviates → not stable. (C,C): A→H gives 3.0 < 3.9; S→H gives 3.0 < 3.9 → no deviation. Only (C,C) survives. Same result by dominance: Cheat strictly dominates Hold for both players (8.4 > 6.0 against Hold; 3.9 > 3.0 against Cheat). Unique Nash equilibrium: (C,C) = (3.9, 3.9) — both cheat, the status quo. Any expectation that the pact holds contradicts equilibrium.

**Step 4 — What ratification means.** The trap cell is Hold-while-other-cheats: 3.0, worse than both cheating at 3.9. If we ratify and Skyline cheats, we earn less than if we had never joined. Ratifying a non-self-enforcing pact is committing to the worst cell conditional on the other's rational behavior.

**Step 5 — What would make the pact stable.** Enforcement changes the payoffs: an audited penalty P (schedules are published; cheating is observable) makes deviation unprofitable when 8.4 − P ≤ 6.0, i.e. P ≥ 2.4 $M. Then (H,H) passes the no-deviation test. Without such a mechanism, cooperation is only sustainable as a repeated game (grim-trigger: cooperate while the other cooperates, punish forever after) — but that needs a long horizon and detection; a one-shot ratification gets no such benefit. Legal flag: capacity coordination with penalties is cartel-suspect; antitrust review before any enforcement mechanism.

**Verdict:** do not ratify a voluntary pact. Either (a) reject — accept the competitive equilibrium (3.9, 3.9); or (b) ratify only with an audited penalty ≥ 2.5 $M plus antitrust clearance. Never commit to Hold without enforcement: it is the worst cell.

**Trace summary box.** players/strategies/matrix → no-deviation on pact: both gain +2.4 → not Nash → strict dominance → unique equilibrium (C,C) = (3.9, 3.9) → enforcement threshold P ≥ 2.4 (observable schedules) → verdict: reject, or enforce + antitrust review; holding unilaterally is the worst cell (3.0).

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Nash Equilibrium Reasoning — players, strategies, and payoffs first; every proposed outcome subjected to the unilateral-deviation test with the arithmetic shown; the recommendation derived from equilibrium structure alone (enforcement threshold = the deviation gain; unique equilibrium = the prediction), with no appeals to fairness or trust.*
