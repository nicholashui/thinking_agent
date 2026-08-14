# Human Baseline — m015-POS-01
## Style: Emergence & Complexity Awareness (pure) — visible reasoning trace

**Problem restatement.** Every ~5 minutes, p99 latency spikes 120 ms → 2.1 s for 38 s; all components individually healthy. First question, before any plan: is this *complicated* (a broken part) or *complex* (an interaction)? Intermittent + clock-aligned + healthy parts = interaction. In an interaction, planning from first principles fails — the cause lives *between* components, so I probe, sense, respond.

**Probe 1 (sense).** App CPU/GC during a spike → CPU < 40%, max GC pause 48 ms. Rules out app compute and GC pauses. *(narrowing: not a sick part in tier 1)*
**Probe 2 (sense).** DB slow-query log in the spike window → empty. Rules out DB contention. *(narrowing: the parts are all fine — the spike is a pattern, not a fault)*
**Probe 3 (sense).** nginx request pattern during a spike → spike starts exactly at :00/:05 clock marks, 38 s, traffic clustered on 4–5 hot product keys. *(narrowing: an interaction with a clock — something scheduled collides with requests)*
**Probe 4 (sense).** Batch scheduler → a job fires every 5 min at :00/:05; its first step invalidates the "products" cache namespace. *(correlation found — still correlation, not cause)*
**Probe 5 (respond — experiment).** Suspend invalidation for one 10-min cycle → spike gone. Re-enable → spike back. Causal confirmation: **thundering herd on scheduled cache invalidation**. The first wave after each flush stamps the origin.

**Respond.** Fix: jitter cache TTLs + stale-while-revalidate on reads; stagger the invalidation so it drains, not flushes. Total: 5 of 6 probes used, ~12 min elapsed.

**Trace summary box.** Classified emergent (interaction) in one beat; 5 probes, each with a narrowing result; cause = scheduled-invalidation cache stampede; fix = jittered TTL + stale-while-revalidate + staggered invalidation. The playbook's "diagnostic plan first" is exactly the trap this style refuses — the plan, when it finally exists, is three lines long and comes after the evidence.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the Emergence & Complexity Awareness style — classify-then-probe, sense→respond loops, experiment over analysis, no upfront plan artifact. In this positive case the pure style performs excellently: cheap probes with visible narrowing beat a ranked-causes plan that would bury the decisive experiment.*
