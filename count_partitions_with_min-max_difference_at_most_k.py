class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        dp[0] = 1

        # prefix[i] = dp[0] + dp[1] + ... + dp[i]
        pref = [0] * (n + 1)
        pref[0] = dp[0]

        from collections import deque
        maxD = deque()
        minD = deque()

        l = 0

        for r in range(n):
            # update deques
            while maxD and maxD[-1] < nums[r]:
                maxD.pop()
            maxD.append(nums[r])

            while minD and minD[-1] > nums[r]:
                minD.pop()
            minD.append(nums[r])

            # ensure valid window
            while maxD[0] - minD[0] > k:
                if maxD[0] == nums[l]:
                    maxD.popleft()
                if minD[0] == nums[l]:
                    minD.popleft()
                l += 1

            # dp[r+1] = sum(dp[l : r+1])
            dp[r+1] = (pref[r] - (pref[l-1] if l > 0 else 0)) % MOD

            # update prefix
            pref[r+1] = (pref[r] + dp[r+1]) % MOD

        return dp[n]
