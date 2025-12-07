class Solution:
    def countOdds(self, low: int, high: int) -> int:
        start = low if low % 2 == 1 else low + 1
        return max(0, (high - start) // 2 + 1)

# class Solution:
#     def countOdds(self, low: int, high: int) -> int:
#         return ((high+1)//2)-(low//2)

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
