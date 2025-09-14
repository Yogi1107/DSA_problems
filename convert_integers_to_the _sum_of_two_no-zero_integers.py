#Leet code Questions Solutions. 

#Date : 14/09/2025
#Problem 1317 : Convert Integer to the sum of two no-zero integers

class Solution:
    def getNoZeroIntegers(self, n: int):
        for a in range(1, n):
            b = n - a
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]
