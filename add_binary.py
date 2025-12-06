class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            bitA = int(a[i]) if i >= 0 else 0
            bitB = int(b[j]) if j >= 0 else 0

            total = bitA + bitB + carry
            res.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(reversed(res))

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:

#         return bin(int(a,2) + int(b,2))[2:]
        
