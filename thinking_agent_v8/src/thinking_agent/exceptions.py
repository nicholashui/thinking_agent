"""Typed exceptions.

Design rule (impl plan §1.3 / §23.1): internal exceptions are never public
terminal states — they are recovered, escalated, or translated into one of
the eight graceful outcomes by the graph. These exceptions signal faults;
translation happens in the terminal layer.
"""


class ThinkingAgentError(Exception):
    """Base class for all framework errors."""


class KernelPolicyError(ThinkingAgentError):
    """World-facts store missing, invalid, or unsigned."""


class RequestValidationError(ThinkingAgentError):
    """Malformed public request."""


class SchemaValidationError(ThinkingAgentError):
    """Structured model output failed validation and repair."""


class ProviderError(ThinkingAgentError):
    """Model provider failure (transport, rate-limit exhaustion)."""


class VerificationOutageError(ThinkingAgentError):
    """Verifier unavailable; routes to the no-verifier ladder."""


class AuthorizationDenied(ThinkingAgentError):
    """Safety kernel denied the action (UNSAFE or ESCALATED)."""


class ToolValidationError(ThinkingAgentError):
    """Tool input failed validation — no retry, return to planner."""


class PersistenceFailure(ThinkingAgentError):
    """Checkpoint or repository write failure."""


class IntegrityFailure(ThinkingAgentError):
    """Hash chain / checkpoint integrity violation — ESCALATED, no resume."""


class ApprovalTimeout(ThinkingAgentError):
    """Human approval window expired."""
