class Solution:
    def numMagicSquaresInside(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def isMagic(r, c):
            # center must be 5
            if grid[r+1][c+1] != 5:
                return False
            
            nums = set()
            for i in range(r, r+3):
                for j in range(c, c+3):
                    if grid[i][j] < 1 or grid[i][j] > 9:
                        return False
                    nums.add(grid[i][j])
            
            if len(nums) != 9:
                return False
            
            s = sum(grid[r][c:c+3])
            
            # rows
            for i in range(r, r+3):
                if sum(grid[i][c:c+3]) != s:
                    return False
            
            # columns
            for j in range(c, c+3):
                if grid[r][j] + grid[r+1][j] + grid[r+2][j] != s:
                    return False
            
            # diagonals
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s:
                return False
            
            return True
        
        count = 0
        for i in range(rows - 2):
            for j in range(cols - 2):
                if isMagic(i, j):
                    count += 1
        
        return count