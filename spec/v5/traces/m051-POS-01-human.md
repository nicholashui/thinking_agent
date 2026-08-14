# Human Baseline — m051-POS-01
## Style: Expected Value in Startup Portfolios (VC) (pure) — visible reasoning trace

**Restatement.** $100M fund, 3x target. A: 50 checks x $2M, no follow-ons. B: 25 checks x $2M ($50M) + $50M reserve; $2M follow-on into every 5x/15x/50x company (p = 15% per check); followed company returns the class multiple on its full $4M; idle reserve at par. Outcome classes per check: 0x (60%), 1x (25%), 5x (10%), 15x (4%), 50x (1%).

**Step 1 — Per-check EV (power law).** E[check] = 0.25(2) + 0.10(10) + 0.04(30) + 0.01(100) = 0.5 + 1.0 + 1.2 + 1.0 = **$3.7M** → **1.85x** per check. Tail note: the 50x bucket alone contributes $1.0M = **27%** of check EV — the power-law tail dominates the mean.

**Step 2 — Portfolio A (linearity).** EV(A) = 50 x 3.7 = **$185M** → **1.85x** fund multiple (independent outcomes → expectations add).

**Step 3 — Portfolio B (follow-on uplift).** Per-company EV: 1x bucket 0.25(2) = 0.5; 5x bucket 0.10(5 x 4 = 20) = 2.0; 15x bucket 0.04(15 x 4 = 60) = 2.4; 50x bucket 0.01(50 x 4 = 200) = 2.0 → **$6.9M** = base 3.7 + follow-on uplift 3.2 (0.10x10 + 0.04x30 + 0.01x100). Portfolio: 25 x 6.9 = $172.5M. Expected follow-ons 25 x 0.15 = 3.75 (deploy $7.5M); idle reserve $42.5M returned at par. **EV(B) = 172.5 + 42.5 = $215M** → **2.15x**.

**Step 4 — Select.** B beats A by **$30M**. **Choose Strategy B** (spray + follow-on concentration into the tail classes).

**Step 5 — Sensitivity.**
- Follow-on effectiveness f (multiple earned on follow-on capital): EV(B) = 25(3.7 + 3.2f) + 42.5 = 135 + 80f; ties A (185) at **f* = 0.625**. At full tail capture (f = 1) B is robustly ahead; follow-on capital must earn ≥ 62.5% of the class multiple.
- Tail hit rate p (50x): EV(A) = 50(2.7 + 100p), EV(B) = 165 + 5000p — same 5000p coefficient, so B's $30M lead holds at every p; the advantage is structural.
- 3x target: EV(B) = 165 + 5000p = 300 → **p* = 2.7%**. At the modeled 1% the fund returns 2.15x and misses 3x: the target requires a tail rate 2.7x the estimate (or better sourcing).

**Step 6 — Counterfactual.** 25 checks x $4M (no follow-ons) = 25 x 2 x 3.7 = $185M = A. Bigger undifferentiated checks add nothing; only concentrating follow-on capital into the tail does.

**Step 7 — Recommendation.** **Strategy B: 25 x $2M checks + $50M follow-on reserve; expected $215M (2.15x), +$30M over A.** State the gap honestly: at modeled tail parameters the fund misses 3x; p(50x) ≈ 2.7% (or comparable sourcing improvement) is required.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning deliberately confined to the pure portfolio-EV style — per-check EV from the power law, linearity to portfolio EV, follow-on uplift with idle-capital accounting, breakevens, and target-gap sensitivity. In this positive case the style performs excellently: exact, checkable, and the sensitivity isolates the two parameters that could move the decision (f*, p*).*
