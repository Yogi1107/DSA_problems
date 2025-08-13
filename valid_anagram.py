#Leet code Questions Solutions. 

#Date : 13/08/2025
#Problem 242: Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            return sorted(s) == sorted(t)