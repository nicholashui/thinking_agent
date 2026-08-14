"""No-Docker acceptance test (impl §0.3 / §25.6)."""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
FORBIDDEN = ["Dockerfile", "docker-compose.yml", "docker-compose.yaml",
             "compose.yml", "compose.yaml"]


def test_no_docker_artifacts():
    found = [str(p) for name in FORBIDDEN for p in REPO.rglob(name)
             if ".git" not in p.parts]
    assert found == [], found
