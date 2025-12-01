class Solution:
    def fillCups(self, amount: List[int]) -> int:
        total = sum(amount)
        mx = max(amount)
        return max(mx, (total + 1) // 2)
