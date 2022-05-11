from shingle import shingle


def test_shingle():
    word = "Hi Mom"
    shingles = shingle(word, 3)
    assert shingles == {"hi ", "i m", " mo", "mom"}


test_shingle()