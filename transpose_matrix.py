#Transpose Matrix : 867

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for c in range(cols):
            new_row = []
            for r in range(rows):
                new_row.append(matrix[r][c])
            result.append(new_row)

        return result

# class Solution:
#     def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
#         rows = len(matrix)
#         cols = len(matrix[0])
#         ans = []

#         for r in range(cols):
#             row = []
#             for с in range(rows):
#                 row.append(0)
#             ans.append(row)

#         for r in range(rows):
#             for c in range(cols):
#                 ans[c][r] = matrix[r][c]


#         return ans

        
        
