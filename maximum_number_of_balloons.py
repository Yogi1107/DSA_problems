# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         freq = {}

#         for ch in text:
#             freq[ch] = freq.get(ch, 0) + 1

#         return min(
#             freq.get('b', 0),
#             freq.get('a', 0),
#             freq.get('l', 0) // 2,
#             freq.get('o', 0) // 2,
#             freq.get('n', 0)
#         )

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = defaultdict(int)
        balloon = 'balloon'

        for x in text:
            if x in balloon:
                counter[x]+=1
            
        if any(c not in counter for c in balloon):
            return 0
        else:
            return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])
        
