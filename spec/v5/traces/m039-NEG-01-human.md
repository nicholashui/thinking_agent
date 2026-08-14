# Human Baseline Trace — Asymmetric Upside / Barbell Strategy
## Test Case: m039-NEG-01 (Negative)

Method discipline: strict pure barbell — classify any symmetric "middle" bet as the forbidden category FIRST, then build safe core + convex tail, and only then price. Structure before arithmetic.

### 1. Classify the candidates
The bond ladder is exactly the middle: an average, symmetric bet on credit — +6.2% most of the time with a 0.3% downside. No convexity anywhere in its payoff; it is a linear claim with a small print tail. That is the forbidden category.
The barbell shape is available: safe core + optional convex tail. The choice is obvious on structure alone.

### 2. Price the middle (to know what we are declining)
EV(M) = 0.997·124,000 − 0.003·300,000 = 123,628 − 900 = $122,728 (+6.14%).
Decline anyway. The 0.3% × 15% credit event is a fat tail the ladder does not hedge — the investor is short that tail by holding it. Barbell rule: never carry someone else's credit tail on a symmetric claim.

### 3. Build the barbell
Core: 85% T-bills at 4.5% → +$76,500, guaranteed floor.
Tail: 15% ($300k) structured note on OTM index calls — 90% → $0, 10% → 5× (+$1.2M). True asymmetry: the core never loses, the tail can only lose its 15%.

### 4. Verify the preconditions (barbell only works if they hold)
(1) Tail optional: one premium in, capped at the $300k — the note's loss is capped at 15%. Optionality intact.
(2) Convexity: markets are sometimes expensive; but optionality is about being long the tail when it pays, not about spot pricing. The 10% × 5× is what the tail is for. If it were fair-priced, there would be no opportunity.
(3) Survivability: worst case −15% if the tail dies; that is within the 20% pain cap. Structure is sound.

### 5. Price the barbell
Tail slot EV = 0.90·(−300,000) + 0.10·(+1,200,000) = −270,000 + 120,000 = −$150,000 (−50% on the slot). Negative — expected, for convexity; premium is the price of the lottery ticket, and the 10% branch is what we are actually buying.
EV(B) = 0.90·(−223,500) + 0.10·(+1,276,500) = −201,150 + 127,650 = −$73,500 (−3.7%).
Negative EV, but EV is the EV purist's metric — the barbell is not priced on EV, it is priced on skew: 90% of years the portfolio is roughly flat (core intact), and the 10% branch pays 5×. The ladder pays a small, sure amount that the family office does not need; the tail is the only interesting risk here.

### 6. The follow-on clause
Year-2 contribution of $200k: voluntary top-up to keep the 5× alive. If the family office has the cash, it contributes; the alternative (1.2× cap) is worse in the state where the index is up. The 5× remains the relevant payoff. The tail's true exposure is $500k if they contribute and the trade goes wrong — still a bounded, survivable 25%. Optionality survives the clause.

### 7. Decision
Take B: 85% core + 15% tail. Reject the ladder's symmetric certainty; own the convex tail.

### 8. Final answer
EV(B) = −$73,500 but positive skew and bounded; EV(M) = +$122,728 rejected on structure (symmetric middle, unhedged credit tail). Allocation 85/15.
