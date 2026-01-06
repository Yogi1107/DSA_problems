class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        worda = ""
        wordb = ""
        for i in word1:
            worda += i
        for i in word2:
            wordb += i
        
        return worda==wordb
        
