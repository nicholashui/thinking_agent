# v6 Routed AI Trace — m022-POS-01 (blinded)
## Aurigen Biotech — Phase 3 continue vs license now
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,strategy | g:decide,estimate,guarantee,predict | c:(none)
- Router top3: m023, m024, m050; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m023 + m024 first-class passes, synthesized (m050 = synthesis context). Gate (R4): m003 inversion (guarantee goal). Flags: closed-scope fast-path candidate (P8 — fully specified inputs); no tempo (no deadline).
### WHAT — frame + structure-first scan (S1)
- Decision: continue Phase 3 vs license now; every input is given and calibrated → closed scope. Structure: 3 decision nodes (D1 today / D2 post-success / D3 post-failure) + 3 chance nodes (trial, market, rescue) — the rescue arm (cost $15M, p 0.25) is IN the supplied data though unflagged as an option; a tree with a stubbed failure branch is not a tree.
### WHY — P1 input-provenance audit
- MEASURED/calibrated (trust): p_success 0.6 (Phase 2 signal + comparable trials), market 0.5/0.5, rescue 0.25 (comparable programs), offers firm; no anchor, no interested-party input. H1 the tree's fold is the decision; falsifier: any supplied branch left unpriced → P3.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m023 opportunity cost — value each choice by its best forgone alternative): continue forgoes the $55M now; launch forgoes the $150M; abandon-on-failure forgoes a rescue worth 0.25×170−15 = 27.5 — the forgone-alternative lens makes the failure branch un-stubbable. Fold: D2 = max(launch 170, license 150) = 170; D3 = max(rescue 27.5, abandon 0) = 27.5; root = 0.6×170 + 0.4×27.5 − 40 = **73** > 55 → continue.
- Pass S2 (m024 regret — long-horizon): regret licensing now if AT-9 succeeds (forgoes EV 18 vs the license); regret launching on success into low demand (the license beats launch by $130M in that state). Asymmetry favors continue: the downside states are priced (rescue), the upside is uncapped.
- Synthesis (V1–V3): passes AGREE with the general route → proceed, agreement recorded; m050 context (inversion-by-safety): every failure pathway (trial fail, rescue miss, low-demand launch) enumerated — none unpriced.
### GATES — m003 inversion (R3)
- >=6 ranked failure categories (L×I): (1) p_success overestimate — margin to p* 0.474 is only 0.126 high/catastrophic; (2) trial fails AND rescue misses (joint 0.30) → $55M sunk vs the $55M license-now high/medium; (3) launch into low demand (joint 0.3) — license beats launch by $130M there medium/medium; (4) rescue q overestimate (q* 0.088 — 3× margin) low; (5) regulatory tail / financing dilution low; (6) pipeline correlation low.
- Un-mitigable residual: calibration-band error on 0.6 (Phase 2 signal, not a measured frequency). Never/always: never abandon on failure while the rescue clears q* by 3×; always re-check the $170M license threshold before accepting a success-node offer; always price every branch the data supplies.
### DO — P8 closed-scope fast path + P3 branch completeness
- Fully specified → stages compressed; no retrieval. P3: failure branch priced BEFORE selection — D3 = 27.5 (not 0), root 73 (not 62), p* = 67.5/142.5 = **0.474** (0.56 without the rescue arm). Commit: continue; on success launch (reject the $150M — $20M short of indifference); on failure rescue (do not abandon); reject the $55M pre-trial license.
### REVIEW — insight pass (S2, packet gate)
- I1: the failure branch is the policy's robustness asset — the rescue clears its break-even 3× while trial success clears p* by only 0.126; the parameter that matters is the one the tree forces you to price.
- I2: the $150M offer is a state-contingent hedge (+130 low-demand, −170 high); its EV gap to launch is exactly the launch edge — $170M is a renegotiation floor, not a ceiling.
### DECISION PACKET
- Conclusion: continue Phase 3; contingent policy — launch-on-success (reject $150M), rescue-on-failure (do not abandon), reject $55M pre-trial license. Fold 170/27.5/73; thresholds p* 0.474, license >= $170M, q* 0.088.
- Status: SOLVED (exact fold-back, dual-route verified, no external action). Assumptions: 0.6/0.5/0.25 calibrated; offers firm; cash non-binding.
- Evidence: 73 vs 55; rescue contribution 0.4×27.5 = 11; p* 0.474 (0.56 stubbed); 170 vs 150 = $20M cushion; q* 0.088 vs 0.25.
- Alternatives: license-now (rejected, 18 short); abandon-on-failure (rejected, 0 vs 27.5); rescue (selected). Uncertainty: p_success ±0.1 clears 0.474; rescue q robust to 3× error; license negotiability (>= 170 flips D2).
- Risks: trial slippage into the financing window; accepting the success-node license without re-checking 170; rescue branch re-stubbed at implementation.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | same verdict + contingent policy; rescue in-frame in both |
| Logical Validity | 5 | 5 | Tie | full fold 170/27.5/73 in both — v6 AI prices D3 in-frame (v5 AI: 62, p* 0.56) |
| Coherence & Structure | 4 | 5 | AI | human home-voice winding; dual-pass + gate + packet auditable |
| Depth of Reasoning | 5 | 5 | Tie | both compute p*/170/q*; AI adds m003 ranked failures + m023/24 cross-checks |
| Efficiency | 5 | 5 | Tie | both one clean pass; AI's P8 fast path, no review repair |
| Handling of Uncertainty | 5 | 5 | Tie | three thresholds + declared residual in both |
| Insight / Non-obviousness | 4 | 5 | AI | failure-branch-as-robustness-asset; $150M as state-contingent hedge / renegotiation floor |
| Overall Quality | 5.0 | 5.0 | Tie | identical rubric completion; AI edges breadth |

Winner: AI (narrow). Why: the routed P3 branch-completeness gate + m023 opportunity-cost pass priced the failure branch (rescue, 27.5) in-frame — the exact quantified gap (62 vs 73; p* 0.56 vs 0.474) where the non-routed v5 AI lost this baseline; the human's tree discipline equals the result, the routed contracts add ranked failure coverage and the hedge/floor insight.
