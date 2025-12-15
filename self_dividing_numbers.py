# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         result = []
        
#         for i in range(left, right + 1):
#             is_valid = True
#             for j in str(i):
#                 if j == '0' or i % int(j) != 0:
#                     is_valid = False
#                     break
            
#             if is_valid:
#                 result.append(i)
        
#         return result


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            if "0" in str(i):
                continue
            else:
                x=i
                flag=True
                while x>0:
                    r=x%10
                    if i%r!=0:
                        flag=False
                        break
                    x=x//10
                if flag:
                    res.append(i)
        return res
