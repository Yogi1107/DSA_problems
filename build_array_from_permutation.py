#Leet code Questions Solutions. 

#Date : 24/09/2025
#Problem 1920 : Build Array from Permutation

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0,len(nums)):
            result.append(nums[nums[i]])

        return result
        