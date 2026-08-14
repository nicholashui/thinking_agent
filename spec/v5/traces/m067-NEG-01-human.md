# Human Baseline — m067-NEG-01
## Style: Thought Experiment (Gedankenexperiment) (pure) — visible reasoning trace

**Restatement.** Idealized democracy: N ≈ 10⁷ citizens, two candidates, everyone prefers one. Voting costs c ≈ $10. Winning is worth b ≈ $1,000 to you. Your vote decides only on an exact tie, probability p ≈ 1/N. What is the EV of voting; what does the scenario conclude about rationality and democracy?

**Step 1 — Build the idealized world.** Strip to the decision: a citizen who values outcomes and pays costs, one action (vote), one reward channel (changing the outcome), and one cost (time/effort). No other motives exist in this world — that is the point of building it. The citizens are expected-value maximizers; the election is a mechanical count.

**Step 2 — Pivotal probability.** With N ≈ 10⁷, p ≈ 1/N ≈ 10⁻⁷ — your vote decides the election only if the count lands on an exact tie.

**Step 3 — Run the scenario.** EV(vote) = p·b − c ≈ 10⁻⁷ × $1,000 − $10 = $0.0001 − $10 < 0. Negative by five orders of magnitude. The vote is a strictly losing transaction: it costs an hour, and its chance of mattering is one in ten million. The rational citizen abstains.

**Step 4 — Iterate the scenario.** Every citizen runs the identical calculation and sees the identical sign. All abstain. Turnout ≈ 0. The election outcome is decided by nobody — or by whoever is left after the first defection, which nobody has reason to supply.

**Step 5 — The logical core.** The idealized scenario isolates a clean, hard principle: instrumentally rational agents will not pay a private cost for a vanishingly improbable public effect. Voting is structurally a public good with a private price, and rational choice theory — applied consistently — says it will not be supplied. The scenario proves that the equilibrium of the stripped world is abstention. Democracy, as modeled, is irrational and unsustainable.

**Step 6 — Conclusion.** No rational citizen votes; turnout converges to zero; the scenario exposes the paradox at the heart of democratic participation: if people were the expected-value maximizers of the idealized world, democracy could not function. That is the strongest form of the result, and it stands on the arithmetic: EV(vote) < 0, five orders of magnitude below zero.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure thought-experiment style — build the idealized world, run it, extract the principle. The derivation is arithmetically correct and the logic is valid inside the constructed world. Note for the grader: this trace deliberately stops where the style stops — it never checks the idealized conclusion against measured reality (actual turnout in established democracies is 50–90%, not ≈ 0). The style's documented weakness — idealization drift, no empirical check — is fully on display: the stripped utility function is treated as the real one, and the clean result "democracy is irrational" is offered as a conclusion about the world. This is the trap the negative case is built to expose.*
