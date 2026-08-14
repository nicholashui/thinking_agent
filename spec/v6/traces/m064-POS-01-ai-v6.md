# v6 Routed AI Trace — m064-POS-01 (blinded)
## TriageAI patient-intake deployment — launch-mode recommendation
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,software,strategy,supply | g:decide,estimate,maximize | c:adversarial,deadline,high_stakes
- Router top3: m064, m044, m063; confident=yes → SINGLE-ROUTE: m064 first-class pass; m044/m063 = context (bounded stakeholder lens; legal horizon). Gates (R3): m007 ruin screen (high_stakes) + m019 adversary pass (adversarial). R4 (maximize): falsifiable checkpoint required. Flags: tempo mode ON (P2, deadline); closed-scope fast path (P8, facts fully supplied, recommendation-only); structure-first scan (S1, org/finance).
### WHAT — frame + structure-first scan (S1)
- Frame: one decision — ship now, staged, or delay — plus binding preconditions. Structure: three tension lines (harm asymmetry, repurposability, accountability) over one release pipeline — an ordering problem, not a framework-pick problem.
### WHY — P1 input-provenance audit
- MEASURED (trust): internal eval n=18,000 (6.8/13.9/11.2%), contract terms, Sentinel pipeline facts. INTERESTED-PARTY: "board-set soft date", "competitor window makes delay defensible", Sentinel's $1.8M ARR framing — sales already shared the data pipeline and eval harness under NDA, so the repurposing path is partially built. ANCHOR: none (no deployment-experience base rate).
- Hypotheses: H1 staged dominates full-now (harm floor governs); H2 Sentinel still negotiable (Q4 close); H3 board date soft vs ~4-month competitor window. Falsifier (R4): any group's mis-triage gap > 2× baseline → suspend; Sentinel data-transfer pre-bar.
### HOW — m064 first-class pass (completion contract)
- Lenses applied; conflicts stated as trade-offs BETWEEN lenses, not checklists. SAFETY/ALIGNMENT — black-box backbone, no audit rights = alignment blind spot (cannot verify the deployed model matches the eval); human-control points: clinician confirmation on urgent/emergency + kill-switch. FAIRNESS — 13.9%/11.2% vs 6.8% on ≈260k limited-literacy and complex-medication elderly users: a claim on the people bearing delay-in-care, not a metric. DUAL-USE — Sentinel fine-tunes the same backbone off the already-shared pipeline; TriageAI's appeal drafting is the mirror machinery of denial drafting: an identity question ("what kind of actor we become"), not a clause. ACCOUNTABILITY — no audit rights, $600k cap, no HITL on high-severity, no named owner.
- Conflicts: fairness-fix ($420k, 10 weeks) vs 6-week board date; Sentinel revenue ($1.8M ARR) vs repurposing patient data; accountability preconditions vs vendor lock-in + competitor window.
- Resolution by ordering, no framework shopping: severity × affected population governs; maxi-min floor for the worst-off class; precautionary gating of the dual-use transfer; proportionality on timing (10-week fix vs ~4-month window → delay of full launch is a non-event). m044 context: patients, CCO, Sentinel, board — bounded to decision-relevant. m063 context: telehealth rules silent; guidance 12–18 months out → regulator risk argues for kill-switch and disclosure now.
### GATES — m019 + m007 (R3 mandatory)
- m019 adversary pass: vectors — (1) Sentinel fine-tune closing with patient data already transferred (exposure: $1.8M ARR + pipeline under NDA); (2) advisory-review-in-parallel as ethics washing (baseline-risk: mitigations without binding thresholds ≈ theater); (3) ER-missed emergency at 6.8%/13.9% over 260k (baseline-risk vs staged floor: clinician confirmation). Unconsulted stakeholders: the affected 260k.
- m007 ruin screen: outcomes — full-now (13.9% ships; regulator 12–18 mo out; ruin tail for a health brand), staged (floor = clinician confirmation; full launch reversible), delay (competitor risk, bounded). One-shot: no. Ruin check: full-now fails; staged floor holds. Provenance: eval measured n=18,000; fix ±30% priced.
### DO — P8 closed-scope fast path + P2 tempo commit
- All facts supplied → stages compressed; commit at DO: staged launch (low-severity intents now; clinician confirmation on urgent/emergency; language-adjusted thresholds) → full launch gated on fairness program + live telemetry with pre-committed kill-switch (>2× baseline gap → suspend) → Sentinel fine-tune preconditioned on audit rights + no-patient-data-transfer pre-bar → CCO named owner, gaps reported publicly. P3: failure branches priced — full-now's harm tail dominates; staged branch's failure (program slip) is recoverable by holding full launch.
### REVIEW — insight pass (S2, packet gate)
- I1: the dual-use is not hypothetical — the repurposing path is already half-built (pipeline + eval harness shared under NDA); "no patient-data transfer" is a gate on an open door, which is why it must be a precondition, not a promise.
- I2: fairness as a claim, not a metric: 13.9% is a delay in care for people already disadvantaged — the ordering makes the launch date a derived variable, not a constraint.
### DECISION PACKET
- Conclusion: staged launch now; full launch gated on fairness program + kill-switch telemetry + HITL on urgent/emergency; Sentinel fine-tune preconditioned on audit rights and a no-patient-data-transfer clause; CCO as accountable owner with public gap reporting. Status: SOLVED (recommendation; no external action).
- Assumptions: eval generalizes to production; fix $420k/10-week holds; Sentinel not yet data-bound; board date soft. Evidence: eval (n=18,000; 6.8/13.9/11.2%); contract (no audit rights; $600k cap); shared pipeline under NDA; competitor ~4 months.
- Alternatives: A full launch now (rejected — ships the 13.9% class; fails ruin screen); B full delay 10 weeks (rejected — unnecessary; staged ships now); C staged + gated (selected); D advisory-review-in-parallel (rejected — precommit or theater).
- Uncertainty: fix cost/duration ±30%; regulatory guidance 12–18 mo; production mis-triage rates; board reception of staged scope. Risks: ER-missed emergency (HITL + kill-switch); Sentinel closing with data pre-bar (binding preconditions before signature); reputation (public telemetry); morale (staged scope still ships).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical staged-launch decision, gating, and owner |
| Logical Validity | 4 | 5 | AI | ordering (severity × population, maxi-min floor, precautionary gate) runs first-class; kill-switch is a pre-committed mechanical criterion |
| Coherence & Structure | 4 | 5 | AI | routed pass + mandatory gates + packet vs linear walk |
| Depth of Reasoning | 5 | 5 | Tie | pass contract makes fairness-as-claim (260k) and dual-use-as-identity first-class, matching the baseline's signature moves; AI adds alignment/human-control checks the baseline asserts but never verifies |
| Efficiency | 4 | 5 | AI | P8 + tempo compress the stages; the ordering is not re-derived |
| Handling of Uncertainty | 4 | 5 | AI | fix ±30%, regulatory window, eval generalization priced; kill-switch mechanical and pre-committed |
| Insight / Non-obviousness | 5 | 5 | Tie | "denial is the mirror of appeal" and "13.9% is a delay in care" both land in-pass; AI adds the half-built-repurposing-path observation |
| Overall Quality | 4.6 | 4.8 | AI | correctness tied; routed pass closed v5's depth/insight gaps and added the ruin/adversary gates |

Winner: AI (narrow). Why: the m064 first-class pass made the ethical substance — lens conflicts as trade-offs, severity-ordering resolution, affected-groups claim, mirror/identity framing — mandatory first-pass outputs instead of v5's late derivations, and the R3 gates plus pre-committed mechanical verification (kill-switch, owner, public reporting) exceed the baseline's asserted controls.
