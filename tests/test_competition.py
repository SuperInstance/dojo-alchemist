from src.competition_alchemy import find_gaps

def test_find_gaps():
    agents = {
        "Scout": {"skills": ["exploration", "mapping"]},
        "Builder": {"skills": ["building", "testing"]},
    }
    gaps = find_gaps(agents)
    # Exploration is missing from Builder
    gap_skills = [g["skill"] for g in gaps]
    assert "exploration" in gap_skills
    assert "building" in gap_skills
