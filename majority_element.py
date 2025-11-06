# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dict_ = {}
#         majority_number = len(nums) // 2
        
#         for i in nums:
#             dict_[i] = dict_.get(i, 0) + 1
#             if dict_[i] > majority_number:
#                 return i


# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)

#         return candidate


class Solution:
    #from collections import defaultdict
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count ==0:
                candidate=num
            if num!=candidate:
                count-=1
            else:
                count+=1

        return candidate
        
