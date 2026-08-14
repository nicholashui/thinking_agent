# v6 Routed AI Trace — m046-NEG-01 (blinded)
## PayShip ledger architecture — recommendation memo (closed-scope, fully specified)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,security,software,strategy | g:decide,estimate,guarantee,maximize | c: (none)
- Router top3: m070 m018 m019; confident=yes → SINGLE ROUTE: top-1 as first-class pass, top-3 as context. Historical lookup: the negative-case record for this signature routes AWAY from the model whose proposal is on trial (its failure mode stays out of first-class position). Gates (R4, guarantee-goal): m003 inversion MANDATORY. Flags: closed-scope fast path ON (P8); tempo OFF.
### WHAT — frame + structure-first scan
- Deliverable: settle whether a derived log-and-cache ledger may be the system of record for money movement. Correctness under failure and auditability outrank scale. Success: no unrecoverable divergence; one unambiguous record per mutation; headroom at 1M/day.
### WHY — P1 input-provenance audit
- The derivation is INTERESTED-PARTY input: the proposer's identity ("proud" practitioner), schedule and reputation all benefit from the derived design winning. The NUMBERS are measured (50k→1M/day ≈ 12/s steady, 200/s peak; 10k+ tps RDBMS) — but the CONSTRAINT LIST is an anchor, not evidence: throughput enumerated, correctness assumed. P10: arithmetic first, then frame.
### HOW — first-class passes (routed top-3, no divergence)
- Pass S1 (evidence-graded SWOT — every item graded, unsupported items dropped): S — unbounded scale, near-zero cost, simpler machinery: TRUE but graded LOW RELEVANCE — throughput is non-binding at 12–200/s vs 10k+ tps (~2 orders headroom), so the strengths optimize a non-constraint → DROPPED. W — no crash atomicity at the mutation boundary; reconciliation detects but cannot classify divergence; repair cost multiplicative in partitions: HIGH evidence → KEPT. O — S3 append-only export as archive/reporting tier: HIGH evidence → KEPT. T — monetary audit expects one auditable source of truth per mutation; divergence visible during the repair hour to balance checks, rate limits, customer reads: HIGH → KEPT.
- Pass S2 (strongest defensible form of the opposing design): genuinely simpler, genuinely unbounded, idempotency keys cover retries, the append-only log IS the audit trail, reconciliation converges within an hour. Strongest form still fails: "what is the state when a process dies between append and apply, at 200/s, on 40 partitions?" — no boundary to attribute it to; the log that is the audit trail gets patched by the repair job.
- Pass S3 (adversary pass — vectors + quantified exposure + baseline-risk): (1) crash between append and apply — exposure: every mutation, all partitions; (2) retry duplication after partial apply — exactly-once unachievable across a crash; (3) divergence reads during the repair hour — balance checks/rate limits/customer-facing; (4) audit-trail reconstruction — impossible for the divergence window; (5) repair cost — multiplicative in partitions (×40), unbounded without replayable per-mutation state; (6) scale-up irony — the failure mode appears exactly at the 1M/day the design claims to serve. Baseline-risk: the transactional ledger's known modes (hot-account contention, migration) are bounded with decades of playbooks; the derived design's are unbounded.
### GATES — m003 inversion (R4)
- ≥6 ranked failure categories (L×I): (1) crash between append and apply high/critical; (2) retry/duplicate after partial apply high/critical; (3) divergence visible during the repair hour high/high; (4) audit reconstruction impossible med/critical; (5) repair cost multiplicative at scale-up high/high; (6) exactly-once across crash high/critical; (7) rate-limit/balance read of divergent cache mod/mod.
- Un-mitigable residual: none in the derived design's class — the pattern encodes exactly the named categories; residual is migration risk (dual-write window). Never/always: never accept a derived design that rejects a battle-tested pattern in a high-stakes domain without enumerating what the pattern encodes; always test the crash boundary, not just whole-transaction loss; always demand per-mutation attribution before "eventually consistent".
### DO — P8 fast path + P3 branch pricing
- Memo: retain the transactional double-entry RDBMS ledger (one ACID transaction per mutation, partition by account); S3 append-only export as archive/reporting tier; reconciliation = detection/monitoring, not a repair path. Adopted-derived-design branch priced: unbounded repair + audit failure + regulator exposure — cost NOT bounded. Verification: divergence = 0 through dual-write mirror-check migration; audit replay reconstructs any mutation; p99 < 50 ms at 200/s peak.
### REVIEW — insight pass
- I1: reconciliation detects but cannot attribute — a design whose repair cannot classify divergence is unrepairable, not eventually consistent. I2: the derived design is a correct answer to a non-binding constraint; a pattern is a compressed failure-mode list, and rejecting it without reading the list is where the derivation loses the ecosystem's accumulated experience.
### DECISION PACKET
- Conclusion: keep the battle-tested transactional ledger as the system of record; demote the derived log to archive. Status: SOLVED.
- Assumptions: 1M/day is the ceiling (at 10×, revisit partitioning, not the ledger shape); audit requires per-mutation single truth; repair cost grows with partitions (first-principles model, confirmed by the mirror check).
- Evidence: 12–200/s vs 10k+ tps (non-constraint); crash-window model (attribution-free divergence, multiplicative repair); audit requirement; SWOT evidence grading.
- Alternatives: derived S3-ledger (rejected: unbounded repair, no audit truth) · transactional RDBMS (selected) · hybrid + archive tier (selected component) · streaming-store ledger (rejected: complexity, no binding need).
- Uncertainty: real-world crash frequency (bounded by mirror check); partition hotness (data-dependent). Risks: proposer preference → cost-of-repair math attached; migration divergence → mirror-check gate; audit rejection of reconciliation-only repair → audit-readiness section.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human approves the derived ledger; AI retains the transactional one |
| Logical Validity | 2 | 5 | AI | human's derivation valid inside an incomplete constraint list; AI tests the crash window |
| Coherence & Structure | 4 | 5 | AI | human's chain is consistent but misses the tell; routed passes expose it in-pass |
| Depth of Reasoning | 3 | 5 | AI | human never opens append→apply; AI models crash, audit, non-binding scale, repair scaling |
| Efficiency | 3 | 4.5 | AI | v5's catch at the WHY falsification stage is now the opening pass; one stage saved |
| Handling of Uncertainty | 2 | 5 | AI | human asserts; AI names crash model, mirror check, partition hotness |
| Insight / Non-obviousness | 2 | 5 | AI | "detects but cannot attribute" is the routed pass's first read; the human's log-as-ledger move is wrong |
| Overall Quality | 2.6 | 4.9 | AI | routed evidence-graded SWOT + steelman + adversary + inversion gate catch the omission first-pass |

Winner: AI (clearly). Why: the router's trap-avoidance (m046 absent from its own negative-case route) replaced the v5 "correct-but-late" WHY catch with first-class passes — evidence-graded SWOT, strongest-form steelman, and an adversary pass with quantified exposure all land on the omitted binding constraints (crash atomicity, auditability) before selection, and the inversion gate makes the failure enumeration complete and ranked. Same verdict as v5, gap closed one stage earlier, and the ecosystem check is now explicit rather than an afterthought.
