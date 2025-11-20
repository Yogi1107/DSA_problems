class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        while max_:
            min_, max_ = max_, min_ % max_
        return min_
        
