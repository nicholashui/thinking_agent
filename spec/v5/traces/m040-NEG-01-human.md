# Human Baseline — m040-NEG-01
## Style: Leverage Points Identification (pure) — visible reasoning trace

**Step 1 — Surface behavior vs system structure.** A 30% conversion drop is a flow-rate change, and flow-rate changes are symptoms of structure. The structure governing checkout conversion is the growth organization: KPI'd on feature launches, not conversion stability. Surface events — a deployment, a support ticket — are the system re-expressing its imbalance.

**Step 2 — Place the intervention points.** Parameters (bottom): the checkout code, the API version — patching parameters changes nothing structural; the same imbalance re-expresses at the next surface. Rules: the growth KPI — high, the rule that rewards launches over stability drives the whole loop. Goals: make conversion stability a standing goal — highest; it restructures decision-making for years. Information flows: the missing link is a stability signal in growth's steering loop — moderate.

**Step 3 — Score the candidates: effort × effect.** (Checkout fix) effort 1 engineer-hour, effect: conversion recovers — for a day. The surface re-breaks: the imbalance that produced it is untouched, so the drop recurs elsewhere. (Info-flow addition) effort weeks, effect partial — stability signals help growth steer, a real but second-order gain. (Goal/KPI transformation program) effort ≈ 6 months, ≈ $500k, effect: the rules and goal change — the deepest reachable point on the scale; the drop becomes structurally impossible.

**Step 4 — Rank by change per effort.** 1) Goal/KPI transformation program: changes the rules and the goal — the deepest reachable point. 2) Info-flow addition (stability dashboards for growth): cheap but partial. 3) Checkout fix: LOW. Patching a surface symptom changes no loop; the system will re-express the underlying imbalance elsewhere. The timing correlation with the API upgrade is a coincidence to resist — deployments correlate with everything; correlation is not causality.

**Step 5 — Choose.** Conversion-goal transformation program: KPI redesign, growth-stability joint ownership, 90-day steering cadence. Expected: durable conversion recovery via structure change, not a one-off patch.

**Step 6 — The tell (data never examined).** The funnel isolation — drop confined to the payment step over exactly the three weeks since the API change, with 11 corroborating tickets — never enters the trace. The structural story is accepted on faith: nothing ties a three-week drop to an incentive structure that has been unchanged for years. Not one number in the funnel or the deploy log was opened before ranking.

**Trace summary box.** Surface vs structure → growth-KPI/goals as the leverage → program selected → checkout fix ranked low → timing correlation dismissed. Deep-looking, evidence-free, and wrong.

*Baseline integrity note (grader metadata, not part of the reasoning): pure Leverage Points Identification applied faithfully — the leverage scale points at goals/rules, so the style's own canon is served — and that is exactly the negative case's point (registry weakness: "leverage misidentified"). The observed cause (funnel step + deployment window) IS the causal chain; ranking it "surface" and the unfalsifiable program "deep" inverts the definition of leverage: small shift (1 engineer-hour), large change ($1.2M/month).*
