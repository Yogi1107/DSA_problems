class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        triangle = [[1]]
        for i in range(1,rowIndex+1):
            prev_row = triangle[i-1]
            child = [1]
            for j in range(1,i):
                child.append(prev_row[j-1]+prev_row[j])
            child.append(1)
            triangle.append(child)

        return triangle[-1]
      
