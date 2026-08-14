# Human Baseline Trace — Organizational Feedback Loop Analysis
## Test Case: m086-POS-01 (Positive)

Method discipline: strictly and purely feedback-loop analysis. Every claim names a loop, its sign, and the stock it acts on; nothing is asserted about org behavior without a mechanism; measurements are stocks, policies are flows.

### 1. The system in stock terms
- Reps' time stock: 480 min/day, already fully committed (14 × 33 = 462 min).
- Pipeline stock: real calls × conversion (12%); commission flows from closed deals.
- Support capacity stock: 8 agents at 90% utilization (≈ 7.2 agent-equivalents).

### 2. Time-budget audit — where the resistance is located
20 × 33 = 660 > 480 min. Even at zero prep and admin, 20 × 25 = 500 > 480. Honest compliance is structurally impossible: the quota cannot raise call counts, only change what gets logged. Resistance is not attitudinal — it is a conservation law at the time stock.

### 3. Loop map (signed)
- **B1 time-compression**: quota ↑ → minutes per real call ↓ → call quality ↓ → conversion ↓ → revenue ↓ → quota pressure ↑.
- **B2 gaming**: quota ↑ → logged calls ↑ while real calls stay flat → CRM data quality ↓ → lead quality ↓ → conversion ↓ → pressure ↑. Gaming is B2's steady state.
- **R1 comp-attrition**: revenue ↓ → commission ↓ → attrition ↑ → hiring/training load ↑ → effective selling capacity ↓ → revenue ↓ further.
- **B3 support-bottleneck**: data quality ↓ → support disputes ↑ (15 min each) → admin backlog ↑ → lead routing delayed → conversion ↓.
- **R2 KPI-illusion**: dashboard compliance ↑ → leadership confidence ↑ → enforcement deepened → gaming ↑.

### 4. Falsifiable predictions (markers + timing)
- Months 2-3: gaming signature — end-of-day timestamp clustering; > 25% of logged calls with duration < 5 min.
- Q2: paper compliance ≥ 95% while median real talk time and real call count stay flat — the paper-vs-real divergence IS the resistance signal.
- Q3-Q4: conversion 12% → ~9-10%; attrition 8% → ~13%; support backlog +40%; net revenue −6 ± 2% at month 12.

### 5. Redesign — levers that change loop structure
- Remove the activity quota; contract on outcome (segment-level conversion × quality-weighted pipeline) — collapses B1/B2 at their source.
- Add a peer deal-review loop (quality check before CRM close) — protects the quality stock R2 cannot see.
- Give support a capacity lever: auto-generated call notes + 2 extra agents if the backlog threshold is hit — unclamps B3.
- Reset triggers, honoring 2019/2021: conversion < 10% or gaming markers above threshold → rollback by design, not post-mortem.

### 6. Final answer
20×20 as mandated will fail while succeeding on paper: ~98% compliance dashboard with flat real calls and declining revenue by Q4. Resistance lives in the time stock; support amplifies it. The plan that makes 20×20 work is replacing it: outcome contract + peer review + support capacity + pre-committed reset triggers.
