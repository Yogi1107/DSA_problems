# class Solution:
#     def makeGood(self, s: str) -> str:
#         stack = []

#         for char in s:
#             # If the last character in stack and current char are the same letter but different case
#             if stack and stack[-1] != char and stack[-1].lower() == char.lower():
#                 stack.pop()  # remove the bad pair
#             else:
#                 stack.append(char)  # add current char to stack

#         return "".join(stack)


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
        
