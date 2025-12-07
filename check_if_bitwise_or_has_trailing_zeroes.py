class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        a = 0
        for x in nums:
            if x%2 == 0:
                a += 1
                if a >= 2:
                    return True
        return False


# class Solution:
#     def hasTrailingZeros(self, nums: List[int]) -> bool:
#         even_count = 0
#         for i in nums:
#             if i % 2 ==0:
#                 even_count += 1

#         if even_count >= 2:
#             return True
#         else:
#             return False
        
