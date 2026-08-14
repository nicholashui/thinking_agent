"""State reducers (impl plan §8.6).

Rules:
- append-like reducers are associative and idempotent per key;
- single-writer fields use plain overwrite (last write wins) and are only
  written by their designated owning nodes.
"""

from typing import Any


def append_by_key(key: str | None):
    """Append a list, deduplicating on `key` (or the whole item when key is None)."""

    def _reducer(left: list | None, right: list | None) -> list:
        out: list = []
        seen: set = set()
        for item in (left or []) + (right or []):
            if key is None:
                k = _stable(item)
            else:
                k = str(item.get(key)) if isinstance(item, dict) else _stable(item)
            if k in seen:
                continue
            seen.add(k)
            out.append(item)
        return out

    return _reducer


def merge_by_key(key: str | tuple[str, ...]):
    """Merge dict items on `key` (or a composite tuple of keys); later
    writes overwrite earlier ones for the same key (impl §8.6: candidate
    reports merge by candidate ID AND verifier identity; style results by
    style ID AND generation)."""
    keys = (key,) if isinstance(key, str) else key

    def _k(item: Any) -> str:
        if isinstance(item, dict):
            return "|".join(str(item.get(f)) for f in keys)
        return _stable(item)

    def _reducer(left: list | None, right: list | None) -> list:
        merged: dict[str, Any] = {}
        order: list[str] = []
        for item in (left or []) + (right or []):
            k = _k(item)
            if k not in merged:
                order.append(k)
            merged[k] = item
        return [merged[k] for k in order]

    return _reducer


def overwrite(left: Any | None, right: Any | None) -> Any:
    """Single-writer: the new value wins."""
    return right


def _stable(item: Any) -> str:
    import json

    if isinstance(item, (str, int, float, bool)):
        return str(item)
    return json.dumps(item, sort_keys=True, default=str)
