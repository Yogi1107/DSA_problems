#leetcode problem
#Problem 1967 : Number of Strinmgs that appear as substring in word
#Date: 16-09-2025

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count
