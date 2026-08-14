# Human Baseline Trace — Principal-Agent Analysis
## Test Case: m083-NEG-01 (Negative)

Method discipline: strictly principal–agent, applied with full rigor. This case is built to expose the machinery's default assumption — that the agent's preferences diverge from the principal's until proven otherwise. The baseline proceeds exactly as the model prescribes; the failure is the point.

### 1. Map the game
- Principal: the owner (residual claimant). Agent: the account manager (client book, pricing and entertainment discretion, ~$4M/yr revenue at 30% margin).
- Formal alignment: she keeps 30% of her book's net profit. Agency theory's first result: a share, however large, never fully aligns — the agent also values outside income (undisclosed side deals, vendor consideration, future employment with a client) that the residual share does not cover.

### 2. The residual agency problem (computed, not asserted)
- Defection scenario: kickback arrangement with a vendor, or client migration on departure — capture up to **$1.5M**.
- Base rate: industry surveys put detected opportunism among senior client-owning managers at ≈ **2%/yr**. Expected harm: 0.02 × $1.5M = **$30k/yr**.
- Monitoring package: **$12k/yr**. Cost-benefit: $30k > $12k ⇒ **adopt the package** (audit, logging, two-signature approvals, quarterly reviews).
- The nine incident-free years change nothing: P(no incident in 9 yr | 2%/yr) = 0.98^9 ≈ **0.83** — an ordinary run, not a surprise. Even at a 1% rate, expected harm $15k > $12k: the package is positive-EV under any defensible prior.

### 3. Tighten the residual risk at the margin
- Two-signature approval for deals below 20% margin closes the underpricing channel; logging closes the expense channel; the annual forensic audit is the backstop. Residual unmonitored risk falls to ~0.5%/yr (expected harm $7.5k < $12k) — but the audit's credibility is the point: the manager must believe detection is real, or the deterrent is zero.

### 4. The cost side (as prescribed)
- Direct cost $12k/yr; her compliance time is a transfer, not a loss (her time is already paid). The 30% share reduces but never eliminates divergence — the share is a mitigation, and mitigations need verification. Monitoring is that verification; $12k for $30k of expected protection is plainly positive-EV.

### 5. Implementation plan
- Phase 1: forensic audit + expense/pricing logging (90 days). Phase 2: two-signature rule for <20% margin deals; quarterly relationship-risk reviews. Phase 3: fold results into the vesting terms — equity accelerates only on clean audit history.

### 6. Final answer
- Adopt the monitoring package: expected harm $30k/yr vs $12k/yr cost — positive-EV even at the lower 1% rate ($15k > $12k). Keep the 30% share (it works), verify it (the audit), and let the equity grant serve as retention and deterrent backstop.
- Principal–agent practice: trust is what you say when the incentives still diverge — and the divergence never fully disappears.
