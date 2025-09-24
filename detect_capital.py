#Leet code Questions Solutions. 

#Date : 24/09/2025
#Problem 520 : Detect Capital

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count_caps = 0
        for char in word:
            if char.isupper():
                count_caps += 1
        
        if count_caps == len(word) or count_caps == 0 or (word[0].isupper() and count_caps == 1):
            return True
        return False
		
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()