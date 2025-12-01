# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries.sort()
#         left, right = 0, sum(batteries) // n

#         def can_run(t):
#             total = 0
#             for b in batteries:
#                 total += min(b, t)
#             return total >= n * t

#         while left < right:
#             mid = (left + right + 1) // 2
#             if can_run(mid):
#                 left = mid
#             else:
#                 right = mid - 1

#         return left


class Solution:
        
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        m = len(batteries)
        if n==m:
            return min(batteries)
        if m < n:
            return 0
        batteries.sort()
        S = sum(batteries[:-n]) # extra battery life to distribute to maximize time 
        L = batteries[-n:] 
        for i in range(n-1):
            if S < (i+1) * (L[i+1] - L[i]):
                return L[i] + S // (i+1)
            S -= (i+1) * (L[i+1] - L[i])
        return L[-1] + S // n
