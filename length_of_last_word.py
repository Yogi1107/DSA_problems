#Leet code Questions Solutions. 

#Date : 08/08/2025
#Problem 58 : Length of the last word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words_list = s.split()
        #print(words_list[-1])
        length_of_last_word = len(words_list[-1])
        return length_of_last_word
