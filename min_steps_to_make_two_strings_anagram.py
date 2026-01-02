# from collections import Counter

# class Solution:
#     def minSteps(self, s: str, t: str) -> int:
#         count_s = Counter(s)
#         count_t = Counter(t)
        
#         steps = 0
#         for ch in count_t:
#             if count_t[ch] > count_s[ch]:
#                 steps += count_t[ch] - count_s[ch]
        
#         return steps

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(t) - Counter(s)).values())
