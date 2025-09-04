#Leet code Questions Solutions. 

#Date : 04/09/2025
#Problem 1929: Concatenation Of Arrays

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums
		
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
		return nums + nums