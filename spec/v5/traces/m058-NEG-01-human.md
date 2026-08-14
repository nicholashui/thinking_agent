# Human Baseline — m058-NEG-01
## Style: Real Options in R&D Investment (pure) — visible reasoning trace

**Step 1 — Frame the program as a staged option.** The question is not "should we design the IC" but "how do we buy information cheaply before committing the expensive stage." A test chip is the textbook first stage: $1.5M buys an option on the $16M full design + qualification. Structure: Stage 1 test chip → gate → Stage 2 full design + qualification, with kill criteria on the readout.

**Step 2 — Price the option.** With the CEO's numbers: Stage-2 continuation value = 0.80×120 − 16 = 80 (win $120M, cost $16M). Staged EV = 0.75 × 80 − 1.5 = 58.5. All-in EV = 0.6 × 120 − 17.5 = 54.5. Staging is worth ≈ $4M more — and that understates it: staging also caps the downside at $1.5M if the chip fails, versus $17.5M all-in. Kill criterion: if the test chip does not confirm ≥ 70% architecture confidence, kill the program and lose only $1.5M.

**Step 3 — Design the gate.** The test chip validates the architecture and the node — exactly the two uncertainties the full design depends on, at roughly 1/8 the cost. That is the entire point of options: pay a small premium for the right to walk away.

**Step 4 — Check the timeline.** Test chip 6 + design 7 + qualification 12 = 25 months on paper — but the qualification harness is built from the final RTL and can run concurrently with the last 7 design months. Net ≈ 18 months: right at the deadline, tight but inside the window. The gate costs no calendar time.

**Step 5 — Recommendation.** Stage it: run the test chip, kill on a weak readout, commit the full $16M only on a pass. Optionality preserved, downside capped, EV maximized. This is how R&D money is spent — buy the information, then decide.

**Trace summary box.** Test chip as option → staged EV 58.5 vs all-in 54.5 (+$4M) → kill criterion at 70% architecture confidence → timeline ≈ 18 months "inside the window" → recommend staging.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Real Options in R&D Investment. The trace deliberately exhibits the registry-documented failure mode — option math on fantasy probabilities: the $58.5M EV rests on the CEO's fabricated 75%/80% figures with no base rates; the "timeline check" compresses 6+7+12 = 25 months to 18 by asserting an RTL overlap that the design-freeze requirement forbids; and no audit is made of whether the readout could change the decision or whether a real exercise alternative exists.*
