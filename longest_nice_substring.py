class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        
        char_set = set(s)
        
        for i, ch in enumerate(s):
            if ch.swapcase() not in char_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                
                return left if len(left) >= len(right) else right
        
        return s
