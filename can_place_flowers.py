# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n == 0:
#             return True
#         planted = 0
#         length = len(flowerbed)
#         for i in range(length):
#             if flowerbed[i] == 1:
#                 continue
            
#             empty_left = (i==0) or (flowerbed[i-1]==0)
#             empty_right = (i==length-1) or (flowerbed[i+1]==0)

#             if empty_left and empty_right:
#                 flowerbed[i] = 1
#                 planted += 1
#                 if planted >= n:
#                     return True

#         return planted >= n        


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return flowerbed[0] == 0
        if len(flowerbed) == 2:
            if flowerbed[0] == 1 or flowerbed[1] == 1:
                return False
            else:
                n -= 1
                return n == 0
        if flowerbed[0] == flowerbed[1] == 0:
            if n-1 == 0:
                return True
            else:
                flowerbed[0] = 1
                n -= 1
        if flowerbed[-1] == flowerbed[-2] == 0:
            if n-1 == 0:
                return True
            else:
                flowerbed[-1] = 1
                n -= 1
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] == 0:
                if n-1 == 0:
                    return True
                else:
                    flowerbed[i] = 1
                    n -= 1
        return n == 0
                
