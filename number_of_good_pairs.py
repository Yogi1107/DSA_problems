#Leet code Questions Solutions. 

#Date : 25/09/2025
#Problem 1512 : Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            result[i] = nums.count(i)

        good_pairs = 0
        for i in result.keys():
            good_pairs += (result[i] * (result[i]-1) // 2)

        return good_pairs
        

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
        # count = 0
        # index = 0
        # while index < len(nums):
        #     for i in range(index+1, len(nums)):
        #         if nums[index] == nums[i]:
        #             count += 1
        #     index += 1
        # return count