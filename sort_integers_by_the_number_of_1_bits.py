# class Solution:
#     def sortByBits(self, arr: list[int]) -> list[int]:
#         arr.sort(key=lambda x: (bin(x).count('1'), x))
#         return arr

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Count bits for current and next element
                cnt1 = bin(arr[j]).count('1')
                cnt2 = bin(arr[j+1]).count('1')
                
                # Swap if:
                # 1. First element has more 1s than the second
                # 2. They have same 1s, but first element is larger (tie-breaker)
                if cnt1 > cnt2 or (cnt1 == cnt2 and arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        return arr
