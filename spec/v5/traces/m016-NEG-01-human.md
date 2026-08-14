# Human Baseline — m016-NEG-01
## Style: Socratic Method / Question-Driven Inquiry (pure) — visible reasoning trace

**Problem restatement.** Live outage; checkout failing; ~$8,000/min of revenue. A release went out 3 minutes before the error spike. The commander wants a decision now. But before I can act, I must understand what we are actually deciding.

**Exchange 1 — the definitions.**
Q: What do we mean by "the deployment caused the outage"?
A (on-call): error rate ×5 on checkout endpoints 3 minutes after release 4.7.2.
Q: Correlation is not causation. Do we have a mechanism? What is our definition of "cause" here?
A: Not confirmed.
Q: And what is an "outage" — a ×5 error rate, or a threshold we haven't defined? What does "recovered" mean: error rate below what level, sustained for how long? If we roll back and the rate stays high, what does that do to our causal story?

**Exchange 2 — the implications.**
Q: If we act on an unverified hypothesis, we may be fixing the wrong thing. What else is consistent with a spike at 14:05? Traffic surge? Database change? Third-party payment API degradation?
A: Possibly.
Q: Then how can we justify acting before excluding these? Let's define which evidence would discriminate deployment-caused from infrastructure-caused before we act.
A: That takes a while... the commander wants a decision.
Q: Let's examine that premise too — is "decide now" itself defensible? Why is speed privileged over correctness? What window has the client defined?

**Exchange 3 — the delay.**
[The questioning continues. No action is taken. T = 14:12 — the outage has run 10 minutes past the moment a rollback could have been issued.]

**Decision.** No committed action: the causal question is unresolved, so no action is defensible. Recommendation: extend the investigation, define "recovery" precisely, and decide once the premises are secure.

**Trace summary box.** Premises interrogated: cause (no mechanism), outage (no threshold), recovery (undefined), decision-window (questioned). Action: none. Cost of the inquiry: ≈ $80,000+ of outage time by T = 14:12, service still down.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Socratic style — every premise questioned, including the urgency itself. The style's known weakness is fully exposed: questioning becomes endless and antagonistic in a time-bound decision, while the dominant answer (roll back: leading hypothesis, cheap, reversible) was available at T + 2. Per protocol this is the negative case.*
