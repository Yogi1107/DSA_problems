#Leet code Questions Solutions. 

#Date : 23/08/2025
#Problem 1784 : Sum of Unique Elements

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result_dict = {}
        result = []
        for i in nums:
            result_dict[i] = nums.count(i)
        
        for i in result_dict.keys():
            if result_dict[i] == 1:
                result.append(i)

        return sum(result)
        
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        total = 0
        for key, value in hashmap.items():
            if (value == 1):
                total += key

        return total

        