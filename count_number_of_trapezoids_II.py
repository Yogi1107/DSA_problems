import math
from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: list[list[int]]) -> int:
        N = len(points)
        if N < 4:
            return 0

        # ---------- Count Parallelograms correctly ----------
        midpoint_map = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                mid = (x1 + x2, y1 + y2)
                midpoint_map[mid].append((i, j))

        parallelogram_count = 0

        # Only count pairs of segments with same midpoint AND not collinear
        for segs in midpoint_map.values():
            k = len(segs)
            if k < 2:
                continue

            for a in range(k):
                i1, j1 = segs[a]
                x1 = points[i1][0] - points[j1][0]
                y1 = points[i1][1] - points[j1][1]

                for b in range(a + 1, k):
                    i2, j2 = segs[b]
                    x2 = points[i2][0] - points[j2][0]
                    y2 = points[i2][1] - points[j2][1]

                    # Reject collinear (parallel) diagonals → fake parallelogram
                    if x1 * y2 == y1 * x2:
                        continue

                    parallelogram_count += 1

        # ---------- Group UNIQUE points on each parallel line ----------
        line_groups = defaultdict(lambda: defaultdict(set))

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]

                dx = x2 - x1
                dy = y2 - y1
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g

                # normalize
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                slope_key = (dy, dx)

                C = dy * x1 - dx * y1
                line_groups[slope_key][C].add(i)
                line_groups[slope_key][C].add(j)

        # ---------- Count trapezoids ----------
        trapezoid_count = 0

        for slope_key, line_map in line_groups.items():
            counts = [len(s) for s in line_map.values()]

            L = len(counts)
            for i in range(L):
                p_i = counts[i]
                if p_i < 2:
                    continue
                s_i = p_i * (p_i - 1) // 2

                for j in range(i + 1, L):
                    p_j = counts[j]
                    if p_j < 2:
                        continue
                    s_j = p_j * (p_j - 1) // 2

                    trapezoid_count += s_i * s_j

        result = trapezoid_count - parallelogram_count
        return max(result, 0)    # Never return negative


# class Solution:
#     def countTrapezoids(self, points: List[List[int]]) -> int:
#         n = len(points)
#         inf = 10**9 + 7
#         slope_to_intercept = defaultdict(list)
#         mid_to_slope = defaultdict(list)
#         ans = 0
        
#         for i in range(n):
#             x1, y1 = points[i]
#             for j in range(i + 1, n):
#                 x2, y2 = points[j]
#                 dx = x1 - x2
#                 dy = y1 - y2
                
#                 if x2 == x1:
#                     k = inf
#                     b = x1
#                 else:
#                     k = (y2 - y1) / (x2 - x1)
#                     b = (y1 * dx - x1 * dy) / dx
                
#                 mid = (x1 + x2) * 10000 + (y1 + y2)
#                 slope_to_intercept[k].append(b)
#                 mid_to_slope[mid].append(k)

#         for sti in slope_to_intercept.values():
#             if len(sti) == 1:
#                 continue
            
#             cnt = defaultdict(int)
#             for b_val in sti:
#                 cnt[b_val] += 1
            
#             total_sum = 0
#             for count in cnt.values():
#                 ans += total_sum * count
#                 total_sum += count

#         for mts in mid_to_slope.values():
#             if len(mts) == 1:
#                 continue
            
#             cnt = defaultdict(int)
#             for k_val in mts:
#                 cnt[k_val] += 1
            
#             total_sum = 0
#             for count in cnt.values():
#                 ans -= total_sum * count
#                 total_sum += count
        
#         return ans
