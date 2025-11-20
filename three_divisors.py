class Solution:
    def isThree(self, n: int) -> bool:
        result = []
        for i in range(1,n+1):
            if n % i == 0:
                result.append(i)
        
        if len(result) == 3:
            return True
        else:
            return False
        
# class Solution:
#     def isThree(self,n:int)->bool:
#         r=int(n**0.5)
#         if r*r!=n:return False
#         if r<2:return False
#         for i in range(2,int(r**0.5)+1):
#             if r%i==0:return False
#         return True
