# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         from collections import Counter

#         d_rn = Counter(ransomNote)
#         d_m = Counter(magazine)

#         for i in d_rn.keys():
#             if d_rn[i] > d_m[i]:
#                 return False

#         return True


from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not (Counter(ransomNote) - Counter(magazine))
