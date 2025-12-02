from typing import List
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # count how many points at each y
        cnt = defaultdict(int)
        for x, y in points:
            cnt[y] += 1
        
        # For each y-level, compute number of ways to choose 2 points on that line
        # i.e. num_pairs[y] = C(cnt[y], 2) if cnt[y] >= 2
        pair_counts = []
        for y, c in cnt.items():
            if c >= 2:
                pair_counts.append(c * (c - 1) // 2)
        
        # Now, across all distinct y-levels, choose any two (with their pair_counts)
        # The total number of trapezoids = sum over all distinct pairs i < j of pair_counts[i] * pair_counts[j]
        result = 0
        accum = 0  # cumulative sum of pair_counts seen so far
        for pc in pair_counts:
            result = (result + pc * accum) % MOD
            accum = (accum + pc) % MOD
        
        return result
