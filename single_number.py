#Leet code Questions Solutions. 

#Date : 14/08/2025
#Problem 136: Single Number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_ = {}
        for i in nums:
            dict_[i] = nums.count(i)
        for i in dict_.keys():
            if dict_[i] == 1:
                return i
        