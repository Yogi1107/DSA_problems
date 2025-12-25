# import math

# class Solution:
#     def minEatingSpeed(self, piles, h):
#         for k in range(1, max(piles) + 1):
#             total_hours = 0
#             for pile in piles:
#                 total_hours += math.ceil(pile / k)
            
#             if total_hours <= h:
#                 return k


# class Solution:
#     def minEatingSpeed(self, piles, h):
#         left, right = 1, max(piles)
#         answer = right

#         while left <= right:
#             mid = (left + right) // 2
#             hours = 0

#             for pile in piles:
#                 hours += (pile + mid - 1) // mid  # ceil(pile / mid)

#             if hours <= h:
#                 answer = mid
#                 right = mid - 1   # try smaller speed
#             else:
#                 left = mid + 1    # need faster speed

#         return answer
# 0 1 2 3 
# 3 6 7 11

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_of_piles = len(piles)
        total_of_bananas = sum(piles)
        low = math.ceil(total_of_bananas / h)
        high = math.ceil(total_of_bananas / ( h - total_of_piles + 1))
        # n = len(piles)
        # s = sum(piles)
        # l, r = math.ceil(s/h), math.ceil(s/(h - n + 1))

        while low < high:
            middle = (low + high) // 2
            hours_spent = sum(math.ceil(pile / middle) for pile in piles)
            if hours_spent <= h:
                high = middle
            else:
                low = middle + 1

        return high
