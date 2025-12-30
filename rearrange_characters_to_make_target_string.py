from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq_s = Counter(s)
        freq_t = Counter(target)

        ans = float('inf')
        for ch in freq_t:
            ans = min(ans, freq_s[ch] // freq_t[ch])

        return ans
