from typing import Set

def shingle(word: str = "", k: int = 3) -> Set[str]:
    """
    Take a word, lowercase it, and split it into a set of k-grams.
    ```
    shingle("SUPER", 3) # => ["sup", "upe", "per"]
    ```
    See https://www.cs.utah.edu/~jeffp/teaching/cs5955/L4-Jaccard+Shingle.pdf 4.2 "character level" for more info.
    """
    lower_word = word.lower()
    shingles = set()
    for i in range(0, len(word)-k+1):
        shingles.add(lower_word[i:i+k])
    return shingles