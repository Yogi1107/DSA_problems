class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        result = 0 
        prev = 0
        streak = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                streak += 1
            else:
                prev = streak
                streak = 1
            
            if streak <= prev:
                result += 1

        return result
