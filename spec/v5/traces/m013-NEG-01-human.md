# Human Baseline — m013-NEG-01
## Style: Root Cause Analysis (5 Whys + deeper) — pure — visible reasoning trace

**Problem restatement.** Nightly ETL reports SUCCESS yet drops ~0.4% of rows; reconciliation has flagged the mismatch for
6 days; the next run starts in 2 hours. Drill to the deepest evidence-supported cause and fix the root.

**Why 1 — rows are lost.** Transform log: "skipping row: field 'region' is null" on ~0.4% of rows, every run for 6 days (E2).
Mechanism at this level: a silent skip inside the transform.

**Why 2 — region is null.** Vendor schema v2.1 shipped 6 days ago — exactly the onset of the mismatch (E1) — and changed
`region` from required to optional (E3). Upstream records now arrive without the field.

**Why 3 — nothing catches it.** The ingest path has no schema validation (E5), so nulls reach the skip branch silently.
Validation would catch this — noted as a control point, but it is not the *cause*; the cause is upstream.

**Why 4 — the vendor shipped a breaking change without notification.** Changelog confirms v2.1 (E3); release notes bury the
"clients should validate optional fields" advice (E4); no customer notification was sent; support confirms the gap and
schedules v2.2 in 6–8 weeks (E4).

**Why 5 — why no notification?** The vendor's release process has no client-impact notification gate: nothing requires the
schema change to be announced, sequenced, or coordinated (E4 — no notification is performed or scheduled).
**Root (deepest supported): the vendor's release/communication process.**

**Verification per link.** Links 1–2 fully evidenced (log + changelog dates align with the 6-day onset). Link 3 evidenced
(code path). Link 4 evidenced (support statement). Link 5 is only partially evidenced — vendor internals are unobservable
from our side; flagged as inference, not asserted.

**Fix at the root.** The root sits inside the vendor, which we cannot change — so the fix must change our relationship to it:
(1) escalate at contract/SLA level: require a client-impact notification policy and a committed v2.2 timeline; (2) until the
root lands, interim containment at our boundary: schema validation + dead-letter queue + alert at ingest, and re-inject the
6-day backlog. The interim is explicitly labeled interim: the true fix is the vendor's process.

**Trace summary box.** Chain: dropped rows ← nulls skipped ← `region` optional (v2.1) ← no ingest validation ← vendor
shipped breaking change silently ← vendor release process lacks client-impact notification (root, outside our control).
Fix: vendor-process change via escalation (primary); validation + dead-letter (interim, 30 min).

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to strict RCA — depth to the deepest
supported cause; interim fixes labeled interim. The pure style's exposure is exactly here: the actionable lever (a 30-minute
boundary fix that fully contains the harm) is treated as interim while the main effort targets a root we cannot touch.*
