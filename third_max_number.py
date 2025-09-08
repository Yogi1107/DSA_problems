# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)
#         mx=nums[0]
#         mx1=nums[0]
#         mx2=nums[0]
#         print(mx)
#         for i in range(1,len(nums)):
#             if nums[i]<mx:
#                 mx1=nums[i]
#                 break

#         for j in range(1,len(nums)):
#             if nums[j]<mx1:
#                 mx2=nums[j] 
#                 break       

#         return mx2
        

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = sorted(set(nums),reverse=True)
        if len(result) > 2:
            return result[2]
        else:
            return result[0]