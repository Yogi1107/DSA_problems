from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        result = []

        rows = len(matrix)
        cols = len(matrix[0])

        # Your i, j idea stays
        i = 0
        j = 0

        # Added limits (extension of your approach)
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        while top <= bottom and left <= right:

            # ---- move right ----
            j = left
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # ---- move down ----
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # ---- move left ----
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # ---- move up ----
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
