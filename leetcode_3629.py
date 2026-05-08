from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums):
        n = len(nums)

        if n == 1:
            return 0

        MAXV = max(nums) + 1

        # ---------- SIEVE ----------
        is_prime = [True] * MAXV
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(MAXV ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, MAXV, i):
                    is_prime[j] = False

        # ---------- BUILD PRIME -> INDICES ----------
        divisible_map = defaultdict(list)

        for idx, val in enumerate(nums):

            temp = val
            factors = set()

            d = 2

            while d * d <= temp:
                while temp % d == 0:
                    factors.add(d)
                    temp //= d
                d += 1

            if temp > 1:
                factors.add(temp)

            for f in factors:
                divisible_map[f].append(idx)

        # ---------- BFS ----------
        q = deque([(0, 0)])   # (index, distance)
        visited = [False] * n
        visited[0] = True

        used_prime = set()

        while q:

            i, steps = q.popleft()

            if i == n - 1:
                return steps

            # Adjacent moves
            for ni in [i - 1, i + 1]:

                if 0 <= ni < n and not visited[ni]:
                    visited[ni] = True
                    q.append((ni, steps + 1))

            # Prime teleportation
            val = nums[i]

            if is_prime[val] and val not in used_prime:

                for ni in divisible_map[val]:

                    if not visited[ni]:
                        visited[ni] = True
                        q.append((ni, steps + 1))

                used_prime.add(val)

        return -1
