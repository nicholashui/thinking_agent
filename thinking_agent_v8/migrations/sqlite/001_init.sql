-- Thinking Agent v8 — application schema, migration 001
-- Writers per impl §19.3: kernel tables are operator-written only;
-- judge-pipeline tables are append-only at the application layer.

CREATE TABLE IF NOT EXISTS task_runs (
  task_id TEXT PRIMARY KEY,
  thread_id TEXT NOT NULL,
  terminal_status TEXT NOT NULL,
  packet_json TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS audit_events (
  event_id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  stage TEXT NOT NULL,
  component TEXT NOT NULL,
  event_type TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sdl_ledger_entries (
  sequence_number INTEGER PRIMARY KEY AUTOINCREMENT,
  entry_id TEXT NOT NULL UNIQUE,
  entry_type TEXT NOT NULL,
  challenge_id TEXT,
  verdict TEXT,
  payload_hash TEXT NOT NULL,
  hash_prev TEXT NOT NULL,
  hash TEXT NOT NULL,
  created_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS sdl_gap_map (
  gap_id TEXT PRIMARY KEY,
  signature_key TEXT NOT NULL UNIQUE,
  gap_type TEXT NOT NULL,
  magnitude REAL NOT NULL,
  evidence_ref TEXT NOT NULL,
  last_updated TEXT NOT NULL
);
