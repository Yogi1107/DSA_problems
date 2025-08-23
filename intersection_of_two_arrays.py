#Leet code Questions Solutions. 

#Date : 23/08/2025
#Problem 367 : Intersection of two arrays

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)
        return list(set(result))

        
#class Solution:
#    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#        return list(set(nums1).intersection(set(nums2)))