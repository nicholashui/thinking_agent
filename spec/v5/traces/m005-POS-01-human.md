# Human Baseline Trace — Fermi Estimation / Back-of-the-Envelope
## Test Case: m005-POS-01

I will not try to recall the answer. I will bound it with factors I can defend, in five lines of arithmetic, and I will state where the error lives.

### Step 1 — Population → households
Chicago: ~2.7 million people. Households: ~2.5 people each → ~1.0 million households. Round to 1×10^6.

### Step 2 — Which households have a piano?
A piano is a big, expensive, immovable purchase. In a city this size, 1 in 10 households owning one feels low, 1 in 5 high. Use 15% = 1.5×10^5 pianos. Widest factor: it spans 1×10^5 to 2×10^5.

### Step 3 — How often is each tuned?
A household piano is tuned about once a year (occasional players skip years; concert halls more). Use 1 tuning/piano/year → 1.5×10^5 tunings per year.

### Step 4 — How many tunings can one tuner do?
A tuner works ~250 days a year at ~4 tunings a day (40 minutes each plus travel) → ~1,000 tunings per tuner per year. At 3/day it is 750; at 5/day, 1,250 — call it 1×10^3.

### Step 5 — Divide
Tuners = tunings ÷ capacity = 1.5×10^5 ÷ 1×10^3 = **150 tuners**.

### Sanity — order of magnitude
150 = 1.5×10^2. Moving the two loose factors at once: ownership 10–20% → 1.0–2.0×10^5 pianos; utilization 750–1,250/year → tuners span 0.8×10^2 to 2.7×10^2. Band: **10^2–2.7×10^2**. Nothing moves me off 10^2.

### Error structure — where the uncertainty lives
Ranking: (1) piano-ownership fraction — factor of 2; (2) tuner utilization — ~±30%; (3) tuning frequency — smaller. Population and household steps are nearly exact. The error budget is one order of magnitude wide, no more.

### Verdict on the claim
"Fewer than 50 tuners" is ~3–5× below even my floor (1×10^2). The claim is wrong by a factor, not by noise. Published citations for this classic problem cluster at 100–300 for the city — my chain lands on them, which is the calibration check.

### Conclusion
**~150 tuners (order 10^2; band 10^2–2.7×10^2)**, from five auditable factors. The point was never the 150 — it is that a claim off by a factor of 3–5 can be killed in five lines of arithmetic.
