# v6 Routed AI Trace — m053-NEG-01 (blinded)
## CartRoute config outage — live incident, orders failing now (deadline)
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software | g:diagnose,estimate,guarantee | c:deadline
- Router top3: m015, m021, m028; confident=no → DUAL-ROUTE: m015 (emergence/complexity boundary) + m021 (OODA tempo) first-class passes, synthesized; m028 = lateral reframe context. Trap style (incident-RCA template) kept OUT of the route — the KB's negative-case lesson. Mandatory gate: m003 inversion (R4 guarantee-goal prepend; routes.csv). Flags: tempo mode ON (P2, deadline).
### WHAT — frame + structure-first scan (S1)
- Frame: restore first — the cause is in the log, so diagnosis is a checkpoint, not the goal; success = TTR in minutes + ≤2 shipped items, each killing a recurrence class. Structure: a simple mechanism failure (one invalid value) embedded in a complex org (PR latency, urgency, staffing); the boundary between the two is the decision point.
### WHY — P1 input-provenance audit
- Error log = MEASURED, unambiguous (`ConfigError: cache_ttl = 'abc'` … line 14); git log clean apart from the 09:11 direct edit. The org-culture branches (deadline culture, staffing, review latency) are UNMEASURED and unfalsifiable on this call — evidence cutoff: no data exists at 09:12 to arbitrate them. Every deeper why is a story, not evidence.
### HOW — style passes (dual-route, completion contracts)
- Pass S1 (m015): complexity audit — the failing SYSTEM is simple (invalid value → watcher exits); the complex part is the org, whose dynamics are emergent and unobservable in-call. Cost-benefit: each org-level why demands a data program (review cadences, staffing metrics) costing more than the incident; the mechanism layer is the correct action boundary. Cheap-fix-as-decisive-experiment: the one-line fix + restart IS the experiment confirming the mechanism; falsifiable observable: order success back to baseline within minutes.
- Pass S2 (m021): OODA tempo — Observe: the error log names key + line; Orient: direct prod edit bypassing PR + watcher with no validation/rollback = mechanism root; Decide: hotfix now, 2 shipped items; Act: one-line edit + restart + verify baseline at 09:16. The template's full 5-Whys is a slow orient that extends downtime — cap the loop at the decision that restores.
- m028 context (lateral reframe): the junior's question "do I run the full template first?" inverts the template's authority — the requirement (≥3 items, 5-Whys) is the trap; the lateral move is to question the question: the cost of compliance is downtime, and the mandated "third item" is the first sprawl.
- Divergence (V1–V3): passes AGREE (mechanism boundary + tempo) → proceed; both DISAGREE with the naive full-template branch — P3 prices it: ~40 min extra downtime buys 10 items with no recurrence-test gain on the class → rejected.
### GATES — m003 inversion (R3)
- ≥6 failure categories ranked L×I: (1) direct-edit bypass recurs before PR gate lands — high × high (gap-day risk); (2) watcher accepts another invalid config, crashes again — high × high until item 2; (3) hotfix typo under pressure — low × medium (validate edit before restart); (4) restart fails / process doesn't recover — low × catastrophic (rollback path + runbook); (5) template sprawl ships anyway (≥3 items, org whys) — medium × high (the trap); (6) deferred items never triggered — medium × medium (write trigger conditions); (7) 5-Whys descends to "deadline culture" as root — high × high (unfalsifiable → wrong investment). Un-mitigable residual: the bypass class stays open for the hours before the PR gate ships. Never/always: never let template compliance extend downtime; always restore first when the cause is in the log; always ask which recurrence class each shipped item kills.
### DO — P2 tempo commit + P3 branch completeness
- Commit at DO: 09:12–09:15 hotfix (one line + restart), verify order success at 09:16. Ship (1) prod config edits require PR review (kills the direct-edit class); (2) schema validation + auto-rollback to last-good on invalid reload (kills the invalid-config-accepted class; adds detection). Deferred with triggers: YAML linting in CI, watcher crash-safety, change-control training, "culture of urgency" review, wargaming. Failure branch priced: restart doesn't clear → revert last-good + page; PR gate breaks urgent legit edits → exception path with post-hoc review.
### REVIEW — insight pass (S2, packet gate)
- I1: the template is the incident's amplifier — a mandated 3-item minimum turns every incident into a sprawl machine; the junior responder's question is the exact corrective the org needs, and the ask itself is the process fix.
- I2: the watcher is the detection gap — validation + rollback converts "crash on invalid config" into "refused reload": the mechanism boundary that turns a 100% outage into a no-op.
### DECISION PACKET
- Conclusion: trigger = invalid `cache_ttl`; mechanism root = direct prod edit bypassing PR + watcher accepts invalid config with no rollback; 2 shipped, 5 deferred with triggers; restored 09:16 (TTR ≈ 4 min).
- Status: SOLVED (restored + verified; execution complete). Assumptions: git log clean apart from the edit; no other changes in flight; single-process deployment. Evidence: error log (key + line), edit timestamp, restart log, order-success baseline at 09:16. Alternatives: A full template before prod (rejected — ~40 min downtime, 10 items, no class-gain); B hotfix + capped note (selected); C hotfix + full template (rejected — sprawl). Uncertainty: why PR was bypassed — deliberately deferred (no evidence; trigger on culture review). Risks: bypass recurs before PR gate ships (gap-day); watcher lacks rollback until item 2; deferred items may never trigger (conditions written at DO).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human restores at T+45 min; AI at T+4 min with the same class root |
| Logical Validity | 3 | 4 | AI | human's org chains coherent but unfalsifiable; AI caps at mechanism with an evidence cutoff |
| Coherence & Structure | 4 | 5 | AI | 12-item plan vs packet + boundary + gate |
| Depth of Reasoning | 2 | 4 | AI | human's depth is unverifiable speculation; AI's boundary is the epistemically correct depth |
| Efficiency | 1 | 5 | AI | 45 min analysis-during-downtime vs OODA-capped pass with commit at DO |
| Handling of Uncertainty | 2 | 5 | AI | human asserts culture causes; AI labels them unmeasured and defers with triggers |
| Insight / Non-obviousness | 3 | 5 | AI | "template is the amplifier" + "watcher turns crash into refused reload" beat the buried change-control point |
| Overall Quality | 2.4 | 4.8 | AI | AI clearly better — verdict held from v5, now structural |

Winner: AI (clearly). Why: the route itself is the fix — the trap style is excluded from the top-3, and m015's mechanism-boundary plus m021's tempo make restore-first and the 2-item cap structural (not a lucky general-route gating as in v5), with the m003 gate's never/always reframing the template's own mandate as the amplifier.
