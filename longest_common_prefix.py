#Leet code Questions Solutions. 

#Date : 05/08/2025
#Problem 14. Longest Common Prefix
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)
        
        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        
        return strs[0][:i]
