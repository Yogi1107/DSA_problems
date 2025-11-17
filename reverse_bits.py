#190: Reverse Bits

class Solution:
    def reverseBits(self, n: int) -> int:
        binary_representation = bin(n)[2:].zfill(32)
        reverse_bin_representation = binary_representation[::-1]
        return int(reverse_bin_representation, 2)

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         return int(
#             (
#                 bin(n)[2:].zfill(32)
#             )[::-1],
#             2
#         )
#     __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        
