class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp 

        return one


# class Solution:
#     def climbStairs(self, n: int) -> int:
        
#         temp = [0] * n
        

#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         elif n > 2:
#             temp[0] = 1
#             temp[1] = 2

#             for i in range(2, n):
#                 temp[i] = temp[i-1] + temp[i-2]

#             return temp[-1]

#         else:
#             print("try a different number")        
        
