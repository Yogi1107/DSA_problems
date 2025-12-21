class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        deleted = 0
        sorted_pairs = [False] * (n - 1)

        for c in range(m):
            bad = False
            for r in range(n - 1):
                if not sorted_pairs[r] and strs[r][c] > strs[r + 1][c]:
                    bad = True
                    break

            if bad:
                deleted += 1
            else:
                for r in range(n - 1):
                    if strs[r][c] < strs[r + 1][c]:
                        sorted_pairs[r] = True

        return deleted
