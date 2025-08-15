#Leetcode Problems

#Date:15/08/2025
#Problem : 326 :Power of three

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(32):
            if 3**i == n:
                return True
        return False
        