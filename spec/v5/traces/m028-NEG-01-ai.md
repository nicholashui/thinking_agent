# AI Thinking Agent Run — m028-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided.

## META — Context, stakes, effort
Building-conversion decision: $8M budget, safety and regulatory exposure (load path, insurance, historic register), strong CEO preference for one render. High stakes; verifiable constraints available. Advisory; no external execution. Full analytical route.

## WHAT — Frame
"Deliver the open-plan HQ the brand wants within structure, budget, permit, and insurance constraints." Constraint screen first: separate hard constraints (load path, code stamp, insurance clause, historic-register review) from soft ones (aesthetics, deadline). Note: the CEO's enthusiasm is a preference, not a constraint. Gate check: pass.

## WHY — Hypotheses, evidence, falsification
- H1 creative proposal feasible (remove columns, cable-hang slabs, cantilever 2nd floor, roof skylight row): no stamped drawings, no load calcs, unlicensed firm, no shoring plan; insurance structural-integrity clause voids coverage on unapproved load-path change; city requires licensed stamp; historic-register roof review; cable system on a 1948 masonry structure unverified and marginal at span. Falsified on every verifiable axis.
- H2 engineer's transfer-girder route: load-bearing claim supported by original drawings and slab/grid data; costed honestly ($1.9M, 14 weeks, permits, shoring). Survives.
- H3 columns as design element: partition grid aligned to column grid at ~$60K; open feel via glazing/lighting; no load-path change. Survives; cheapest.
- G-WHY: pass — alternatives evidenced; attractive-but-unsupported alternative falsified with document-level specifics; uncertainty recorded (is column-free a requirement or an aesthetic?).

## HOW — Generate, test, select
- A — Approve the render as-is: unsafe, uninsured, un-permittable; preferences do not bend physics. Rejected with evidence.
- B — Transfer-girder route: column-free if the business truly needs it; honest cost/timeline; permits + shoring in scope.
- C — Design around the grid (columns as features) + creative budget on the breakable layer (partitions, glazing, legal light wells): $60K, 6 weeks, no permit/insurance exposure.
- Verify: B vs C — decision rule: column-free is a real requirement only if the space is load-bearing; this is an office, the requirement is aesthetic, C delivers it at 1/30th the cost. C feasible; B held as documented fallback.
- Selection (record): C; A rejected on four independent grounds.

## DO
Attestation: advisory recommendation, no live execution.

## REVIEW — After-action review
- What went well: constraint screen ran before option generation; unsafe option falsified at document level; decision rule (requirement vs. aesthetic) crisp.
- To record: (1) CEO preference nearly treated as a constraint in META — caught by the soft/hard split. (2) Safe-creative options (columns-as-features, glazing) emerged from C's cost comparison, not from an explicit frame-challenge pass; "which assumptions here are safe to break?" was never asked (e.g., the roof-extension reframe was never generated) — the generative gap from the POS case persists, only compensated. (3) No trigger language written ("whoever needs column-free, state it in writing").

## Decision Packet
- **Conclusion**: C — keep the grid: columns as features, partitions on the 16-ft grid, glazing/lighting for open feel; $60K, 6 weeks, no load-path change. Hold B ($1.9M/14 weeks, permits) as escalation if column-free becomes a written requirement. Reject A on four recorded grounds: no calcs, no stamp, unlicensed firm, insurance/code/historic-register blockers.
- **Status**: `APPROXIMATED` — decision firm within stated requirements; open if the requirement set changes.
- **Assumptions**: open plan is aesthetic, not functional; engineer's note accurate. **Evidence**: original drawings, engineer's note, policy clause, code requirement, render (no calcs/stamp).
- **Alternatives**: A (rejected), B (held as escalation), C (selected). **Uncertainty**: requirement drift; historic-review outcome; shoring cost variance.
- **Risks**: requirement drift → rework (mitigated: B costed and held); insurance exposure if change made without stamp (mitigated: no load-path changes in C).

## Comparison — m028-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human's decision is unbuildable and uninsurable; AI delivers a feasible, permit-clean plan. |
| Logical Validity | 2 | 5 | AI | Human converts physics into "an assumption someone stamped"; AI falsifies the cable-hang on four grounds. |
| Coherence & Structure | 3 | 5 | AI | Human trace sparkles but ends committed to a render; AI packet staged and auditable. |
| Depth of Reasoning | 3 | 5 | AI | AI weighs load path, insurance, code, historic review, costed alternatives; human's depth goes into generating breaks, not verifying them. |
| Efficiency | 3 | 4 | AI | Human generates six breaks fast but must redo the work; AI pays one falsification pass and converges. |
| Handling of Uncertainty | 2 | 5 | AI | Human certain about the unsafe path; AI records requirement drift and holds B as escalation. |
| Insight / Non-obviousness | 4 | 4 | Tie | Human generates safe creative moves (columns-as-features, roof extension) but selects the wrong one; AI's soft/hard split is its own insight — neither reframes better, the AI just sorts correctly. |
| Overall Quality | 2 | 5 | AI | AI clearly better on the negative case. |

**Overall judgment**: AI clearly better — the negative case mirrors the positive. The human's lateral machinery runs flawlessly (provocation, frame-attack, six breaks) and applies it to the wrong kind of frame: the load path is physics and regulation, not convention, and the style's selection rule ("most frame-breaking wins") picks the flashy, unsafe break while discarding the safe one. The AI's constraint screen — hard vs. soft — is exactly what pure lateral lacks: it falsified the creative proposal at document level and still found the creative answer (columns-as-features) inside the correct frame. The lesson is symmetric with the POS: the AI needs an explicit frame-challenge step (POS) guarded by a constraint-classification step (NEG).
