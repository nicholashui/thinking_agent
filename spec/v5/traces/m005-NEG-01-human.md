# Human Baseline Trace — Fermi Estimation / Back-of-the-Envelope
## Test Case: m005-NEG-01

Volume is the easy half. Water content is the whole problem. I will show my work including the wrong path, because that path is exactly what this style does to you.

### Step 1 — Volume (safe)
A fair-weather cumulus is roughly a cube: ~1 km × 1 km × 1 km ≈ 1×10^9 m³.

### Step 2 — The factor (dangerous)
A cloud is water. Water's density I know cold: 1,000 kg/m³. Multiply: 1×10^9 m³ × 1,000 kg/m³ = **1×10^12 kg**. One trillion kilograms. The arithmetic feels fine.

### Step 3 — Calibration against the world (the catch)
Check what that number means. The same cloud raining 5 mm over its 1 km² footprint deposits 5×10^3 m³ = 5×10^6 kg of water — the total a heavy shower delivers. If the cloud held 1×10^12 kg, it would last 2×10^5 such showers, and it rains within hours. A 1,000-meter-deep water column over its footprint is a lake, not a cloud. The number is absurd by ~6 orders.

### Step 4 — Correct factor
The error is the factor: cloud air carries liquid water as droplets at ~0.3–1 g/m³ (liquid water content), not 1,000 kg/m³ — off by 10^6. Recompute: 1×10^9 m³ × 0.5 g/m³ = 5×10^8 g = **5×10^5 kg = 500 metric tons**.

### Step 5 — Sanity vs published
Published figures for a typical cumulus: ~500 metric tons (~1.1 million pounds). My corrected chain lands on it. The naive chain was wrong by a factor of 10^6 — and it felt fine while I was doing it, which is the point.

### Honest verdict on the method
This case exposes exactly where back-of-envelope breaks: the arithmetic is never the danger, the factor is. Liquid water content is not derivable from first principles; it is a domain fact I either know or don't. If I don't know it, the honest Fermi output is parameterized — "X g/m³ × 1×10^9 m³" — with a band spanning X's range (3×10^5–1×10^6 kg), not a confident number. Precision without factor validity is the illusion this style produces.

### Conclusion
**≈5×10^5 kg (500 t; band 3×10^5–1×10^6)**. And the lesson: five correct lines of arithmetic can certify a factor that is wrong by six orders of magnitude.
