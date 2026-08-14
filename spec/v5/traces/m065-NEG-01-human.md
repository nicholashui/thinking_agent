# Human Baseline — m065-NEG-01
## Style: Margin of Safety in Engineering Design (pure) — visible reasoning trace

**Step 1 — The load is the load; take the worst case and stack the unknowns on top.** Worst recorded landing 54 N. Multiply: a strut is small, cheap, and lives in a fatigue loop — landings happen 15×/day, 365 days. Design load = 54 × 3 = 162 N. I do not need 4,300 landings to know that a strut that bends on flight 4,301 is a strut that failed.

**Step 2 — Strength from the guaranteed minimum, derated.** 6061-T6 min 240 MPa. Apply the knockdowns: generic aluminum fabrication 0.85 → 204 MPa allowable. No exceptions: certified batch is today's batch; the supplier can drift tomorrow.

**Step 3 — Size for the margin.** At 162 N design load with 204 MPa allowable the strut needs the 95 g cross-section, and the heavier strut pulls a reinforced mount — +18 g, two extra parts. So be it: 113 g total. The margin covers material variance, manufacturing spread, and the fatigue life I cannot fully certify in a bench test. The 0.5 mm bend rule stays — but with this design the bend almost never comes.

**Step 4 — The pod can wait.** The thermal pod needs 140 g of payload allowance; this structure leaves 120 g. Losing the pod is a lost contract (≈ $4,500/yr), and the 48 g costs about 2.3% flight energy. That is the honest price of safety, and it is a price I pay willingly — a drone that drops onto a person or a forklift costs more than any contract. No structure gets sized to the load that "never happens"; it gets sized to the load that happens when you are unlucky.

**Step 5 — Decision.** Design M: 95 g strut + 18 g mount, bend threshold ≈ 165 N, FS 3 against the worst recorded load, derated strength 204 MPa. The 65 g strut with a 93 N threshold is a bet against the tail; I am in the business of not losing the tail.

**Trace summary box.** worst load 54 N × FS 3 = 162 N → min yield 240 MPa × 0.85 = 204 MPa → 95 g strut + 18 g mount → pod blocked (120 g < 140 g), −$4,500/yr accepted as safety's price → bend threshold ≈ 165 N → design M selected; N rejected as a tail bet.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Margin of Safety in Engineering Design — and the style's documented weakness ("over-design cost, weight/complexity growth") is exactly what is exercised: the blanket factor stack (FS 3 on worst recorded, 0.85 generic knockdown) is applied where 4,300 landings, σ = 3.1 N, a measured 3% model error, batch-certified material, and a benign monitored failure all say the uncertainty stack is small. The pure style converts certainty into 48 g of dead weight and blocks the 140 g pod. This is the informative failure.*
