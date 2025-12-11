# from collections import defaultdict, deque

# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         waiting = defaultdict(deque)
        
#         # put each word into a bucket based on the first character it needs
#         for w in words:
#             waiting[w[0]].append(iter(w[1:]))
        
#         count = 0
        
#         # process characters in s
#         for c in s:
#             queue = waiting[c]
#             size = len(queue)
            
#             for _ in range(size):
#                 it = queue.popleft()
#                 nxt = next(it, None)
                
#                 if nxt is None:
#                     count += 1  # word completed
#                 else:
#                     waiting[nxt].append(it)  # move iterator to next bucket
        
#         return count


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        # 1. word count
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        # 2. check subsequence / string.find method
        def is_subsequence(s, word):
            i = 0
            for char in word:
                i = s.find(char, i) + 1 # s.find(char, i) in s[i:], return -1
                if not i:
                    return False
            return True
        
        # 3. count and return
        res = 0
        for word in word_count:
            if is_subsequence(s, word):
                res += word_count[word]
        return res
