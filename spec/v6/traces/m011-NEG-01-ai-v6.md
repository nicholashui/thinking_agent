# v6 Routed AI Trace — m011-NEG-01 (blinded)
## SwiftCourier — complaint spike, 1-month decision window
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,product,science,software,supply | g:diagnose,guarantee,maximize | c:deadline
- Router top3: m031, m040, m066; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m031 + m040 first-class passes, synthesized (m066 = synthesis context). Gate (R3): m003 inversion (route-listed; guarantee goal prepends it). Flags: tempo mode ON (P2 — decision inside a month).
### WHAT — frame + structure-first scan (S1)
- Frame: diagnose the 120→240/day complaint rise and plan an intervention; decision due in a month; leadership favors speed targets + 15% capacity. Structure first: complaint count = measured PROXY (meaning can change); GPS delivery time = STATE. Hypothesized loops: complaints→pressure→speed→complaints (balancing); safety→attrition→capacity→delivery→complaints (fix that backfires). Local data: (a) GPS median 28 min, unchanged (27.5 before); (b) 80% "delivery time/ETA" tags; (c) 2% dispute-verified; (d) live-tracking app update week 5; (e) headcount/routes/mix unchanged.
### WHY — P1 input-provenance audit
- (a)–(e) are MEASURED local data — evidence, not diagram-fodder. Leadership's speed/capacity package = INTERESTED-PARTY option (they own the delivery metric; "cut the target" is the visible knob). Key move: the series' meaning changed in week 5 (app rollout) without the state changing — proxy drift, testable.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m031 scientific method — falsification battery): H1 service degradation: edge "complaints driven by actual delivery time" FAILS the audit (28 vs 27.5) → H1 falsified on its own edge. H2 expectation/funnel shift (live tracking: ETA shows 12 min, arrives 28): spike timing matches week-5 rollout; 80% tag share with unchanged actuals; 2% verified share ⇒ mostly unverified claims → H2 leads. H3 mix/seasonality: refuted by (e). Weakness gate-check (hypothesis-space blind): all three hypotheses enumerated before testing; none tested in isolation.
- Pass S2 (m040 leverage points — misidentification gate-check): the trap this signature punishes is "loop unbalanced → strengthen dampening edges" (the human's move). Leverage check: which loop edge is falsifiable against local data? "Speed→complaints" edge = FAILED audit; "displayed-ETA→complaints" edge = testable (A/B). High leverage = the expectation/display channel + the measurement system (complaint meaning), NOT delivery speed; flow targets and courier buffers are low-leverage here.
- Synthesis (m066 strong inference): pair DECISIVE experiments that discriminate H1 vs H2 vs H3, not single-hypothesis tests: (1) A/B the tracking display (correct/hide ETA countdown on a random 10–20% of orders, 2-week read) — H2 ⇒ complaints drop on the corrected arm; H1 ⇒ no effect, audit trend confirms; (2) dispute-verification sampling of tags (n ≈ 100/day) — decides whether the claims are events at all. Divergence (V1–V3): m031 and m040 AGREE (reject speed/capacity; display fix + measurement); general route agrees (v5 AI's answer) → proceed, agreement recorded.
### GATES — m003 inversion (R3)
- ≥6 ranked failure categories (L×I): (1) speed target 34→28 imposed → near-miss safety events + courier resignations (graded pilot: 3 near-misses, 4 resignations) high/catastrophic; (2) +15% capacity on a falsified premise → cost + idle fleet, no complaint change high/medium; (3) display fix only if H2 wrong → complaints persist, credibility loss medium/medium; (4) A/B without tag segmentation → cannot read which class moved medium/low; (5) policy from 98%-unverified claims medium/medium; (6) rushing past the 2-week read inside the month deadline medium/medium; (7) no churn proxy → attrition blind spot low/medium.
- Un-mitigable residual: an unmeasured latent service issue under H2's shadow — owned by the dispute-verification sample. Never/always: never scale policy to a proxy whose edge failed its audit; always fix the displayed promise before touching delivery operations; always segment + verify before intervening.
### DO — P2 tempo commit (deadline) + P3 branch completeness
- Budget: week 1 instrument (tag segmentation, dispute sample, display A/B ramp); weeks 2–3 read; decision week 3 — one week margin inside the month. Commit: reject speed targets and capacity; fix ETA display accuracy; run A/B + verification sample; watch churn. Negative branch priced: if the A/B shows display correction does NOT move complaints (H2 wrong, H1 real) → audit-trend recheck + verification sample, THEN a strictly conditional speed-target pilot with safety/attrition monitoring — never unconditional.
### REVIEW — insight pass (S2, packet gate)
- I1: the series' information content changed in week 5 without the service changing — the company now measures disappointment (12 shown vs 28 actual), a gap it created for free; correcting the displayed promise is near-zero cost and diagnostic.
- I2: the management-favored fix is exactly the one the data refutes: speed targets act on the visible edge while the invisible safety→attrition loop converts the intervention into its own failure — the fix that backfires; the graded pilot's near-misses/resignations are the inversion gate's prices.
### DECISION PACKET
- Conclusion: spike = expectation/funnel shift from live tracking (ETA mismatch), not service degradation; reject speed/capacity; fix display; instrument + verify complaints; A/B the display; decide week 3 on measured data.
- Status: SOLVED (diagnosis supported by local measurements; plan with priced fallback; decision 1 week inside deadline).
- Assumptions: (a)–(e) accurate; tags meaningful; rollout causal; A/B read time 2 weeks.
- Evidence: GPS unchanged; rollout-week timing; 80% tags; 2% verified; (e) unchanged; m003-priced branch.
- Alternatives: A speed+capacity (rejected — falsified edge; priced: near-misses/resignations) · B display-fix + measurement (selected) · C monitor-only (rejected — action window).
- Uncertainty: H2 magnitude unknown until A/B (2 weeks); residual H1 (~15–20%) with priced fallback; series 98% unverified.
- Risks: H2 wrong → measurement program still detects H1 within 2 weeks (diagnostic under both); imposing A risks safety incidents + attrition; churn proxy needed.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human prescribed the speed/capacity fix (hidden truth: near-misses + resignations); AI refused, targeted the confound |
| Logical Validity | 4 | 5 | AI | human diagram internally consistent but edge unfalsified; AI tests every edge |
| Coherence & Structure | 4 | 5 | AI | dual-pass + inversion gate + packet vs self-justifying diagram |
| Depth of Reasoning | 4 | 5 | AI | human drew the side-effect loop but mitigated it; AI prices it as a rejection cause (m003) |
| Efficiency | 3 | 5 | AI | human jumps to intervention; AI's measurement plan is the minimal correct action, fits the month |
| Handling of Uncertainty | 3 | 5 | AI | human folds contradictions into the diagram ("lagging instrument"); AI quantifies verification gap + fallback |
| Insight / Non-obviousness | 2 | 5 | AI | proxy-meaning change; fix that backfires; display gap created for free |
| Overall Quality | 3.1 | 4.9 | AI | AI clearly better |

Winner: AI (clearly). Why: the router held m011 out of top-3 on this signature (diagram-substitutes-for-measurement failure), installing instead a falsification battery (m031) + leverage verification (m040) + decisive-experiment pairing (m066), with m003 inversion pricing the management-favored branch (near-misses, resignations) before DO — the human baseline is exactly the trap this route was built to avoid.
