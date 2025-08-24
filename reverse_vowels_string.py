#Leet code Questions Solutions. 

#Date : 24/08/2025
#Problem 345 : reverse vowels in a string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)   # convert to list since strings are immutable
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]  # swap vowels
                i += 1
                j -= 1
        
        return "".join(s)


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        i = 0
        j = len(s)-1
        s = list(s)
                   

        while(i<j):
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i+=1
                j-=1


        res = ''.join(s)
        return res

        