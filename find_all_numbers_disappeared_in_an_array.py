#Leetcode Problem: 448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []
        for i, n in enumerate(nums):
            if n > 0:
                result.append(i+1)
        return result


# __import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         r = set(range(1, len(nums) + 1))
#         res = list(r - set(nums))
#         return res
