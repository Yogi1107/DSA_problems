# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         vowels = set("aeiou")
#         n = len(word)
#         count = 0

#         for i in range(n):
#             if word[i] not in vowels:
#                 continue

#             seen = set()
#             for j in range(i, n):
#                 if word[j] not in vowels:
#                     break   # stop when you hit a consonant

#                 seen.add(word[j])

#                 if len(seen) == 5:
#                     count += 1

#         return count

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        last_consonant = -1
        n = len(word)
        last_vowels = {v:-1 for v in "aeiou"}
        ans = 0
        for i, c in enumerate(word):
            if c in last_vowels:
                last_vowels[c] = i
                ans += max(min(last_vowels.values())-last_consonant, 0)
            else:
                last_consonant = i

        return ans
