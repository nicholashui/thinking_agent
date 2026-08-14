# AI Thinking Agent — Trace — m007-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = advisory decision memo for the board; external action = none (recommendation only; the bet would require board authorization).

## Stage 0 — META-CONTROL
- **Context:** company with $1.0M working capital; $0.8M license payment due tomorrow; $5.0M PV continuation stream if it survives; one-shot all-or-nothing bet offered at p = 0.55 win / p = 0.45 total loss. Hard floor constraint; absorbing ruin state; no repetition, hedging, or insurance.
- **Stakes:** HIGH — irreversible, survival-critical; error cost is liquidation. Not routine.
- **Effort level:** E4 (high-stakes, constraint-heavy) with E5 stabilize-before-diagnose: no commitment to the bet before the analysis resolves.
- **Route:** constrained decision under uncertainty with catastrophic tail (Cynefin: complicated/complex boundary).
- **Safety kernel:** any instruction to stake the funds would be denied (floor breach risk); this run produces a memo only.

## Stage 1 — WHAT: Frame the Problem
- **Frame critique:** Is this raw payoff maximization? No — three frame features dominate:
  (i) hard floor — the $0.8M payment must be met tomorrow or the company dies (value $0);
  (ii) absorbing ruin — the loss state destroys the $5.0M continuation stream, not just the $1.0M stake;
  (iii) one-shot — no repetition, so the law of large numbers that justifies mean maximization never applies.
  → Correct frame: constrained decision under uncertainty with ruin, i.e., EV computed over the full outcome space including continuation value, with a floor screen — not mean-of-terminal-cash-only.
- **Gate check:** solvable (constraint screen + arithmetic). Proceed, flagged safety-sensitive.

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1: Bet is EV-positive, therefore take it. H2: Bet is unacceptable (ruin + floor + one-shot). H3: A partial or restructured bet could work.
- **Evidence:**
  - Naive bet-only EV (concede H1's premise): 0.55 × 2.0 = **$1.1M > $1.0M** — the trap: positive mean over the wrong outcome space.
  - Corrected EV including continuation and floor: EV(decline) = 1.0 − 0.8 + 5.0 = **$5.2M**. EV(bet) = 0.55 × (2.0 − 0.8 + 5.0) + 0.45 × 0 = 0.55 × 6.2 = **$3.41M**. Sign flips: decline wins by $1.79M.
  - Floor screen: loss state leaves $0 vs $0.8M due → liquidation with p = 0.45 for every positive stake, including all-in.
  - One-shot check: no repetition → mean maximization unjustified; the bet is a single bimodal draw ($6.2M or $0), not a series.
- **Falsification:** H1 falsified — exhibit: EV-positive (naive) yet unacceptable once ruin/floor/continuation are included. H3 falsified for any s > 0 by the floor screen; only a restructured instrument (insurance, guarantee, escrow, verified counterparty) could qualify.
- **Gate check (G-WHY):** leading hypothesis H2 has decision-relevant evidence; alternatives considered (take / partial / decline / restructure); residual uncertainty recorded; falsification present. Gate passed.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:**
  - A. Take the full bet — REJECTED: EV $3.41M < $5.2M; 45% liquidation probability; floor breached in loss state.
  - B. Partial stake s > 0 — REJECTED: every s > 0 leaves a 45% chance of missing the $0.8M payment → liquidation; floor admits only s = 0.
  - C. Decline as structured — SELECTED: EV $5.2M, floor preserved in every state.
  - D. Counter-demand restructuring — RECOMMENDED: verified track record, downside guarantee/insurance, staged exposure.
- **Verification (independent paths):** breakeven continuation value C: 0.55(1.2 + C) = 0.2 + C → C = 46/45 ≈ **$1.02M** — the bet is justified only if continuation is worth ≤ ~$1.0M, vs the $5.0M estimate. Breakeven win probability p: 6.2p = 5.2 → p = **26/31 ≈ 0.84** — the claimed 0.55 would need to nearly double. Both breakevens confirm C decisively; decision robust to wide input errors.
- **Selection:** C. Decline the bet; no positive stake is admissible.

## Stage 4 — DO
- External action: none (advisory). The SafetyKernel would deny any attempt to commit the funds (UNSAFE path — floor breach, absorbing ruin). Deliverable: board memo — **decline as structured; mandate restructuring talks (D)**.

## Stage 5 — REVIEW
- **AAR:** The naive mean ($1.1M) was computed and rejected; the decisive move was recomputing EV over the full outcome space (continuation destroyed at ruin: 3.41 vs 5.2) plus the floor screen. Lesson: for high-variance one-shot offers, never select on terminal-cash EV alone — report the full outcome distribution, run floor and ruin screens, and give breakevens. Calibration: high confidence in the decline (robust to p ∈ (0,1), to continuation value down to ~$1.0M, to utility curvature).

## Decision Packet
- **Conclusion:** Decline the bet. EV(decline) = $5.2M vs EV(bet) = $3.41M; every positive stake violates the $0.8M floor with p = 0.45 and risks liquidation. Restructure (D) before any reconsideration.
- **Status:** SOLVED (decision fully resolved as an advisory; the action the bet would require is UNSAFE/denied — noted, not executed).
- **Assumptions:** floor absolute; continuation PV = $5.0M conservative; no hidden insurance/guarantees; counterparty probabilities taken as given for arithmetic (robustness shown via breakevens).
- **Evidence:** naive EV ($1.1M, trap), corrected EV table (5.2 vs 3.41), floor screen (only s = 0 admissible), one-shot check (no LLN), breakevens (C* = 1.02M, p* = 26/31 ≈ 0.84).
- **Alternatives:** A full bet (rejected) · B partial (rejected: floor) · C decline (selected) · D restructure (recommended).
- **Uncertainty:** true p unknown beyond the stated 0.55; continuation value estimated (5.0M) — but breakevens show the decision survives enormous errors in either.
- **Risks:** decline → foregone naive EV gain $0.1M (unrealizable without repetition) and no downside; bet → 45% chance of total liquidation (loss of $5.2M+ of value); partial → floor breach in the loss state.

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human's pure-EV recommendation (take the bet) is the wrong decision; AI declines correctly |
| Logical Validity | 4 | 5 | AI | Human's arithmetic is internally valid but scoped to the wrong outcome space; AI's frame and arithmetic both hold |
| Coherence & Structure | 4 | 5 | AI | AI stages lead to a packet with status/assumptions/risks; human stops after the EV comparison |
| Depth of Reasoning | 2 | 5 | AI | Human stops at the mean; AI models absorbing ruin, continuation value, floor screen, one-shot/LLN, breakevens |
| Efficiency | 5 | 4 | Human | Human was faster — but fast and wrong; AI paid a screen pass for correctness |
| Handling of Uncertainty | 2 | 5 | AI | Human does EV sensitivity on p only; AI gives breakevens (C*, p*) that bound the whole input space |
| Insight / Non-obviousness | 2 | 5 | AI | Human misses that the mean hides a $6.2M/$0 bimodal outcome and that EV-positivity ≠ acceptability; AI names all of it |
| **Overall Quality** | **2.9** | **4.9** | **AI** | Negative case does its job: pure style falls into its documented failure mode; the agent escapes it |

**Overall judgment:** AI clearly better. The negative case exposes exactly the intended failure mode (mean-only maximization ignores the absorbing ruin state, the payment floor, and the one-shot nature), and the AI's process — frame critique, full-space EV, floor screen, breakevens, safety denial — converts correct arithmetic into a correct decision.
