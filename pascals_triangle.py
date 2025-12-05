from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        triangle = [[1]]  # First row
        
        for i in range(1, numRows):
            prev_row = triangle[i - 1]
            # Start with 1
            row = [1]
            # Compute inner values
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            # End with 1
            row.append(1)
            triangle.append(row)
        
        return triangle
