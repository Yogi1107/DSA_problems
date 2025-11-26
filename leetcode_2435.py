class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][r] = number of ways to reach cell (i,j) with sum % k = r
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0] % k] = 1

        for i in range(m):
            for j in range(n):
                current_mod = grid[i][j] % k
                for r in range(k):
                    if i > 0:
                        dp[i][j][(r + current_mod) % k] = (dp[i][j][(r + current_mod) % k] + dp[i-1][j][r]) % MOD
                    if j > 0:
                        dp[i][j][(r + current_mod) % k] = (dp[i][j][(r + current_mod) % k] + dp[i][j-1][r]) % MOD

        # We want paths where total sum % k == 0
        return dp[m-1][n-1][0]
