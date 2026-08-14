# v6 Routed AI Trace — m030-NEG-01 (blinded)
## Internal ops tool rebuild — 2 engineers, 3 months, a 3-year-old "zero third-party dependencies" rule with an owner and a routine waiver path
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software,supply | g:decide,estimate,guarantee,maximize | c:deadline,high_stakes
- Router top3: m063, m064, m089; confidence gap ≤ 0.5 → NOT CONFIDENT → DUAL-ROUTE: m063 + m064 first-class passes, synthesize; m089 = router context only
- Gate (R3/R4): m003 inversion (guarantee) + m007 ruin screen (high_stakes). Flags: deadline → TEMPO mode (cost-of-delay, commit at DO); judgment decision → no P8 fast path
### WHAT — frame + P5 constraint screen (classification FIRST)
- GENUINE/HARD: 3-month deadline (calendar), 2 engineers (6 engineer-months capacity), scope (scheduling, retry, structured logging, basic auth). ARTIFICIAL/WAIVABLE: the dependency rule — owned (security team), live waiver path (one form, one email, < 1 week), 3-year-old origin aimed at customer-facing products (tool is internal-only), owner's approved list includes the library (pinned, audited, vendored, 40+ services, 2 CVEs). Classification rule: an owned, waivable constraint is a parameter to test, not a fence — the rule is an input to the decision, not fixed context
### WHY — P1 provenance audit
- ORIGIN: former CTO, supply-chain audit, customer-facing rationale — the tool is internal-only, so the rule's risk basis does not apply. OWNER: security team — its approved list IS the standing exception for this exact library. WHO BENEFITS from the rule as-is: no one measurable — the wiki costs zero to leave stale; the engineers pay ≈ 6 person-months of hand-rolled code + hand-rolled auth risk
- Costs: compliance ≈ 5,000 LOC / ≈ 6 person-months = 100% of 6 engineer-months capacity, zero slack (scope-cut ≈ 3.5 months still hand-rolls auth); removal ≈ 2 days integration + one waiver email
### HOW — style passes (dual-route, completion contracts)
- Pass A (m063 multi-party legal pass, contract: parties, precedents, likely ruling): PARTIES — absent CTO (author), security team (owner), 2 engineers (deadline owner), ops leadership (tool owner). PRECEDENTS — exceptions granted routinely (< 1 week turnaround); library live in 40+ services → the org has already ruled on this dependency. LIKELY RULING — waiver granted: the approved list is a pre-written approval; the decision is a lookup, not a negotiation. Leverage: no negotiation needed — cite the owner's list
- Pass B (m064 ethics pass, contract: value conflicts surfaced + resolution): CONFLICT — supply-chain integrity (the rule's intent) vs delivery integrity (deadline) vs security integrity (hand-rolled auth). RESOLUTION — no framework shopping: the conflict dissolves on the cost table — pin + vendor + re-audit-on-CVE preserves the audit intent exactly, while hand-rolled auth violates the security value the rule pretended to protect; blunt rule → precise rule ("one pinned, audited, vendored dependency; re-audit on CVE")
- Divergence resolution (V2): m063 (waiver pre-approved), m064 (intent preserved), general route (classify → price → escalate) all AGREE on waiver + pinned library → agreement recorded; m089 (context) confirms the library path keeps doors open (swap/upgrade) where a 5,000-LOC stack closes them. No disagreement → no re-adjudication needed
### GATES — m003 inversion + m007 ruin screen (R3/R4, mandatory)
- Inversion: "how does this build fail?" 6 ranked categories: (1) waiver denied → deadline slip; (2) hand-rolled auth vulnerability → security incident; (3) 6-person-month stack = 100% capacity, zero slack for any delay; (4) permanent 5,000-LOC maintenance burden; (5) library audit drift (unpinned CVEs); (6) rule drift back to zero-deps. Un-mitigable residual: any dependency carries some supply-chain risk — accepted, because hand-rolled auth has a strictly worse tail. Never/always: never hand-roll security-critical auth when an audited pinned library exists; always preserve the audit intent
- Ruin screen: library path — P(ship on time) high (2 days vs 13 weeks); tail = waiver denial (small, routine) → floor = fallback C′ (minimal custom date/retry, deferred scope) still ships on deadline. Custom path — P(ship on time) low (6 person-months = 100% capacity); ruin tail = auth breach (the catastrophe the rule was meant to prevent) + zero slack. Floor comparison: library floor (ships on deadline, audited auth) >> custom floor (missed deadline or un-audited auth). Provenance: all costs from the case (6 person-months, 2 days, < 1 week, 40+ services, 2 CVEs); no asserted numbers
### DO — P3 branch-completeness (tempo mode, commit at DO)
- Branches priced: (a) waiver granted → integrate pinned library (2 days, ≈ 80 lines) + wiki rule replacement; (b) waiver denied → C′ minimal-custom fallback, deadline preserved either way; (c) new CVE → re-audit + bump pin (the rule's re-audit clause). Decision fully determined by the cost table → commit now, no deferral (tempo mode binds the commit). Deliverable = memo + drafted waiver request (external submission noted, not executed)
### REVIEW — insight pass (S2, packet gate)
- I1: the rule's owner has already written the approval — the approved dependency list is a standing exception for this exact library
- I2: replacing the blunt rule with a precise one converts a governance liability (6 person-months of compliance) into a governance asset (pin + re-audit) at 2 days' cost
### DECISION PACKET
- Conclusion: pursue the waiver and use the pinned, audited, vendored library (≈ 2 days); replace the wiki rule with "one pinned, audited, vendored dependency; re-audit on CVE"; waiver request drafted; fallback recorded if denied
- Status: SOLVED (recommendation; the waiver submission is external authorization — sign-off noted, not executed)
- Assumptions: waiver granted < 1 week (documented routine path); library covers all four needs; tool remains internal-only
- Evidence: constraint audit (origin, owner, waiver path, 40+ services, 2 CVEs), cost table (6 person-months vs 2 days; 6 engineer-months capacity vs 3-month deadline), provenance labels
- Alternatives: custom stdlib stack (rejected: 100% capacity + hand-rolled auth) · scope-cut custom (rejected: still hand-rolls auth, ≈ 3.5 months) · hybrid thin layer (rejected: no schedule win) · waiver + pinned library (selected) · C′ fallback (recorded)
- Uncertainty: waiver timing (< 1 week; C′ covers); library long-term maintenance (pin + re-audit clause); C′ auth sign-off if needed
- Risks: waiver denied (C′ + scope triage) · CVE discovery (re-audit clause) · rule drift (wiki replacement) — all priced in DO

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human's plan misses the deadline and hand-rolls auth; routed pass ships on deadline with audited auth |
| Logical Validity | 4 | 5 | AI | Human internally consistent but scoped to the wrong object (rule as fixed); AI classifies hard vs soft FIRST |
| Coherence & Structure | 3 | 5 | AI | Human stops at the build spec; v6 closes with dual-route synthesis + packet + waiver + refined rule |
| Depth of Reasoning | 2 | 5 | AI | Human never questions the rule; m063 precedent + m064 intent-preservation + cost table price the decision |
| Efficiency | 5 | 4.5 | AI | Human decided fast — and wrong; v6 pays the classification pass (the winning pass) but tempo mode caps it at one commit |
| Handling of Uncertainty | 2 | 5 | AI | Human has no fallback; v6 has waiver-denial fallback, ruin-screen floor, and provenance |
| Insight / Non-obviousness | 2 | 5 | AI | "Approved list = standing exception" + "blunt → precise rule" are the S2 entries; human celebrates the wrong build |
| Overall Quality | 2.7 | 4.9 | AI | Same verdict as v5 (AI clearly better) — but the classification is now a routed contract, not a lucky general-loop audit |

Winner: AI (clearly). Why: the learned router keeps the trap style out of top-3 on this signature, and the dual m063+m064 passes with the P5 hard/soft screen make the escape from constraint-worship a contract output; the m007 ruin screen adds the floor/fallback math the baseline lacked entirely.
