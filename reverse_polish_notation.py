class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                    stack.append(a*b)
                else:
                    division = a / b
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(int(division))
            else:
                stack.append(int(i))
        return stack[0]
        
		
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)  # truncates toward zero
        }
        
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]
