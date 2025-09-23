#Leet code Questions Solutions. 

#Date : 23/09/2025
#Problem 3005 : Count Elements with Maximum Frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        result = {}
        for i in nums:
            result[i] = nums.count(i)
        
        count = 0
        
        max_ = max(result.values())
        
        for i in result.keys():
            if result[i] == max_:
                count+=result[i]

        return count