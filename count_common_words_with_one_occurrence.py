#leetcode problem
#Problem 2085 : Count Common Words With One Occurrence
#Date: 16-09-2025

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_dict = {}
        words2_dict = {}
        count = 0
        for i in words1:
            words1_dict[i] = words1.count(i)
        for i in words2:
            words2_dict[i] = words2.count(i)

        for i in words1_dict.keys():
            for j in words2_dict.keys():
                if i == j and words1_dict[i] == 1 and words2_dict[j] == 1:
                    count+=1
        
        return count
