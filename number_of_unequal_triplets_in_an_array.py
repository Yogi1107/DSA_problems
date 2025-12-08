class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(nums)
        res = 0
        left = 0
        remaining = len(nums)
        
        for value, count in freq.items():
            remaining -= count
            # count triplets where this number is the middle one
            res += left * count * remaining
            left += count
        
        return res
