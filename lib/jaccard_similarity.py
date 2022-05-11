
from typing import Set


def jaccard_smilarity(set1: Set[str], set2: Set[str]) -> float:
    if len(set1) == 0 and len(set2) == 0:
        return 0.0
    return (len(set1.intersection(set2))/len(set1.union(set2)))