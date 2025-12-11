class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return int((list(s).count(letter) * 100) / len(s))
