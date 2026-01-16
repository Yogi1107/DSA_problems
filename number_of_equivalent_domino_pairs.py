# class Solution:
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         count = {}

#         for a, b in dominoes:
#             key = (min(a,b), max(a,b))
#             count[key] = count.get(key, 0) + 1

#             result = 0
#             for k in count.values():
#                 result += k * (k-1)//2

#         return result

class Solution:
    def numEquivDominoPairs(self, dominoes):
        arr = [[0] * 10 for _ in range(10)]
        for a, b in dominoes:
            arr[a][b] += 1
        res = 0
        for i in range(1, 10):
            for j in range(i, 10):
                c = arr[i][j] + arr[j][i]
                if i == j:
                    c //= 2
                res += c * (c - 1) // 2
        return res
