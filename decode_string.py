class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""
        num = 0

        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)

            elif i == '[':
                stack.append((result, num))
                result = ""
                num = 0

            elif i == ']':
                prev_result, repeat = stack.pop()
                result = prev_result + result * repeat

            else:  # alphabet
                result += i

        return result



# 3 → num = 3
# [ → push ("", 3)
# a → result = "a"
# 2 → num = 2
# [ → push ("a", 2)
# c → result = "c"
# ] → "a" + "c"*2 = "acc"
# ] → "" + "acc"*3 = "accaccacc"
