#Leet code Questions Solutions. 

#Date : 11/09/2025
#Problem 709 : To Lower Case

class Solution:
    def toLowerCase(self, s: str) -> str:
        n = len(s)
        text = ""
        for i in range(n):
            a = s[i]
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                a = chr(ord(s[i]) + 32)
            text += a
        return text
        