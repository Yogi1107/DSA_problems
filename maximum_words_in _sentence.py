#Leet code Questions Solutions. 

#Date : 04/09/2025
#Problem 2114: Maximum number of Words found in a sentence

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        length_list = []
        word_count = 0
        for i in sentences:
            words = i.split()
            word_count = len(words)
            length_list.append(word_count)
        return max(length_list)
        