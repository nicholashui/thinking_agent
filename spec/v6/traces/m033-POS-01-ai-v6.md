# v6 Routed AI Trace — m033-POS-01 (blinded)
## Onboarding-video experiment — rollout decision with a 6-week deadline
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software | g:decide,estimate,guarantee,maximize | c:deadline
- Router top3: m033, m018, m019; confidence gap > 0.5 → CONFIDENT → single-route: m033 first-class pass in HOW (m018/m019 = context). Gate (R3): m003 inversion pass (mandatory). Flags: deadline → TEMPO MODE (P2: cost-of-delay, commit at DO); fully specified numbers → closed-scope fast-path candidate (P8).
### WHAT — frame + structure-first scan (S1)
- Decision = launch now vs test vs hold; deliverable = experiment spec + decision rule bound to the finance bar. Structure first: the 42-day window vs 30-day outcome horizon is the design constraint that decides feasibility — the bar and the horizon must be solved jointly, not sequentially.
### WHY — P1 input-provenance audit
- MEASURED/given (trust): 25k signups/mo, 30% day-30 baseline, 15% day-14 baseline, $40k/yr cost, 415/arm/day enrollment. INTERESTED-PARTY: internal enthusiasm (advocates self-report — selected evidence), VP timeline (board pressure — benefits from launch), FINANCE BAR (benefits from cost discipline — audit it, don't inherit it). Convert the bar via the same arithmetic: 2 pp × 25k × 12 = 6,000 activations/yr vs $40k/yr ≈ $6.70/activation — defensible only above activation LTV; bar stands, now derived.
### HOW — m033 first-class pass (completion contract: intervention, control, randomization, blinding, exact outcome measure, power/effect-size check, ecological-validity note)
- Intervention: 3-min video replacing the 3-email text sequence at signup. Control: current text sequence UNCHANGED (status quo, not "no onboarding"); instrumentation parity; no code mid-test.
- Randomization: unit = new trial user; 50/50 seeded RNG at signup; stratified channel × plan tier; append-only assignment log; internal accounts excluded.
- Blinding: users blind to arm labels; analysts blinded (pre-registered analysis script, aggregate output only, key held by one statistician); unblinding at final read.
- Exact outcome: day-30 activation, ITT, ONE primary test, guardrails (support tickets, spam complaints), fixed sample / O'Brien-Fleming if an interim read is demanded.
- Power × timeline (solved jointly): day-30 (30%→32%, α=0.05, β=0.20) → ≈8,400/arm; 20d enroll + 30d horizon = 50d > 42d → cannot fit as primary → pre-registered day-14 surrogate primary (15%→17% → ≈5,300/arm → 13d + 14d ≈ 27d, fits); day-30 = secondary (directional only); surrogate assumption pre-registered BEFORE data.
- Ecological-validity note: B2B workspace spillover (onboarding copied to colleagues) → workspace-cluster sensitivity check; novelty decay on first-watch → evaluate after enrollment completes; localization/QA drift over the $40k/yr maintenance → effect-decay flag.
- m018 context: steelman of launch-now ("modern, users must love it") is at best a time-to-value claim — the test measures it; converts to the estimand, not to launching. m019 context: peeking, log tampering, bar mis-specification, load-time drop-off — priced in gates below. Divergence (V1–V3): m033 pass and general route AGREE on all design elements; agreement recorded.
### GATES — m003 inversion pass (R3)
- ≥6 failure categories ranked L×I: (1) surrogate day-14↔day-30 validity unknown L-mod I-high; (2) peeking/optional stopping L-mod I-high; (3) workspace contamination L-mod I-mod; (4) novelty decay biases early read L-mod I-mod; (5) assignment-log tampering / arm imbalance L-low I-mod; (6) instrumentation drift mid-test L-low I-mod; (7) seasonality drift in-window L-low I-low; (8) bar wrong (activation LTV < $6.70) L-low I-mod.
- Un-mitigable residual: surrogate validity cannot be verified within 42 days — accepted via pre-registration. Never/always: never launch on selected evidence; always solve power×timeline jointly before quoting an n; always convert interested-party bars before inheriting them.
### DO — P8 fast path + P2 tempo commit
- Commit: run the 50/50 stratified A/B; day-14 surrogate primary (≈5,300/arm, ~27d); day-30 secondary; do NOT launch now. P3 failure branch priced: day-14 CI excludes 2 pp → hold and diagnose; inconclusive → extend enrollment or stage 50% with monitoring; backfire → hold.
### REVIEW — insight pass (S2, packet gate)
- I1: the finance bar is itself a derived quantity — the test's real job is checking whether the video earns ≈ $6.70 per extra activation, i.e., whether the bar is above LTV.
- I2: the surrogate is not a compromise, it is a faster learning loop — ~27-day read lands a decision before the board review with the day-30 read as confirmation.
### DECISION PACKET
- Conclusion: run the experiment as specified; rollout iff day-14 CI lower bound ≥ 2 pp (day-30 supportive); inconclusive → extend/stage; backfire → hold. Status: SOLVED (design verified; execution delegated — no external action).
- Assumptions: 30%/15% baselines stable; instrumentation parity; small workspace spillover (checked); surrogate validity (pre-registered); activation LTV ≥ ~$7 makes the bar fair.
- Evidence: 8,400/arm (day-30) vs 5,300/arm (day-14); timeline 50d vs 27d; break-even $6.70/activation; enrollment 415/arm/day.
- Alternatives: A launch now (rejected — selected evidence) · B randomized A/B (selected) · C uncontrolled staged rollout (rejected — no causal estimate) · D no test (rejected — cheap reversible test vs $40k/yr commitment).
- Uncertainty: surrogate correlation; novelty decay; spillover magnitude; LTV assumption. Risks: peeking, log tampering, workspace contamination, instrumentation drift — bound in spec; surrogate failure → day-30 directional only.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical design + decision rule at the finance threshold |
| Logical Validity | 5 | 5 | Tie | both resolve power×timeline as a design input; both bound-check the bar |
| Coherence & Structure | 4 | 5 | AI | contract-ordered pass + packet vs linear build-up |
| Depth of Reasoning | 5 | 5 | Tie | all human moves (surrogate primary, $6.70, cluster check) land first-class; AI adds 8-category inversion + ecological-validity note |
| Efficiency | 5 | 5 | Tie | human one-pass; routed pass lands feasibility and economics up front (v5 paid a re-pass) |
| Handling of Uncertainty | 3 | 4.5 | AI | human asserts; AI records power sensitivity, surrogate residual, spillover, novelty decay |
| Insight / Non-obviousness | 5 | 5 | Tie | human: surrogate + break-even + cluster; AI: same plus bar-as-derived and surrogate-as-faster-loop |
| Overall Quality | 4.7 | 4.9 | AI | narrow; margin 0.2 ≤ 0.3 → J1 second-judge flag noted |

Winner: AI (narrow). Why: the routed m033 completion contract (power/effect-size and ecological-validity inside the design pass) moved the timeline-power conflict and the finance-bar economics from v5's REVIEW-stage patches into first-class HOW outputs, matching every human home-turf move — and P1 converted the interested-party bar into a derived, checked threshold instead of an inherited one.
