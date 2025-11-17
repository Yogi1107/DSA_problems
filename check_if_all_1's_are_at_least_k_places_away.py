class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        lastOne = -(k+1)

        for i in range(n):
            if(nums[i] == 1):
                if ( i- lastOne - 1 < k):
                    return False

                lastOne = i
            
        
        return True
        
# class Solution:
#     def kLengthApart(self, nums: List[int], k: int) -> bool:
#         if k == 0:
#             return True
#         prev = None
#         for i, num in enumerate(nums):
#             if num == 1:
#                 if prev is not None and i - prev <= k:
#                     return False
#                 prev = i
#         return True
