#Leet code Questions Solutions. 

#Date : 12/08/2025
#Problem 216 : Remove Duplicate


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
