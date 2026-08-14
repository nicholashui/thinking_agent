#!/usr/bin/env python3
"""Deep-review amendments for thinking_agent.v6.md — ADDITIONS ONLY.
Inserts the strengthened mechanisms at their logical anchors, then appends
§II.10 (the deep-review change log) before the final End-of-document."""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = os.path.join(ROOT, "thinking_agent.v6.md")
s = io.open(p, encoding="utf-8").read()

# --- A) §II.2.8 + §II.2.9: insert after the §II.2.7 block (before "## II.3") ---
block_2 = """
### II.2.8 Routing-confidence gate (deep review)

The measured recall (62.3% @1, 82.1% @3 on positive cases) means the winning
style is NOT first for ~38% of situations and not in top-3 for ~18%. To
overperform reliably, routing must not gamble on a single pick:

```text
G1  If top-1 score - top-2 score <= AMBIGUITY_THRESHOLD (default 0.5), the
    signature is AMBIGUOUS: run the top-2 style passes and synthesize
    (divergence resolution, §II.4.4).
G2  If top-1 score <= MIN_ROUTE_SCORE (default 1.0), no style has evidence
    for this signature: run the general loop with ALL mandatory protective
    gates (R3) and record the situation as a CURRICULUM GAP — it becomes a
    new scenario through absorb-and-learn (§II.4.1).
G3  The routing decision (signature, scores, gate taken) is recorded in the
    packet's routing section — routing is auditable per episode.
G4  IDF-weighted trigger scoring (§II.2.5) is MANDATORY v1.1, not optional:
    every curriculum update recomputes trigger weights by rarity across the
    100 models before the next routing pass.
```

### II.2.9 Style-pass contracts (deep review)

The corpus's style-adoption failure was the agent reaching style moves late or
partially (inversion categories at REVIEW, likelihood scenarios undeclared,
exposure magnitudes unquantified). Every routed module therefore has an
OBJECTIVE COMPLETION CONTRACT — a pass that does not produce its outputs is
not complete and is re-run (bounded by the loop monitor) or reported as a
gate failure:

| Module | Mandatory outputs (completion contract) |
|---|---|
| m003 Inversion pass | >= 6 failure categories, ranked by likelihood x impact, un-mitigable residual named, "never/always" reframing stated |
| m006 Provenance audit | >= 3 likelihood parameter scenarios, posterior range, decision-threshold flip demonstrated, artifact in packet |
| m007 Ruin screen | full outcome distribution, log-utility/ruin check, one-shot check, floor/Kelly computation, probability provenance, decline/restructure alternative |
| m019 Adversary pass | enumerated exploit vectors (guessable formats, identity gates), quantified exposure per vector, unconsulted stakeholders, baseline-risk comparison |
| m011 Systems scan | stocks/flows/loops named, falsifying observable stated, local-data-first check, cheap-fix-as-decisive-experiment |
| m022 Branch enumeration | every decision branch priced incl. negative/failure branch, sensitivity on probabilities |
| m033 Experiment design | intervention, control, randomization, blinding, exact outcome measure |
| m097 Reference-class forecast | reference class named, base-rate distribution stated, inside/outside view separated |

The registry's strengths (winning moves) and weaknesses (trap triggers) are
the pass's checklist: strengths must be demonstrated, weaknesses must be
gate-checked (R2/R3).
"""

anchor_2 = "\n## II.3 The Embedded Curriculum (extends v5 §23)"
assert anchor_2 in s
s = s.replace(anchor_2, block_2 + anchor_2, 1)

# --- B) §II.3.1-3: insert before "## II.4" ---
block_3 = """
### II.3.1 Drift monitoring and curriculum expansion (deep review)

"All time" requires the configuration to stay true as the world changes:

```text
D1  KB rate drift: if any style's pos_win_rate or neg_failure_rate moves
    more than 0.2 since its last evaluation, the style is RE-EVALUATED on a
    blind sample of its historical records (§II.2.6) before further routing.
D2  Domain drift: if a signature class's routed outcomes degrade (win rate
    below target for 2 consecutive curriculum passes), the class is flagged
    and new scenarios are generated for it (absorb-and-learn, §II.4.1).
D3  Expansion cadence: at least one new scenario per curriculum pass (from
    losses, drift flags, or domain gaps); the configuration grows, never
    shrinks without a judge verdict.
D4  Blind re-runs: quarterly, a stratified 10% sample of §II.2.6 is re-run
    blind to detect judge or router drift.
```

### II.3.2 The overperformance contract (deep review)

"Overperform human" is defined operationally and tracked per curriculum pass
in comparison_matrix.csv:

```text
T1  Per-signature win rate: for every signature class with >= 5 historical
    records, the agent's win rate must be >= 0.5 (target >= 0.7 after the
    deep-gap modules land) — this is the routing-level overperformance
    definition.
T2  Style-home-turf closure: the POS split must trend toward >= 50% AI wins
    as modules install (current baseline: 2/106 — the entire purpose of the
    style library).
T3  Protective split held: NEG split must stay >= 90% AI wins (current:
    100/106 = 94.3%).
T4  Dimension floors: efficiency >= 4.3 and insight >= 4.3 (current 4.07 /
    4.12) via the closed-scope fast path (P8) and the insight pass (§II.4.5).
T5  Calibration: judge scores agree with human-expert scores on a monthly
    20-case calibration sample at >= 80% verdict agreement.
```

The contract's honest current state is stated in §II.8: the agent does not
yet meet T2; the contract defines the measured path and the convergence
criterion for "all time" — every curriculum pass must move T1-T5 toward
target, and a pass that does not is itself a curriculum item.

### II.3.3 Judge integrity (deep review)

```text
J1  Contested verdicts (margin <= 0.3 or judge confidence low): a second
    independent judge scores the episode; disagreement is escalated to the
    human-expert calibration panel.
J2  Calibration cadence: monthly, 20 stratified cases scored by human
    experts; judge verdicts re-weighted by agreement (provenance-gated).
J3  The judge is outside the model's write path (invariant 11 applies to
    verdicts as to KB writes): the model may challenge a verdict; it may
    not change one.
"""
anchor_3 = "\n## II.4 Absorb-and-Learn (extends v5 §22)"
assert anchor_3 in s
s = s.replace(anchor_3, block_3 + anchor_3, 1)

# --- C) §II.4.4 + §II.4.5: insert before "## II.5" ---
block_4 = """
### II.4.4 Divergence resolution: style pass vs general route (deep review)

The corpus's meta-pattern: the AI's machinery wins protective cases, the
styles win home-turf cases — the all-time winning move is BOTH, checked
against each other:

```text
V1  When a style pass (R1) produces a conclusion, the general route's
    conclusion for the same stage is also produced (or the last general
    route result retained).
V2  If they AGREE: proceed; the agreement is recorded in the packet.
V3  If they DISAGREE: run branch-completeness (P3) and the calibration pass
    (P4) on BOTH conclusions before selection; the disagreement and its
    resolution are recorded in the packet's risks.
V4  If the style pass fails its completion contract (§II.2.9): the general
    route governs, and the failure is a curriculum item (the module is
    re-run or improved via absorb-and-learn).
```

### II.4.5 Insight pass and structure-first scan (deep review)

The corpus's two lowest AI dimensions (insight 4.12, structure-at-first-sight
losses) get explicit passes:

```text
S1  STRUCTURE-FIRST SCAN (WHAT/WHY entry): before arithmetic, name the
    structure — stocks/flows/loops/equilibria (m011), decision tree shape
    (m022), causal graph (m055), incentive alignment (m083), game structure
    (m073). The scan's outputs enter the frame; the scan is mandatory when
    the signature contains systems/causal/org/finance domains.
S2  INSIGHT PASS (HOW exit, before the packet): require 1-2 non-obvious
    observations — a counterintuitive implication, a hidden branch (LR-),
    a reframing, or a calibration surprise. A packet without an insight
    entry is incomplete (packet gate).
```
"""
anchor_4 = "\n## II.5 Algorithm deltas (extends v5 §24.4)"
assert anchor_4 in s
s = s.replace(anchor_4, block_4 + anchor_4, 1)

# --- D) §II.5 pseudocode: add the new gates (insert before closing ``` of the code block) ---
old_code_tail = """# REVIEW (epilogue):
verdict = judge.score(state, protocol_8_dimensions)       # §II.3
KB.update(state.styles, verdict)                          # invariant 11, kernel write
if verdict.loser_is_us: absorb_and_learn(state, verdict)  # §II.4.1
```"""
new_code_tail = """# REVIEW (epilogue):
verdict = judge.score(state, protocol_8_dimensions)       # §II.3
KB.update(state.styles, verdict)                          # invariant 11, kernel write
if verdict.loser_is_us: absorb_and_learn(state, verdict)  # §II.4.1
drift_check(state, KB)                                    # §II.3.1 D1-D2
if packet_missing_insight(state): run_insight_pass(state) # §II.4.5 S2
```"""
assert old_code_tail in s
s = s.replace(old_code_tail, new_code_tail, 1)

# --- E) Rules 36-38 (append to the §II.6 rules block, before "## II.7") ---
old_rules = "35. A style whose failure mode is known must be paired with its gate. (R2/R3)"
new_rules = """35. A style whose failure mode is known must be paired with its gate. (R2/R3)
36. A routed style pass that does not produce its completion contract has not run. (§II.2.9)
37. When routing is ambiguous, run two styles and synthesize — never a single unconfident pick. (§II.2.8)
38. The overperformance contract is tracked every pass; a pass that does not move T1-T5 toward target is itself a curriculum item. (§II.3.2)"""
assert old_rules in s
s = s.replace(old_rules, new_rules, 1)

# --- F) §II.10 deep-review change log (append before the final End-of-document) ---
block_10 = """
## II.10 Deep-review amendments (2026-08-07)

Deep review of the assembled v6 toward the overperformance objective —
ADDITIONS ONLY (no detail removed; no wrong content found: all numbers
re-verified — 212/212 records, 107/102/3 tally, 82.1/62.3/97.2 routing,
harness 177/177 + 187/187, deterministic).

| ID | Review finding | Amendment | Where |
|---|---|---|---|
| R1 | Routing recall leaves ~18% of situations without the winning style in top-3 | Routing-confidence gate (dual-route on ambiguity, curriculum-gap on no evidence); IDF v1.1 mandatory | §II.2.8, §II.2.5 |
| R2 | Style adoption was partial/late in the corpus | Objective completion contracts per module; incomplete pass = not run | §II.2.9 |
| R3 | No check between the routed style and the general route | Divergence resolution (agree → proceed; disagree → branch-complete + calibrate both) | §II.4.4 |
| R4 | "Overperform in all time" was not operational | The overperformance contract: T1-T5 targets, tracked per pass, honest baseline stated | §II.3.2 |
| R5 | No drift/expansion governance for sustained performance | Drift monitoring (KB rates, domain), blind re-runs, expansion cadence | §II.3.1 |
| R6 | Judge single-point-of-failure | Second judge on contested verdicts; monthly human calibration | §II.3.3 |
| R7 | Insight (4.12) and structure-at-first-sight deficits | Insight pass (packet gate) + structure-first scan | §II.4.5 |
| R8 | New rules missing | Rules 36-38; pseudocode gates added | §II.6, §II.5 |

Honest status: the amendments define the measured path to overperformance
(T1-T5); the end-to-end regression re-run (routing + modules active on the
corpus) remains the documented next proof (§II.8, §II.9). The claim "will
overperform humans in all time" is not asserted — the CONTRACT that converges
toward it, with tracking and failure detection, is what the document now
specifies.
"""
assert s.rstrip().endswith("*End of document.*")
s = s.rstrip()
s = s[: -len("*End of document.*")] + block_10 + "\n---\n\n*End of document.*\n"
io.open(p, "w", encoding="utf-8").write(s)
print("amendments applied")
