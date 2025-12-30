class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return [i for i in range(len(nums)) if nums[i] == target]
        
        # result = sorted(nums)
        # return [i for i in range(len(result)) if result[i] == target]
