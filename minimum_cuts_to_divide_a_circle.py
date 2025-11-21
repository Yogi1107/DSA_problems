import math
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        if n % 2 == 0:
            return n//2
        else:
            return n
        
