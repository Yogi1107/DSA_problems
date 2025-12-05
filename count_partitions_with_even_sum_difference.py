from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        # If total sum is odd, difference (leftSum - rightSum) = 2*leftSum - total
        # will always be odd for any leftSum → no valid partitions
        if total % 2 != 0:
            return 0
        # Otherwise, for every valid split point 0 <= i < n-1, partition difference is even
        return len(nums) - 1
