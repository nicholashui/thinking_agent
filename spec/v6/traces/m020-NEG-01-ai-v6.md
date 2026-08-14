# v6 Routed AI Trace — m020-NEG-01 (blinded)
## Annual conference ticketing platform — adopt / incumbent / hybrid (decision due by end of week)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,strategy | g:decide,maximize,predict | c:deadline
- Router top3: m011, m020, m023; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m011 + m020 first-class passes, synthesized (m023 = synthesis context). No R3 gates triggered (no adversarial / one_shot / high_stakes / unmeasured in signature). Tempo mode ON (P2, deadline).
### WHAT — frame + structure-first scan (S1)
- Decision: ticketing platform — adopt new (analytics, lower fee, modern UI) vs 8-year incumbent (no major outage) vs hybrid. Structure: registration pipeline — 12,000 records → 3-week migration → ticket sales in 6 weeks; one new component (the platform) in an otherwise unchanged system with an 11-0 run history.
### WHY — P1 input-provenance audit + base-rate classification
- UNCHANGED + historically successful (take as given): venue (same terms), team, vendors, runbook, cancellation/liability insurance — 11 consecutive runs, rising feedback scores; the runbook and insurance ARE the existing mitigations.
- DELTA (the only genuine risk surface): the ticketing migration — 12,000-record transfer, 3-week integration window, unknown support-load profile vs the incumbent's 8-year uneventful record.
- INTERESTED-PARTY: the new platform's pitch (analytics/lower fee) is the vendor's claim; the association's own base rate is the measured authority.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m011 systems scan): stocks/flows — 12,000 registrant records flow through one new node (platform) into sale day; the only loop is post-launch support-load feedback; falsifiable observable: dress rehearsal at T-3 with numeric criteria (migration hash check, load test) — fail or window overshoot converts adopt → incumbent.
- Pass S2 (pre-mortem, DELTA-SCOPED — base-rate-aware contract): Assume the 12th conference is called a disaster. Back-cast causes — every cause must have scenario support; generic insured causes (venue fire, wifi, speaker illness, food poisoning, double-booking, badge printers) are DISCARDED as duplicate coverage — runbook + insurance already mitigate them and they are unchanged in 11 runs:
  - D1 migration data corruption (L High × I High) → hash-verified staging dry-run.
  - D2 support-load spike on new vendor at sale day (L Med × I Med-High) → SLA (4-hr response) + monitored queue.
  - D3 vendor stability post-migration (L Low × I High) → data escrow; incumbent copy retained warm.
  - Capped at 3, ranked by L×I — no flat list; the method's "lists risks without ranking" weakness gate-checked.
- Synthesis (V1–V3): passes AGREE — delta = ticketing; decision = adopt-with-gate. m023: the fee/analytics upside is small but real; the hybrid's cost is one rehearsal — deferral is the expensive choice (decision debt on a deadline).
### DO — P3 branch completeness + tempo commit
- Negative branch priced: adoption failure at rehearsal → rollback within 48h to the incumbent (warm read-only copy, refreshed at cutover) — priced, pre-specified, not a hope. Decision committed at DO: adopt with gated rollout, this week.
### REVIEW — insight pass (S2, packet gate)
- I1: the incumbent's 8-year outage-free record is a reference class — the new platform's risk is not "unknown support load" but first-trial-of-a-proven-in-general system; the rehearsal converts it to a measured quantity before the irreversible event.
- I2: the fee savings make the hybrid nearly free — the real cost of "wait for more data" is not money but the missed decision week.
### DECISION PACKET
- Conclusion: adopt the new platform with gated rollout — sign with SLA (4-hr response); full dress rehearsal at T-3 (staging migration, hash-verified, load test, numeric criteria); incumbent read-only DB retained warm and refreshed to cutover; rule — rehearsal fail or SLA unmet by sale day → roll back within 48h.
- Status: SOLVED (decision made with a defined checkpoint; no external action). Assumptions: unchanged plan continues its base rate; incumbent rollback copy refreshable; rehearsal fits the 3-week window. Evidence: 11-run record, insurance schedule, incumbent uptime, vendor fee/feature comparison, window timing.
- Alternatives: A full cutover (rejected — first signal is a crashed sale day); B keep incumbent (rejected as default — measured savings foregone for unmeasured risk); C adopt-with-gated-rollout (selected). Uncertainty: vendor responsiveness (SLA + rehearsal), migration data quality (hash check), fee-savings accuracy. Risks: rehearsal failure → pre-specified 48h rollback; migration corruption → hash check; support overload → SLA + queue monitoring; excluded event risks unchanged, covered.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human never decides the ticketing question; AI commits with a gate |
| Logical Validity | 4 | 5 | AI | human internally valid but goal-displaced; AI's unchanged-vs-delta chain stays on-goal |
| Coherence & Structure | 3 | 5 | AI | human: 15 equal-weight causes; AI: dual-pass synthesis → packet |
| Depth of Reasoning | 4 | 4 | Tie | human's enumeration thorough + self-aware; AI's delta pass narrower but decision-relevant |
| Efficiency | 2 | 5 | AI | human re-derives what runbook/insurance encode; AI caps the pass at 3 delta risks |
| Handling of Uncertainty | 2 | 5 | AI | human: no ranking, deferral by implication; AI: rehearsal gate + numeric criteria + 48h rollback |
| Insight / Non-obviousness | 3 | 5 | AI | human's migration-integrity insight buried at item 8/15; AI: reference-class + near-free-hybrid |
| Overall Quality | 2 | 4.9 | AI | AI clearly better on the negative case |

Winner: AI (clearly). Why: the dual-route base-rate-aware pass (m011 scan + delta-scoped pre-mortem with the discard rule, capped at 3 ranked causes) makes the strict pre-mortem's 15-item manufacture structurally impossible, while the tempo-commit at DO blocks the deferral the pure style implies.
