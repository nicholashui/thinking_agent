# Human Baseline — m019-POS-01
## Style: Red Teaming / Devil's Advocate (pure) — visible reasoning trace

**Problem restatement.** Review "Operation First-Response": CSAT 68→88 via bonus-tied CSAT, 2 h auto-close, open-gated surveys, Helix migration, investor-newsletter publication. I treat the proposal as hostile — every line item is an attack surface.

**Step 1 — Attack the incentives.** Bonus (+15%) on CSAT ≥ 7/10, no response-rate floor: agents gain by (a) steering ratings ("I'll escalate that if you rate 7"), (b) cherry-picking easy tickets, (c) holding hard tickets past the month reset. The bonus converts the metric into a target — Goodhart in its purest form. Any agent can lift a score ~10–15 pts by steering 1 in 5 surveys; the headline "88" is manufactured.

**Step 2 — Attack the metrics.** Three defects. (a) Auto-close 2 h after first reply: default-resolved measures "didn't complain within 2 h", not resolution — real dissatisfaction never re-enters the measurement. (b) Survey only to email-openers: openers skew satisfied → selection bias, direction known, upward. (c) FRT ≤ 2 min met by bot auto-ack on creation — resolves nothing; the newsletter number is a vanity metric.

**Step 3 — Attack the security surface.** Worst line item in the plan. Ticket history = PII + payment-reference strings + password-reset tokens. The plan copies all of it to pre-SOC2 staging in week 1; staging has a public unauthenticated ticket-export endpoint; admin access is a shared vendor login; SSO absent until week 6; no DPIA; legal/DPO never consulted. A token leak is an account-takeover path; a breach triggers GDPR/CCPA notification. Fatal — in the plan's own text.

**Step 4 — Attack the stakeholders.** Unmodeled: (a) enterprise accounts' procurement/security teams run a 60–90-day vendor-risk review before approving any new portal — a 2-week go-live violates customer policy and will be blocked at the account level, killing the quarter; (b) agents carry double-system workload with no staffing plan → attrition; (c) legal/DPO (Step 3); (d) investors — the newsletter publishes an unvalidated, gaming-prone number: reputational and securities exposure.

**Step 5 — Rank and verdict.** Fatal: F4 (breach exposure), F3 (procurement timeline kills the program), F1/F2 (success metric invalid). Non-fatal if fixed: F5 (publication can be held). Verdict: do not proceed as written. Conditions: kill the auto-close default; survey the full population with a response-rate floor; decouple bonus from raw CSAT (QA-audited scores); DPIA + SSO + auth on Helix before any data copy; remove the export endpoint; consult procurement and legal; hold the newsletter until data validity is demonstrated.

**Trace summary box.** Five findings: F1 bonus gaming (steering, cherry-picking); F2 metric invalidity (auto-close + open-gated survey + bot FRT); F3 unmodeled stakeholders (60–90-day review vs 2-week go-live, agent workload, legal absent); F4 security/privacy (pre-SOC2 staging, unauth export, shared admin, no DPIA); F5 premature publication. Verdict: block as written; six conditions to proceed.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Red Teaming — attacks on assumptions, incentives, metrics, security, stakeholders; findings ranked by likelihood × impact; verdict with blockers. In this positive case the style performs exactly as designed: all five planted flaws found, ranked, converted into a conditional verdict.*
