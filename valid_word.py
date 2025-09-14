#Leet code Questions Solutions. 

#Date : 14/09/2025
#Problem 3136 : Valid Word1


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        word_ = word.lower()
        vowels = set("aeiou")
        consonants = set("bcdfghjklmnpqrstvwxyz")

        has_vowel = False
        has_consonant = False

        for ch in word_:
            if not (ch.isalpha() or ch.isdigit()):
                return False   # 🚨 reject if special char
            if ch in vowels:
                has_vowel = True
            elif ch in consonants:
                has_consonant = True

        return has_vowel and has_consonant
