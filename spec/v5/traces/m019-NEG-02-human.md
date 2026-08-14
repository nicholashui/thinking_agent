# Human Baseline Trace — redteaming-NEG-01
**Model**: Red Teaming / Devil's Advocate (strict)
**Case**: Aegis Bank — Atlas settlement-platform migration, go/no-go review
**Task**: Stress-test the go-live decision; render verdict.

---

## 0. Stance

My job: find why Atlas fails. A bank's settlement engine is the last place for optimism. If I cannot name a scenario in which this goes wrong, I have not thought hard enough. Every finding below is real and must be closed before I sign anything. "Mostly worked in shadow mode" is not "works in production."

## 1. Attack: the evidence, adversarially

- Shadow mode ≠ production. Shadow runs observe; they do not operate. Reconcile checks were run by the same team, on the same code, with the same biases. Four weeks of zero discrepancies may mean the checks are blind, not that the system is correct.
- The SLA is "99.95% of batches"; p99.9 is 1.4× over target. The tail is where banks die. An untested tail is a finding.
- One P3 audit finding remains OPEN (logging verbosity in the operator UI). "P3" is an audit's way of saying "we noticed something." In a settlement system, unreadable logs are an incident waiting to happen. Close it before go-live.
- Rollback was tested twice by the team that built the system. Tested by the authors is an opinion, not a test.

## 2. Attack: the new platform's risk surface (every objection, full severity)

- **Cloud-provider dependency**: a region-wide outage on day one of settlement stops money movement across 4M customers. Is there a second provider? No. Finding: HIGH.
- **Canary corruption**: the 5% canary shares the ledger schema with the migration pipeline; a canary-time schema drift would corrupt shared state *and* poison the rollback. Finding: HIGH.
- **Config typo**: one fatigued engineer, one bad flag, one Tuesday. "Approvals" are paper; failures are real. Finding: HIGH.
- **Migration data drift**: shadow showed 4 weeks of parity, but the mainframe dataset holds 15 years of history. Year-15 edge cases were never exercised. Finding: HIGH.
- **Third-party API changes**: the new platform's dependencies ship breaking changes on their schedule, not ours. Finding: HIGH.
- **Insider threat**: an admin with the new console can alter settlements with none of the mainframe-era controls. Privilege escalation in the old system is a CVE; in the new system it is a design. Finding: HIGH.
- **Leap-second handling (2032)**: a known class of datetime-library bug, unverified on Atlas. Finding: HIGH — must be closed before go-live regardless of the calendar.
- Collectively: this review has zero confidence to sign a go-live in 3 weeks.

## 3. The status quo, for completeness

- Vendor EOL is 6 months out. The two critical CVEs are real but *theoretical*: no exploitation in the wild, and the mainframe has run settlement for 15 years without an incident.
- Six months is plenty to revisit this decision. A delayed migration is strictly safer than an untested one. The mainframe risk is known and manageable; the Atlas risk is unknown and unquantified.

## 4. Verdict

**Delay the go-live. Do not sign.** Close every finding above — including the P3 and the p99.9 tail, add a second independent security review of the Atlas console — then run 12 more weeks of shadow with *adversarially seeded* errors, and re-present. The cost of being wrong on a bank's settlement engine is not payable in dollars; the cost of delay is a schedule, and we have a schedule. We have time.

## 5. Trace notes (self-audit)

The attack was thorough, and every objection was recorded as HIGH severity — with no likelihood assigned and no cost-to-mitigate computed. Note what this review did NOT do: it never compared the residual risk of go-live against the residual risk of staying on a mainframe with two unpatched critical CVEs past vendor EOL; it never asked whether its own bar ("zero residual risk") is achievable, or whether delay itself carries risk; it treated 6 months as unlimited runway and "theoretical" CVEs as if they could not become real. The frame — attack the new thing, trust the old thing — was never challenged.
