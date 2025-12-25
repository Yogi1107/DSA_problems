from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # Sort happiness in descending order
        happiness.sort(reverse=True)
        
        total = 0
        
        for i in range(k):
            # Effective happiness after i decrements
            current = happiness[i] - i
            
            if current <= 0:
                break
            
            total += current
        
        return total
