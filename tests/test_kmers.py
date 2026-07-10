from core_lib.kmers import (
    GenerateKmers,
    CountKmers,
    MostFrequentKmers,
)

def test_generate_kmers():
    assert list(GenerateKmers("ATGCG", 3)) == ["ATG", "TGC", "GCG"]
    assert list(GenerateKmers("AT", 3)) == []
    assert list(GenerateKmers("ATGCG", 0)) == []
    assert list(GenerateKmers("ATGCG", 5)) == ["ATGCG"]

def test_count_kmers():
    assert CountKmers("ATATAT", 2) == {"AT": 3, "TA": 2}
    assert CountKmers("AT", 3) == {}
    assert CountKmers("A", 1) == {"A": 1}

def test_most_frequent_kmers():
    assert MostFrequentKmers("ATATAT", 2) == ["AT"]
    assert set(MostFrequentKmers("ATGCGATG", 3)) == {"ATG"}
    assert MostFrequentKmers("AT", 3) == []

if __name__ == "__main__":
    test_generate_kmers()
    test_count_kmers()
    test_most_frequent_kmers()
    print("All k-mer tests passed!")
