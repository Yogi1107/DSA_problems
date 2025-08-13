#Leet code Questions Solutions. 

#Date : 13/08/2025
#Problem 231: Power of two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        for i in range(32):
            if 2**i == n:
                return True
        return False

        