#leetcode problem 3370

class Solution:
    def smallestNumber(self, n: int) -> int:
        l, r=1, 10
        res = -1
        while l<=r:
            m = (l+r)//2
            x = 2**m - 1
            if x >= n:
                r = m - 1
                res = x
            else:
                l = m + 1
        return res
        
# class Solution:
#     def smallestNumber(self, n: int) -> int:
#         outputs = {
#             1: 1,
#             2: 3,
#             4: 7,
#             8: 15,
#             16: 31,
#             32: 63,
#             64: 127,
#             128: 255,
#             256: 511,
#             512: 1023,
#             1024: 2047,
#         }
#         prev = 1
#         for output in outputs.keys():
#             if output > n:
#                 return outputs[prev]
#             prev = output
        
#         return outputs[1024]

