class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        planted = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 1:
                continue
            
            empty_left = (i==0) or (flowerbed[i-1]==0)
            empty_right = (i==length-1) or (flowerbed[i+1]==0)

            if empty_left and empty_right:
                flowerbed[i] = 1
                planted += 1
                if planted >= n:
                    return True

        return planted >= n        
