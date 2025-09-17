#Leet code Questions Solutions. 

#Date : 17/09/2025
#Problem 168 : Excel Sheet Column Title

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while (columnNumber > 0):
            offset = (columnNumber - 1)%26
            res += chr(ord('A')+offset)
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]