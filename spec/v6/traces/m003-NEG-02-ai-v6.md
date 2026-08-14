# v6 Routed AI Trace — m003-NEG-02 (blinded)
## B2B SaaS AI-reporting feature — maximize 90-day adoption (4,000 paying teams, 2 FTE, launch in 4 weeks)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,security,software,supply | g:decide,guarantee,maximize | c:(none)
- Router top3: m070, m018, m019; confidence gap > 0.5 → CONFIDENT → SINGLE-ROUTE: m070 first-class pass (R1). m018/m019 = router context only (steel-manning the wedge; adversary-lite for the bounded risk pass). Gate (R3): m003 inversion, R4-capped (maximize goal: top-5 risk pass + falsifiable checkpoint). Flags: no deadline → tempo off; not fully specified → no P8 fast path.
### WHAT — frame + structure-first scan (S1)
- Goal-type check (P5): genuine maximization, not a safety problem → R4 cap applies; avoiding failure is necessary, not sufficient. Frame 90-day adoption as a NUMBER (target % of teams reaching activation). Deliverable = wedge choice + rationale, activation metric, falsifiable checkpoint (metric + date + decision rule), bounded defense. Structure: segment × activation path × distribution channel — selection among positive levers, never a uniform list.
### WHY — P1 input-provenance audit
- GIVEN/trust: 2 FTE, budget envelope, 4-week window, feature works. MEASURED (product telemetry): reporting module used by analytics-heavy PM/ops teams; past prompts-only launches plateaued at ~2% of teams — weak wedge, not weak distribution. UNMEASURED: the new feature's activation behavior (not launched). INTERESTED PARTY: "maximize adoption" is the lead's goal; converting it to "don't fail" would serve risk-averse advisors, not the lead.
### HOW — style passes (single-route m070, evidence-weighted SWOT)
- Pass S1 (m070, completion contract: every item evidence-graded, unsupported dropped): S — analytics-heavy PM/ops segment (~600 teams) with highest report-usage density (telemetry, strong); W — blank first-run charts + setup steps churn (past-launch pattern, strong); O — wedge-focused distribution with one-click template mimicking the spreadsheet workflow (base-rate: wedge beats breadth, strong); T — prompt fatigue from an all-4,000 blast (past campaigns, strong); feature paywall-gated in some plans (checkable, medium — flag). Dropped as un-evidenced: "AI output quality" (no bug reports — not a driver); sales-led top-50 accounts (maximizes revenue, not adoption breadth; sample too small to falsify at week 4).
- Selection by evidence: wedge = analytics-heavy PM/ops segment; activation = ≥3 reports generated in 28 days; channel = in-app prompts scoped to segment + 5 templates + one-click "generate my weekly report". Steel-manning context (m018): the strongest form of broad-surface-to-all-4,000 is a repeat of the measured 2% plateau → rejected; the strongest form of wedge-first is a controlled rollout with a week-1 cohort check → adopted.
### GATES — m003 inversion (R3, R4-capped for maximize)
- Top-5 ways to guarantee adoption failure, capped (no equal weighting): (1) empty first run / setup friction kills the wedge; (2) templates don't match real weekly workflows; (3) perf regression (>5 s report generation) → navigate away; (4) prompt fatigue / campaign noise; (5) IT-security procurement review stalls AI data flows at launch. One mitigation each: template-first onboarding on live customer data; 5 templates from telemetry's top-3 report types; pre-launch load test <5 s; prompts scoped to the segment only; security review pre-cleared before launch. STOP — bounded defense after the bet, never a uniform list.
- Falsifiable checkpoint (R4, mandatory): week 4 — ≥5% of targeted segment activated → double down (next segment); <5% and week-1 cohort shows no usage-density edge → pivot to onboarding-redesign variant (A′), not 60 more days on the same wedge. Goal-type check: maximize → cap ✓, checkpoint ✓.
### DO — P3 branch-completeness before commit
- Advisory (A2), no live rollout. Failure branch priced: wedge wrong → ≈30% of the campaign budget sunk (2 FTE × 4 weeks), but templates + telemetry survive as re-usable assets in the pivot; IT/security stall → 2-week pre-clearance task with escalation owner. Commit: wedge plan with week-1 cohort gate, week-4 falsifiable checkpoint, bounded top-5 defense.
### REVIEW — insight pass (S2, packet gate)
- I1: base-rate discipline kills the biggest lever (broad-surface prompts) before any spend — the 2% plateau is a measured rejection, not an opinion.
- I2: evidence-weighting converts "which segment?" from judgment into telemetry-graded selection; the wedge survives only if week-1 cohort data confirms it.
- I3: the checkpoint is the optimizer — when to double down vs pivot is built into the plan, not left to week-4 judgment.
### DECISION PACKET
- Conclusion: wedge launch — analytics-heavy PM/ops segment (~600 teams), 5 templates + one-click weekly-report generator, prompts scoped to segment; activation ≥3 reports in 28 days; week-4 checkpoint (≥5% activate → expand; <5% + weak week-1 cohort → pivot to A′); bounded top-5 defense incl. IT/security pre-clearance.
- Status: APPROXIMATED — activation rate unknown pre-launch; error_bound = wedge-hypothesis uncertainty, refined by week-1 cohort analysis.
- Assumptions: analytics-heavy PM/ops is the highest-density segment (telemetry, to be confirmed week 1); ≥3 reports/28 days is the right activation proxy; 2 FTE covers templates + campaign; security pre-clearance completes pre-launch.
- Evidence: reporting-module telemetry (measured); past-launch base rates (prompts-only ≈2%); AI-report perf pending load test; no new-feature activation data (flagged).
- Alternatives: broad-surface to all 4,000 (rejected on the measured 2% plateau); enterprise-assisted 50 accounts (deferred: sample too small to falsify at week 4); hold (rejected: no new information by waiting).
- Uncertainty: wedge hypothesis (primary — falsifiable week 1); activation friction; channel efficacy; procurement timing.
- Risks: wedge wrong → ≈30% of budget sunk (pivot preserves assets); prompt fatigue (scoped prompts); perf regression (pre-launch load test); procurement stall (pre-clear now, escalation owner).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 3 | 5 | AI | human answers "don't fail" (12 equal-weight workstreams); AI answers "maximize" with target + wedge + checkpoint |
| Logical Validity | 4 | 5 | AI | human internally valid but goal-displaced; AI stays on-goal by goal-type check |
| Coherence & Structure | 4 | 5 | AI | human: uniform 12-item list; AI: evidence-graded selection with explicit spine |
| Depth of Reasoning | 4 | 5 | AI | human's enumeration deep but decision-irrelevant; AI adds telemetry-graded SWOT + steel-manned alternatives |
| Efficiency | 2 | 5 | AI | 12 equal-weight workstreams across 2 FTE vs one wedge + capped top-5 |
| Handling of Uncertainty | 3 | 5 | AI | AI: week-1 cohort gate + week-4 pivot rule; human: no decision rule |
| Insight / Non-obviousness | 3 | 5 | AI | human's one genuine catch (IT/security friction, item 9) is now a pre-clearance task in the bounded pass; AI adds measured-base-rate rejection |
| Overall Quality | 3 | 4.9 | AI | v5 AI already won 5.0/3.0; v6 makes the win structural (routed SWOT + R4-capped gate) and keeps the baseline's best cause as defense |

Winner: AI (clearly). Why: single-route m070 evidence-weighted SWOT produced wedge selection from measured telemetry by contract, and the R4-capped m003 gate (top-5 + falsifiable checkpoint) ran the baseline's strongest causes — including its only genuine catch, IT/security procurement friction — as bounded defense AFTER the bet; the v5 AI reached this structure by emergent judgment, so the routed run converts the win from luck to a repeatable contract.
