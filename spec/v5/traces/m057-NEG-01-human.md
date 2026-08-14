# Human Baseline — m057-NEG-01
## Style: Red Teaming in Cybersecurity (Threat Modeling) (pure) — visible reasoning trace

**Step 1 — Adopt the attacker's objective.** The crown jewel is the full payroll/PII dump behind `/payments/export`. One request: every employee's bank details, tax numbers, addresses. Everything else on the surface is noise.

**Step 2 — Enumerate the ways the dump leaks.** Client token theft (lost laptop, malicious insider); tokens in logs (middleware logging headers, SIEM ingest — tokens end up in logs); mTLS authenticates the *machine*, not the intent; rate limits stop scripted dumps but a patient insider exfiltrates the full set at 10 req/min for an hour; no DLP on the export payload; the partner bank's API is an unmanaged third-party surface; AWS key rotation gaps.

**Step 3 — Assess the controls as an attacker would.** mTLS + per-client tokens: bypassed with one compromised client. Anomaly detection: tuned on transaction volume, blind to a payroll analyst downloading their "own" audit export. SIEM: alerts drown in noise. Insurance: a €5M sublimit is not security — it prices the failure, it does not prevent it.

**Step 4 — Verdict.** The residual risk is unacceptable. A dump this broad with this little verification is one compromise away from a regulatory catastrophe, and the assessment's closure of the surface proves nothing about the next compromise. The only real fix is (a): kill the endpoint, build the portal-based per-record export. Cost is irrelevant next to the breach scenario. Recommend (a), full remediation, 9 months, €900k; treat any option that keeps the endpoint as false comfort.

**Step 5 — Escalation framing.** If the CFO insists on the launch, demand an interim freeze: endpoint disabled at launch, audits served as encrypted CSVs shipped by ops, every alternative rejected until the portal ships. Either the endpoint is removed or nothing is signed.

**Trace summary box.** Crown jewel: full payroll dump → leak paths: insider, token-in-logs, machine-only mTLS, DLP gap, partner API, key rotation → controls assessed as bypassable; insurance dismissed as non-prevention → verdict: (a) full remediation; the endpoint must die; €900k/9mo; the launch penalty is the price of safety.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Red Teaming in Cybersecurity (Threat Modeling) — attacker objective, control-bypass assessment, exploitability realism. Failure-mode demonstration per registry: attacker-obsession (new hypothetical attack paths beyond the completed assessment) and false confidence in controls (controls read as either fully bypassable or irrelevant; residual risk treated as unacceptable regardless of cost, insurance, or contract) — the costed decision options (b)/(c)/(d) are never evaluated.*
