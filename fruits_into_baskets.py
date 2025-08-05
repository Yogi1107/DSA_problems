#Leet code Questions Solutions. 

#Date : 05/08/2025
#Problem 904 : Fruits into baskets

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        c = 0
        i = 0
        for j in range(len(fruits)):
            d[fruits[j]] += 1
            while len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i+=1
            c = max(c,j-i+1)
        return c