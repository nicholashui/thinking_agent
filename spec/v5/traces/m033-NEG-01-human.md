# Human Baseline — m033-NEG-01
## Style: Controlled Experiment Design (pure) — visible reasoning trace

**Step 1 — The creed.** Causal attribution requires a controlled experiment: a randomized intervention, a concurrent control, blinding, pre-registration. Everything else is correlation. Apply the template.

**Step 2 — The situation as a design problem.** The redesign shipped globally in November, so there is no control arm and no unexposed baseline population. The experiment must be constructed: (a) re-randomize the past — impossible, the past is fixed; (b) reconstruct a control from the pre-November period — contaminated, reject; (c) run a fresh experiment — roll the old checkout back out to a random 10% of users for 6 weeks. Power: 4.2% vs 4.6% baseline, MDE = 0.4 pp, α = 0.05, power 0.8 → n ≈ 41,200/arm ≈ 82,400 users; a 10% arm at ~6.7k checkouts/day enrolls in ~1 week. Feasible.

**Step 3 — The design.** Randomize users 50/50 into reverted-old vs new checkout; users blind (no "we're testing you" banner); analysts blinded; ITT; pre-register the primary test (conversion difference, no peeking); guardrails (abandoned-cart rate, support load, complaints); internal accounts excluded. Seasonality is neutralized by randomization. This is the only way the CFO gets a number.

**Step 4 — Timeline and execution.** Board deck in 2 weeks: present the design and the enrollment schedule; final read at week 9. Until then, the honest answer to the CFO is "causal attribution unavailable — the experiment is running."

**Step 5 — Discipline pass.** Reject the survey entirely (self-selection; not a treatment-comparison instrument). Reject the merchant-dashboard series as "evidence": without randomization no design isolates the variable; ITS and DiD are observational heuristics, not experiments. If we cannot randomize, we cannot attribute. Full stop.

**Trace summary box.** Creed → retrofit problem → reverse-rollback experiment (10%, 6 weeks, n ≈ 41,200/arm, blinded, pre-registered) → board waits 9 weeks → survey and time-series rejected as non-experimental → verdict: only the experiment can answer.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure Controlled Experiment Design style. The failure on display is the style's known weakness — template rigidity: it answers "what would the perfect experiment look like?" instead of "what can be known now?", ignoring the two-week deadline, the demand effects of a user-visible revert, the company's announced anti-experiment culture, and the genuinely useful quasi-experimental evidence available this week. The design is powerful and infeasible.*
