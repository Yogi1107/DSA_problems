#Leet code Questions Solutions. 

#Date : 24/08/2025
#Problem 389 : Find the difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t= list(t)

        for i in range(len(s)):
            if s[i] in t:
                t.remove(s[i])
        return "".join(t)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))