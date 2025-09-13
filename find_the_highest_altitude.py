#Leet code Questions Solutions. 

#Date : 13/09/2025
#Problem 1732 : Find the highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        copies = gain[:]
        copies = [0 for x in range(len(gain)+1)]
        currMax = 0
        for i in range(1, len(gain)+1):
            copies[i] = copies[i-1] + gain[i-1]
            currMax = max(copies[i],currMax)
        return currMax
        

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxValue = max(gain[0], 0)
        for i in range(1, len(gain)):
            gain[i] = gain[i-1] + gain[i]
            maxValue = max(maxValue, gain[i])
        return maxValue 

        		