class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if arr[i] == 2 * arr[j]:
                    return True

        return False


# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         seen = set()

#         for num in arr:
#             if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
#                 return True
#             seen.add(num)

#         return False
