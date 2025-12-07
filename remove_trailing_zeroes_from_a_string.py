class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        ans=""
        num=num[::-1]
        z=0
        for d in num:
            if d=='0':
                z+=1
            else:
                break
        num=num[::-1]
        return num[:len(num)-z]

# class Solution:
#     def removeTrailingZeros(self, num: str) -> str:
#         return num.rstrip('0')
        
