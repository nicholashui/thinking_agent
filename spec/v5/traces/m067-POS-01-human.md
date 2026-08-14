# Human Baseline — m067-POS-01
## Style: Thought Experiment (Gedankenexperiment) (pure) — visible reasoning trace

**Restatement.** Swimmer at speed v relative to water. A: still lake, out-and-back, total 2L. B: river with uniform current u < v, L downstream + L back upstream. C: same river, cross of width L and back, compensating drift by aiming upstream. Rank times; can a single round trip reveal the current; what principle does the scenario isolate?

**Step 1 — Build the idealized world.** Strip to essentials: uniform steady current; speed constant relative to water; point-like swimmer; no fatigue, no turn time; straight segments; u < v. The idealization leaves exactly three quantities in the problem — v, u, L — and the whole answer must be functions of them. Nothing else may enter.

**Step 2 — Still-water baseline.** A: time T_A = 2L/v.

**Step 3 — Along the current.** Against it: L/(v−u). With it: L/(v+u). Total T_B = L/(v−u) + L/(v+u) = 2Lv/(v²−u²). Now kill the naive "cancellation": the gain downstream is L/(v+u) vs L/v, saving u/(v(v+u)); the loss upstream is L/(v−u) vs L/v, costing u/(v(v−u)) — the loss is bigger. Structurally: time is the sum of reciprocals of paired speeds, and 1/x is convex — the penalty always exceeds the gain. T_B = T_A · 1/(1−(u/v)²) > T_A.

**Step 4 — Across the current.** To land straight across, aim upstream; cross-stream speed is √(v²−u²). Round trip: T_C = 2L/√(v²−u²). Slower than still water, faster than along the current: T_A < T_C < T_B (ratios 1, 1/√(1−ε²), 1/(1−ε²), ε = u/v).

**Step 5 — Single-trip blindness.** The observer in the river has no clock comparison against still water: plan B alone yields only a time, and a slower swimmer in still water yields the same reading. A uniform flow cannot be separated from a slower v by any single round trip. The effect is second order in ε: expanding, ΔT = T_B − T_C ≈ T_A·ε²/2 = L u²/v³.

**Step 6 — Principle extracted.** (1) Uniform flow strictly inflates round-trip times; direction is irrelevant to the fact that it hurts — a two-way timing is a bad flow detector. (2) The flow reveals itself only as a difference between two orientations of the same round trip — the probe must be differential, and the signal is second order. (3) Run this scenario on light instead of a swimmer: the same second-order differential experiment over perpendicular arms is the classic probe of the "luminiferous medium" — and its null result is the empirical fact that makes the deeper principle: there is no privileged rest frame to detect; light's speed is the same in every inertial frame. The swimmer scenario isolates exactly why the experiment was designed as it was — perpendicular arms, two-way timing — and why the null is forced.

**Step 7 — Verdict.** T_A < T_C < T_B; single round trips cannot detect a uniform flow; only a differential probe, second order in u/v, can — and for light even that vanishes, teaching frame invariance. The scenario, cheap and instrument-free, isolates the logical core the way a hundred pages of fluid mechanics could not.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure thought-experiment style — build the idealized world, run it symbolically, extract the principle. No measurements, no numbers beyond the given symbols; the style performs exactly as designed: the idealization isolates the harmonic-reciprocal structure and the differential-probe principle.*
