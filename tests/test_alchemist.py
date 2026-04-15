from src.synthesize import synthesize

def test_synthesize():
    result = synthesize([
        {"agent": "Scout", "idea": "exploration territory mapping pattern"},
        {"agent": "Builder", "idea": "building construction pattern testing"}
    ])
    assert len(result["sources"]) == 2
    assert result["novel"]
    assert "pattern" in result["shared_concepts"]
