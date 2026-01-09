class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = []

        for i in range(1, len(num) - 1):
            if num[i-1] == num[i] == num[i+1]:
                result.append(num[i] * 3)   # store "777" not 7

        return max(result) if result else ""

# class Solution:
#     def largestGoodInteger(self, num: str) -> str:
#         max=-1
#         for i in range(0,10):
#             j=0
#             x=""
#             while(j<3):
#              x+=str(i)
#              j+=1
#             if x in num:
#                 y=int(x)
#                 if(max<y):
#                   max=y
#         if max==-1:
#             return ""
#         elif max==0:
#             return "000"
#         return str(max)
