class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Count occurrences of each number initially
        from collections import Counter
        
        right_count = Counter(nums)
        left_count = Counter()

        result = 0

        for j in range(n):
            right_count[nums[j]] -= 1  # j moves out of right side
            
            # If nums[i] == nums[j] * 2 and nums[k] == nums[j] * 2
            target = nums[j] * 2
            if target in left_count and target in right_count:
                result = (result + left_count[target] * right_count[target]) % MOD

            left_count[nums[j]] += 1  # j moves into left side

        return result % MOD
