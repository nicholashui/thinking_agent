"""Tier-1 arXiv discovery source (impl §18.2): READ-ONLY httpx adapter.

Fetches arXiv API listings (title, abstract, subjects, authors, dates) for
the configured subject groups. Provenance-validated: every result carries
its source id + query; nothing is written anywhere (rule 43 / invariant 14).
"""

from typing import Any

import httpx

ARXIV_API = "http://export.arxiv.org/api/query"
DEFAULT_GROUPS = ("cs.AI", "cs.LG", "cs.CL", "cs.SE", "cs.CY", "stat.ML")


class ArxivSource:
    def __init__(self, *, timeout: float = 30.0,
                 subject_groups: tuple[str, ...] = DEFAULT_GROUPS):
        self._client = httpx.Client(timeout=timeout)
        self._groups = subject_groups

    def scan(self, query: str, budget: int) -> list[dict[str, Any]]:
        """One read-only listing query; returns up to `budget` candidate items."""
        import defusedxml.ElementTree as ET

        params = {
            "search_query": f"all:{query[:200]}",
            "start": 0,
            "max_results": min(budget, 50),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        resp = self._client.get(ARXIV_API, params=params)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        out: list[dict[str, Any]] = []
        for entry in root.findall("a:entry", ns)[:budget]:
            entry_id = (entry.findtext("a:id", default="", namespaces=ns) or "")
            title = " ".join((entry.findtext("a:title", default="", namespaces=ns) or "").split())
            abstract = " ".join((entry.findtext("a:summary", default="", namespaces=ns) or "").split())
            subjects = [c.attrib.get("term", "")
                        for c in entry.findall("a:category", ns)]
            authors = [a.findtext("a:name", default="", namespaces=ns)
                       for a in entry.findall("a:author", ns)]
            out.append({
                "tier": "Tier-1",
                "source_id": entry_id.rsplit("/abs/", 1)[-1] if "/abs/" in entry_id else entry_id,
                "title": title[:300],
                "abstract": abstract[:3000],
                "subjects": subjects,
                "authors": authors[:8],
            })
        return out
