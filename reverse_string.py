#Leet code Questions Solutions. 

#Date : 24/08/2025
#Problem 344 : reverse string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s