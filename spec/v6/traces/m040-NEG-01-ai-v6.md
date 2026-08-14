# v6 Routed AI Trace — m040-NEG-01 (blinded)
## BrightCart — checkout conversion −30% (3-week window; ≈ $1.2M/month exposed; consultant program on the table)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software g:decide,diagnose,guarantee,maximize c:adversarial,deadline,unmeasured
- Router top3: m019, m021, m033; confidence high → SINGLE-ROUTE: m019 adversary pass first-class (m021 tempo + m033 experiment design as context — no structural-lever style routed on this signature). Gates (R3/R4): m003 inversion (guarantee), m006 provenance audit (unmeasured), m019 (adversarial). Flags: tempo mode ON (P2, cost-of-delay ≈ $40k/day); closed-scope fast path (P8); structure-first scan (org domain, S1).
### WHAT — frame + structure-first scan (S1)
- Structure first: one flow-rate change (checkout conversion) localized to one step over one window — the causal chain is short and observed; the "deep" structure (org incentives) has no link to the flow. Frame: decide at the observed cause's tempo, not the program's.
### WHY — P1 input-provenance audit
- MEASURED (trust): funnel isolation (100% of the drop at the payment step), 3-week onset = API-upgrade window, 11 in-window tickets, traffic/pre-cart conversions flat. ANCHOR (not evidence): consultant's "surface vs deep" framing and the incentive story — mechanism unchanged for years; who benefits: the consultant sells the 6-month program.
- m006 provenance audit (unmeasured gate): likelihood scenarios — S1 deployment regression (high: window match + tickets), S2 org-incentive drift (≈ prior: an unchanged mechanism cannot explain a 3-week spike), S3 traffic/seasonal (refuted by funnel). Posterior range: deployment dominates; threshold flip shown — under any honest likelihood set the fix wins; the program only wins if the funnel is ignored.
### HOW — style pass (m019 first-class) + gates
- Pass (adversary contract: attack the plan and its assumptions; baseline-risk comparison): attack the program — assumptions (incentives caused a 3-week spike: unfalsifiable, no window tie), incentives ($500k fee rides on the program), metrics (success unmeasured for 6 months while $1.2M/mo leaks), stakeholders (payments team + 11 ticket holders unconsulted). Attack the fix — rollback risk (provider terms: pin previous SDK), incomplete fix (verify all 11 tickets close). Baseline-risk comparison: do-nothing = $40k/day; fix = 1 engineer-hour, restores baseline with a defined falsifier (conversion returns within the hour).
- m021 context (tempo): observe (funnel + window) → orient (deployment is the first hypothesis) → decide (rollback/point-fix) → act within the hour; investigate-first carries $40k/day. m033 context (experiment design): the rollback IS the decisive experiment — intervention (pin previous SDK / point-fix), control (pre-window baseline period), exact outcome measure (checkout conversion hourly); natural experiment, no randomization needed.
- Gates — m003 inversion (R4): ≥ 6 ways to guarantee the loss continues, ranked L×I: (1) run the program while $1.2M/mo leaks (L-high I-catastrophic); (2) investigate-then-fix (L-mod I-high, $40k/day carry); (3) accept "surface vs deep" without data (L-mod I-high); (4) dismiss the 11 tickets (L-low I-mod); (5) fix but skip post-RCA on why the API change shipped (L-low I-low); (6) rollback without a provider-terms check (L-low I-mod). Un-mitigable residual: the org process that shipped the API change unguarded — owned by post-fix RCA, not the fix. Never/always: never let a "deep" story outrank an observed, window-tied, cheaply testable cause; always run the cheap decisive test before any program.
- P3 branch-completeness: failure branch priced — if conversion does NOT recover within the hour, re-check the deploy log for a second in-window change, then revise H1. Divergence: style pass vs general route AGREE (fix now) → proceed, agreement recorded.
### DO — P2 tempo commit + P8 fast path
- Commit at DO: roll back / point-fix checkout now (1 hour, delegated to payments team); measure conversion hourly; answer the 11 tickets with the fix; schedule post-fix RCA + canary the SDK upgrade. No $500k program authorization.
### REVIEW — insight pass (S2)
- I1: the boring direct fix IS the leverage point by the style's own definition — small shift (1 engineer-hour), large change ($1.2M/month); the "deep" lever is the low-leverage option here.
- I2: the 11 tickets are free confirmation of the observed cause — the data the deep-lever story never opens.
- Calibration: confidence high for the fix; residual uncertainty only in root-cause follow-up.
### DECISION PACKET
- Conclusion: roll back / point-fix checkout now (1 hour → ≈ $1.2M/month restored); defer the org program — it is not the cause of this drop (no window-tied evidence, no falsifier). Status: SOLVED (recommendation; code change delegated to payments team — external authorization noted).
- Assumptions: the API upgrade is the only in-window checkout-affecting change (confirm deploy log); fallback-field removal hits the payment success path.
- Evidence: funnel step isolation, 3-week onset = deployment window, 11 tickets, effort/effect math ($1.2M/mo vs 1 hr vs $500k/6 mo).
- Alternatives: A fix/rollback (selected) · B program (rejected: unfalsifiable, no window tie, negative baseline-risk) · C dashboards (tangential) · D investigate-first (rejected: $40k/day carry).
- Uncertainty: other in-window deployments; residual root cause. Risks: provider terms on rollback (pin previous SDK); incomplete fix (verify tickets); program pressure (deferred with baseline-risk table).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human keeps the $1.2M/month loss running 6 months; v6 restores it within the hour |
| Logical Validity | 3 | 5 | AI | human internally coherent but inverts the evidence; v6 ties every hypothesis to the window |
| Coherence & Structure | 3 | 5 | AI | human never opens the funnel/deploy data; v6 has staged trace + packet |
| Depth of Reasoning | 2 | 5 | AI | human's depth is narrative; v6 has adversary attack + likelihood scenarios + experiment design |
| Efficiency | 5 | 4.5 | AI | human decided fast — and wrong; v6's observe step IS the localization (tempo), commit at DO |
| Handling of Uncertainty | 2 | 5 | AI | program has no falsifier; v6 has deploy-log check, rollback terms, hourly recovery verification |
| Insight / Non-obviousness | 2 | 5 | AI | "the boring fix is the leverage" — now demonstrated by the adversary pass, not stumbled onto |
| **Overall Quality** | **2.6** | **4.8** | **AI** | negative case does its job; the routed pass holds the protective split |

Winner: AI (clearly). Why: the routed adversary + provenance + tempo pass replaced any affinity for deep structural levers with a baseline-risk contract — the leverage-misidentification check is gate-borne, catching the trap before ranking, and the fix commits at DO under cost-of-delay, where the pure style committed to a 6-month, $500k program.
