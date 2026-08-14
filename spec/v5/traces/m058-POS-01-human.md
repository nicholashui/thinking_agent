# Human Baseline — m058-POS-01
## Style: Real Options in R&D Investment (pure) — visible reasoning trace

**Step 1 — Frame as options, not projects.** Each project is a compound option: Stage 1 buys the right (not the obligation) to fund Stage 2. The job is to price the options — and then design the gates so the prices are real, because a gate that buys no decision-relevant information is a milestone, not an option.

**Step 2 — Price the options (staged EV).** A: pass 80% → continuation value 0.30×400 − 36 = 84 → staged EV = 0.8×84 − 4 = 63.2. B: 0.6×(0.40×250 − 28) − 2 = 41.2. C: 0.9×(0.15×100 − 9) − 1 = 4.4. Portfolio = 108.8; year-1 spend €4+2+1 = €7M ≤ €10M.

**Step 3 — Price the alternative (all-in).** A: 0.24×400 − 40 = 56. B: 0.24×250 − 30 = 30. C: 0.135×100 − 10 = 3.5. Portfolio = 89.5 — and the year-1 commitment is €80M, blowing the budget. All-in is not merely worse (≈ €19M); it is infeasible. And the best all-in single pick, A at 56, is far below the staged portfolio's 108.8. Staging wins twice: it preserves the kill option and it is the only structure the capital allows.

**Step 4 — Pre-commit kill criteria before any stage runs** (they must not be negotiated after results are known). K1: continuation EV < 0 at any gate → kill, funds return to the pool. K2 — payoff-mix floor: conditional success ≤ 20% with payoff < €300M → kill; a project that can only justify itself as a near-terminal lottery ticket should not hold capital. This is where C sits at p2 = 15%: its Stage-1 trial must beat expectations or it dies at the gate.

**Step 5 — Design the gates for decision relevance.** An option is worth only its information: A's screen must test melt processability (the separator film's dominant failure mode), B's the electrochemical stability/reproducibility that actually kills membranes, C's the coating yield. Pass/fail on the dominant mode shifts the conditional probability the continuation decision depends on. A gate measuring anything else is theater.

**Step 6 — Handle C honestly: it is a quasi-option.** C's Stage-2 outcome is terminal — once funded, no further branch exists. A gate only has value if it lets you change course; C has exactly one real decision point (gate 1) and after that it is a lottery ticket. Hold it only while the pool can afford it (it can: €7M), with a kill-first redeployment rule.

**Step 7 — Redeployment discipline.** When a project dies, its Stage-2 funds (B €28M, C €9M — up to €37M) return to the pool and go to the survivor with the best marginal EV first: A's scale-up acceleration, then a new derivative. Scale winners, starve the rest, kill without mercy.

**Trace summary box.** 3 projects as compound options → staged EV 108.8 vs all-in 89.5 (+€19M), €7M vs €80M year-1 (only staging feasible) → numeric kill criteria pre-committed (continuation-EV < 0; payoff-mix floor) → gates designed to test dominant failure modes → C treated as quasi-option → killed capital redeployed winners-first.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Real Options in R&D Investment: stage to buy information, kill early, scale winners. Signature moves: the payoff-mix kill floor, gate information-design, the quasi-option read on C, and the triggered redeployment rule — option-structure refinements beyond the EV arithmetic itself.*
