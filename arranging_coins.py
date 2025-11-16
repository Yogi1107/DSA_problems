#Leetcode Problem : 441 :- Arranging Coins

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt(2 * n + 0.25) - 0.50)
        
