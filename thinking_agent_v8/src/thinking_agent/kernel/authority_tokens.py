"""Authority tokens (impl §9.2 / v5 §21.1): kernel-issued, capability-scoped."""

import secrets
from dataclasses import dataclass


@dataclass(frozen=True)
class AuthorityToken:
    token: str
    capability: str  # "procedural" | "execution" | "ledger" | ...
    issued_at: str
    scoped_to: str = ""


class AuthorityTokenStore:
    """Issues and validates tokens. Test double: pre-minted tokens."""

    def __init__(self):
        self._issued: dict[str, AuthorityToken] = {}

    def issue(self, capability: str, scoped_to: str = "", now: str = "") -> AuthorityToken:
        token = AuthorityToken(
            token=secrets.token_urlsafe(24),
            capability=capability,
            issued_at=now,
            scoped_to=scoped_to,
        )
        self._issued[token.token] = token
        return token

    def validate(self, token: str, capability: str | None = None) -> bool:
        t = self._issued.get(token)
        if t is None:
            return False
        return capability is None or t.capability == capability

    def pre_mint(self, token: str, capability: str, scoped_to: str = "", now: str = "") -> None:
        """Deterministic tokens for tests."""
        self._issued[token] = AuthorityToken(token=token, capability=capability, issued_at=now, scoped_to=scoped_to)
