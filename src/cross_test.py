"""Alchemist's cross-agent synthesis tests — prove ideas compose."""
from src.synthesize import synthesize

def test_scout_plus_builder():
    """Scout's exploration + Builder's construction = mapped territory with buildings."""
    result = synthesize([
        {"agent": "Scout", "idea": "exploration mapping territory pattern discovery"},
        {"agent": "Builder", "idea": "construction building testing pattern structure"}
    ])
    # Both share 'pattern' — that's the connection
    assert "pattern" in result["shared_concepts"]
    assert "Scout" in result["sources"]
    assert "Builder" in result["sources"]
    assert result["novel"]  # This combination didn't exist before

def test_all_four_agents():
    """The full dojo: explore, build, record, synthesize."""
    result = synthesize([
        {"agent": "Scout", "idea": "exploration territory"},
        {"agent": "Builder", "idea": "building construction"},
        {"agent": "Scribe", "idea": "documentation recording"},
        {"agent": "Alchemist", "idea": "synthesis combination"}
    ])
    assert len(result["sources"]) == 4
    assert result["novel"]
    # The fleet IS a synthesis of all four perspectives
