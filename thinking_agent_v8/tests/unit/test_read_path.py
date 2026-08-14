"""Read-path assertion (impl §9.5, v5 V1): task nodes never read security
knobs from request/state/config; packet schema cannot override knobs."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from thinking_agent.domain.decision_packet import DecisionPacket  # noqa: E402
from thinking_agent.kernel.policy_audit import (  # noqa: E402
    assert_no_knob_override_fields,
    scan_directory,
)

SRC = Path(__file__).resolve().parents[2] / "src" / "thinking_agent"


def test_task_plane_has_no_knob_reads():
    violations = scan_directory(SRC)
    assert violations == [], [str(v) for v in violations[:5]]


def test_packet_cannot_override_kernel_knobs():
    fields = set(DecisionPacket.model_fields)
    assert assert_no_knob_override_fields(fields) == []
