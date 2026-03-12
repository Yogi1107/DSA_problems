class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.components = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def unite(self, a, b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa

        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1

        self.components -= 1
        return True


class Solution:
    def maxStability(self, n, edges, k):
        mandatory = []
        optional = []

        for u, v, s, must in edges:
            if must:
                mandatory.append((u, v, s))
            else:
                optional.append((u, v, s))

        # Check mandatory cycle
        dsu = DSU(n)
        for u, v, _ in mandatory:
            if not dsu.unite(u, v):
                return -1

        def canAchieve(x):
            dsu = DSU(n)

            # Phase 1: mandatory edges
            for u, v, s in mandatory:
                if s < x or not dsu.unite(u, v):
                    return False

            # Phase 2: free edges
            for u, v, s in optional:
                if s >= x:
                    dsu.unite(u, v)

            # Phase 3: upgrades
            upgrades = 0
            for u, v, s in optional:
                if s < x and 2*s >= x:
                    if dsu.unite(u, v):
                        upgrades += 1
                        if upgrades > k:
                            return False

            return dsu.components == 1

        lo, hi = 1, 200000
        ans = -1

        while lo <= hi:
            mid = (lo + hi)//2
            if canAchieve(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
