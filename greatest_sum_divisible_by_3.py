class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        smallest_one = float("inf")
        smallest_two = float("inf")
        for n in nums:
            total += n
            if n% 3 == 1:
                smallest_two = min(smallest_two, n+smallest_one)
                smallest_one = min(smallest_one, n)
            if n % 3 == 2:
                smallest_one = min(smallest_one, n+smallest_two)
                smallest_two = min(smallest_two, n)

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - smallest_one
        if total % 3 == 2:
            return total - smallest_two


# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         n = len(nums)
#         max_sum = 0
        
#         # Iterate over all subsets using bitmask
#         for mask in range(1 << n):
#             s = 0
#             for i in range(n):
#                 if mask & (1 << i):
#                     s += nums[i]
#             if s % 3 == 0:
#                 max_sum = max(max_sum, s)
        
#         return max_sum


# class Solution:
#     def maxSumDivThree(self, nums: List[int]) -> int:
#         s = sum(nums)
        
#         if s % 3 == 0:
#             return s
        
#         r11 = 10000
#         r12 = 10000
#         r21 = 10000
#         r22 = 10000
        
#         for num in nums:
#             if num % 3 == 1 and num < r12:
#                 if num < r11:
#                     r12 = r11
#                     r11 = num
#                 else:
#                     r12 = num
#             if num % 3 == 2 and num < r22:
#                 if num < r21:
#                     r22 = r21
#                     r21 = num
#                 else: 
#                     r22 = num
#         if s % 3 == 1:
#             return s - min(r11, r21+r22)
#         if s % 3 == 2:
#             return s - min(r21, r11+r12) 
