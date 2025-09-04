#Leet code Questions Solutions. 

#Date : 04/09/2025
#Problem 1672: Richest customer wealth

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = []
        for sub_list in accounts:
            wealth.append(sum(sub_list))
        return max(wealth)

        