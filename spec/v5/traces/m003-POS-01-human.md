# Human Baseline — m003-POS-01
**Human Thinking Model**: Inversion ("invert, always invert") — strict, pure application.
**Prompt contract**: Reason ONLY in the Inversion style. Full visible trace. Task: "A customer must NEVER be double-charged for a single order. Make sure of it." Deliverable: reliability strategy for the checkout rewrite's money path.

---

## Trace

**Step 1 — State the goal.**
Guarantee that no customer is ever double-charged, across the new checkout, shipping in 6 weeks. The goal is stated as a positive guarantee; per the method, I invert before designing anything.

**Step 2 — INVERT.**
The inverted question: *How do we make absolutely sure a customer IS double-charged for a single order?* Every enumerated way to guarantee the bad outcome is a required line of defense. I enumerate thoroughly and refuse to stop early.

**Step 3 — Enumerate: all the ways to guarantee a double charge.**
1. *Network/retry*: a provider timeout is treated as failure; the client retries; both the original and the retry succeed — two authorizations for one order. Ambiguous timeout responses are the classic cause.
2. *Idempotency*: no idempotency key, keys reused across checkout sessions, or keys evicted from cache so the retry looks new.
3. *Auth–capture race*: authorization succeeds but the response is slow; the capture command fires twice (double-click, parallel tabs, replay of the capture).
4. *Webhook redelivery*: provider re-delivers `charge.succeeded`; the handler runs the completion path twice — double capture, double fulfillment.
5. *Human ops*: an operator manually re-enters a payment the system marked "failed" that actually succeeded; the refund desk re-issues a refund already processed.
6. *Provider failover*: multi-provider routing submits one order to two providers on an ambiguous failover decision.
7. *Refund cascade*: partial refunds, chargebacks, and refund retries compound; the balance check races and issues a duplicate refund line.
8. *Ledger/rounding*: currency conversion and decimal rounding on splits mint a duplicate line in the ledger that reconciles as a second charge.

**Step 4 — Rank by likelihood × impact.**
(2) idempotency keys > (1) retry/timeout ambiguity > (4) webhook redelivery > (3) auth–capture race > (5) human ops > (7) refund cascade > (8) ledger/rounding > (6) provider failover. The top five are the design's spine.

**Step 5 — Design against each (prevent / detect / respond).**
1. Retry policy: no blind retries on ambiguous results; retries carry idempotency keys and are exponential with jitter. 2. Idempotency: per-session nonce, storage-level dedupe (unique constraint, not cache), keys immutable for session lifetime. 3. Capture-once: capture command is idempotent against a ledger-state precondition — the second capture fails deterministically. 4. Webhooks: event-id journal with dedupe; completion path is a state machine that cannot run twice. 5. Ops: two-person verification for any manual re-entry or refund; every manual action is a logged, versioned transaction. 6–8 (detect): real-time double-charge detector on the ledger (two captured lines, one order key) that auto-quarantines and auto-refunds within 24h; daily reconciliation with mismatch paging.

**Step 6 — Handle "NEVER" honestly (the method's honesty move).**
Absolute zero is unattainable: there is a failure domain outside our stack — provider-side duplicates beyond our API, merchant-side duplicate card entry. So "never" is reframed as: *≤1 double-charge per 1,000,000 payment sessions*, with defense-in-depth, and a guaranteed detect-and-remediate loop (auto-refund ≤24h, customer notification SLA) for the un-mitigable residual. The guarantee is enforceable only because the invariant is continuously monitored, not because prevention is total.

**Step 7 — Verdict on the method here.**
Inversion is near-necessary for this problem class: the inverted question generated 8 distinct categories in one pass, ranked, with a P/D/R mapping and an explicit residual. The completeness is the product — a mitigation-first answer ("add idempotency, add retries") would miss categories 5–8.
