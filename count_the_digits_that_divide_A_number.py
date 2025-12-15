class Solution:
    def countDigits(self, num: int) -> int:
        result = []
        for i in str(num):
            if num % int(i) == 0:
                result.append(i)
        return len(result)
        
