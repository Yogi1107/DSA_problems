class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m] -= 1
            for c in left:
                if right[c] > 0:
                    res.add((m,c))
            left.add(m)
        return len(res)
        
# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:   
#         if len(s) <= 2:
#             return 0

#         chars = set(s)
#         res = 0
#         for ch in chars:
#             first = s.find(ch)
#             last = s.rfind(ch)

#             if first != last:
#                 res += len(set(s[first + 1:last]))

#         return res
