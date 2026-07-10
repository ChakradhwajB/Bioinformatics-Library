from collections import Counter
from typing import List, Generator, Dict

def GenerateKmers(seq: str, k: int) -> Generator[str, None, None]:
    """
    Yields all Kmers with length k.

    Args:
        seq (str): The input sequence.
        k (int): The length of a kmer.
    Returns:
        Generator[str, None, None]: A generator function yielding all Kmers.
    """
    n = len(seq)
    if k <= 0 or k > n:
        return
        
    for i in range(n - k + 1):
        yield seq[i:i + k]

def CountKmers(seq: str, k: int) -> Dict[str, int]:
    """
    Outputs the count of each Kmer in a sequence.

    Args:
        seq (str): The input sequence.
        k (int): The length of a kmer.
    Returns:
        Dict[str, int]: A dict storing the Kmer sequence with the amount of Kmers.
    """
    return dict(Counter(GenerateKmers(seq, k)))

def MostFrequentKmers(seq: str, k: int) -> List[str]:
    """
    Outputs the most Frequent Kmers.

    Args:
        seq (str): The input sequence.
        k (int): The length of a kmer.
    Returns:
        List[str]: A list with kmers of maximum length.
    """
    counts = CountKmers(seq, k)
    
    if not counts:
        return []
        

    max_count = max(counts.values())
    
    return [kmer for kmer, count in counts.items() if count == max_count]