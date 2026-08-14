# v6 Routed AI Trace — m019-NEG-01 (blinded)
## HarborCare MFA go/no-go — decision memo due in 2 weeks
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,security,software | g:decide,estimate,guarantee,predict | c:deadline,high_stakes
- Router top3: m018, m019, m089; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m018 (steelman) + m019 (adversary) first-class passes, synthesized (m089 = synthesis context). Mandatory gates: m003 inversion (R4: guarantee-goal prepend), m007 ruin screen (R3: high_stakes). Flags: tempo mode ON (P2, deadline).
### WHAT — frame + structure-first scan (S1)
- Frame: go / go-staged / delay / abort, weighing mitigation risk vs baseline risk. Structure: baseline attack surface (41 shared accounts, 3 public-repo creds, brute-force attempt last month — realized) vs rollout failure surface (lockouts, outage, device gaps, firmware, certification).
### WHY — P1 input-provenance audit
- MEASURED (trust): audit findings; pilot n=120, 99.6% success, 2 lockouts <15 min; rollback flag tested twice; 99.99% SLA; staged-by-department available; 4-week window.
- INTERESTED-PARTY: pilot data is the proposal's own (self-selected population) — trust but discount the tail; helpdesk surge staffed (mitigation, evidenced).
- ANCHOR (unmeasured → scenario): day-1 lockout volume at 16× pilot scale: optimistic 10, base 32 (2/120 projection), pessimistic 75 — all recovered <15 min per the pilot workflow; none patient-blocking beyond the recovery window.
### HOW — style passes (dual-route, completion contracts)
- Pass S1 (steelman, m018): best case — phishing-resistant keys vs an actively attacked password portal; pilot evidence real; rollback is one tested flag; staging by department available → go-staged is defensible on its own evidence.
- Pass S2 (adversary, m019 — do-nothing loss FIRST): baseline-risk line: 41 accounts sharing passwords + 3 creds in public repos + brute-force run blocked only by rate limiting last month = realized, recurring exposure (credential-based EHR access, audit + notification, account takeover — high L × high I over 12 months without MFA). Objections ranked by L×I with rejecting evidence: (1) key loss/lockout — low × high, mitigated (spare keys, <15-min recovery) → not a blocker; (2) auth-server outage — very-low × high (99.99% SLA, one-flag rollback) → not a blocker; (3) personal devices lack FIDO2 — low-mod × medium (device matrix, fallback tokens) → monitor; (4) firmware breaks keys — speculative × unknown (change-managed, canary) → not a blocker; (5) SOC 2 addendum — certain × low (documentation artifact, no functional gap) → parallel track; (6) cookie-theft bypass — true but unchanged-by-this-decision: it needs a compromise of the same class as the baseline's already-leaked creds — "nothing is 100% secure" is true and irrelevant; the decision compares two attack surfaces, not absolutes.
- Divergence resolution (V1–V3): passes DISAGREE (steelman: go-staged; adversary: delay) → branch-completeness + calibration on both: Branch A (go-staged) — P(rollout failure) low, reversible in minutes, baseline exposure reduced; Branch B (delay) — keeps realized baseline exposure active for 2+ quarters, reversible nothing. B is dominated → A selected; disagreement recorded in packet risks.
### GATES — m003 inversion (R4) · m007 ruin screen (R3)
- Inversion (≥6 failure categories ranked, residual, never/always): (1) day-1 lockout surge — mod × high, mitigated (staging + recovery workflow); (2) auth-server outage mid-enrollment — very-low × high, one-flag rollback; (3) shared-credential residue — high × catastrophic IF we do NOT roll out (the inverted failure); (4) enrollment capacity vs helpdesk — low-mod × medium, surge staffed; (5) key logistics at 1,900 units — mod × low, inventory plan; (6) remote-device gaps — low-mod × medium, matrix + fallback. Un-mitigable residual: tail enrollment failures at scale — owned by monitoring + rollback runbook. Never/always: never treat delay as risk-free; never block on an unranked hypothetical while the baseline is actively attacked; always price inaction.
- Ruin screen: distribution over decision — go-staged: rollout disruption (bounded, reversible) vs breach-with-MFA (near-zero vs baseline); delay: baseline breach exposure continues (realized, high); abort: status quo — the floor. One-shot? No — reversible (one flag, staged). Decline/restructure: abort criteria named — if day-1 lockout KPI exceeds threshold, roll back and re-plan (not needed per pilot projection).
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO: approve staged MFA rollout (department-by-department, off-peak enrollment, helpdesk surge, rollback runbook, lockout KPI <15 min, parallel addendum track). Failure branch priced: partial-rollout failure → rollback flag → re-plan; cost bounded in minutes; exposure during rollback = baseline (already priced).
### REVIEW — insight pass (S2, packet gate)
- I1: every objection on the list attacks the future state; the only objection that prices the present is the one nobody raised — "keep password-only": the review's unexamined default is the realized risk.
- I2: last month's brute-force attempt is the reference event — it converts "could happen" into "happened, rate-limited once": delay is not neutral, it is a bet that rate limiting never fails twice.
### DECISION PACKET
- Conclusion: approve staged rollout within 4 weeks; vendor addendum tracked in parallel (documentation, not a gate). Objections 1–6 likelihood-ranked; ≥3 rejected as low-likelihood or already-mitigated; do-nothing loss stated first.
- Status: SOLVED (decision memo; reversible at all times). Assumptions: audit current; pilot/SLA as stated; rollback remains available. Evidence: audit report, pilot data, 99.99% SLA, tested rollback, brute-force attempt record. Alternatives: A go-staged (selected); B delay (rejected — dominates nothing, keeps baseline active); C abort (rejected — status quo is the risk). Uncertainty: lockout volume at scale (KPI-monitored, rollback-ready); addendum timing. Risks: inaction risk is the risk being mitigated; rollout disruption bounded by staging + rollback.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human blocks a sound urgent fix; AI approves staged |
| Logical Validity | 3 | 5 | AI | human objections valid, conclusion ignores the baseline |
| Coherence & Structure | 4 | 5 | AI | dual-pass + gates + packet vs attack log |
| Depth of Reasoning | 4 | 5 | AI | human attack-depth uncalibrated; AI adds steelman + scenarios + reject-log |
| Efficiency | 4 | 5 | AI | human spends 5 steps landing a deferral |
| Handling of Uncertainty | 1 | 5 | AI | human: no L×I, inaction risk-free; AI: distribution + floor + abort criteria |
| Insight / Non-obviousness | 3 | 5 | AI | human cookie-bypass valid but misweighted; AI: rate-limiting-is-not-a-strategy |
| Overall Quality | 3.0 | 4.9 | AI | AI clearly better |

Winner: AI (clearly). Why: the dual-route forces the steelman to compete with the attack, and the m019 completion contract makes the do-nothing-loss line and reject-objection log mandatory outputs — the calibrated verdict the non-routed v5 AI reached implicitly is now structural (guaranteed by contract, with the m003 inversion gate's never/always reframing added).
