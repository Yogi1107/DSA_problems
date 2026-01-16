class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')

        count = 0
        while n != 0:
            if n & 1 :
                count += 1
            n = n >> 1
        return count
