#Leet code Questions Solutions. 

#Date : 13/09/2025
#Problem 258 : add the Digits

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  
            temp = 0
            for digit in str(num):
                temp += int(digit)
            num = temp
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        if not num:  return num
        # return 9  if num % 9 == 0  else num % 9
        return num % 9  or  9

        # digits = [ int(c) for c in str(num) ]
        # print( f'digits={digits}' )
        # while 10 <= sum( digits ):
        while 10 <= num:
            # digits = [ int(c) for c in str(sum(digits)) ]
            digits = [ int(c) for c in str(num) ]
            num = sum( digits )
            # print( f'digits={digits}' )
        return num