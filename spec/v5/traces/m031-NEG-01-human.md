# Human Baseline — m031-NEG-01
## Style: Scientific Method (pure: Hypothesis → Experiment → Update) — visible reasoning trace

**Step 1 — Frame the phenomenon.** P99 dispatch latency 300 ms → 9 s over 2 h, error rate climbing, no deploys (freeze), dashboards clean. Define the measurement: P99 and error rate per minute, correlated with DB, CPU, request-rate — every variable observable today.
The nulls are only as good as the instruments, so the instruments themselves go on the hypothesis list below.

**Step 2 — Hypothesis set, each with a falsifier.**
- H1 deploy regression: falsifier — change freeze (no deploys in 48 h). Eliminated.
- H2 DB contention: falsifier — slow-query log empty, CPU/memory normal. Null.
- H3 traffic surge: falsifier — request rate +8%, seasonal expectation. Null.
- H4 dispatch-path code fault: stands. Falsifier: an APM deep profile showing normal in-app time.
- H5 instrumentation drift (dashboard lies): stands. Falsifier: an independent sampler reproducing the same clean numbers.

**Step 3 — The discriminating experiment.** Clean numbers matter: the APM deep profile of the dispatch path plus canary sampling, and a second sampler for H5.
Each run needs 15–20 minutes for statistical reliability. We must not act on hypothesis alone — an unconfirmed fix can make it worse, and it would contaminate the measurement.
The commander's deadline is a business constraint, not an epistemic one; knowledge is worth its cost.

**Step 4 — Run the experiments (min 20).** While they run: nulls are informative. H2, H3 eliminated. The H4 profile shows in-app time normal — another null. The H5 sampler reproduces the clean numbers — instrumentation exonerated.
Four clean nulls: the data say the service itself is healthy.

**Step 5 — Refine the hypothesis space.** If the service is healthy, the fault is in how we measure, or the effect is emergent. The disciplined move is more controlled observation, not improvisation.
Instrument the dispatch path end-to-end (every await, every queue, every call) and hold the run until the sample is clean. The burn rate is a cost of knowledge; acting early forfeits the experiment.
Whatever the cause, it will show itself once the measurement is complete.

**Step 6 — Interim status.** Cause not yet identified. Status: NEEDS_EVIDENCE. Request 20 more minutes for the instrumented run. Recommend no mitigation yet.
Decision point: the commander wants action; the method wants one more controlled observation. The method wins — acting on an unconfirmed hypothesis is how outages get misdiagnosed.

**Trace summary box.** Change-freeze falsifies deploys → DB and traffic nulls → APM null → instrumentation null → clean dashboards ⇒ "keep observing"; the outbound queue and the 2-hour-old batch job never enter the hypothesis space; the burn continues through every test.

*Baseline integrity note (grader metadata, not part of the reasoning): pure Scientific Method applied faithfully — falsifiers, controlled observation, refusal to act before confirmation. That is the point of the negative case: the method's rigor inverts into tempo blindness ($13k per 20-min test under a $40k/hr burn) and hypothesis-space blindness (a dashboard-scoped space cannot see the outbound layer; clean nulls are misread as eliminations instead of frame failure).*
