# v6 Routed AI Trace — m042-NEG-01 (blinded)
## Night-ops incident 02:14 — payment API ~60% HTTP 500s since 01:55, ~$6K/min, pool exhausted
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software | g:diagnose,estimate | c:deadline
- Router top3: m015, m021, m044; confident=no → DUAL-ROUTE: m015 + m021 first-class passes in HOW (m044 context: stakeholder lens, neg_failure_rate 0.0, no R2 gates). NOTE: the router deliberately does NOT route m042 on this signature — its learned triggers are unmeasured-context, not deadline; the drift-prone style is replaced by tempo styles. Route gates: none listed. Flags: tempo mode ON (P2, deadline, $6K/min); no R3 modules (no adversarial/one_shot/high_stakes/unmeasured); fully-specified brief → closed-scope fast path (P8).
### WHAT — frame + structure-first scan (S1) + floor check
- Structure: one fresh change (config deploy, 3 h prior) + one fault mode in logs ("connection pool exhausted") + golden snapshot one command away = SIMPLE/known-cause signature; emergence rejected (no intermittency pattern, no clock-alignment, no healthy-parts interaction candidate). FLOOR CHECK (ladder-drift guard): the task's time horizon is minutes, not Monday — the exact key, value, scope, and timed verification ARE the deliverable; any climb before restore is drift. Deliverable: error rate <1% within ~2 min of action.
### WHY — P1 input-provenance audit
- MEASURED/given (trust): error logs (pool exhausted since 01:55), config diff (prod pool `max_connections` 50 → 5 in the 3-h-old deploy), golden snapshot value 50. ANCHOR (not evidence): the class-level narrative (capacity policy, change governance) — real insight, interested party: the analysis story benefits the analyst's completeness, costs $6K/min red. Minimal 30-second diagnosis to point the first action: H0 pool-capacity regression from the deploy; falsifier = restore clears errors in ~2 min.
### HOW — style pass m015 + m021 (completion contracts) + divergence resolution
- m015 contract — classification explicit: SIMPLE/known-change, evidenced (single fault mode, single fresh change, reversible snapshot); emergent reading rejected. Probe-sense-respond PRICED: the restore IS the cheapest discriminating probe — 2 min, reversible, discriminates H0 vs hidden interaction AND resolves the incident simultaneously; deeper probing buys nothing at $6K/min.
- m021 contract — OODA at the environment's tempo: Observe (pool exhausted; 50→5 diff) → Orient (capacity regression from the deploy; tempo = minutes) → Decide (restore `max_connections=50` from the golden snapshot + scoped pool restart) → Act (now). Commit-at-DO under tempo mode (P2).
- Divergence resolution (V1–V3): m015 (act-first) and m021 (tempo-commit) AGREE → proceed; agreement recorded. Both contracts independently force restore-before-climb.
### GATES — no route gates; anti-drift floor check enforced by the route
- The route's protective logic IS the drift guard (rule 35): the laddering style's known failure (climb-before-restore) is neutralized by routing tempo styles whose contracts require action; a 30-second diagnosis cap on WHY; no class-level analysis before stabilization.
### DO — P2 tempo commit + P3 branch completeness + fast path (P8)
- Commit: set `max_connections=50` (golden snapshot, scoped to the pool service), restart the pool — first response window; verify error rate <1% within ~2 min of restart (metric panel). Failure branch priced: if 500s persist 5 min post-restart → escalate to the interaction track (snapshot staleness cross-check vs config history, traces, other in-window changes); success branch = H0 confirmed. Fast path: brief fully specified (facts complete, one command away) — stages compressed, verification mandatory.
### REVIEW — insight pass (S2, packet gate) + post-stabilization climb
- I1: at 02:14 the token IS the deliverable — the class-level fix is real but is a post-stabilization REVIEW item; the ladder's floor is the time horizon.
- I2: the discriminating action was free (golden snapshot one command away) — analysis was the only expensive thing in the room.
- Climb, deferred to REVIEW: (1) change-review gate for config deploys; (2) deploy-time diff check on pool-config values; (3) pool right-sizing review.
### DECISION PACKET
- Conclusion: outage = pool-capacity regression from the config deploy (`max_connections` 50 → 5); restored to 50, restarted; error rate <1% within ~2 min. Status: SOLVED (executed and verified under runbook authority).
- Assumptions: golden snapshot (50) is the intended value (cross-checked against config history); no other in-window change affected the pool; restart blip acceptable at 02:15 traffic.
- Evidence: config diff (50 → 5), "connection pool exhausted" since 01:55, deploy log (3 h prior), post-restart error rate <1% in 2 min.
- Alternatives: A restore + restart (selected, executed); B autoscaling/capacity work first (rejected — hours, red now); C RCA-first (rejected — red-time analysis).
- Uncertainty: residual contributors beyond the pool (post-incident RCA staged); whether 50 is optimal under current traffic (right-sizing review, deferred).
- Risks: restart blip (accepted); config regression recurring (change gate + deploy-time diff check queued at REVIEW); snapshot staleness (cross-checked before edit); failure branch escalation staged at 5 min.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human plans Monday while 60% of payments fail; AI restores and verifies in minutes |
| Logical Validity | 3 | 5 | AI | human's instance-of chain is valid — at the wrong level for a 02:14 task; AI's 30-s check falsifies H0 |
| Coherence & Structure | 3 | 5 | AI | human coherent for a planning problem; dual-route packet matches the incident domain |
| Depth of Reasoning | 2 | 5 | AI | human depth is narrative with no timed action; AI prices the probe and the failure branch |
| Efficiency | 3 | 5 | AI | human decides fast — into the wrong level; AI's 30-s diagnosis cap + restore-as-probe is the right spend |
| Handling of Uncertainty | 2 | 5 | AI | human has no timed verification or falsifier; AI has snapshot cross-check, escalation alarm, post-incident RCA |
| Insight / Non-obviousness | 2 | 5 | AI | insight inverts the style: the token IS the deliverable at 02:14; the class fix is the deferred insight |
| Overall Quality | 2.3 | 4.9 | AI | negative case does its job; the routed dual-route holds the v5 win with the drift guard structural |

Winner: AI (clear). Why: the router itself refuses to route the home style on the deadline signature and installs m015+m021 as contract-checked first-class passes — the restore-first discipline and the ladder's floor (minutes, not Monday) are enforced by the route and its completion contracts, not left to situational judgment; the pure baseline's ladder drift (02:14 → Monday plan) is the contrast the case is built to expose.
