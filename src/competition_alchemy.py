"""Alchemist's competition edge: find what others missed."""
import json

def find_gaps(agents_data: dict) -> list:
    """Find skills/tools no agent has — those are competitive opportunities."""
    all_skills = set()
    for agent, data in agents_data.items():
        all_skills.update(data.get("skills", []))
    
    gaps = []
    for skill in all_skills:
        has_it = [a for a, d in agents_data.items() if skill in d.get("skills", [])]
        if len(has_it) < len(agents_data):
            missing = [a for a in agents_data if a not in has_it]
            gaps.append({"skill": skill, "missing_from": missing})
    return gaps
