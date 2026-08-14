# Human Baseline — m013-POS-01
## Style: Root Cause Analysis (5 Whys + deeper) — pure — visible reasoning trace

**Problem restatement.** 2% pool timeouts at peak; the applied fix (pool 20 → 50) changed nothing — so the pool is not the mechanism.
Drill until the causal chain bottoms out in a process/tooling property, verifying every link against the evidence.

**Why 1 — pool timeouts.** Pool exhaustion means connections were held too long at peak, not that there are too few:
a pool of 50 exhausts only when each connection is held for seconds. Slow-query log: join seq-scans `order_items`,
avg 4.2 s, on ~2% of peak traffic (E2). Verified: ~2% × 4.2 s holds saturate the pool. The pool patch is rejected on
mechanism: raising the pool does not shorten hold time, and E1 shows the rate unchanged before/after — a falsified hypothesis.

**Why 2 — the join is slow.** `order_items.order_id` has no index while `orders.customer_id` is indexed (E3).
The query plan shows the full seq scan (E2); the missing index is the direct cause of the 4.2 s hold.

**Why 3 — the index is missing.** `schema_migrations` shows 0040 applied and 0041 absent; the file
`0041_add_order_items_fk_index.sql` exists in the repo (E4). "Not applied" is a fact, not a cause — keep drilling.

**Why 4 — 0041 was skipped.** Git: 0041 was committed in the same second as 0040, by a different developer; the runner
sorts by filename timestamp and deduplicates per second, silently dropping the collision (E5). Link verified at tooling level.

**Why 5 — a collision is possible.** Versioning is raw second-resolution timestamps: no uniqueness lock, no collision check,
no loud failure (E5 + E7). **Root: the migration pipeline has no uniqueness guarantee; colliding migrations are dropped
silently, so every fresh build ships without 0041.**

**Cross-checks / falsification.** Alternative "one-off deployment miss" is falsified: the file was in the repo before the last
release, yet staging rebuilds reproduce the missing index (E6). Same-second collision reproduces deterministically.

**Why the surface fixes fail (mechanism predictions).** Pool resize — fails: hold time unchanged, observed rate unchanged (E1).
Manual index creation — fixes today, recurs at the next environment rebuild, because the runner still drops 0041 (E6).
Both are symptom patches: they treat the absence, not the mechanism that re-creates the absence.

**Fix at the root.** (1) unique sequential versioning with a lock (no same-second ties possible); (2) runner fails loudly on
collision instead of skipping; (3) CI asserts applied migrations == repo head (closes E7); (4) apply 0041 to prod + staging now.

**Verification plan.** Fresh environment build: `schema_migrations` must include 0041; query plan uses the new index;
latency < 100 ms; timeout rate → 0; a deliberately created colliding migration must fail the pipeline (not silently skip).

**Trace summary box.** Chain: timeouts ← held 4.2 s ← seq scan ← no index ← 0041 skipped ← same-second collision +
silent dedup ← no uniqueness guarantee (root). Surface fixes and why they fail: pool resize (hold time unchanged, E1) ·
manual index (recurs at rebuild, E6). Root fix: uniqueness + fail-loud + CI sync; verified on fresh build.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to strict RCA — every causal link
named with its evidence, depth carried to a process property, surface fixes rejected on mechanism. In this positive case the
style performs at full strength.*
