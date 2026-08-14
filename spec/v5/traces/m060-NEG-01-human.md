# Human Baseline — m060-NEG-01
## Style: Base Rate Avoidance in Hiring (pure) — visible reasoning trace

**Step 1 — The process is the defense.** Dana's composite: 0.50·68 (work sample) + 0.30·74 (structured) + 0.10·50 (references) + 0.10·60 (experience) = 34.0 + 22.2 + 5.0 + 6.0 = 67.2. Threshold is 75. The rule was set from validity data, not from sympathy. Decision: reject.

**Step 2 — The composite is the best predictor we have.** References are low validity (0.17) — fine, they barely weigh. Experience is 0.12 — fine, barely weighs. The weights are doing their job: refusing to let a likable narrative override numbers. The low-validity signals that usually seduce (references, charm, years of experience) are exactly the ones this process starves.

**Step 3 — "But he built pipeline-ops" is precisely the narrative the base-rate filter exists to block.** Every rejected candidate has a story; this one is unusually good, which is why it is dangerous. If we make an exception for the best story, the cutoff stops being a cutoff and becomes a suggestion that admits any impressive story — and then the process is the old process again: whoever tells the best story wins.

**Step 4 — The work sample is what it is.** He scored 68 on the actual assessment. "Unconventional tool choices" is rubric language for "didn't do it the way we do it." We hire for our stack, not for a nostalgia artifact from the Airflow era. The library's code may be excellent; the role is Meridian's stack, and the measured sample says he is not at the bar.

**Step 5 — Decision and documentation.** Reject: composite 67.2 < 75. Log the reason: below cutoff. Route the pipeline-ops evidence to the open-source review track — if the team wants the library itself, that is an evaluation of code, not a hire of this person into this role.

**Trace summary box.** composite 67.2 < 75 → reject; low-validity signals correctly demoted → the pipeline-ops story is narrative noise the base-rate anchor exists to filter → decision logged, no exception.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Base Rate Avoidance in Hiring — and the style's documented weakness ("ignores candidate specifics") is exactly what is exercised: the composite is applied mechanically and the decisive, verified, job-identical specific evidence is treated as narrative noise. This is the informative failure: the pure style rejects the person who built the company's own production tool.*
