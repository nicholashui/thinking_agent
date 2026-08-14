# v6 Routed AI Trace — m013-POS-01 (blinded)
## Checkout API 2% pool-timeout incident — incident analysis, 60 min
### META (routing — blind router output)
- Signature: d:engineering,medical,product,software | g:decide,diagnose,guarantee,predict | c:deadline
- Router top3: m013, m091, m001; confident=no → DUAL-ROUTE: m013 (causal drill) + m091 (practiced-routine re-drill) first-class passes, synthesized; m001 = first-principles context. Mandatory gate: m003 inversion (R4 guarantee-goal prepend; routes.csv). Flags: tempo mode ON (P2, deadline).
### WHAT — frame + structure-first scan (S1)
- Frame: explain the 2% failure at mechanism level; prescribe a recurrence-proof fix verified on a fresh build. Structure: causal chain as fault tree (symptom → links → root), not a list.
### WHY — P1 input-provenance audit
- All 7 evidence items MEASURED (observability stack, repo, schema_migrations — first-party; E6 is an empirical reproduction, strongest form). No interested-party anchor; no party benefits from a wrong root. Evidence accepted, still cross-checked per link.
### HOW — style passes (dual-route, completion contracts)
- Pass S1 (m013): 5-whys, every link verified by evidence, fault-tree structure, prevention-vs-detection gap separated. Why1 timeouts ← connections held ~4.2 s by the slow join on ~2% of peak traffic (E2: seq scan, 4.2 s avg — 2% × 4.2 s holds saturate any pool; E1's unchanged rate falsifies the pool patch on mechanism: pool size does not shorten hold time). Why2 hold ← seq scan ← `order_items.order_id` unindexed (E3; `orders.customer_id` indexed shows selective access is the norm). Why3 missing index ← migration 0041 absent from `schema_migrations` (E4). Why4 0041 absent ← same-second timestamp collision with 0040 + runner's silent per-second dedup (E5 — first tooling-level link). Why5 collision possible ← versioning has no uniqueness guarantee, no lock, no fail-loud (E5+E7) → ROOT: the pipeline silently drops colliding migrations; every fresh build ships without 0041. Fault tree: pool patch and manual index are detection/symptom-side; the generative mechanism is the versioning property — prevention requires removing the mechanism, not the symptom.
- Pass S2 (m091): chunked re-drill — the naive stopping chunk ("0041 not applied → apply it + CI check") fails its own re-drill: the chunk is a fact, not a mechanism; re-drill it → collision/dedup (E5). A recurrence-proof fix must make the absence un-reproducible.
- Divergence resolution (V1–V3): passes DISAGREE — S1: fix the versioning pipeline (uniqueness + fail-loud + CI sync); S2 routine: apply 0041 + CI-sync check only. P3 branch-completeness + calibration on both: recurrence test (fresh build, E6) — S2's branch re-loses the index at every rebuild (runner still drops 0041); S1's branch removes the mechanism → S1 selected; disagreement recorded in packet risks.
### GATES — m003 inversion (R4 / routes.csv)
- ≥6 failure categories ranked L×I: (1) fresh build re-loses index — certain × catastrophic (E6) if versioning unguaranteed; (2) same-second collision recurs — high × high without uniqueness lock; (3) manual-index drift across envs — high × medium (surface fix); (4) CI green while runner silently skips — medium × high (closes only if CI asserts applied == repo head); (5) past historic collisions un-audited — medium × medium; (6) pool-patch retry — low × medium (falsified, E1). Un-mitigable residual: real contention on the new lock unexercised → verify with a deliberately colliding migration (fail-loud test). Never/always: never treat a migration absence as a one-off; always ask what mechanism reproduces it; always verify on a fresh build.
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO: (1) unique sequential versioning + lock, fail-loud on collision; (2) CI assertion applied == repo head (closes E7); (3) apply 0041 to prod + staging now (idempotent DDL); (4) audit `schema_migrations` vs repo for prior silent skips. Failure branch priced: if the new runner breaks apply-order → revert to timestamped runner is one flag (reversible, low exposure). Verification: fresh build must include 0041; plan uses the index; latency < 100 ms; timeout rate → 0; a deliberate colliding migration fails the pipeline loudly.
### REVIEW — insight pass (S2, packet gate)
- I1: the pool fix was not merely ineffective — its unchanged rate (E1) is the decisive falsifier: the patch's own before/after comparison proves the mechanism is hold time, not pool count.
- I2: the cause of the absence is not the absence — "0041 not applied" is a fact; the root is the versioning property that re-creates the absence on every fresh build, which is why staging (frequently rebuilt) reproduces the issue while prod looks stable.
### DECISION PACKET
- Conclusion: root = same-second migration-timestamp collision silently dropped by the runner's per-second dedup, leaving `order_items.order_id` unindexed on every fresh build; fix = unique sequential versioning + fail-loud on collision + CI applied==head sync; apply 0041 now; verify on a fresh build incl. a deliberate collision.
- Status: SOLVED (recommendation packet; execution deferred to owner). Assumptions: E1–E7 current; runner dedups per second by filename timestamp (E5). Evidence: E1–E7 cited per link. Alternatives: A pool resize (rejected — falsified, E1); B manual index (rejected — recurs at rebuild, E6); C mechanism fix (selected). Uncertainty: historic silent skips beyond 0041 (audit added); collision rate under real contention (fail-loud test). Risks: reverting to timestamped runner if uniqueness rollout misbehaves (reversible); other runner-side silent behavior (CI sync closes).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both deliver the mechanism root + recurrence-proof fix; 5/5 rubric |
| Logical Validity | 5 | 5 | Tie | per-link evidence both; AI adds fault-tree + re-drill of the naive chunk |
| Coherence & Structure | 4 | 5 | AI | staged packet + fault tree + gate vs linear drill |
| Depth of Reasoning | 5 | 5 | Tie | AI now reaches the tooling root the v5 run missed; no depth gap left |
| Efficiency | 3 | 5 | AI | dual-pass + gate land the same depth with a packet, not a longer chain |
| Handling of Uncertainty | 5 | 5 | Tie | both flag partially-verified links; AI's recurrence test + fail-loud residual named |
| Insight / Non-obviousness | 5 | 5 | Tie | AI's "cause of the absence is not the absence" + rate-as-falsifier match the human's |
| Overall Quality | 4.7 | 4.9 | AI | AI marginal — effectively parity on content, ahead on structure/efficiency |

Winner: AI (marginal; effectively parity). Why: the routed m013+m091 dual pass reproduces the gold-standard chain link by link (mechanism root, recurrence prediction, uniqueness fix) — the v5 AI's stopping point ("0041 not applied") is now a contract failure the re-drill catches; the m003 gate's never/always reframing and the fault-tree packet add structure and efficiency, edging the tie.
