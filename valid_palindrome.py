#Leet code Questions Solutions. 

#Date : 13/08/2025
#Problem 125: Valid Palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalnum():
                if 'A' <= i <= 'Z':
                    result += i.lower()
                else:
                    result += i
        if result[::-1] == result:
            return True
        else:
            return False