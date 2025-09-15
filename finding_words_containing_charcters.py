#Leet code Questions Solutions. 

#Date : 15/091/2025
#Problem : Find Words Containing Character


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index = []
        for i in range(len(words)):
            if x in words[i]:
                index.append(i)
        
        return index

        