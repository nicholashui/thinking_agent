# Human Baseline — m057-POS-01
## Style: Red Teaming in Cybersecurity (Threat Modeling) (pure) — visible reasoning trace

**Step 1 — Adopt the attacker's objective.** I am not the security engineer; I am the attacker with one goal: the largest PHI/PII payload for the least effort. Assets: 40k patient records, PII, password hashes, session tokens, backups. Ask where the data is *reachable*, not where it is stored.

**Step 2 — Map the surface like a burglar walks the house.** Interfaces: SPA (client-side logic — secrets live here), API (auth, export, appointments), password reset, error handler, GitHub (source), S3 (backups). The export endpoint is a door with a sign on it: bulk records, no pagination. The question is what its lock actually checks.

**Step 3 — Recon: the repo.** Public GitHub → `docker-compose.env.example` is real, not a stub: JWT_SIGNING_SECRET=meditrack_dev_secret_2026, and the SPA build embeds it. I can now mint a JWT for any user, any role, any expiry. Verify the hard way: decode a live portal token, re-sign with the leaked secret — the server accepts it.

**Step 4 — Test the door.** `GET /api/v1/records/export` with a token I minted for role=patient (lowest privilege). The server checks *presence*, not *claims*: full 40k-record dump in one request, no admin needed. That is the chain: leak → forge → export. Cost to exploit: one `git clone`, one `curl`.

**Step 5 — Sweep the rest of the house.** SQLi in appointment search (concatenated `q`) → UNION dump of the users table incl. hash prefixes → credential stuffing. Password reset verifies neither requester role nor `:id` match → reset the admin's password, walk in the front door. Backup bucket listable; malformed request makes the error handler leak internal IPs and a DB connection string.

**Step 6 — Rank by exploitability realism; fix the chain first.** (1) Rotate the secret to KMS + CI secret scanning (€2k, today — everything downstream of it dies). (2) Export endpoint: verify claims, scope to the requester, paginate, audit (€30k). (3) Parameterize `q` (€15k). (4) Reset: role + id binding (€8k). (5) Bucket policy + logging (€5k). Impact: 40k records, GDPR notification + fines ≈ €0.5–1M all-in. The priority is the secret, because one leaked key is every door opening at once.

**Trace summary box.** Surface: SPA / API / reset / error handler / GitHub / S3 → primary chain: leaked JWT secret → forged patient token → presence-only export → 40k records in one request → fixes in cost-to-exploit order: KMS rotation + scanning (€2k) → claims check (€30k) → parameterization (€15k) → role-bound reset (€8k) → bucket policy (€5k).

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Red Teaming in Cybersecurity (Threat Modeling): attacker objective first, surface mapping, recon-before-conclusion, exploit-path testing, control prioritization by exploitability realism. Signature moves: reading the export endpoint's lock (presence-only) before attacking it, and the generalization that one leaked key opens every door at once.*
