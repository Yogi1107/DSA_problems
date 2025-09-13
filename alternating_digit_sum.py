#Leet code Questions Solutions. 

#Date : 13/09/2025
#Problem 2544 : Alternating Digit Sum 

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        str_n = str(n)
        summ = 0
        for i in range(len(str_n)):
            if i%2==0:
                summ += int(str_n[i])
            else:
                summ -= int(str_n[i])
        return summ

        
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=c=0
        for i in str(n):
            t=int(i)
            if c%2!=0:
                t=-t
            s+=t
            c+=1
        return s
        