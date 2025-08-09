#Leet code Questions Solutions. 

#Date : 09/08/2025
#Problem 27 : Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the next position to place a non-val element
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
