# class Solution:
#     def countEven(self, num: int) -> int:
#         count = 0
#         for i in range(2,num+1):
#             if len(str(i)) > 1:
#                 s = 0
#                 for j in str(i):
#                     s += int(j) 
#                 if s % 2 == 0:
#                     count += 1

#             elif i % 2 == 0:
#                 count += 1

#             else: 
#                 continue

#         return count

class Solution:
    def countEven(self, num: int) -> int:
        # Calculate digit sum of num
        digit_sum = sum(int(d) for d in str(num))
        
        # If digit sum is even
        if digit_sum % 2 == 0:
            return num // 2
        else:
            return (num - 1) // 2
