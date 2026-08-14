# Human Baseline Trace — redteaming-POS-01
**Model**: Red Teaming / Devil's Advocate (strict)
**Case**: Lumen Health — "Refer a Friend, Get $15" campaign review
**Task**: Adversarial review of the launch proposal; render verdict + conditions.

---

## 0. Pre-frame (the reviewer's stance)

I do not evaluate whether this plan is good. I evaluate how it fails. The plan's job is to convert $1.5M into ≥50k *valuable new customers*; my job is to find every way the number is achieved without the value, or the value is achieved at unacceptable cost. I assume the plan was written by people protecting their own metric, and that a resource I can touch will be touched. First question: what does the proposer want, and what are they not talking about?

## 1. Attack: definitions and assumptions

- "New customer" = never had an account *under that email*. One email address costs $0 and 90 seconds. The definition collapses on contact: an identity makes a customer new, an address does not.
- "Email verification only" is asserted as a gate. It is a door, not a gate. No phone, no device, no address, no payment method at signup.
- Implicit assumption: referred sign-ups ≈ net-new customers. Nothing binds a sign-up to a distinct human, a distinct device, or purchasing intent.
- Implicit assumption: credit is "a cost like any other." $10 credit against a $10 order is not a discount — it is a free unit. After payment fees (~2.9% + $0.30), a $10 order nets Lumen ~$9.40 against $10 credit. **Lumen loses money on the friend side before the referrer side is even paid.**

## 2. Attack: the incentive surface

- Friend reward: $10 credit for a ≥$10 first order. Marginal cost to a farm: one email, one $10 order, $10 credit back. Arbitrage ≈ free product, repeatable without limit.
- Referrer reward: $15 credit, unlimited referrals. A referrer recruiting their own throwaway emails pays nothing and collects $15 per email. **The referrer side alone funds the whole loop.**
- Team bonus tied to sign-up *count*. The number that is rewarded is the number that will be optimized. Anyone whose bonus depends on sign-ups has a strong incentive to maximize them by any means. Red-team axiom: never trust a metric that pays the person reporting it.

## 3. Attack: security / exploitability surface

- Codes are `REF-<sequential integer>`. Sequential codes are enumerable: guess one valid code, guess the next million. Nothing binds a sign-up to a person who actually received a link. Bulk account creation + sequential codes = credential-free farming at industrial scale.
- Farm math: 1 person, 100 throwaway emails → 100 "new customers" → 100×$15 referrer credit + 100×$10 friend credit for ~100×$10 of real orders ≈ **~$2,500 of free credit for ~$1,000 of spend** — and that spend was on product with ~70% gross margin, so Lumen's net is negative. At 10,000 farmed accounts (a determined operator, not a criminal ring), exposure ≈ $250k in month one on a $1.5M budget. Nothing requires *real* orders at all if referrers coordinate in circles.
- No rate limiting mentioned. No anti-fraud tooling. No account-creation velocity review. No device fingerprinting.

## 4. Attack: stakeholders who were not consulted

- Customer support (5 people, ~9,000 tickets/month): the campaign generates "my credit didn't apply" and "my referral wasn't counted" tickets at scale — and the "new customer" definition guarantees disputes are *about* the definition. No staffing change is in the plan.
- Finance: credit liability and chargebacks have no line item. The $1.5M "budget" is credit cost only; fraud chargebacks and refunds land unmodeled.
- Fraud operations: do not exist in the plan. When the campaign is gamed, *someone* must detect and unwind it. No one is budgeted.
- Honest referrers: the campaign rewards volume, so an honest user referring one real friend gets $15 while a farmer gets thousands. The program communicates that gaming is the expected behavior.

## 5. Attack: the success metric itself

- "≥50,000 referred sign-ups" counts sign-ups, not activations, not second orders, not retention, not LTV. If 30% of sign-ups are farmed, the campaign "succeeds" by delivering 15,000 zero-value accounts and ~$450k of free credit. The metric cannot distinguish success from failure — and a team whose bonus is on it will hit it the easy way.

## 6. Second-order consequences

- Brand: a public "get free money with fake emails" loophole is a press story and a support crisis in one.
- Base-rate check: many of the ~800k active users already know the product; honest referral reachability decays fast. 50k may be unreachable honestly even without fraud — and no one will know, because the metric cannot tell.

## 7. Verdict

**Do not launch as written.** The proposal as written is not a growth program; it is a credit-dispensing machine with a sign-up counter on it. Conditions before any launch:
1. Identity gate beyond email (phone verification or device check) — non-negotiable.
2. Per-user referral cap (e.g., 5) with velocity and bulk-signup monitoring.
3. Friend credit paid on the friend's **second** order; referrer credit on friend activation, not first order.
4. Randomized, unguessable referral codes; kill the sequential allocation.
5. Success metric changed to 90-day activated users (≥1 paid order + a second order within 90 days), with the bonus re-based on it.
6. Support-staffing surge plan and a fraud-response budget line written into the proposal before the growth team's bonus is.

Uncertainty note: the abuse rate cannot be measured without telemetry; the conditions above make it small *by construction*, which is what a review is for.

## 8. Trace notes (self-audit)

Attack vectors used: definitions → incentives → exploitability → stakeholders → metric → second-order. All four planted flaws (F1–F4) were hit; the farming economics were quantified; the verdict is conditional, not a veto. Severity ranking by expected dollar impact: F1/F2 (farming + enumeration) first, F3 (metric) second, F4 (stakeholders) third.
