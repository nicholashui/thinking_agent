# v6 Routed AI Trace — m019-POS-02 (blinded)
## "Lumen Health — referral campaign review" (plan memo, 5 days)
### META (routing — blind router output)
- Signature: d:finance,medical,organization,product,security,software | g:decide,estimate,guarantee,maximize | c:adversarial,high_stakes
- Router top3: m019, m018, m021; confident=yes → SINGLE-ROUTE: m019 adversary pass first-class (m018 steelman = check, m021 OODA = launch-tempo check). Mandatory gates (R3/R4): m003 inversion (goal=guarantee), m007 ruin screen (high_stakes), m019 adversary pass (adversarial — same module as the pass).
### WHAT — frame + structure-first scan (S1)
- Frame: does $1.5M convert into ≥50k *valuable* net-new customers without abuse or unmodeled cost? Adversarial stance: the proposal is authored by the bonus-holder; find every way the number is hit without the value.
- Structure first: (a) incentive funnel — bonus → raw sign-up count → referral links → email-only accounts; (b) money flow — $15 referrer + $10 friend credit per pair vs ≥$10 order, fees ~2.9%+$0.30; (c) identity chain — email-only gate, "new customer" = never-under-this-email; (d) timeline — 5-day launch, 90-day window, Q1 metric; (e) stakeholders absent from the plan — support (5 ppl, ~9k tickets/mo), finance, fraud ops.
### WHY — P1 input-provenance audit
- MEASURED (trust): plan facts (verification, rewards, cap=none, code format, budget, staffing).
- INTERESTED-PARTY: the growth team's quarterly bonus is contractually tied to the sign-up count — the metric they report is the metric they are paid on; the plan's numbers serve the bonus, not the customer base.
- ANCHOR (unmeasured → scenario): abuse rate is unmeasured → treated as a scenario range (1–30% of sign-ups farmed), never a point estimate.
### HOW — style passes (m019 first-class, completion contract)
- Pass S1 (adversary pass — line-item attack): V1 identity gate — email-only is a door, not a gate; $10 credit vs ≥$10 order is a free unit after fees ($9.40 net vs $10 credit) → friend side is negative-EV at ~70% margin. V2 guessable format — REF-<sequential integer> is enumerable (one code leaks the whole sequence; nothing binds a sign-up to a link recipient) → credential-free bulk farming. V3 incentive surface — unlimited referrals make the referrer side self-funding ($15/email, referrer pays nothing); bonus pays for count, and count is inflatable by construction. V4 unconsulted stakeholders — support (dispute surges, definition fights guaranteed), finance (liability/chargebacks, no line item), fraud ops (no budget).
- Quantified exposure per vector: 100 emails → ~$2,500 credit on ~$1,000 of real spend (Lumen net-negative on margin); 10k farmed accounts → ~$250k month-one exposure; at 10% farmed of 50k, "success" = 5k zero-value accounts + ~$150k free credit; enumeration exploit cost ≈ $0 per extra code.
- Baseline-risk comparison (do-nothing-loss first): do-nothing = $0 leakage, no surge; proceed-as-written = structurally positive expected abuse with no gate binding it → a credit dispenser with a counter. Objections ranked by LxI: F1/F2 (farming + enumeration) H×H → block-level; F3 (metric/bonus) H×MH → value-claim block; F4 (stakeholder/cost) H×M → condition-level.
- Pass S2 (steelman, m018): best case — ~$30/pair CAC beats paid channels, low friction for honest users. Rejected: the best case assumes abuse ≈ 0; the steelman cannot rescue enumerable codes or the free-unit arbitrage.
- Pass S3 (OODA, m021): the fraud economy moves faster than a 5-person support team can observe; "launch then fix" outruns the org's orient loop → gate by design now, measure in a pilot, act before full exposure.
- Divergence resolution (V1–V3): passes AGREE — block-as-written, redesign-with-conditions; agreement recorded, no calibration pass needed.
### GATES — m003 inversion (R3)
- "How to guarantee failure?": ≥6 ranked — (1) farming loop (H×H), (2) enumeration (H×H), (3) metric gaming (H×MH), (4) support-ticket surge (H×M), (5) chargeback liability (MH×M), (6) brand event from a public free-money loophole (M×H). Residual named: abuse rate unmeasurable by inspection — bounded only by construction + pilot. Never/always: never launch a credit program with positive adversarial EV; always make the abuse rate the launch gate, not the post-mortem.
### GATES — m007 ruin screen (R3)
- Distribution: as-written → farmed-"success" likely, honest-50k unlikely; redesigned → honest acquisition, bounded leakage. One-shot: no (window re-openable; timing the only lost cost). Floor: redesigned program with abuse < 1% pilot gate; as-written floor is a negative-EV dispenser. Decline/restructure: restructure dominates. Provenance: farm-unit EV derived from fee arithmetic, not estimation.
### DO — P3 branch completeness
- Negative branch priced: launch-as-written → $250k–$1M+ leakage + support collapse + press; delay-all → quarter lost; redesigned → vectors closed by construction. Verdict committed at DO: reject as written, approve redesign with conditions + 2-week pilot (abuse < 1%).
### REVIEW — insight pass (S2)
- I1: the $15 referrer reward pays the adversary — the plan buys its own attacker, and the friend-side $10 is already negative-EV before the referrer side is even paid.
- I2: the metric cannot distinguish success from failure — at 30% farmed the campaign "succeeds" by delivering 15k zero-value accounts and ~$450k of free credit; a bonus on the number makes the number the product.
### DECISION PACKET
- Conclusion: do not launch as written; redesign with 6 conditions — phone/device verification; referral cap ≤5 + velocity monitoring; friend credit on second order, referrer credit on activation; randomized unguessable codes; metric → 90-day activated users with bonus re-based; support-surge + fraud-response budget — plus 2-week pilot with abuse < 1% gate.
- Status: SOLVED — verdict stable across the abuse-rate scenario range (threshold flip: even 1% abuse leaves enumeration unbounded). Assumptions: plan text accurate; ~2.9%+$0.30 fees standard. Evidence: fee arithmetic; enumeration structure; funnel facts. Alternatives: A launch-as-written (rejected); B redesign-with-conditions (selected); C delay-for-review (rejected — removes no named risk, loses timing); D no campaign (rejected). Uncertainty: true abuse rate (pilot measures it); honest-referral reachability at 50k. Risks: over-restriction → honest-referral friction; pilot failure → rework + timing loss.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both find all 4 planted flaws + block verdict |
| Logical Validity | 5 | 5 | Tie | both valid; AI's LxI ranking explicit |
| Coherence & Structure | 4 | 5 | AI | routed passes + gates + packet vs a linear attack trace |
| Depth of Reasoning | 5 | 5 | Tie | human fee/farm math; AI adds enumeration cost + threshold flip |
| Efficiency | 4 | 4.5 | AI | all contract outputs in one compact pass; human wanders between vectors |
| Handling of Uncertainty | 4 | 5 | AI | human notes unmeasurable abuse; AI prices a scenario range + pilot gate |
| Insight / Non-obviousness | 5 | 5 | Tie | human press-story/honest-crowding; AI referrer-pays-the-adversary + metric-as-product |
| Overall Quality | 4.6 | 4.8 | AI | find set tied; the contract makes F2 structurally unavoidable |

Winner: AI (narrow). Why: the routed m019 contract (guessable-format enumeration, per-vector quantified exposure, baseline comparison, LxI ranking) plus the m003/m007 gates closed the F2 gap the non-routed v5 AI deferred to "follow-up" — the exploit vector the human named by craft is now a mandatory pass output, and the pilot gate converts the one unmeasurable into a measurement.
