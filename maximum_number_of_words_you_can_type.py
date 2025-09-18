#Leet code Questions Solutions. 

#Date : 18/09/2025
#Problem 1935 : Maximum Number of words you can Type 

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        
        count = 0
        for word in text.split(" "):
            found = False
            for char in word:
                if char in broken_set:
                    found = True
                    break
            if not found:
                count += 1
        
        return count
		

def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    broken = set(brokenLetters)
    return sum(1 for word in text.split() if not (set(word) & broken))

def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
       text_list = text.split()
       count = 0
       for word in text_list:
            if all(ch not in word for ch in brokenLetters):
                count += 1
        
       return count