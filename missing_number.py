#Leet code Questions Solutions. 

#Date : 24/08/2025
#Problem 268 : Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_nums = len(nums)
        for i in range(len_nums + 1):
            if i not in nums:
                return i

# n = len(nums)
# expected_sum = n * (n + 1) // 2   # sum of numbers 0..n
# actual_sum = sum(nums)
# return expected_sum - actual_sum    

def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)

        for i in range(len(nums)):
            result ^= i ^ nums[i]

        return result
