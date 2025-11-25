# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         freq = {}

#         for ch in s:
#             freq[ch] = freq.get(ch, 0) + 1

#         for i, ch in enumerate(s):
#             if freq[ch] == 1:
#                 return i

#         return -1


class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = float("inf")

        for char in ascii_lowercase:
            first = s.find(char)
            last = s.rfind(char)

            if first!=-1 and first == last:
                result = min(result, first)

        return -1 if result == float("inf") else result
