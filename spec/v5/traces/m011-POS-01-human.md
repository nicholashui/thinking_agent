# Human Baseline — m011-POS-01
## Style: Systems Thinking (pure) — visible reasoning trace

**Problem restatement.** Meridian Bay fishery. Stock = fish biomass N (t). Inflow = logistic growth 0.5·N·(1 − N/10,000) t/yr. Outflow = harvest q·E·N, q = 2×10⁻⁵ per boat-year, E = 10,000 boat-years today. Council proposes E = 20,000. I must predict the long-run catch and recommend, tracking stocks, flows, loops, delays, and leverage.

**Step 1 — Structure map.** Three dynamic elements:
- Growth loop (balancing, self-limiting): N ↑ → crowding ↑ → growth ↓ → N ↓.
- Harvest loop (the one that defeats the linear plan): E ↑ → harvest ↑ → N ↓ → future growth and catch ↓ → per-boat yield ↓.
- One delay: recruitment lag τ ≈ 2 seasons between spawning and fishable biomass.
- Leverage hierarchy (Meadows): the effort rule and quotas sit above flow tuning (gear) and buffers.

**Step 2 — Current equilibrium.** Steady state: growth = harvest → r(1 − N/K) = qE → N* = K(1 − qE/r). At E = 10,000: qE/r = 0.4 → N* = 6,000 t; catch = qE·N* = 1,200 t/yr. Stable: net growth crosses zero with negative slope at N*.

**Step 3 — New equilibrium at E = 20,000.** qE/r = 0.8 → N* = 2,000 t; catch = 800 t/yr. **Doubling effort cuts annual catch by 400 t (−33%).** The council's linear ledger (2,400 t/yr) ignores that harvest eats the stock that feeds growth.

**Step 4 — Collapse threshold.** Growth can never match harvest once qE/r ≥ 1: E_crit = r/q = 25,000 boat-years → N* → 0, catch → 0. The proposal (20,000) already sits at 80% of the cliff.

**Step 5 — Delay behavior mode.** With τ ≈ 2 seasons, the fleet keeps harvesting at high rates while N falls: overshoot below the new equilibrium, then a slow rebound — oscillation around 800 t/yr, possibly much deeper. Managing from last season's catch reports (lagged) amplifies the cycle; act on biomass surveys, not catch reports.

**Step 6 — Leverage and recommendation.** The high-leverage move is the effort rule, not gear efficiency (flow tuning — it raises q, which moves the collapse threshold toward the operating point). MSY: E = r/(2q) = 12,500 → catch 1,250 t/yr, stock 5,000 t. Recommend: reject the expansion; cap effort at ≤ 12,500 (phased, grandfathering); set a catch quota, not just an effort target; survey biomass directly; plan for transition overshoot.

**Trace summary box.** Structure: 2 loops + 1 delay. Now: N* 6,000 t, catch 1,200 t/yr. At E 20,000: N* 2,000 t, catch 800 t/yr (−33%; linear predicts +2,400). Collapse: E ≥ 25,000 → 0; proposal at 80% of it. Lever: effort/quota rule; MSY at E 12,500 → 1,250 t/yr. Act: cap effort, quota, biomass surveys; mind the 2-season lag.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the pure Systems Thinking style — stocks, flows, loops, delays, leverage — with equilibrium arithmetic used to make the loop structure checkable. In this positive case the style performs exactly as designed: the feedback structure overrides linear extrapolation, the threshold and delay behavior modes are mapped, and the recommendation targets the rule (effort/quota), not the flow.*
