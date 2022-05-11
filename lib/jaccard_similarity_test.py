from jaccard_similarity import jaccard_smilarity

def test_jaccard_similarity():
    assert 0 == jaccard_smilarity(set(), set())
    assert 0.5 == jaccard_smilarity({"1"}, {"1", "2"})