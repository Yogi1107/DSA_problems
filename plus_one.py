# #Leet code Questions Solutions. 

# #Date : 24/08/2025
# #Problem 66 : Plus One

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         result = ""        
#         for i in digits:
#             result += str(i)
#         print(result)
#         summ = int(result) + 1
#         result_ = [int(i) for i in str(summ)]
#         return result_
		
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         for i in range(len(digits) - 1, -1, -1):
#             if digits[i] == 9:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 return digits   
#         return [1] + digits 

help(set)
