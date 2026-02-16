class Solution:
    def reverseBits(self, n: int) -> int:
        binary_32 = bin(n)[2:].zfill(32)
        reversed_binary = binary_32[::-1]
        return int(reversed_binary, 2)

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         result = 0

#         for _ in range(32):
#             result = (result << 1) | (n & 1)
#             n >>= 1

#         return result
