# class Solution:
#     def addMinimum(self, word: str) -> int:
#         operations = 0
#         expected = 'a'

#         for ch in word:
#             while ch != expected:
#                 operations += 1
#                 expected = chr((ord(expected) - ord('a') + 1) % 3 + ord('a'))
#             expected = chr((ord(expected) - ord('a') + 1) % 3 + ord('a'))

#         # complete remaining "abc"
#         if expected == 'b':
#             operations += 2
#         elif expected == 'c':
#             operations += 1

#         return operations



class Solution:
    # def addMinimum(self, word: str) -> int:
    #     expected='a'
    #     count=0
    #     for i in word:
    #         while i!=expected:
    #             count+=1

    #             if expected=='a':
    #                 expected='b'
    #             elif expected=='b':
    #                 expected='c'
    #             else:
    #                 expected='a'
    #         if expected=='a':
    #             expected='b'
    #         elif expected=='b':
    #             expected='c'
    #         else:
    #             expected='a'
    #     if expected=='b':
    #         count+=2
    #     if expected=='c':
    #         count+=1
    #     return count


class Solution:
    def addMinimum(self, word: str) -> int:
        groups = 1
        for i in range(1, len(word)):
            if word[i] <= word[i-1]:
                groups += 1
        return groups * 3 - len(word)
