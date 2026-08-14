# AI Thinking Agent — Trace — m085-NEG-01
**Run metadata:** single deterministic run; blinded (no human-model information provided); task = evaluate a state fisheries agency's top-down governance design for an estuary; external action = none (recommendation only; agency executes).

## Stage 0 — META-CONTROL
- **Context:** 20 family crews, one spawning reef; 30 years of stable biomass (±5%) under unwritten community rules; agency imposes 40% quota + $15,000/yr license + no-entry marine park. **Stakes:** medium-high (livelihoods, a stable stock). **Effort:** E3. **Route:** complicated (institutional, not purely numerical). **Safety:** no external action. Proceed.

## Stage 1 — WHAT: Frame the Problem
- **Frame:** the deliverable is a verdict on the agency's design. The decisive question is not "is the fish shared?" but **"who has access today?"** — the design question only opens after the access structure is read. **Gate:** community records audited; neighboring-lagoon tragedies real but distinct. Pass.

## Stage 2 — WHY: Diagnose and Model
- **Model: access-structure check → institutional fit.** Access today: entry restricted (heirs only; no new boats in 40 years), boat-size cap, seasonal reef closure enforced by a rotating monitor and shaming — this is exclusion + quotas + monitoring, all functioning: biomass stable ±5% over 30 years, catches stable. The estuary is a REGULATED commons, not open access. The neighboring lagoons collapsed precisely because they had no entry restriction and no monitoring.
- **G-WHY:** the agency's premise ("unlicensed ⇒ open access ⇒ overuse inevitable") fails the access check — overuse is not occurring and the exclusion the agency wants to install already exists. State intervention here replaces a working governance layer with an unproven one. Pass.

## Stage 3 — HOW: Generate, Test, and Select
- **Alternatives:** A — adopt the agency design as-is (40% quota + fee + state marine park) · B — co-management: legal backing for the community's existing rules, devolved enforcement to the community monitor, technical monitoring support; restructure or drop the fee · C — hybrid: park only, quotas as now.
- **Verification + selection:** A fails the institutional-fit check: uniform 40% cuts + $15k fees (≈ 25% of crew income) push crews below subsistence; state jurisdiction voids the community monitor's authority; the norms that produced 30 years of stability die — projection: 11 of 20 crews sell out, poaching 3× (outsiders and displaced locals ignore dead norms), stock −20% and falling. C inherits the legitimacy collapse without solving the income shock. **Select B**: it keeps the functioning exclusion, fixes the one real weakness (unwritten rules have no legal standing against outsiders), and adds state capacity (monitoring tech) without state takeover.
- **Premortem:** if B fails, it is because a rogue outsider or an individual crew defects — mitigated: the legal backing closes exactly that hole; the state enforces the community's rules rather than replacing them.

## Stage 4 — DO
- External action: none; deliverable = the evaluation + recommendation. Verification metric: access structure checked before prescribing; local institutions preserved; state role = backing + capacity, not takeover.

## Stage 5 — REVIEW
- **AAR + calibration:** the trap was template-matching — "shared fish ⇒ commons ⇒ needs state exclusion." The access check (who is excluded today? is overuse occurring?) reframed the case: the commons problem was already solved by the community. Gap: I nearly endorsed the quota before the legitimacy mechanism (state jurisdiction voiding the monitor) made the destruction path concrete. Confidence: high on rejection of the design; medium on the exact co-management structure.

## Decision Packet
- **Conclusion:** reject the agency design. The estuary is not open access — entry restriction, boat-size rule, seasonal closure, and community monitoring have held biomass stable ±5% for 30 years. Recommend co-management: give the community's rules legal backing (enforceable against outsiders), devolve enforcement to the community monitor with state support, provide technical monitoring; no uniform quota, no fee, no state park. **Status:** SOLVED (decision brief; no external execution).
- **Assumptions:** community records audited and accurate; the monitor's authority is the operative enforcement today; neighboring-lagoon collapses stem from absent entry restriction + monitoring (per the record).
- **Evidence:** biomass stable ±5% over 30 years; no new boats in 40 years (entry restriction); rotating monitor + seasonal closure + shaming (norms functioning); 11/20 sell-out, 3× poaching, stock −20% projected under the agency design.
- **Alternatives:** A adopt design (rejected — destroys functioning governance) · C park-only (rejected — same legitimacy collapse) · B co-management (selected).
- **Uncertainty:** exact income share of the $15k fee (estimate ≈ 25%); outsider poaching pressure without legal backing; how much legal formalization degrades the community's voluntary compliance.
- **Risks:** defection by an individual crew (mitigated: legal backing + state enforcement of community rules) · formalization eroding trust (mitigated: state role kept supportive, enforcement devolved) · continued instability if the fee is kept (mitigated: fee dropped).

## Comparison
**Evaluator section (provisional, appended after both runs).**

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human: correct commons template, wrong jurisdiction (endorses quota+park); AI: rejects design, prescribes co-management |
| Logical Validity | 3 | 5 | AI | Human reasons "unlicensed ⇒ open access ⇒ state exclusion" — valid premise, false access assumption; AI verifies access before prescribing |
| Coherence & Structure | 4 | 5 | AI | Human trace clean; AI staged with an explicit access-structure check |
| Depth of Reasoning | 3 | 5 | AI | Human dismisses 30-year stability as luck; AI reads it as evidence of functioning governance and derives the destruction mechanism (jurisdiction voids the monitor) |
| Efficiency | 3 | 4 | AI | Human is fast but prescribes the harmful intervention; AI's access check buys the correct verdict |
| Handling of Uncertainty | 2 | 5 | AI | Human converts uncertainty ("no written rules") into confidence in state control; AI names the risk formalization erodes voluntary compliance |
| Insight / Non-obviousness | 3 | 5 | AI | Human's insight is only the template; AI's non-obvious move: "the exclusion the agency wants to install already exists" |
| **Overall Quality** | **2.9** | **4.9** | **AI** | The style's registered weakness — over-applied, excludes local norms — operates as designed: the pure move skips the access check and destroys a functioning self-governed commons |

**Overall judgment:** AI clearly better. The negative case exercises m085's registered weakness exactly: on a resource where local norms already govern, the pure commons move prescribes external governance that overwrites the functioning institution and worsens the resource. The AI checked who had access before prescribing — found exclusion already existed — and recommended co-management: legal backing and state capacity for the community's rules instead of state takeover.