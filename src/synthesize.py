"""Alchemist's synthesis engine."""
from typing import List, Dict

def synthesize(sources: List[Dict[str, str]]) -> Dict:
    concepts = set()
    for src in sources:
        words = src.get("idea", "").lower().split()
        concepts.update(w for w in words if len(w) > 4)
    return {
        "sources": [s["agent"] for s in sources],
        "shared_concepts": sorted(concepts),
        "novel": True
    }
