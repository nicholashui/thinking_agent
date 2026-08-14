# Human Baseline — m042-NEG-01
## Style: Abstraction Laddering (pure) — visible reasoning trace

**Climb — what is this an instance of?**
- The thing on the screen: 60% of payment requests failing at 02:14.
- Rung 1: this is an instance of *capacity failure* — the pool is exhausted; we are out of connections.
- Rung 2: capacity failure is an instance of *provisioning policy* — pool sizing is never right-sized after traffic shifts; nobody reviews it.
- Rung 3: provisioning policy is an instance of *change governance* — the deploy that touched the pool config three hours ago is the token instance: configuration changed without a review gate.
- Rung 4 (goal rung): this is an instance of *operational learning* — fixing the pool fixes tonight; fixing the class of config regressions fixes every night. The deliverable is the class.

**The Monday descent (the style's own clock).**
- Monday 09:00: schedule a capacity right-sizing review; write a pool-sizing runbook.
- Tuesday: standing change-review gate for config deploys; diff check on pool values at deploy time.
- Wednesday: autoscaling proposal for connection pools under traffic spikes.
- And now? The config says `max_connections=5`; the previous golden value was 50. Increasing the pool would be the token fix — but 50 is incidental: the instance is policy, and any number chosen tonight is re-introduced drift until the governance rung is fixed. I'll fold the value into the Monday plan.

**Return up — the ledger.** The deepest fix is class-level. The concrete number can be changed later, with the review in place.

**Trace summary box.** 60% errors → capacity → provisioning policy → change governance → operational learning (goal rung) → Monday: right-sizing review, change gate, autoscaling. Token descent: pool 5 → 50, deferred pending the governance fix.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Abstraction Laddering. The signature moves — climbing from the token to the class and scheduling the descent for "Monday" — are the style's strength on planning problems and its failure here: the incident's time horizon is minutes, not Monday, and the token (`max_connections=5`) IS the deliverable.*
