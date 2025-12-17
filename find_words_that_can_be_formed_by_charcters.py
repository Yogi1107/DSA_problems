from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0

        for word in words:
            # word_count = Counter(word)
            # if all(word_count[c] <= char_count[c] for c in word_count):
            #     total += len(word)
            if not (Counter(word) - char_count):
                total += len(word)


        return total
