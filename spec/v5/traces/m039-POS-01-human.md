# Human Baseline Trace — Asymmetric Upside / Barbell Strategy
## Test Case: m039-POS-01 (Positive)

Method discipline: strict pure barbell — classify any symmetric/negative-skew "middle" bet as the forbidden category FIRST, then build safe core + convex tail, and only then price. Structure before arithmetic.

### 1. Classify the candidates
M is the classic middle bet: frequent small gains, rare large loss (96% / −30%). Negative skew with a 4% tail — this is the ruin class. Barbell rule: never sit in the middle; only a safe core plus an optional convex tail is allowed.

### 2. Price the middle (to know what we are declining)
EV(M) = 0.96·72,000 − 0.04·300,000 = 69,120 − 12,000 = $57,120 (+5.71%).
Decline anyway: EV is the wrong lens for negative skew. The 4% × 30% drawdown is the cost of the "income" — a single shock erases 5+ years of it. Ruin avoidance beats EV maximization.

### 3. Build the barbell
Core: 92% T-bills at 4.5% → +$41,400, guaranteed. This covers the floor; no path loses money.
Tail: 8% deep OTM index calls — capped loss $80,000, no margin, no roll, no follow-on. Optionality verified: one premium, done.

### 4. Verify the preconditions (barbell only works if they hold)
(1) Tail genuinely optional: capped, no follow-on obligations — yes, contract-clean.
(2) Convexity cheap: forced sellers (quarter-end de-risking, income-product demand) ⇒ premium ≈ 60% of fair value — yes, tail-friendliness confirmed before sizing.
(3) Tail loss survivable: 8% of capital, worst case +4.1% total. Pain cap is 10%; 8% < 10% — sized correctly. Never bet the floor.

### 5. Price the barbell
Tail slot EV = 0.70·0 + 0.25·160,000 + 0.05·720,000 = 40,000 + 36,000 = $76,000 on $80,000 (+95% on the slot; the forced-seller discount is doing real work).
EV(B) = 41,400 + 76,000 = $117,400 (+11.74%) — double the middle's EV.

### 6. Skew-correct ranking
Worst case: B = +$41,400 vs M = −$300,000. P(loss > 20%): 0% vs 4%. B dominates on EV, worst case, and ruin simultaneously.
Trap: SD(B) ≈ $162.9k vs SD(M) ≈ $72.9k — variance says M is "safer." Variance is a symmetric measure on asymmetric payoffs: it punishes B for its upside surprise and rewards M for never moving except to lose. Correct metrics: worst case, ruin probability, downside deviation, skew.

### 7. Decision
Take B: 92% core + 8% tail. EV +11.74%, zero ruin, positive skew — and the middle, whatever its EV, is declined on structure.

### 8. Final answer
EV(B) = $117,400 vs EV(M) = $57,120; worst case +$41,400 vs −$300,000; P(loss>20%) 0% vs 4%; SD trap explained (variance mis-ranks skew); preconditions verified (cheap, optional, survivable); allocation 92/8.
