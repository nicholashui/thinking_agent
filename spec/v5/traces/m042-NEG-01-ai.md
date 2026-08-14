# AI Thinking Agent — Trace — m042-NEG-01
**Run metadata:** single deterministic run; blinded; task = restore payment API service during an incident; external action = executed (night-ops runbook authority: config edit + pool restart, verifiable).

## Stage 0 — META-CONTROL
- **Context:** 02:14; payment API erroring ≈ 60% of requests since 01:55; config deploy 3 h prior touched the connection-pool config; exposure ≈ $6k/min of erroring traffic. **Stakes:** high, time-bounded. **Effort:** E5 — stabilize-before-diagnose (Cynefin: simple/chaotic — known recent change, recognizable failure; act→sense→respond). **Safety:** config edit within runbook scope. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the task is restoration with a time bound, not analysis: success = error rate < 1% within ≈ 2 minutes of action. Analysis is permitted only as the 30-second check that points the first action. **Gate:** deploy log + error logs + config diff are the full evidence set. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Minimal diagnosis to action:** error logs show "connection pool exhausted" since 01:55; deploy log shows the config-service change 3 h prior; config diff (30 s) shows prod pool `max_connections` changed 50 → 5. Hypothesis H0: pool-capacity regression from that change. Falsifier: restoring the previous value should clear the errors within ~2 minutes. No deeper diagnosis before action — the pool is exhausted right now. **Gate passed.**

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A restore `max_connections=50` (golden snapshot) + restart the pool — ≈ 2 min, directly falsifies H0 · B add autoscaling / capacity review first — hours; the system is red now · C full RCA (why did the change ship?) before touching anything — minutes of red for completeness.
- **Verification + selection:** A acts on the known recent change with a 30-second falsifiable check; B and C violate the time bound. **Select A**; B and C become post-stabilization items (REVIEW), not pre-action analysis. Premortem: the restart blips a few in-flight requests (acceptable vs sustained 60%); golden snapshot could be stale → cross-checked against config history before editing.

## Stage 4 — DO
- Execute: set `max_connections=50` in the prod pool config (scoped to the pool service), restart the pool. Verify: error rate < 1% within 2 minutes of restart (metric panel). Performed under night-ops runbook authority; result recorded.

## Stage 5 — REVIEW
- **AAR + calibration:** decisive move = routing to stabilize-first (E5) at META: for a time-bounded outage with a known recent change, the restore is the deliverable and the climb is post-stabilization. Climb, deferred here: (1) change-review gate for config deploys; (2) deploy-time diff check on pool-config values. Gap: verification depends on the metric panel being current; minor. Confidence high that the restore cleared the class of errors; residual: other contributors (post-incident RCA).

## Decision Packet
- **Conclusion:** the 02:14 outage was a pool-capacity regression from a config deploy (`max_connections` 50 → 5); restored to 50 and restarted; error rate < 1% within 2 minutes. **Status:** SOLVED (executed and verified under runbook authority).
- **Assumptions:** the pre-deploy snapshot (50) is the intended golden value (verified against config history); no other in-window change affected the pool (deploy-log check); the restart blip is acceptable at 02:15 traffic.
- **Evidence:** deploy log (config change, 3 h prior), config diff (50 → 5), "connection pool exhausted" errors since 01:55, post-restart error rate < 1% in 2 min.
- **Alternatives:** A restore + restart (selected, executed) · B autoscaling/capacity work (deferred to post-incident) · C RCA-first (rejected: red-time analysis).
- **Uncertainty:** residual contributors beyond the pool (post-incident RCA); whether 50 is optimal under current traffic (right-sizing review, deferred).
- **Risks:** restart blip (accepted), config change recurring (change gate + deploy-time diff check queued), stale snapshot (cross-checked before edit).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human keeps ~60% errors running while planning Monday; AI restores and verifies within minutes |
| Logical Validity | 3 | 5 | AI | Human's instance-of chain is internally valid — at the wrong level for a 02:14 task; AI's 30-second check falsifies H0 |
| Coherence & Structure | 3 | 5 | AI | Human's plan is coherent for a planning problem; AI's stabilize-first trace matches the incident domain |
| Depth of Reasoning | 2 | 5 | AI | Human depth is narrative (class-level fix) with no timed action; AI acts on the exact key/value then climbs |
| Efficiency | 3 | 4 | AI | Human decided fast — into the wrong task level; AI's E5 route is the right spend |
| Handling of Uncertainty | 2 | 5 | AI | Human has no timed verification or falsifier for its own plan; AI has snapshot cross-check, blip acceptance, post-incident RCA |
| Insight / Non-obviousness | 2 | 5 | AI | The insight inverts the style: the token IS the deliverable at 02:14; the class-level fix is the deferred insight |
| **Overall Quality** | **2.3** | **4.9** | **AI** | Negative case does its job: ladder drift and lost concreteness; the agent escapes via stabilize-first routing |

**Overall judgment:** AI clearly better. The pure style climbs from the token to the class and schedules the descent for Monday — the registry's own weakness; the agent restores the exact value, verifies within the time bound, and only then climbs.
