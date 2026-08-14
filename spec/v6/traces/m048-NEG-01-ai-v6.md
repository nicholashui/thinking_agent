# v6 Routed AI Trace — m048-NEG-01 (blinded)
## FreshBasket branch 12 — 14-day milk OOS; decide the intervention
### META (routing — blind router output)
- Signature: d:engineering,medical,organization,science,supply | g:decide,guarantee,maximize,predict | c:deadline
- Router top3: m091 (9), m020 (8), m026 (8); top-1/top-2 gap = 1.0 > 0.5 → CONFIDENT → single-route: m091 first-class pass, m020 + m026 corroborating. Mandatory gate (R4): m003 inversion (guarantee goal). Flags: tempo mode ON (P2 — deadline, cost-of-delay ~$650/day); closed-scope fast path (P8 — fully specified).
### WHAT — frame + structure-first scan (S1)
- Frame: anomaly diagnosis with a sharp onset window (14 days ago) and a visible local check; the decision is the intervention. Structure: store stock fed by a reorder loop (reorder point 600 / order qty Q); the DC and supplier loops exist but are ruled out by evidence, not modeled first — a sustained 360/day deficit with flat demand and a full-fill DC means the store's own ordering is suppressed.
### WHY — P1 input-provenance audit + cheap-checks triage (m091 chunking)
- Inputs: POS flat 400/day (3 months), DC fill 99.7% ships-exactly-what-ordered, manager shift log "milk out again by 11am — check reorder qty" on day 1, settings screen changed 14 days ago (reorder qty 400 → 40) — all MEASURED. The proposed 3–4 week chain-model/S&OP program is INTERESTED-PARTY (a program needs a data-hungry rationale; who benefits from the study?). Chunk the anomaly (m091): (1) onset-window change, (2) parameter value, (3) deficit arithmetic, (4) two one-line falsifications (demand stability; DC fill) — every chunk is checkable in minutes; none needs a model.
### HOW — style passes (single-route) + m003 gate
- Pass S1 (m091 chunking, first-class): audit the onset window → settings screen: reorder qty 40 vs 400, changed 14 days ago; verify deficit 360 = 400 − 40/day matches the observed OOS exactly; rule out demand (POS flat 400) and upstream (99.7% fill, ships exactly what is ordered) in one line each. H1 parameter corruption CONFIRMED with decision-relevant evidence — an honest chain model's calibration would need "effective supply ~40/day," which IS the same parameter screen.
- Corroboration m020 (pre-mortem): assume the analyst's S&OP/safety-stock program is one year later and failed — work backward: OOS persisted (the parameter was never restored; reorder optimization inherits Q=40; safety stock sized against the wrong effective supply), ~$9k+ window bleed, a month consumed with no measured change. The program's failure branch is not "small miss" but "no mechanism touches the parameter" — it fails by construction unless it audits parameters, and the audit IS the fix.
- Corroboration m026 (analogy, mapping made explicit before transfer): known family — "printer is unplugged / settings-screen typo": persistent deficit + exact onset + exact arithmetic + visible local check ⇒ local parameter restore, not redesign.
- Gate m003 (INVERSION — completion contract): ≥6 failure modes of the ANALYST'S PROPOSED program, ranked by likelihood × impact: (1) OOS continues while data is collected (certain, ~$650/day) · (2) reorder optimization inherits corrupted Q=40 (high) · (3) safety stock sized on wrong effective supply (high) · (4) 3–4 weeks of bleed ≈ $9k+ (certain) · (5) S&OP joins a DC already at 99.7% fill — no lever (medium) · (6) program success metric (fill rate) unchanged by definition (medium) · (7) manager's day-1 log ignored → trust loss (medium) · (8) opportunity cost vs the 5-minute restore (certain). Un-mitigable residual: why the parameter changed — no change control (process follow-on, not blocking). NEVER: never defer a visible parameter restore to a structural program; ALWAYS: always check what changed at onset before modeling the chain.
- Divergence (V1–V3): m091/m020/m026 agree (cheap restore first); vs the general route — the non-routed v5 run reached the same verdict; agreement recorded, no divergence.
### DO — tempo mode (P2) + P8 fast path (fully specified)
- Commit NOW: restore reorder qty 40 → 400 (5 minutes, per store procedure); audit the rest of the settings screen (other fields, same onset); notify the manager; monitor on-hand + OOS 1–2 days. Cost of delay priced: every day ≈ $650 + 360 units. The restore is itself the decisive experiment — if the deficit were not from Q, the OOS would not end within ~1 day. P3: failure branch priced — if OOS persists >2 days post-restore, escalate to lead-time/variability analysis (pre-declared boundary); not needed today.
### REVIEW — insight pass (S2, packet gate)
- I1: any honest chain model of this OOS must be calibrated with "effective supply ≈ 40/day" — the model would re-derive the parameter screen it refused to open; the program's 12-week data collection is the expensive route to the 5-minute fact.
- I2: the restore is also the test — 5 minutes + ~1 day of monitoring discriminates parameter corruption from systemic variability; that is the cheapest decisive experiment in the case, and the 3–4 week program buys the same information later and after ~$9k of bleed.
### DECISION PACKET
- Conclusion: restore reorder qty to 400 now; verify orders return to 400/day and OOS ends within ~1 day; audit the settings screen; defer chain model / safety stock / S&OP unless the cheap checks fail — they did not.
- Status: SOLVED (evidence-complete: onset window + log + exact arithmetic; recommendation issued; execution per store procedure).
- Assumptions: demand stays flat 400/day; DC continues full fill; no other settings changed.
- Evidence: settings change 14 days ago (onset match); 400 − 40 = 360/day = observed deficit; 99.7% fill (upstream ruled out); POS stable (demand ruled out); manager log flags the parameter on day 1.
- Alternatives: A restore parameter (selected) · B chain model + safety stock + S&OP 3–4 wk (rejected — no mechanism touches Q; inherits the corruption) · C DC/supplier project (rejected — no upstream evidence) · D do nothing (floor).
- Uncertainty: causal attribution exact (arithmetic), not probabilistic; residual: why the change occurred (no change control) — process follow-on, not blocking.
- Risks: OOS persists >2 days → escalate (boundary pre-declared); other corrupted fields on the settings screen; parameter edits without change control (process gap — 4-eyes follow-on).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human fixes the wrong thing (3–4 week program); AI restores the parameter, OOS ends in a day |
| Logical Validity | 2 | 5 | AI | human's model reproduces OOS only via "effective supply ~40/day" — the parameter it refused to read; AI's falsifications one-line sound |
| Coherence & Structure | 3 | 5 | AI | human's systemic narrative coherent but detached from the window; AI's chunked triage auditable |
| Depth of Reasoning | 3 | 4.5 | AI | human's depth misdirected (chain diagram, safety-stock math); AI deeper on the actual causal chain + 8-category inversion |
| Efficiency | 1 | 5 | AI | 3–4 weeks + data collection vs 5 minutes + 1–2 day monitor |
| Handling of Uncertainty | 2 | 4.5 | AI | human validates nothing; AI pre-declares the escalation boundary and prices the program's failure branch |
| Insight / Non-obviousness | 2 | 4.5 | AI | human misses the visible cause on the desk; AI reads the log + screen and adds restore-as-decisive-experiment |
| Overall Quality | 2.1 | 4.8 | AI | same verdict as v5 (AI clearly better); routed run adds failure-branch pricing and tempo discipline |

Winner: AI (clearly). Why: the routed m091 chunking + m003 inversion gate made cheap-checks-first and the systemic program's 8 ranked failure modes (it inherits Q=40 and has no mechanism touching the parameter) first-class contract outputs before DO, converting the pure style's data-hungry over-modeling into a 5-minute fix under deadline tempo — the non-routed v5 run already won on triage; the routed run prices the wrong branch's failure and the restore as the decisive experiment it already was.
