#Leet code Questions Solutions. 

#Date : 17/08/2025
#Problem 459 : Repeated Substring Pattern

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         n = len(s)
#         for k in range(1, n // 2 + 1):
#             if n % k == 0:  # substring length must divide n
#                 substring = s[:k]
#                 if substring * (n // k) == s:
#                     return True
#         return False


        