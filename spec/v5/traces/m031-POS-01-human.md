# Human Baseline — m031-POS-01
## Style: Scientific Method (pure: Hypothesis → Experiment → Update) — visible reasoning trace

**Step 1 — Frame and measure the phenomenon.** Symptom: 14:02–14:06, ~3% of checkout requests 504 after 30 s; otherwise P99 410 ms. Define the measurement: % of requests exceeding 30 s per minute, bucketed by which tables/upstreams the request touched. What cannot be measured, cannot be tested.
Operationalization: "touches the orders table" is read from each trace's SQL statements; the 3% figure is the window's timeout rate minus the baseline rate, so the measurement carries its own control.

**Step 2 — Hypothesis set, each carrying its falsifier.**
- H1 payment-provider maintenance (folklore): predicts 14:00-sharp onset, a payment-provider call present in every timed-out trace, all checkout flows affected equally. Falsifier: any timed-out trace with no outbound call, or onset at 14:02.
- H2 scheduled batch job holding row locks on a hot table (not a deploy): predicts a 14:0x cron entry, long-running locked queries at 14:03, timeouts only on requests touching that table. Falsifier: no cron entry, no lock waits.
- H3 app fault (GC pause / pool leak): predicts timeouts spread across tables and across the day, not windowed. Falsifier: strict 14:02–14:06 windowing.
- H4 LB health-check artifact: predicts timeouts independent of request path. Falsifier: path-dependence.
- Priors, stated so revision is honest: H1 is salient (team folklore), but folklore says 14:00 and we observe 14:02 — the prior starts at odds with the data. H2 is cheap to test and window-shaped; it earns the highest information value, not the highest prior.

**Step 3 — Order tests by information per unit cost.** Cheapest decisive test first: read the cron list (1 min, zero load) + snapshot active sessions/lock waits at ~14:03 (1 min). This discriminates H2 from {H1, H3, H4} in 2 minutes and disturbs nothing.
The 20-min APM deep profile is the last resort, not the default: it shows where time goes but cannot explain why only ~3% of requests, only inside 14:02–14:06 — high cost, weak discrimination.

**Step 4 — Run test 1 (at 14:03).** Cron list: "reconciliation — 14:00 daily" ✓. Active sessions: 4 long-running queries, 14:02 start, row locks on orders ✓.
H2 alive; H1, H3, H4 strained — why would an app fault or LB artifact line up exactly with the job?

**Step 5 — Run the discriminating control.** Same 14:02–14:06 window, split checkout requests: those touching orders rows vs those not. Orders-touching: ~3% exceed 30 s. Non-orders-touching: P99 412 ms.
This is the discriminating test: only H2 predicts the split, because only H2 binds the failure to a specific data dependency. Decisive.

**Step 6 — Update, explicitly.** H1 falsified: timed-out traces contain no outbound payment call (the wait precedes the provider call) AND onset is 14:02, not 14:00. H3, H4 falsified: strict windowing + path-dependence. H2 confirmed with a causal chain: job (queue-delayed to 14:02) → 4 connections with row locks on orders → checkout requests touching those rows wait ≥30 s → 504 for the ~3% in the window.
Confidence is not certainty: the chain's weak link is the lock-wait step, inferred from timing + control; a direct blocker view (DB session wait states) would close it.

**Step 7 — Fix and re-test.** Reschedule the job to 03:00, cap it to 1 connection, set lock_timeout. Verification is itself an experiment: next weekday window, same metric, expect 0 timeouts and flat P99.
Pre-register the falsifier: if 14:02–14:06 still shows 504s, the fix is wrong or incomplete and the investigation reopens. Anything else is speculation.

**Trace summary box.** Folklore → hypothesis with a falsifier → 2-minute scheduler+lock test → same-window control split → update ledger (H1 killed by timing + missing outbound call; H2 confirmed by lock chain) → fix → next-window re-test.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Scientific Method style — hypotheses always carry falsifiers, tests ranked by information-per-unit-cost, update made explicit, verification re-run as an experiment. Every winning move (the 14:02 tell, the orders-rows control split) is experiment-designed, not intuited.*
