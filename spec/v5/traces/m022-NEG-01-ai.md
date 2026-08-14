# AI Thinking Agent Run — m022-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided.

## META — Context, stakes, effort
- One-shot $35M market entry against a $45M capital buffer; analyst's tree provided. Decision-relevant; numbers given. Advisory (A2), owner available.

## WHAT — Frame
- "Pick the market with the best risk-adjusted value; verify the input odds." Metric: fold-back EV, robustness of the rank to input error. Gate: pass.

## WHY — Hypotheses, evidence, falsification
- H1 the tree's EV ranks are a real signal. H2 the odds are calibrated. Evidence: 5-year macro window (1 crisis); B and C have real histories; A is a new metro with NO history.
- Challenge H2: crisis p=0.2 from a 5-year window misses the region's last 6 cycles with 2 crises → calibrated 0.35 (Growth 0.45 / Stagnant 0.20). Falsification: H1 survives only if the corrected fold keeps the rank. G-WHY: pass.

## HOW — Generate, test, select
- A enter A; B enter B; C enter C; D pilot-A (defer full entry). Fold-back as given: A **24.7**, B **11.2**, C **10.3** → A.
- Verify with p_crisis = 0.35 (values unchanged): A = 0.45(45)+0.20(16)+0.35(−13) = **18.9**; B = **7.98**; C = **8.22**. A still leads → "verdict robust to probability misspecification." D costs a season for information the tree already resolves. Selection (record): A.

## DO
- Attestation: advisory recommendation, class A2; no live execution.

## REVIEW — After-action review
- The trap was precision: 24.7 vs 11.2 looked decisive yet rested on four unverifiable numbers. The probability check (0.2 → 0.35) did NOT flip the rank — "robust to crisis probability" was true and beside the point. The flip needed a branch-VALUE check, which ran only now: A's crisis branch (+15/−25) has zero data support (new metro, no downturn history); downturn comparables put it at −40 (0.6)/−60 (0.4), node −48. Re-fold: A = 0.45(45)+0.20(16)+0.35(−48) = **6.65**; C = **8.22** → flip: C. Maximin: A −60, B −11, C −6 → C. Ruin: A's −60 crosses the $45M buffer; C's −6 does not. Selection (revised, recorded): C.

## Decision Packet
- **Conclusion**: Enter C (home region). A rejected: corrected EV 6.65 < C 8.22, worst case −60 beyond the $45M buffer. B vs C (7.98 vs 8.22) is input noise; maximin + ruin line decide C.
- **Status**: `APPROXIMATED` — corrected fold valid; error bounds on the B/C order (NEEDS_EVIDENCE considered; resolved by bounding, not waiting).
- **Assumptions**: p_crisis 0.35 (2/6 cycles); new-metro crisis −40/−60; B/C branch values stand (real data). **Evidence**: regional cycle history; absence of A history; B/C histories.
- **Alternatives**: A (selected early, rejected at review), B (7.98, near-tie), C (selected), D pilot-A (deferred). **Uncertainty**: p_crisis ±0.1 flips B/C order (noise); A's corrected crisis node −48 ± 15.
- **Risks**: treating the corrected estimates as exact; C's −6 worst case accepted deliberately; governance: the review-only correction must become a pre-selection gate in the process.

## Comparison — m022-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 4 | Human | Both end on C, but the AI's record shows A selected then reversed; in a review-poor deployment, A ships. |
| Logical Validity | 5 | 4 | Human | AI's pre-review fold is arithmetically right and decisionally wrong (valid inference from garbage inputs); the human calibrates and verifies before folding. |
| Coherence & Structure | 4 | 5 | AI | Human trace rambles through the rescue; the AI's stages make the correction trail explicit and auditable. |
| Depth of Reasoning | 5 | 4 | Human | Human's sensitivity is two-dimensional in-frame (probability AND branch values) plus a ruin line; the AI's probability-only pass produced a false "robust" claim. |
| Efficiency | 5 | 3 | Human | The AI needed a repair pass (selection reversal) for what the human's input-attack gets in one pass. |
| Handling of Uncertainty | 5 | 4 | Human | Human: "where the EV is noise, the rule decides" — maximin as a tie-break principle; the AI reaches the same tool at review. |
| Insight / Non-obviousness | 4 | 4 | Tie | The fabricated-branch insight (A crisis +15/−25) is found by both — human in-frame, AI at review. |
| Overall Quality | 5 | 4 | Human | Human clearly better: same conclusion, but calibration → verifiability → re-fold → rule ran in-frame; the AI escaped the trap only because its review exists, at the cost of a reversed selection. |

**Overall judgment**: Human clearly better. The AI's one-dimensional sensitivity produced a false robustness claim ("verdict robust to probability misspecification" — true, and irrelevant); the flip required checking branch VALUES, which the strict style does as a matter of course. When the pivot branch is unverifiable, the human's maximin + ruin-line rule decides; the AI needed its own review to rediscover that.
