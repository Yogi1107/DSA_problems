# class Solution:
#     def canThreePartsEqualSum(self, arr: List[int]) -> bool:
#         total = sum(arr)

#         if total % 3 != 0:
#             return False

#         target = total // 3
#         current_sum = 0
#         count = 0

#         for num in arr:
#             current_sum += num
#             if current_sum == target:
#                 count += 1
#                 current_sum = 0

#         return count >= 3



class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        ps = accumulate(arr)
        total_sum = sum(arr)

        if total_sum % 3 != 0:
            return False 

        need_sums = [total_sum // 3, 2 * (total_sum // 3), total_sum]
        j = 0

        for i, s in enumerate(ps):
            if s == need_sums[j]:
                j += 1
                
            if j == len(need_sums) - 1:
                return i < (len(arr) - 1)
        
        return False 
