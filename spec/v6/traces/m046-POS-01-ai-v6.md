# v6 Routed AI Trace — m046-POS-01 (blinded)
## FleetSense fleet-tracking architecture — recommendation memo (closed-scope, fully specified)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software,strategy,supply | g:diagnose,estimate,guarantee | c: (none)
- Router top3: m046 m028 m044; confident=yes → SINGLE ROUTE: top-1 as first-class pass, top-3 as context. Gates (R4, guarantee-goal): m003 inversion MANDATORY. Flags: closed-scope fast path ON (P8, fully specified); tempo mode OFF (no deadline).
### WHAT — frame + structure-first scan
- Settle between the team's proposed pattern and a constraint-derived design, argued from the system's actual demands. Success: 1 s dispatch bound at peak, zero assignment loss, least build/operate cost.
### WHY — P1 input-provenance audit
- The proposal is INTERESTED-PARTY input: the team staffs and benefits from the 3–4 month project; "industry-standard" is a framing, not evidence. MEASURED anchors: 1,600→12,800 pings/s, 20→200 assignments/s, ≈20k+ tps Postgres, <50 ms cache reads, 10–100 ms Kafka tail. Every number is arithmetic, not assertion.
### HOW — first-class pass (architecture from fundamentals; units carried; calibration anchor)
- P1 (data): classify each flow by loss-consequence BEFORE pattern vocabulary — lost ping = 5 s stale, vehicle re-pings, no money consequence → EPHEMERAL sensor reading; lost/duplicated assignment = wrong dispatch, contract breach → DURABLE system of record.
- P2 (scale): 8,000/5 s = 1,600/s steady; 1/s burst = 12,800/s peak vs ≈20k+ tps single Postgres = 1.5–2× headroom → scale NON-BINDING.
- P3 (latency): 1 s freshness is the binding demand; write-through cache <50 ms ≪ 1 s; every async hop pays 10–100 ms tail + consumer-lag risk on replaceable data → no queue in the ingest path.
- P4 (change rate): frozen hardware contract vs weekly rule changes → two modules by change rate, not service taxonomy; projection coupling would invalidate rules against the whole stream.
- Ecosystem check: the pattern is a correct response to genuinely high-throughput durable-event domains — its durability/ordering/replay virtues target the WRONG data class here; the only durable flow runs at 20/s and needs none of them.
- Context (m028/m044): frame-break "streaming platform" → it is ingest+dispatch; stakeholders (dispatcher freshness, weekly rule deploys, ops burden) all side with the derived design. No divergence.
### GATES — m003 inversion (R4)
- ≥6 ranked failure categories (L×I): (1) p95 > 1 s at peak high/critical; (2) lost assignment mod/critical; (3) duplicated assignment on retry low/critical; (4) peak > 2× estimate low/high; (5) cache divergence low/mod (write-through, single-writer); (6) rule module coupling into pipeline mod/mod; (7) batch-throughput overestimate low/mod.
- Un-mitigable residual: upstream hardware-protocol change — owned by the hardware contract. Never/always: never insert an async hop into a latency-bound path for replaceable data; always classify by loss-consequence before choosing storage; always load-test at peak before cutover.
### DO — P8 fast path + P3 branch pricing
- Memo: monolith (≤2 services) — Postgres (batched upserts for locations; transactions on assignment state) + in-memory write-through cache; rule module isolated; ≈6 weeks/2 engineers vs 3–4 months/6. Failure branch priced: p95 > 1 s for 2 weeks → revisit cache design, never the ingest path; assignment loss ≠ 0 → single-writer path already transactional.
### REVIEW — insight pass
- I1: location is a sensor reading, not an event — the system of record is assignment state, not the event log. I2: the pattern's virtues are virtues for the wrong data class; the durable flow doesn't need a queue. (v5 gap — pattern-as-working-hypothesis — closed: nothing left for REVIEW to retrofit.)
### DECISION PACKET
- Conclusion: adopt the constraint-derived design; reject the proposed pattern with the loss-consequence + latency + change-rate reasons; effort contrast and metric attached. Status: SOLVED.
- Assumptions: 12,800/s is the real peak (2× margin); Postgres sustains ≈20k+ tps batched; 1 s freshness truly required.
- Evidence: 1,600–12,800/s vs ≈20k tps; <50 ms vs 10–100 ms + lag; ephemeral/durable taxonomy; change-rate split; 6 wks/2 vs 3–4 mo/6.
- Alternatives: proposed pattern (rejected: over-provisioned, latency risk, wrong data class) · Kafka-for-assignments-only (rejected: 20/s needs no queue) · serverless ingest (rejected: per-record cost/latency) · derived design (selected).
- Uncertainty: true peak multiplier (2× margin, load test); Postgres batching throughput (verifiable). Risks: team preference for the pattern → cost table + SLA math in memo; rule-module growth → revisit boundary at 5+ weekly changes.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical verdict and design |
| Logical Validity | 5 | 5 | Tie | same rate math, latency analysis, taxonomy |
| Coherence & Structure | 4 | 5 | AI | routed pass + gate + packet vs linear derivation |
| Depth of Reasoning | 5 | 5 | Tie | derivation now first-pass; gate adds ranked failure completeness |
| Efficiency | 5 | 5 | Tie | both land the design in one pass; the WHY falsification stage is gone |
| Handling of Uncertainty | 3 | 4.5 | AI | AI names margins, load test, sensitivity; human asserts |
| Insight / Non-obviousness | 5 | 5 | Tie | "sensor reading, not event" is first move on both sides; AI adds ecosystem-check framing |
| Overall Quality | 4.6 | 4.8 | AI | routed pass closed v5's depth/efficiency/insight gaps |

Winner: AI (narrow). Why: the routed constraint-derivation pass put the ephemeral/durable split, latency binding and change-rate boundaries at first sight — the v5 run's WHY-stage falsification of the pattern frame is now the opening move — and the inversion gate added ranked failure completeness and a stated residual. Verdict and math identical to the baseline; the routed run just lands them without the spent stage.
