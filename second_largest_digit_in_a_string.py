# class Solution:
#     def secondHighest(self, s: str) -> int:
#         result = []
#         for i in s:
#             if i.isdigit():
#                 result.append(int(i))
#         second_highest = sorted(set(result),reverse=True)

#         if len(second_highest) >= 2:
#             return second_highest[1]
#         else:
#             return -1

class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in range(len(s)):
            if s[i].isdigit():
                l.append(int(s[i]))
        if len(set(l))==1 or len(l)==0:
            return -1
        l=list(set(l))
        a=max(l)
        l.remove(a)
        return max(l)               
