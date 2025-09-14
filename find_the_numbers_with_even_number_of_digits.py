#Leet code Questions Solutions. 

#Date : 14/09/2025
#Problem 1295 : Find numbers with even number of digits

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        len_ = []
        for i in nums:
            len_.append(len(str(i)))
        count = 0
        for i in len_:
            if i%2==0:
                count += 1
        
        return count
		
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        total=0
        for i in nums:
            count=len(str(i))
            if count%2==0:
                total=total+1
        return total