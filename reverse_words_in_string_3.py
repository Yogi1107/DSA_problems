#Leet code Questions Solutions. 

#Date : 11/09/2025
#Problem 557 : Reverse Words int String III


class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        result_string = ""
        list_s = s.split()
        for i in list_s:
            result.append(i[::-1])
        result_string = " ".join(result)
        return result_string
		
class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        res = ""
        for word in arr:
            res += f"{word[::-1]} "
        return res[:-1]
