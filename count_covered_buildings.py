# class Solution:
#     def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
#         from collections import defaultdict
#         import bisect

#         rows = defaultdict(list)
#         cols = defaultdict(list)

#         # Group by rows and columns
#         for x, y in buildings:
#             rows[x].append(y)
#             cols[y].append(x)

#         # Sort rows & columns
#         for x in rows:
#             rows[x].sort()
#         for y in cols:
#             cols[y].sort()

#         covered = 0

#         for x, y in buildings:
#             row = rows[x]
#             col = cols[y]

#             # Binary search in row
#             idx_row = bisect.bisect_left(row, y)
#             has_left = idx_row > 0
#             has_right = idx_row < len(row) - 1

#             # Binary search in col
#             idx_col = bisect.bisect_left(col, x)
#             has_above = idx_col > 0
#             has_below = idx_col < len(col) - 1

#             if has_left and has_right and has_above and has_below:
#                 covered += 1

#         return covered



class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        minRowIndices = [n + 1] * (n + 1)
        maxRowIndices = [0] * (n + 1)
        minColIndices = [n + 1] * (n + 1)
        maxColIndices = [0] * (n + 1)

        for building in buildings:
            row = building[0]
            col = building[1]

            if row < minRowIndices[col]:
                minRowIndices[col] = row
            if row > maxRowIndices[col]:
                maxRowIndices[col] = row

            if col < minColIndices[row]:
                minColIndices[row] = col
            if col > maxColIndices[row]:
                maxColIndices[row] = col

        count = 0
        for building in buildings:
            row = building[0]
            col = building[1]

            if (minRowIndices[col] < row and
                maxRowIndices[col] > row and
                minColIndices[row] < col and
                maxColIndices[row] > col):
                count += 1

        return count
