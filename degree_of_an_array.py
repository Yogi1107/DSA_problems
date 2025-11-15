class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count, first, last = {}, {}, {}

        # Build frequency, first occurrence, last occurrence
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
                first[nums[i]] = i
            last[nums[i]] = i
            count[nums[i]] += 1

        degree = max(count.values())
        ans = float('inf')

        # Check subarray length for all elements with max degree
        for x in count:
            if count[x] == degree:
                ans = min(ans, last[x] - first[x] + 1)

        return ans
