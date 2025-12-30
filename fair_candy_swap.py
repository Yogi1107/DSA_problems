class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice = sum(aliceSizes)
        bob = sum(bobSizes)

        diff = (alice - bob) // 2
        bobSet = set(bobSizes)

        for x in aliceSizes:
            y = x - diff 
            if y in bobSet:
                return [x,y]
        
