class Solution(object):
    def minRemoval(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        max_len = 1

        for right in range(n):
            while nums[right] > k * nums[left]:
                left += 1
            max_len = max(max_len, right - left + 1)

        return n - max_len