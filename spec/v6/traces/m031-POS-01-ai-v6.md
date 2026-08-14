# v6 Routed AI Trace — m031-POS-01 (blinded)
## Checkout API incident — 14:02–14:06 windowed 3% 504s — on-call root cause
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,science,security,software,supply | g:diagnose,estimate,guarantee,maximize,predict | c:deadline
- Router top3: m031, m044, m070; confidence gap > 0.5 → CONFIDENT → SINGLE ROUTE: m031 first-class pass (m044 stakeholder, m070 evidence-weighting = context). Gate (R3): m003 inversion. Tempo mode ON (P2, deadline); closed-scope fast-path candidate (P8) REJECTED — live incident, cause unknown, not fully specified.
### WHAT — frame + structure-first scan (S1)
- Frame: a windowed phenomenon with its own clock — 4-minute window, recurs daily; "~3%" is a measurement with a built-in baseline control. Chain: checkout → orders rows → provider (folklore) vs internal. Success = falsified hypothesis set + fix that survives the next window.
### WHY — P1 input-provenance audit
- MEASURED: 3% of requests 504 after 30 s, 14:02–14:06, P99 410 ms outside, 5 consecutive weekdays. ANCHOR / INTERESTED-PARTY: folklore "provider maintenance at 14:00" — the narrator benefits (explains outages without digging); the provider DENIES — and the denial is measured evidence against the anchor. Freeze-scope note: the change freeze covers deploys; a scheduled job is not a deploy and is invisible to it. The 14:02-vs-14:00 offset is data that already disagrees with the anchor.
- Hypotheses, each with a falsifier (P6): H1 provider maintenance (folklore) — predicts 14:00-sharp onset, an outbound call in every timed-out trace, all checkout flows affected equally; falsifier = a timed-out trace with no outbound call, or onset ≠ 14:00. H2 scheduled batch job, row locks on a hot table (not a deploy) — predicts a 14:0x cron entry, long-running locked queries at 14:03, timeouts only on orders-touching requests; falsifier = no cron entry, no lock waits, no path-dependence. H3 app fault (GC/pool leak) — predicts non-windowed spread; falsifier = strict windowing. H4 LB health-check artifact — predicts path-independence; falsifier = path-dependence.
- Priors stated so revision is honest: H1 salient (folklore) but sits at odds with the measured 14:02 onset; H2 cheap to test and window-shaped — highest information value, not highest prior.
### HOW — style pass (S1 first-class: hypothesis → discriminating test → update; control; strong-inference)
- Test budget = the window itself: a 20-min APM deep profile CANNOT complete inside a 4-min window (5 windows needed); the cron list + active-sessions/lock snapshot (~2 min, zero load) is not the cheap option, it is the ONLY test that fits — information-per-unit-cost ordering is window-forced, not a preference.
- Test 1 (14:03): cron "reconciliation — 14:00 daily" ✓; 4 long-running queries, 14:02 start, row locks on orders ✓ → H2 alive; H1/H3/H4 strained.
- Discriminating control (same window): split checkout by "touches orders rows" — orders-touching ~3% exceed 30 s; non-orders-touching P99 412 ms. Control = same-window subpopulation, so no second-window confound; blinding/randomization N/A — objective instrument data (trace SQL), observational split defined by data dependency.
- Update ledger: H1 FALSIFIED — timed-out traces contain NO outbound payment call (the wait precedes the call) AND onset is 14:02, not 14:00. H3/H4 falsified — strict windowing + path-dependence. H2 CONFIRMED: job (queue-delayed to 14:02) → 4 connections, row locks on orders → checkout touching those rows waits ≥ 30 s → 504 for the ~3%. Weak link: lock-wait step inferred from timing + control; a direct blocker view (DB wait states) would close it.
### GATES — m003 inversion (R3)
- ≥6 failure categories ranked L×I: (1) folklore accepted unchecked — wrong fix, recurrence (H/H); (2) one-at-a-time elimination — burns the window, evidence gone for the day (H/H); (3) APM profile first — cannot fit the window, 5 days burned (H/H); (4) restart/load-injection repro — destroys the evidence window (H/H); (5) provider escalation — dead end, blames the wrong party (M/L); (6) missing path-dependence — app-fault misdiagnosis (M/H); (7) fix without next-window re-test — silent recurrence (M/H); (8) job rescheduled into another peak (M/L).
- Un-mitigable residual: sampled traces may miss rare non-orders-touching timeouts — instrumentation owner. Never/always: never run a test longer than the window; always falsify the anchor against measured timing; always run the control split before fixing.
### DO — tempo commit (P2) + P3 branch pricing
- Probes executed read-only (zero load, no restart). Fix: reschedule reconciliation to 03:00, cap to 1 connection, lock_timeout 5 s. P3: failure branch priced — if 504s persist next window (job moved elsewhere / second writer), fallback = lock_timeout + connection cap on any scheduled writer; cost = one more window, bounded.
- Verification is itself an experiment: next weekday window, same metric (504 rate + P99 by subpopulation). Pre-registered falsifier: any 14:02–14:06 504s → fix incomplete, investigation reopens.
### REVIEW — insight pass (S2, packet gate)
- I1: the window dictates the test budget — the "cheap" 2-min probe is the only complete test, so cheapness and decisiveness coincide by necessity, not compromise.
- I2: the ~3% figure is the measurement's built-in control — the same-window split reuses the baseline rate, so no second window is needed to attribute the excess to the job.
### DECISION PACKET
- Conclusion: daily 14:00 reconciliation job (queue-delayed to 14:02) holds 4 connections with row locks on orders; ~3% of checkout requests touching those rows hit 30 s → 504; provider folklore falsified (no outbound call; 14:02 onset). Fix: reschedule to 03:00 + 1-connection cap + lock_timeout; verify next window.
- Status: SOLVED (cause confirmed by discriminating control; fix submitted, external verification pending). Assumptions: cron list complete; lock snapshot representative; traces unbiased by subpopulation.
- Evidence: cron entry + 4 locked queries at 14:03; control split (3% vs 0%); timed-out traces with no outbound call.
- Alternatives: A APM-first (rejected — cannot fit the window, weak discrimination), B 2-min decisive probe + control split (selected), C observe-and-wait (rejected — costs a day), D provider escalation (rejected — no outbound call).
- Uncertainty: lock-wait step inferred from timing + control; DB wait-states view at next window closes it. Risks: fix incomplete → pre-registered falsifier reopens; instrumentation residual; job rescheduled into another peak.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical root cause, fix, verification plan |
| Logical Validity | 5 | 5 | Tie | same falsification chain (timing, control split, no outbound call) |
| Coherence & Structure | 4 | 5 | AI | routed pass + inversion gate + packet vs embedded ledger |
| Depth of Reasoning | 5 | 5 | Tie | 14:02 tell now a first-class falsifier (v5 gap closed); strong-inference ≥3 live hypotheses |
| Efficiency | 5 | 5 | Tie | window-forced test ordering; no redundant verification (v5 gap closed) |
| Handling of Uncertainty | 3 | 5 | AI | assumptions, residual lock-view, pre-registered falsifier |
| Insight / Non-obviousness | 5 | 4.5 | Human | human's "wait precedes the provider call" still the sharpest move; AI adds window-fits-test + built-in-control |
| Overall Quality | 4.6 | 4.9 | AI | correctness tied; routed pass closes the v5 depth/efficiency/insight gaps as contract outputs |

Winner: AI (narrow). Why: the routed experiment-design pass installs the baseline's winning moves (timing tell as falsifier, info-per-cost ordering, same-window control split) as mandatory contract outputs plus an inversion gate and window-budget argument; the pure baseline stays ahead only on framed insight, so the win is narrow, not a rout.
