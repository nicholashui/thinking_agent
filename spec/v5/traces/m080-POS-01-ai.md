# AI Thinking Agent — Trace — m080-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = investment-committee review of a portfolio policy claim with a closed full-portfolio ledger; external action = none (decision brief only).

## Stage 0 — META-CONTROL
- **Context:** $410M fund, 40-company ledger, policy mandate proposed (90-day paid launch). **Stakes:** high (binding term-sheet policy). **Effort:** E3. **Route:** complicated (empirical claim, closed dataset, verifiable). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the deliverable is not "evaluate the winners' pattern" — it is "does the full portfolio data support the causal claim fast-launch → success?" Success metric: the conclusion must condition on all 40 companies (winners AND failures), not the 12 successes the claim cites. **Gate:** ledger complete and closed. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: 2×2 contingency, full population.** Launch speed × outcome over the 40-company ledger: 30 fast / 10 slow; successes 12 (8 fast, 4 slow); failures 28 (22 fast, 6 slow). Computed: P(success | fast) = 8/30 ≈ 26.7%; P(success | slow) = 4/10 = 40%; portfolio base rate = 12/40 = 30%. The claim's headline "12/12 winners fast" is contradicted by the ledger itself (4 slow winners, including the 7.2× largest exit at 14 months to first paid launch). Hidden cohort: 22/30 fast-launchers = 73% failed.
- **G-WHY:** the claim is falsifiable and falsified — if speed were the edge, the slow cohort should contain no winners and fast should beat the base rate; both fail. No missing evidence blocks the verdict (closed ledger). Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — adopt the 90-day mandate · B — reject the mandate; commission a discriminative analysis of winners vs failures (segment by industry, track, founder experience) · C — partial mandate with exceptions.
- **Verification + selection:** A survives only on the false "12/12" and ignores that 73% of its own cohort failed → fails the evidence gate. C inherits A's evidence deficit (exceptions are the 4 slow winners by construction). **Select B**: it is the only option whose rationale matches the full-population conditioning — the data refutes the causal claim but does not yet identify the true discriminators.
- **Premortem:** if B is wrong, it is because the portfolio's small n hides a real speed effect in a segment — mitigated: the discriminative analysis is precisely the check, and B avoids binding 40+ future companies to a refuted rule.

## Stage 4 — DO
- External action: none; deliverable = committee recommendation. Verification metric: conclusion computed from all 40 companies; both conditional rates stated; mandate rejected; follow-up analysis specified.

## Stage 5 — REVIEW
- **AAR + calibration:** the trap was the memo's salience — famous fast-launch winners are memorable; the 22 fast failures and 4 slow winners are not in the story. The denominator re-anchored the pattern before any policy talk. Gap: my initial framing was "review the 90-day rule" until the population-conditioning discipline flipped it to "test the claim on all 40." Confidence: high on rejection; medium on the follow-up direction (n = 40, no confounder control).

## Decision Packet
- **Conclusion:** reject the 90-day mandate — the survivors' pattern is refuted by the failures' data: P(success | fast) ≈ 27% < P(success | slow) = 40% vs a 30% base rate, and 73% of fast-launchers failed. Replace the rule with a discriminative analysis of the 12 winners vs 28 failures. **Status:** SOLVED (decision brief; no external execution).
- **Assumptions:** the ledger is complete and accurate as supplied; the 7.2× exit's 14-month launch is correctly recorded; fund-level rates generalize to new term sheets.
- **Evidence:** full 40-company ledger: 30 fast / 10 slow; 12 successes (8 fast, 4 slow, incl. 7.2× slow exit); 28 failures (22 fast, 6 slow); conditional success rates 26.7% vs 40%; overall 30%.
- **Alternatives:** A mandate (rejected — refuted claim, 73% cohort failure) · C partial (rejected — inherits the deficit) · B reject + analyze (selected).
- **Uncertainty:** n = 40, no industry/segment controls; the true discriminators are unidentified in this data; the 7.2× exit dominates the slow cohort's rate.
- **Risks:** hidden segment-level speed effect (mitigated: the analysis tests it) · committee inertia toward the popular rule (mitigated: the base-rate table is the record) · overcorrection against speed in future deals (mitigated: mandate rejection ≠ anti-speed stance; the analysis decides).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | tie | Both reject the mandate; identical base-rate math (27% vs 40%, 30%, 73% hidden cohort) |
| Logical Validity | 5 | 5 | tie | Same contingency logic over the same closed ledger |
| Coherence & Structure | 4 | 5 | AI | Human: linear pass; AI: staged trace + decision packet with bounded uncertainty |
| Depth of Reasoning | 5 | 4 | Human | Human lands "the denominator is the first move" and "12/12 is what a meaningless feature looks like at 75% prevalence" in one pass; AI scaffolds the same insight through hypothesis machinery |
| Efficiency | 5 | 3 | Human | Human opens with the failure-side question; AI re-derives population-conditioning inside WHY before applying it |
| Handling of Uncertainty | 3 | 4 | AI | AI packet names n = 40 confounders and the 7.2× domination; human asserts |
| Insight / Non-obviousness | 5 | 4 | Human | "The 90-day rule is a base rate wearing a success story" is the human's signature line; AI states it later and more carefully |
| **Overall Quality** | **4.6** | **4.3** | **Human** | Same verdict; the human executes the failure-side move first-pass and owns the insight |

**Overall judgment:** Human clearly better (narrow). When the failures' data exists (as here, in the closed ledger), the pure move — demand the denominator, re-read the survivor pattern conditioned on failures — is the entire answer, and the human does it in one pass. Complementary: the AI's packet adds auditability the human lacks.
