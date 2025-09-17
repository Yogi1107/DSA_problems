#Leet code Questions Solutions. 

#Date : 17/09/2025
#Problem 434 : Number of Segments in a String

class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        
class Solution:
    def countSegments(self, s: str) -> int:
        
        if s == "":
            return 0
        splitted = s.split(" ")
        print(splitted)
        count = 0
        for i in range(0,len(splitted)):
            if (splitted[i] != " ") & (splitted[i] != ""):
                count += 1


        return (count)