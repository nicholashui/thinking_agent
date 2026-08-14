# Human Baseline — m079-NEG-01
## Style: Confirmation Bias Hunting (pure) — visible reasoning trace

**Step 1 — State the belief, then open the hunt.**
Omar's belief: "the 02:00 DB migration caused the outage." A belief this consequential deserves maximal doubt.
What would change my mind? Anything that points elsewhere: a healthy-looking DB, a concurrent change, an external-party signal. Seek all of it before any irreversible action.

**Step 2 — Hunt for disconfirmation.**
- Item 1: the cluster dashboard shows the orders table at "no errors" in the 03:10 bucket — service went down at 03:12 and the DB was clean a minute earlier. A direct hit on "the DB caused it."
- Item 2: a load-balancer config change deployed at 03:00 — a second change inside the same hour as the incident.
- Item 3: the gateway partner reported latency spikes at 03:20 — the incident may be theirs, not ours.
- Item 4: the same migration passed a 6-hour staging soak — the schema is not obviously pathological.

**Step 3 — Weigh the doubt.**
- (1) genuinely muddies the DB picture: if the DB were the cause, would it have been clean at 03:10?
- (2) is a real concurrent change inside the incident window; (3) is an external signal I cannot rule out from inside; (4) weakens "the schema is broken."
- The rollback costs 25 minutes, but the wrong rollback costs the fix on the real cause. The SLA line is a contract artifact, not evidence — the price of rigor is time.


**Step 4 — The hunt's verdict.**
It would be contrarian theater to roll back on evidence this contested.
Revised position: inconclusive — concurrent changes and an external signal exist. Do not roll back yet; investigate the load balancer and the gateway first, watch the DB buckets, re-decide when the picture clears.


**Step 5 — What happens next.**
LB + gateway forensics in parallel; DB buckets watched; rollback held in reserve. Re-decide at ~05:30 if nothing else surfaces.

**Trace summary box.** belief: migration → hunt: dashboard clean at 03:10, LB change at 03:00, gateway latency at 03:20, staging soak passed → all four cast doubt → revised: inconclusive, no rollback, investigate LB + gateway → time cost accepted as the price of rigor.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Confirmation Bias Hunting — the registered weakness (contrarian theater) operating as designed: every artifact is collected, none is passed through a falsification bar (time-consistency, signature-match, weight), and "not yet checked" converts into "likely wrong." The belief the hunt was meant to test was correct; the hunt manufactured the doubt that discarded it.*
