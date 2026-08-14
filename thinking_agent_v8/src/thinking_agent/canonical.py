"""Canonical JSON and hashing utilities (impl plan §8.1).

All content hashes in the system go through `canonical_json` + `sha256_hex`
so that dict ordering never changes a hash.
"""

import hashlib
import json
from typing import Any


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str
    ).encode("utf-8")


def sha256_hex(value: Any) -> str:
    if isinstance(value, (bytes, bytearray)):
        return hashlib.sha256(bytes(value)).hexdigest()
    return hashlib.sha256(canonical_json(value)).hexdigest()


def content_hash(value: Any) -> str:
    """Short 16-char hash for state signatures."""
    return sha256_hex(value)[:16]


class FrozenDict(dict):
    """A dict subclass whose mutating methods raise. Serializes as a plain
    dict (JSON round-trip clean), so it is safe for pydantic frozen models
    where `MappingProxyType` would break serialization.

    Copy support: `copy.copy`/`copy.deepcopy` rebuild via the C-level
    constructor, bypassing the frozen mutators, so `model_copy(deep=True)`
    works on frozen models holding FrozenDicts."""

    def _immutable(self, *args, **kwargs):
        raise TypeError("FrozenDict is immutable")

    __setitem__ = _immutable
    __delitem__ = _immutable
    clear = _immutable
    pop = _immutable
    popitem = _immutable
    setdefault = _immutable
    update = _immutable
    __ior__ = _immutable

    def __copy__(self):
        return FrozenDict(self)

    def __deepcopy__(self, memo):
        import copy
        out = FrozenDict()
        memo[id(self)] = out
        for k, v in self.items():
            dict.__setitem__(out, copy.deepcopy(k, memo), copy.deepcopy(v, memo))
        return out
