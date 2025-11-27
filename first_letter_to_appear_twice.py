# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         result = []
#         result_ = {}
#         for i in s:
#             result.append(i)
#         for i in result:
#             result_[i] = result.count(i)

#         for i in result_.keys():
#             if result_[i] == 2:
#                 return i 

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen_chars = set()
        for char in s:
            if char in seen_chars:
                return char
            seen_chars.add(char)
        return "" 
        
