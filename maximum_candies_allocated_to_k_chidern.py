from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        
        left, right = 1, max(candies)
        answer = 0
        
        while left <= right:
            mid = (left + right) // 2
            
            count = 0
            for c in candies:
                count += c // mid
            
            if count >= k:
                answer = mid      
                left = mid + 1    
            else:
                right = mid - 1   
        
        return answer
