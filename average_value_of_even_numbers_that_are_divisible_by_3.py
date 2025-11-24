class Solution:
    def averageValue(self, nums: List[int]) -> int:
        result = []
        
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                result.append(i)
        
        if not result:
            return 0
        
        return sum(result) // len(result)
