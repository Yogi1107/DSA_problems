# class Solution:
#     def maxSubarraySum(self, nums: List[int], k: int) -> int:
#         prefix = [float("inf")]*k
#         prefix[0] = 0
#         res = float('-inf')
#         total = 0

#         for i, n in enumerate(nums):
#             total += n
#             length = i + 1
#             prefix_length = length % k
#             res = max(res, total - prefix[prefix_length])
#             prefix[prefix_length] = min(prefix[prefix_length], total)

#         return res
        
from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        least_pre = [inf] * k
        least_pre[-1] = 0
        prefix_sum = 0
        max_sum = -inf
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = i % k
            old_pre = least_pre[mod]
            sub_sum = prefix_sum - old_pre
            if max_sum < sub_sum:
                max_sum = sub_sum
            if old_pre > prefix_sum:
                least_pre[mod] = prefix_sum
        return max_sum
