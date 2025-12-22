class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # result = []
        # for i in range(min(nums),max(nums)+1):
        #     if i not in nums:
        #         result.append(i)
        
        # return sorted(result)

        mn, mx = min(nums), max(nums) + 1
        return sorted(set(range(mn, mx)) - set(nums))
