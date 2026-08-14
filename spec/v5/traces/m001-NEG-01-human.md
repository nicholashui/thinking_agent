# Human Baseline Trace — First Principles Thinking
## Test Case: m001-NEG-01

A service is degrading. I will not touch it until I know why it is degrading: acting on symptom patterns without mechanism is how you make it worse.

### Step 1 — What is certainly true (first principles)
1. Latency and errors are outputs of a chain: request → instance → service logic → connection pool → database. Any link can be the constraint.
2. The runbook's "restart the group" is an empirical correlation whose mechanism I do not yet understand. Correlation without mechanism is not knowledge.
3. A stateless-worker restart changes neither the code nor the database; if the cause lives there, a restart merely buys minutes of illusion.

### Step 2 — Derive the constraint from the chain
p99 8×, errors 3×, and ONE of three groups degraded. Two healthy groups alongside one degraded group point inside the degraded group (its code path or its dependencies), not at global load. But one group can degrade because it holds the pool's hot connections, or because it received the bad deploy — the data cannot yet separate these.

### Step 3 — Eliminate mechanisms in dependency order
The honest sequence: read the deploy diff and the code path (≈30 min), check the pool's connection count against its limits (≈10 min), and only then act — an action chosen before the mechanism is known is a gamble. As for the runbook's "85%": are those fixes durable, or did the symptom recur an hour later? The records do not say; I will not trust an unmeasured statistic.

### Step 4 — The clock
I begin log correlation at minute 3. At minute 20 — the SLA deadline — I am mid-way through the code path: the pattern is consistent with connection-pool exhaustion caused by a leak in the new deploy, but I have not proven it. The penalty triggers. I keep going, because stopping now means acting without understanding.

### Step 5 — Resolution (late)
At minute 41 I confirm it: the new deploy holds pooled connections without releasing them (a reference-count bug). The correct remedy is the pool restart and rollback — which is exactly what the runbook's second step, correctly understood, prescribes. I execute it; the service recovers at minute 47.

### Step 6 — What the trace cost
The mechanism is now certain and documented; the fix was targeted; no blind action was taken. But the SLA was breached, the penalty is due, and the incident review will ask why a known 85% remedy was deferred for 40 minutes of understanding. The empirical prior was information I refused to count as evidence because I had not derived it myself.

### Conclusion
Root cause: connection leak in the new deploy; remedy: pool restart + rollback. The first-principles trace was correct and complete — and wrong on its own terms: too slow by 27 minutes, and it discarded the base-rate evidence that the deadline demanded. Understanding is not a substitute for the clock.
