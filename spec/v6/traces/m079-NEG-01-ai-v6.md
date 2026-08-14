# v6 Routed AI Trace — m079-NEG-01 (blinded)
## PayStream — live-incident rollback decision (05:00 SLA line, hunt requested)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software | g:decide,diagnose,estimate,guarantee | c:deadline
- Router top3: m028, m033, m015; confident=no → AMBIGUOUS → DUAL-ROUTE: m028 + m033 first-class passes, synthesized (m015 = context — its registered "rationalize inaction" weakness is exactly the live-incident trap, held out of the pass set). Gate: m003 (R4 — guarantee → Inversion prepended). Flags: tempo mode ON (P2, deadline: cost-of-delay priced, commit at DO); P8 fast path (ledger closed); E5 stabilize-before-diagnose (containment triage: rollback staged twice + verified, SLA window bounded — one pass); structure-first scan (S1, org/software).
### WHAT — frame + structure-first scan (S1)
- Frame: decide the rollback under time cost; the requested hunt needs a bar for what *earns* a changed mind, or any unexamined artifact can veto a supported conclusion. Structure: incident forensics = causal graph on a timeline — deploy 02:00 → onset 03:12 → first error bucket 03:15+, candidates {migration, LB change, gateway, generic DB failure}.
### WHY — P1 input-provenance audit
- MEASURED (trust): 03:15 first error bucket; 21 lock-wait events on the new index; 96% DB-connection-timeout signature (item 4); LB reverted 03:10 with no effect. INTERESTED-PARTY: the migration author's "never load-tested at scale" admission (self-report — consistent with the measured chain, but weighted as admission, not anchor); the gateway call = provider self-report, retracted at 09:00 with their logs clean.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m028): break the framing — the assumption to attack is "concurrent changes are equally suspect." Lateral move: the 03:00 LB tweak is a natural control — a concurrent change reverted with zero effect is exonerated *by the revert itself*, which removes it from the suspect set rather than adding doubt. Second lateral move: can any candidate other than the migration produce the 03:15 first-error bucket with all 21 lock-wait events referencing the new index? None — the lateral sweep fails to manufacture an alternative.
- Pass S2 (m033): read the ledger as an experiment — the incident IS the observation; staging soak = the underpowered test (2% load, 1/40th rows — proves nothing about the production table); LB revert = a completed control with null effect; gateway = instrument error (retracted, clean logs); 03:10 "clean" bucket = 5-minute granularity artifact (bucket covers 03:10–03:15; first error bucket 03:15, post-deploy 72-min lock-wait escalation pattern). Isolation: the only intervention matching both the temporal signature (02:00 → 03:12 → 03:15) and the error signature (96% DB-timeout = lock waits) is the migration.
- Evidence-graded falsification bar per item (time-consistency, signature-match, weight): item 1 fails time (resolution artifact); item 2 fails signature (monitoring-only, no traffic path, null revert); item 3 fails signature + weight (retracted, clean logs); item 4 fails weight (underpowered). None earns doubt; all four earn post-mortem notes.
- Divergence (V1–V3): m028 and m033 AGREE: migration caused it — roll back now; general route concurs on the anchor chain. Agreement recorded; no branch-complete dispute.
### GATE — m003 Inversion (R4, completion contract)
- ≥6 failure categories, ranked by likelihood × impact: (1) investigate-first 2h+ → SLA breach ≈ $150k + two top accounts at risk [high]; (2) wrong rollback → 25 min + re-investigation, still inside SLA [low]; (3) rollback fails to restore → staged twice, escalation path, bounded [low]; (4) no artifact retention → repeat incident, unlearned [med]; (5) 30-min delay increments ≈ $25k affected volume each [high]; (6) hunt without a bar → contrarian revision + breach [high]. Never/always reframing: "never act before full investigation" is the inversion of safety on a live line. Residual: coarse 5-min monitoring; underpowered soak — post-mortem items, not decision blockers.
### DO — P3 branch completeness + tempo commit (P2)
- A rollback now: 25 min → restore ~04:55, inside 05:00; failure branch = wrong cause → still inside SLA with 45+ min to re-investigate (bounded). B investigate-first: 2h+ → breach certain; failure branch = breach AND real cause untouched. C partial rollback: no partial runbook — infeasible. Commit at DO: execute A now, retain LB/gateway logs for post-mortem; P8 stages compressed.
### REVIEW — insight pass (S2, packet gate)
- I1: the hunter's best doubt (the concurrent LB change) is actually a free control experiment — a change reverted with no effect exonerates itself and leaves the migration as the only remaining cause.
- I2: an underpowered soak passing is worse than no soak — it manufactured the false confidence that made the incident surprising.
### DECISION PACKET
- Conclusion: the migration is the root cause — execute the rollback now (~04:55, inside the 05:00 SLA line); all four disconfirming items fail the falsification bar and become post-mortem items. Status: SOLVED (external action authorized: rollback, runbook-verified).
- Assumptions: runbook reversibility verified; error-code taxonomy accurate; commander authority within the SLA window. Evidence: 02:00→03:12 onset; 03:15 first bucket; 21 lock-wait events on new index; 96% DB-timeout; LB null revert; gateway retraction; soak 2%/1:40.
- Alternatives: A rollback (selected); B investigate-first (rejected — bar + asymmetry); C partial (infeasible). Uncertainty: causality anchored on lock-wait logs + signature, not direct reproduction; 5-min bucket granularity. Risks: rollback fails to restore (staged twice; escalation path); real cause elsewhere (25-min bounded cost; logs retained).
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human revises to "inconclusive — no rollback," breaching the SLA; AI executes the 25-min rollback that preserves it |
| Logical Validity | 2 | 5 | AI | collection-without-grading vs a falsification bar (time, signature, weight) that fails all four items |
| Coherence & Structure | 4 | 5 | AI | dual-route passes + packet under a time budget vs single-track doubt narrative |
| Depth of Reasoning | 3 | 5 | AI | human elaborates each artifact; AI digs to bucket granularity, null-revert control logic, soak power |
| Efficiency | 2 | 5 | AI | human spends the SLA window manufacturing doubt; AI decides in one graded pass (tempo commit) |
| Handling of Uncertainty | 2 | 4.5 | AI | human over-doubts (mis-calibrated); AI names real residuals as post-mortem items, not blockers |
| Insight / Non-obviousness | 1 | 4.5 | AI | manufactured doubt vs the LB-null-revert-as-control-experiment and the false-confidence-soak insights |
| Overall Quality | 2.3 | 4.8 | AI | AI clearly better |

Winner: AI (clearly). Why: the route kept the trap style out of the pass set (confident=no → m028/m033 dual-route with the evidence-grading bar), so every disconfirming item earned a graded verdict instead of doubt — the exact meta-move the pure style lacks — and tempo mode (P2) committed the rollback inside the SLA line.
