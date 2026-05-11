# class Solution:
#     def separateDigits(self, nums: List[int]) -> List[int]:
#         result = []
#         for i in nums:
#             if len(str(i)) > 1:
#                 l = []
#                 s = str(i)
#                 for i in s:
#                     l.append(int(i))
#                 result.extend(l)
#             else:
#                 result.append(i)

#         return result

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num > 9:
                for d in str(num):
                    res.append(int(d))
            else:
                res.append(num)

        return res
