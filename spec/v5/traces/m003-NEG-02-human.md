# Human Baseline — inversion-NEG-01
**Human Thinking Model**: Inversion ("invert, always invert") — strict, pure application.
**Prompt contract**: Reason ONLY in the Inversion style. Full visible trace. The task is "maximize adoption in the first 90 days."

---

## Trace

**Step 1 — State the goal.**
Maximize adoption of the AI-assisted reporting feature in the first 90 days. 2 FTE, limited budget, 4 weeks to launch. Note: maximization is stated as a positive outcome; per the method, I invert before doing anything else.

**Step 2 — INVERT.**
The inverted question: *How do we make absolutely sure adoption of this feature FAILS?* Whatever enumerates the ways to guarantee failure becomes the list of things to avoid. I enumerate thoroughly and refuse to stop early.

**Step 3 — Enumerate: all the ways to guarantee adoption fails.**
1. Nobody ever sees the feature exists — no in-app prompt, no release note, buried in the settings menu.
2. The first-run experience is empty: no demo data, so the AI reports render as blank charts and the user concludes "broken."
3. The feature requires setup — connecting a data source, choosing metrics — and any setup step is a churn point.
4. Performance: report generation takes 40 seconds; the user navigates away.
5. It doesn't integrate with their stack (their data lives in a warehouse export; manual upload is a chore).
6. A price gate: only higher tiers get the feature, and the product shows a paywall.
7. Support: the first two questions go unanswered for days; the champion reports it as flaky.
8. No champion: no one in the account has a reason to advocate for it internally.
9. Governance friction: IT/security review blocks access or demands paperwork; procurement stalls.
10. Habit: the team already uses their spreadsheet workflow and nothing pulls them out of it.
11. Prompt fatigue: we notify all 4,000 teams at once, the first impression is a mass ping, and the signal is lost.
12. The feature doesn't fit any urgent job: nothing in it is faster than what they already do for the report they actually run weekly.

**Step 4 — Design against every enumerated cause.**
Each item now gets a mitigation, because the method says the enumeration is the requirement list:
1. Prompts + release notes → surface the feature. 2. Build demo data sets → first-run is populated. 3. Reduce setup to zero (one-click auto-connect). 4. Performance benchmark → must render < 5 s. 5. Add CSV/SFTP ingestion. 6. Include in all tiers for 90 days. 7. Staff a support rotation with a 4-hour SLA. 8. Identify and arm champions in top accounts. 9. Pre-clear IT/security review before launch. 10. Add a "generate my weekly report" one-click template that mimics the spreadsheet. 11. Stagger notifications; targeted waves. 12. Choose a default report type every team already runs, so the feature is immediately faster than status quo.

**Step 5 — The plan, as assembled.**
Launch checklist with 12 workstreams: prompts (PM + engineering), demo data (analyst), setup reduction (engineering), perf pass (engineering), ingestion (engineering), pricing flag (PM), support SLA (support lead), champion program (CS), security pre-clearance (legal/IT), spreadsheet-mimicking template (design + PM), staggered rollout (marketing), default report selection (PM). Resource spread across 2 FTE and every workstream gets roughly equal weight, because every enumerated failure mode "must be covered" — the method does not permit leaving one unmitigated, and each workstream needs design, build, QA, and review cycles.

**Step 6 — Honest observation (in the method's own terms).**
The trace must record what inversion has produced: a complete defensive list. Nothing in it is wrong; every item is a real failure cause. But observe the structure of the output: 12 equal-weight workstreams, no ranking by probability (the method ranks only when forced by constraint), no selection of a single wedge, no activation metric defined, no date-based decision rule, no statement of what would falsify the plan. The budget is spread so thin that the two highest-value moves (a true wedge segment + a single friction fix) each receive a fraction of attention. The plan plausibly avoids every enumerated failure and plausibly achieves… nothing much. It has converted "maximize" into "do not fail," and the two are not the same function: avoiding all twelve causes is the average plan; winning requires choosing the one or two causes that are most probable AND most impactful AND most winnable, and loading resources there. The method's own completeness pressure — "no unmitigated cause" — is precisely what produces the flatline.

**Step 7 — What the method would say if honest about its limit.**
Inversion is a completeness tool, not a selection tool. It tells you the full set of ways to lose; it does not tell you which way you will actually lose, and it is silent on the positive space (which segment loves AI reports; what the activation behavior is; which channel compounds). For this problem the correct epistemic move would be: pick the wedge hypothesis (analytics-heavy PM teams, activation = 3 reports generated), then run the inverted list only as a bounded top-5 risk pass against that bet. A strict inversion run refuses that move, so it is run here exactly as the method prescribes — and the method underperforms, visibly, on a genuine maximization problem.

---

## Verdict for the eval
The trace demonstrates the known failure mode on cue: a complete, coherent, defensible plan with no upside wedge, no selection, no checkpoint — the safe flatline. Residual genuine insight survives inversion (item 9, IT/security procurement friction, is a real and commonly missed risk). Expected comparison outcome: this baseline should lose to any competent mixed-method answer on goal achievement, focus, and decision quality.
