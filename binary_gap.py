# class Solution:
#     def binaryGap(self, n: int) -> int:
#         binary_n = bin(n)[2:]
#         prev = -1
#         max_gap = 0

#         for i, bit in enumerate(binary_n):
#             if bit == '1':
#                 if prev != -1:
#                     max_gap = max(max_gap, i - prev)
#                 prev = i

#         return max_gap

class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        left = 0
        max_dist = 0

        while left < len(bin_n) and bin_n[left] == '0':
            left += 1
        
        for right in range(left + 1, len(bin_n)):
            if bin_n[right] == '1':
                max_dist = max(max_dist, right - left)
                left = right
        return max_dist