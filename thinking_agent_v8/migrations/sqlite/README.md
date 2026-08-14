# SQLite migrations

Applied in order by `persistence/migrations.py`. Version `001` creates the
application tables (task runs, audit events, SDL ledger, gap map). Kernel
World-Facts live in `configs/kernel/*.yaml` — versioned, signed in
production — NOT in the application database (impl §19.2 separation).
