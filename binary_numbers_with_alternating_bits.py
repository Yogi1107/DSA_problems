# class Solution:
#     def hasAlternatingBits(self, n: int) -> bool:
#         x = n ^ (n >> 1)
#         return (x & (x + 1)) == 0

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]   # remove '0b'

        for i in range(1, len(binary)):
            if binary[i] == binary[i - 1]:
                return False

        return True
