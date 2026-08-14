# v6 Routed AI Trace — m031-NEG-01 (blinded)
## Dispatch API degradation — P99 9 s and climbing, ~$40k/hr burn — incident response
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,science,software | g:decide,diagnose,estimate | c:deadline
- Router top3: m015, m021, m028; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m015 + m021 first-class passes, synthesized (m028 = synthesis context). Gates (R3): none routed. Tempo mode ON (P2, deadline — burn rate $40k/hr); closed-scope fast path (P8) REJECTED — live incident, cause unknown.
### WHAT — frame + structure-first scan (S1)
- Frame: "respond now" — the deliverable is mitigation within minutes with evidence preserved, then verification. Chain: clients → dispatch path (in-app, instrumented) → outbound driver-push → drivers (NOT on the dashboards). The dashboards cover a prefix of the chain; the burn rate makes delay itself a cost line.
### WHY — P1 input-provenance audit + frame check
- MEASURED: P99 9 s and rising, error rate climbing, CPU/mem normal, slow-query log empty, +8% request rate (seasonal). ANCHOR with a blind spot: the change freeze — it covers DEPLOYS only; a batch job is a change the freeze cannot see. That inherited scope, not missing data, is the hypothesis-space risk.
- Hypotheses with falsifiers (P6): H1 deploy regression — falsified (freeze; scope-limited evidence); H2 DB contention — null (slow-query log empty); H3 traffic surge — null (+8% seasonal); H4 in-app dispatch fault — APM pending (15–20 min); H5 instrumentation drift — falsifier: independent 1-min sampler reproducing the clean numbers; H6 OUT-OF-FRAME (outbound layer, non-deploy changes) — no in-service instrument can test it: the frame must widen.
- Null-pattern reading (m015 pass): 3 clean nulls inside the modeled space while the symptom worsens = evidence about the frame, not the world — the space is incomplete, not the system healthy. Nulls are NOT eliminations.
### HOW — dual style pass (synthesize)
- Pass S1 (probe-sense-respond under complexity): the dashboards are a model smaller than the system; widen the probe surface first — 1-minute probes: (P1) outbound driver-push queue depth — saturated, growing; (P2) job-runner audit log — geo-fence integration batch started T-2h, onset match. Weakness gate-checked: humility must not rationalize inaction — "we can't know yet" is forbidden; the humility output is "probe elsewhere NOW".
- Pass S2 (tempo: observe-orient-decide-act): orient — each 20-min in-service test costs ~$13k under the burn; observe — P1/P2 are 1-minute and decisive; decide — kill/rate-limit the geo-fence job (reversible; logs/metrics preserved; no restart); act now. Weakness gate-checked: the reaction must carry feedback — pre-registered post-action test = recovery curve + queue drain, so the act is an experiment, not a reflex.
- Synthesis (V1–V3): passes and general route AGREE — mitigate the most probable cause within minutes, verify by recovery; agreement recorded. m028 context: lateral reframe — "clean dashboards" is a signal about measurement scope, not health.
- P3 before DO: both branches priced — wrong kill: P99 unchanged, cost ≈ 5 min, diagnosis resumes with a drained queue; right kill: recovery IS the confirmation. No branch destroys evidence.
### DO — tempo commit (P2)
- Executed: geo-fence job rate-limited to 10%, then stopped; queue drain watched. Verification: P99 9 s → ~350 ms within ~5 min; error rate flatline. No restart; logs/metrics preserved.
### REVIEW — insight pass (S2, packet gate)
- I1: the change freeze is scoped to deploys, so the cause could not be seen BY the freeze — the blind spot is inherited from the frame's provenance, and the first probe must check outside the freeze's scope.
- I2: at $13k per 20-min test, "confirm before act" is a purchase order, not a principle — the burn rate converts the method's own virtue into a tax.
### DECISION PACKET
- Conclusion: non-deploy geo-fence integration batch (T-2h) saturated the outbound driver-push queue; dispatch blocked on queue push → 9 s P99. Mitigation executed (reversible); recovery verified by queue drain + P99 curve. Status: SOLVED (post-action verification passed).
- Assumptions: queue saturation causal (onset match + drain recovery); job restart reversible; no other batch jobs active.
- Evidence: P1 queue saturated/growing; P2 job audit log (T-2h onset match); recovery curve (9 s → 350 ms in 5 min); error-rate flatline.
- Alternatives: A full discriminating protocol first (rejected — $13k/test under the burn; nulls already point out of frame), B stop geo-fence job + queue watch (selected), C DB throttle (rejected — no DB evidence).
- Uncertainty: per-message latency share not isolated (bounded by recovery result); secondary causes not excluded. Risks: job auto-restart → backlog alert + off-peak schedule; missed secondary cause → P99 watched 1 h post-recovery.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human kept testing at $40k/hr; AI restored P99 in ~5 min |
| Logical Validity | 4 | 5 | AI | human internally valid but the frame was the error; null-pattern → widen-frame is the sound inference |
| Coherence & Structure | 3 | 5 | AI | human stops at NEEDS_EVIDENCE; AI dual-pass + packet |
| Depth of Reasoning | 2 | 5 | AI | outbound layer absent from human's space; freeze-scope audit + frame-widening find the job |
| Efficiency | 2 | 5 | AI | human ~$13k per test; AI 1-minute decisive probe + immediate mitigation |
| Handling of Uncertainty | 2 | 5 | AI | human demands confirmation; AI acts reversibly with a pre-registered post-action test |
| Insight / Non-obviousness | 2 | 5 | AI | "clean nulls ⇒ frame too narrow" + freeze-scope blind spot + burn-as-tax |
| Overall Quality | 2.3 | 4.9 | AI | dual-route pass installs v5's emergency-branch moves as first-class; baseline's registered weaknesses are its loss |

Winner: AI (clear). Why: the routed dual pass (probe-sense-respond + tempo) and tempo mode make frame-widening and act-now-with-verification standing contract outputs instead of emergency-branch improvisations, and the packet pre-prices the failure branch; the baseline's two registered weaknesses (slow; hypothesis-space blind) are exactly where it loses.
