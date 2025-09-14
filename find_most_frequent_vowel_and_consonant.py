#Leet code Questions Solutions. 

#Date : 14/09/2025
#Problem 3541 :Find the most frequent vowel and consonant

class Solution:
    def maxFreqSum(self, s: str) -> int:
        str_ = 'aeiou'
        vowel = {}
        consonant = {}
        for i in s:
            if i in str_:
                vowel[i] = vowel.get(i, 0) + 1
            else:
                consonant[i] = consonant.get(i, 0) + 1
        
        return max(vowel.values(), default=0) + max(consonant.values(), default=0)
		
from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        count = Counter(s)  # count frequencies of all characters

        vowel_max = max((count[ch] for ch in count if ch in vowels), default=0)
        consonant_max = max((count[ch] for ch in count if ch not in vowels), default=0)

        return vowel_max + consonant_max

