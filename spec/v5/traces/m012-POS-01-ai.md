# AI Thinking Agent — Trace — m012-POS-01
**Run metadata:** single deterministic run; blinded (no human-model information provided to the agent); task = analytics verdict + rollout recommendation; external action = none (memo only).

## Stage 0 — META-CONTROL
- **Context:** decide whether an e-commerce banner causes purchases and whether to roll it out, given an observational contingency table (M, B, P) and unit economics.
- **Stakes:** medium (rollout spend/annoyance); **Effort:** E2 (well-specified probability arithmetic + decision pass).
- **Route:** statistics/inference class (Cynefin: complicated — known adjustment machinery). **Safety:** memo only. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the decision is interventional — "roll out to everyone" = do(B=1) for all users. The asked quantity is the causal effect of B on P; the given data are observational (B's exposure rate depends on M).
- **Scope:** use the given strata as the population of record; no randomization performed. **Gate:** solvable from given evidence — yes (adjustment machinery applies). Exit gate passed.

## Stage 2 — WHY: Diagnose and Model
- **Hypotheses:** H1 the naive contrast P(P|B=1) − P(P|B=0) is the effect (marketing's claim). H2 M is a confounder (B ← M → P); the effect requires back-door adjustment on M. H3 the causal effect is zero — all of the naive contrast is selection.
- **Evidence:** M is recorded and is a plausible shared driver (engagement → banner click and purchase). **Falsification:** H1 falsifiable by comparing naive vs adjusted contrast; H2 falsifiable if strata contrasts disagree wildly (effect modification); H3 falsifiable if adjusted contrast ≠ 0.
- **Gate (G-WHY):** leading hypothesis H2 carries decision-relevant evidence; alternatives H1/H3 carried; residual uncertainty recorded. Gate passed.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:**
  - A. Naive contrast: P(P|B=1) = (0.4×0.8×0.55 + 0.6×0.2×0.25)/0.44 = 0.206/0.44 ≈ 0.468; P(P|B=0) ≈ 0.243; contrast ≈ **+0.225**.
  - B. Back-door adjustment on M: P(P|do(B=1)) = 0.4×0.55 + 0.6×0.25 = **0.37**; P(P|do(B=0)) = 0.4×0.50 + 0.6×0.20 = **0.32**; causal effect **+0.05**.
  - C. Zero effect (H3): contradicted by B's +0.05 within both strata.
- **Verification (recompute):** B re-derived on the second pass identically; strata contrasts 0.55−0.50 and 0.25−0.20 both +0.05 → no effect modification, adjustment is the effect. **Selection: B** — A is contaminated by selection into exposure.
- **Premortem / sensitivity:** if M were only partially observed, B would be biased; noted. Decision pass: rollout adds the banner to the 5,600 currently unexposed users → 280 incremental purchases (+$7,000) vs $14,000 annoyance cost → net −$7,000. Even though the true effect is positive, the economics say no to a mass rollout — recommend targeted/engaged or an A/B confirm first.

## Stage 4 — DO
- External action: none (recommendation memo). Deliverable: causal effect +5 pts (not +22.5); marketing claim inflated ≈4.5×; recommend AGAINST mass rollout under given costs (net −$7,000); fallback = A/B test then targeted rollout if +5 pts confirmed.

## Stage 5 — REVIEW
- **AAR:** adjustment arithmetic double-checked and consistent (0.37/0.32; +0.05; inflation 0.225/0.05 = 4.5×); decision pass costed on the adjusted estimate; assumptions (positivity: all four strata present ✓; SUTVA: banner of one user does not affect another ✓; no unmeasured confounder: stated as assumption, residual risk) audited in the decision pass.

## Decision Packet
- **Conclusion:** causal effect of banner = +5 pts (P(P|do(B=1)) = 0.37 vs P(P|do(B=0)) = 0.32); the +22.5 pt claim is ≈4.5× inflated; under given costs the mass rollout loses ≈$7,000/quarter → do not roll out to all; A/B confirm + targeted path.
- **Status:** SOLVED (arithmetic verified; memo delivered; recommendation committed).
- **Assumptions:** no unmeasured confounding beyond M; positivity holds; SUTVA; strata of record stable.
- **Evidence:** given strata; back-door adjustment; independent recomputation; cost arithmetic (280 × $25 = $7,000 vs 5,600 × $2.50 = $14,000).
- **Alternatives:** A naive (rejected — selection bias) · B adjusted (selected) · C zero effect (rejected by strata contrasts).
- **Uncertainty:** estimate assumes M is the only confounder; residual ± risk from unmeasured U would shift +5 pts; no sampling error given (data treated as population of record).
- **Risks:** rolling out despite the economics (rejected); refusing the analytics role (none); U hidden → overstated effect → rollout; the fallback A/B mitigates.

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 4 | Human | Both find +0.05 and reject mass rollout; human's inflation-quantified verdict and decision-flip framing are complete; AI reaches the same decision but states inflation only at REVIEW |
| Logical Validity | 5 | 5 | Tie | Both compute identical adjustment arithmetic (0.37/0.32/+0.05) and correct economics; no factual errors on either side |
| Coherence & Structure | 4 | 5 | AI | AI: staged v5 trace + decision packet; human linear but clean |
| Depth of Reasoning | 5 | 4 | Human | Human leads: 4.5× inflation check explicit in the main argument, homogeneity used as consistency check, assumption audit at the end; AI's premortem is thinner |
| Efficiency | 4 | 5 | AI | AI trace more compact; both single-pass |
| Handling of Uncertainty | 5 | 4 | Human | Human flags residual-U risk and makes the A/B the confirmatory move; AI mentions it only as a risk line |
| Insight / Non-obviousness | 5 | 4 | Human | The decision-flip (naive says roll out, causal says don't) is the non-obvious insight; AI finds it, human owns it as the central thesis |
| **Overall Quality** | **4.8** | **4.4** | **Human** | Positive case: the pure causal pass and the AI converge on effect and decision; the human wins on making the inflation check and decision flip the spine of the argument |

**Overall judgment:** Human (clearly but narrowly). This is the causal style's home turf, and the human's trace is the canonical move set — graph, confounder, back-door adjustment, decision flip. The AI gets every number right and lands the same recommendation, but buries the decisive insight (the 4.5× inflation that flips the decision) until REVIEW rather than making it the organizing thesis; on this case the pure style sets the standard the agent should meet by default.
