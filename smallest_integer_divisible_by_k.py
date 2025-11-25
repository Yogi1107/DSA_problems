class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        for i in range(1, k+1):
            if curr % k == 0:
                return i
            curr = 10 * (curr  % k) + 1
        return -1
