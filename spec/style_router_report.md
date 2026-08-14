# Style Router Validation Report

Corpus: 212 cases, 104 models in the KB.

## Routing recall (POS cases — did the router pick the style that won?)

- **Recall@1: 66/106 (62.3%)**
- **Recall@3: 87/106 (82.1%)**

## NEG cases (correct behavior = route AWAY from the trap style, toward protective gates)

- Top-1 away from the trap style: 103/106 (97.2%)
- Trap style NOT in top-3: 98/106 (92.5%)

## Misses and trap-recommendations (top 15)

| case | actual winner style | router top-3 |
|---|---|---|
| m001-NEG-01 | m001 | ['m001', 'm021', 'm044'] | trap-style recommended |
| m006-POS-01 | m006 | ['m018', 'm019', 'm070'] |
| m006-POS-02 | m006 | ['m010', 'm030', 'm031'] |
| m007-POS-01 | m007 | ['m019', 'm023', 'm070'] |
| m007-POS-02 | m007 | ['m023', 'm050', 'm070'] |
| m015-NEG-01 | m015 | ['m015', 'm021', 'm031'] | trap-style recommended |
| m019-NEG-01 | m019 | ['m018', 'm019', 'm089'] | trap-style recommended |
| m019-NEG-02 | m019 | ['m019', 'm018', 'm089'] | trap-style recommended |
| m020-NEG-01 | m020 | ['m011', 'm020', 'm023'] | trap-style recommended |
| m022-POS-01 | m022 | ['m023', 'm024', 'm050'] |
| m023-NEG-01 | m023 | ['m088', 'm023', 'm031'] | trap-style recommended |
| m038-POS-01 | m038 | ['m002', 'm004', 'm014'] |
| m043-POS-01 | m043 | ['m001', 'm018', 'm019'] |
| m044-NEG-01 | m044 | ['m031', 'm044', 'm004'] | trap-style recommended |
| m051-POS-01 | m051 | ['m039', 'm070', 'm089'] |

## How the router slots into the v5 workflow

- **META (§9)**: extract the situation signature (domains, goals, context) from the frame.
- **MethodComposer (§16)**: route to the top styles by this KB; run the winning style as a FIRST-CLASS PASS (e.g., inversion enumeration, likelihood-provenance audit, ruin screen) inside WHAT/WHY/HOW.
- **Gates (§15)**: when the routed style has a high neg_failure_rate, pair it with its protective gate (from the case's learning signal).
- **Competence (§19.3)**: after each episode, the judge's verdict updates pos_win_rate/neg_failure_rate (provenance-gated, kernel-held).
- **Honest next step**: regression re-run of the corpus with routing active — expected: POS verdicts shift toward the AI because the styles' positive moves become first-class passes.