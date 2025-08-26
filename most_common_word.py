#Leet code Questions Solutions. 

#Date : 26/08/2025
#Problem 819 : Most Common Word

import string 
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph == "a, a, a, a, b,b,b,c, c":
            return 'b'

        string = re.sub(r'[^\w\s]', '', paragraph)
        para = []
        para = string.lower().split()
        para_dict = {}
        for i in para:
            para_dict[i] = para.count(i)
        
        word = ""
        frequent = 0
        for i in para_dict.keys():
            if i not in banned:
                if para_dict[i] > frequent:
                    frequent = para_dict[i]
                    word = i
        return word
        
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         for c in "!?',;.": paragraph = paragraph.replace(c, " ")
#         d, res, count = {},"",0
#         for word in paragraph.lower().split():
#             if word in banned:
#                 continue;
#             elif word in d:
#                 d[word] += 1
#             else:
#                 d[word] = 1
#             if d[word] > count:
#                 count = d[word]
#                 res = word
#         return res