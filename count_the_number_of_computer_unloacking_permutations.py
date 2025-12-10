from typing import List

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)
        
        # If any computer i > 0 has complexity <= complexity[0], it's impossible
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        
        # Otherwise every ordering of the other n-1 computers works:
        # result = (n-1)! % MOD
        res = 1
        for x in range(2, n):  # multiply 2 * 3 * ... * (n-1)
            res = (res * x) % MOD
        
        return res

MOD = 10**9 + 7
facs = {}
facs[1] = 1
facs[2] = 2
for i in range(2,(10**5)+1):
    facs[i] = (facs[i-1] * i) % MOD

# class Solution:
#     def countPermutations(self, complexity: List[int]) -> int:

#         lowest = complexity[0]
#         for c in complexity[1:]:
#             if c <= lowest:
#                 return 0 
#         return facs[len(complexity)-1]
        

