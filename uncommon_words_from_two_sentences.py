#Leet code Questions Solutions. 

#Date : 30/09/2025
#Problem 844 : Uncommon Words from two sentences

from collections import Counter
from typing import List

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        all_words = s1.split() + s2.split()

        word_counts = Counter(all_words)

        result = [word for word, count in word_counts.items() if count == 1]

        return result