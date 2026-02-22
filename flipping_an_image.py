# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         result = []
#         d = {0:1, 1:0}
#         for i in image:
#             result.append(i[::-1])
        
#         for i in range(len(result)):
#             for j in range(len(result[i])):
#                 result[i][j] = d[result[i][j]]

#         return result

# class Solution:
#     def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
#         for row in image:
#             row.reverse()  # flip
#             for i in range(len(row)):
#                 row[i] = 1 - row[i]  # invert
#         return image

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            left, right = 0, len(row) - 1
            while left <= right:
                row[left], row[right] = 1 - row[right], 1 - row[left]
                left += 1
                right -= 1
        return image
