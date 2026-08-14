# v6 Routed AI Trace — m014-POS-01 (blinded)
## Medical-device kit fulfillment — 4-stage serial line, 90/hr contract, 12-week deadline
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,science,security | g:estimate,guarantee,maximize,predict | c:deadline
- Router top3: m014, m031, m018; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m014 + m031 first-class passes, synthesized (m018 = synthesis context). Gate (R3/R4): m003 inversion (guarantee goal). Flags: tempo mode (c:deadline → P2), closed-scope fast-path candidate (P8 — fully specified, deterministic).
### WHAT — frame + structure-first scan (S1)
- Structure first: serial chain → throughput = min(stage rates); the WIP-buffer signature (work piles up ONLY just upstream of one stage) is the system's own statement of where the min lives — read it before the capacity table.
- Frame: decision reduces to "which stage sets the min, which program touches it, what the min becomes"; demand 90/hr vs min 80/hr → shortfall 10/hr. Gate: an option that does not touch the current min element cannot change throughput — pre-filter before pricing.
### WHY — P1 input-provenance audit
- Capacities/durations are given measurements; the only interested-party claim is the managers' "every stage must be upgraded proportionally" (their budget narrative benefits) — falsifiable by the min-element rule, not persuasion. WIP signature is independent evidence, not a claim.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m014 constraint scan — completion contract): binding constraint = S2 assembly: min(120,80,100,110) = 80/hr ∧ WIP at S2's input only ∧ S2 idle 3%. EXPLOIT before invest: recover starvation (staggered breaks, staged changeovers) ≈ +2.4/hr free; subordinate: buffer before S2, priority maintenance, S3 inspects what S2 makes, never starve/flood. SMALLEST-CHANGE-TO-LIFT: A (S2→100) → min = 100/hr ≥ 90, $200k, 8 wk inside deadline; B (→160) → still 100/hr (S3 caps) at 3× cost; C/D/E → 80/hr, zero gain; balanced $1.17M → same 100/hr at 5.85× price. CONSTRAINT-MOVES: post-A min is a TIE S2 = S3 = 100/hr; next lift must touch both (or S3, then re-check); re-locate by WIP signature, not the org chart.
- Pass S2 (m031 scientific check): H1 "S2 binds" with falsifier (any non-S2 program raising throughput kills it — none do); decisive experiment = 2-week post-lift steady-state measurement; update rule: measured < 100/hr → re-diagnose before further spend; the starvation recovery doubles as the free cheap test.
- Synthesis (m018 context): steelman the balanced bundle — "robustness if the constraint moves unpredictably" — priced: with the WIP signature singular at S2, robustness buys the same 100/hr for $970k extra; communicate via the post-A tie, not a blunt rejection. Divergence (V1–V3): m014/m031/general AGREE (A only) — none.
### GATES — m003 inversion (R4)
- ≥6 failure categories ranked L×I: (1) starvation uncorrected → 2.4/hr lost, high; (2) training slip → deadline (front-load A, 8 of 12 wk), high; (3) demand > 100/hr post-lift → tie binds, medium; (4) S3 mis-rated → real cap at 100/hr (verify post-lift), medium; (5) WIP signature misread (measure buffers 2 wk), low; (6) B re-proposed ($600k), low. Residual: demand growth beyond 100/hr at the tie — mitigated by the stated next-lift rule. Never/always: never invest off the min; always re-locate the constraint after a lift.
### DO — P8 fast path (fully specified) + tempo mode (P2, commit at DO)
- Commit: fund A only ($200k); week 1 = starvation recovery + S2 buffer; front-load A (8 wk < 12 wk deadline; cost-of-delay: each week at 80/hr forfeits 10/hr of contract volume); 2-week post-lift measurement; quarterly min re-check.
### REVIEW — insight pass (S2, packet gate)
- I1: the WIP buffer is the line telling you where the money is — the $1.17M "balanced" bundle buys exactly what $200k buys because only one stage can bind at a time.
- I2: B is the most expensive way to do nothing — 3× A's cost for A's exact output; extra assembly capacity is invisible behind S3's 100/hr cap.
### DECISION PACKET
- Conclusion: fund A only; exploit S2 free first; throughput 80 → 100/hr (≥ 90 contract) for $200k inside the deadline; B/C/D/E and the $1.17M bundle add nothing.
- Status: SOLVED (deterministic arithmetic verified ×2; advisory — no external action).
- Assumptions: constant rates, strict serial flow, sustained demand 90/hr, programs mutually exclusive, S3 stable at 100/hr.
- Evidence: min-capacity table pre/post every option; WIP-buffer signature; 3% starvation measurement; Little's Law cross-check (10/hr shortfall × in-line time ≈ observed WIP).
- Alternatives: A (selected) · B (100/hr @ $600k — rejected, capped by S3) · C/D/E (80/hr — rejected, zero gain) · balanced $1.17M (100/hr — rejected) · no-funding floor (contract missed).
- Uncertainty: rate stability, demand near 90–100/hr; post-A S2/S3 tie — either can bind next.
- Risks: training slip (front-load A); demand > 100/hr binds the tie sooner (next-lift rule ready); S3 mis-rating (verify post-lift).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | same verdict (A only), same 100/hr, both inside deadline |
| Logical Validity | 5 | 5 | Tie | identical min-capacity arithmetic on all six options |
| Coherence & Structure | 4 | 5 | AI | dual-pass + gate + packet vs linear TOC narrative |
| Depth of Reasoning | 5 | 5 | Tie | constraint-moves monitoring + smallest-change check now contract outputs, not REVIEW afterthoughts |
| Efficiency | 5 | 4.5 | Human | human's single find→exploit→subordinate→elevate→repeat loop stays leaner than two passes + gates (P8 + min-element-first cut the v5 enumeration cost) |
| Handling of Uncertainty | 3.5 | 5 | AI | human asserts demand; AI states assumptions + next-lift threshold + constant-rate caveat |
| Insight / Non-obviousness | 5 | 5 | Tie | human reads WIP as the system's own signal; AI insight pass now delivers WIP-first + $1.17M-buys-nothing as frame-level outputs |
| Overall Quality | 5.0 | 4.9 | Human (narrow) | gap closed 0.5 → 0.1; margin 0.1 ≤ 0.3 → J1 second-judge flag; verdict roughly equal / complementary |

Winner: Human (narrow — 5.0 vs 4.9, contested J1). Why: the routed m014 contract made WIP-signature-first, exploit-before-elevate, min-element rejection and constraint-moves monitoring first-class HOW outputs instead of verification-discovered afterthoughts, closing the v5 depth and insight gaps (4→5); tempo mode + m003 gate + P8 fast path priced the deadline and kept the loop lean — the only residual gap is efficiency, where the human's single loop still outruns two passes plus gates.
