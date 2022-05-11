from main import potential_duplicates

def test_potential_duplicates():
    assert {"hi"} == potential_duplicates({"1", "2"}, {"1": {"hi"}, "3": {"mom"}})