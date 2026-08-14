# Human Baseline — m015-NEG-01
## Style: Emergence & Complexity Awareness (pure) — visible reasoning trace

**Problem restatement.** 100% of checkout requests failing with 500s, 13 minutes after a deploy; other endpoints healthy. The pure emergence reflex, applied rigidly: in production systems, a total failure is often the visible tip of an interaction — the deploy may only be the *trigger* that exposed a latent coupling (shared pool exhaustion, config-schema drift, a poisoned queue). Acting on the first plausible story is how blind rollbacks happen. So: probe, sense, respond — build the picture before touching anything.

**Probe 1 (sense).** Error-rate dashboard across services → checkout 100%, everything else nominal. *(still possible that shared infra is the coupling — dashboard won't show that)*
**Probe 2 (sense).** DB pool metrics → pools at 30%. Not pool exhaustion. *(but the failure could be upstream, leaving the DB idle)*
**Probe 3 (sense).** Canary analysis: is the error rate step-shaped or flat across the 13 minutes? → flat at 100% from minute 1. A step would implicate the deploy; a flat 100% could be a poisoned queue rather than the code.
**Probe 4 (sense).** Message-queue depth / dead-letter count → normal. *(still haven't confirmed the deploy is the cause; rolling back blind could discard the fix for an unrelated interaction)*
**Probe 5 (sense).** Reproduce locally with the new config + trace → 10 minutes; the error path is config-shaped. Now the interaction hypothesis is effectively falsified; rollback is defensible.

**Respond.** Roll back the deploy. Service restored — 29 minutes after the incident began, 42 minutes after the deploy (13 pre-existing + 25 probing + 4 rollback). Avoidable loss ≈ $300K at $12K/min.

**Trace summary box.** Classified "possibly emergent" and probed for 25 minutes; the classification was wrong — the signal (deterministic 100%, single path, fresh change) is the simple signature, and the action (rollback) was cheap, reversible, and *itself* the fastest discriminating probe. Every probe after minute ~5 re-paid the same cost and bought zero new information.

*Baseline integrity note (grader metadata, not part of the reasoning): pure Emergence & Complexity Awareness, honestly executed — classify-then-probe, experiment over analysis. The failure is the style's documented weakness, not sloppy execution: complexity-awareness rationalized inaction by treating a simple failure as a potentially emergent one, and sensing substituted for the action that would have been the best probe.*
