# v6 Routed AI Trace — m013-NEG-01 (blinded)
## Nightly ETL silent 0.4% row loss — 2 h to next run
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,product,software,supply | g:diagnose,maximize | c:adversarial,deadline
- Router top3: m044, m011, m021; confident=yes → SINGLE-ROUTE first-class pass m044 (stakeholder lens); m011/m021 = top3 context (falsifiable-observable check; tempo). Mandatory gate: m019 adversary pass (R3 adversarial; routes.csv). Flags: tempo mode ON (P2, deadline; maximize-goal → falsifiable checkpoint required).
### WHAT — frame + structure-first scan (S1)
- Frame: stop tonight's silent loss and return the BI dashboard to current within the 2 h window; diagnosis serves the action, not the reverse. Structure: row-flow (source → ingest → transform → warehouse → dashboard) with two mismatched success predicates — job SUCCESS vs rows landed.
### WHY — P1 input-provenance audit
- MEASURED (trust): reconciliation counts (E1), transform skip log (E2), ingest code path (E5). INTERESTED-PARTY: vendor changelog + support (E3/E4) — the vendor benefits from the "known issue, fix in v2.2" frame; the 6–8 week commitment is unverified from our side → discount it, treat v2.2 as uncommitted. ANCHOR: none needed (E1/E2 define the loss).
- Chain (evidence per link): rows dropped ← transform silently skips null `region` (E2) ← `region` optional since v2.1, shipped 6 days ago (E3 — onset matches E1's 6 days) ← no ingest validation, so nulls are silent (E5) ← vendor shipped a breaking schema without client notification (E4). Beyond this the chain enters vendor release-process internals — unobservable from our side and outside our authority, budget, and the 2 h window: control boundary; escalate, don't fix.
### HOW — style pass (m044 first-class + top3 context)
- Pass S1 (m044): stakeholders and their 2 h needs — BI consumers / finance: dashboard current before the weekly review (realized harm today, not a hypothetical); ETL owner: SUCCESS status is false comfort — job semantics must equal rows landed; data-platform owner: a 30-min reversible change beats a 6–8 week wait; vendor account: one scoped ticket, not a renegotiation project. Hidden requirement surfaced: the alerting model watches the wrong predicate (job status, not row counts) — that is the gap the incident exposes.
- Top3 context: m011 scan — stock: warehouse rows; flow: source → ingest with a skip leak; falsifiable observable: rows_in = rows_landed + dead_letter count, checked against reconciliation every run; local-data-first: the reconciliation report already gives the daily leak rate. m021 tempo — observe → orient → decide → act inside 2 h; commit at DO.
- Divergence: single-route (confident) — no style split; general route agrees (containment-first triage); agreement recorded.
### GATES — m019 adversary pass (R3)
- Vectors with quantified exposure: (1) replay races tonight's run — re-injected/duplicate rows during replay, medium — schedule replay after tonight's run, idempotent keys; (2) validation covers only `region` — next optional field ships silently → null class uncaught, high — fail-loud on ANY skip + dead-letter catch-all + alert, not a rule list; (3) alert fires, nobody staffed — high if unowned — assign ETL owner + escalation path; (4) vendor v2.2 fixes nothing (unverified promise) — high if we wait — baseline: don't wait; (5) dead-letter unbounded overnight — medium — replay pipeline + monitor depth. Baseline-risk comparison (the line that decides): inaction = 0.4%/night continues, BI stale at the weekly finance review — realized loss; the boundary fix is a 30-min reversible change closing the harm mechanism tonight.
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO: boundary fix = schema validation + dead-letter + fail-loud alert at ingest as the PRIMARY fix, ships within the 2 h window (not an interim patch awaiting a root); replay the 6-day backlog idempotently after tonight's run; raise ONE scoped vendor ticket (v2.2 timeline ask + client-impact notification policy). Failure branch priced: validation false-positive on a legit new field → dead-letter preserves the rows (no data loss by construction); replay failure → re-runnable, verified against reconciliation.
### REVIEW — insight pass (S2, packet gate)
- I1: the job's SUCCESS status is the actual failure — the alerting model predicates on process completion, not rows landed; the incident is a semantic bug in the success predicate, not only a missing check.
- I2: the deepest evidence-supported cause (vendor release process) is the least actionable — depth and leverage are different axes; the 30-min boundary fix that closes the harm is the primary fix by the 2 h deadline, and the vendor tail is escalation context, not the plan.
### DECISION PACKET
- Conclusion: act at our ingest boundary now (validation + dead-letter + fail-loud alert) as the primary fix; replay the 6-day backlog after tonight's run; one scoped vendor ticket; vendor root documented as escalation context only.
- Status: SOLVED (loss mechanism closed at our boundary tonight; escalation recorded). Assumptions: validation + alert cover the current schema and any unknown null class via fail-loud; replay idempotent; vendor timeline not trusted. Evidence: E1–E6 per link; v2.2 promise discounted (interested-party). Alternatives: A vendor-root fix (rejected — 6–8 wks, loss continues, no control); B boundary fix (selected); C status quo (rejected — realized loss continues). Uncertainty: unknown future null classes — covered by alert + dead-letter, not trust. Risks: replay race (sequenced after tonight's run); alert storm (dedupe + owner); vendor ships new optional fields before rules mature (fail-loud catches).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human targets the vendor root (6–8 wks) while loss continues; AI closes harm tonight |
| Logical Validity | 5 | 5 | Tie | both verify the chain link by link incl. the leap into the vendor |
| Coherence & Structure | 4 | 5 | AI | packet + gates vs linear drill; interested-party discount explicit |
| Depth of Reasoning | 4 | 5 | AI | human digs one link deeper into the unactionable; AI's m044 lens reaches the deepest actionable + hidden requirement (wrong alert predicate) |
| Efficiency | 2 | 5 | AI | tempo-mode commit at DO: 30-min fix vs 6–8 wk renegotiation |
| Handling of Uncertainty | 3 | 5 | AI | human stakes the plan on unobservable vendor internals; AI discounts v2.2, fails loud on unknown nulls |
| Insight / Non-obviousness | 2 | 5 | AI | human's interim/primary inversion vs AI's success-predicate bug + depth≠leverage |
| Overall Quality | 3.4 | 4.9 | AI | AI clearly better — same verdict as v5, now structural |

Winner: AI (clearly). Why: the route is no longer pure-RCA — m044's stakeholder lens makes the boundary fix primary by construction (finance's dashboard is the realized harm), tempo mode commits within 2 h, and the m019 gate's baseline-risk line prices inaction; the human's trap (fixing the unactionable vendor root while labeling the lever "interim") is avoided structurally, not by luck.
