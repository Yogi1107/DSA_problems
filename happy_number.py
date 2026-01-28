class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sum_of_squares(n)

        while fast!=1 and slow!=fast:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))

        return fast == 1
    
    def sum_of_squares(self, num):
        total = 0

        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        
        return total
        
