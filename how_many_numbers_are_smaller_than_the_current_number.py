class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        sorted_nums = sorted(nums)
        d = {}
        x = 0
        for i in range(len(sorted_nums)):
            if sorted_nums[i] in d.keys():
                # x = x - 1
                # d[sorted_nums[i]] = x
                x = x + 1
                continue
            d[sorted_nums[i]] = x
            x = x + 1

        for i in nums:
            result.append(d[i])

        return result


# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         bucket = [0] * 101

#         for num in nums:
#             bucket[num] += 1
        
#         for i in range(1, 100):
#             bucket[i] = bucket[i] + bucket[i - 1]

#         ans = []

#         for num in nums:
#             if num == 0:
#                 ans.append(0)
#             else:
#                 ans.append(bucket[num - 1])
        
#         return ans

        
