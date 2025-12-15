class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 1   # first element
        streak = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                streak += 1
            else:
                streak = 1
            
            count += streak
        
        return count
