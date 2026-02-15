class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ = 0
        b_ = 0
        reverse_a = list(a[::-1])
        reverse_b = list(b[::-1])
        for index, digit in enumerate(reverse_a):
            a_ += int(digit) * (2 ** index)
        for index, digit in enumerate(reverse_b):
            b_ += int(digit) * (2 ** index)

        c = a_ + b_
        result = bin(c).lstrip('0b')

        if result == "":
            return "0"
        
        return result 


#class Solution:
#    def addBinary(self, a: str, b: str) -> str:
    #    return bin(int(a, 2) + int(b, 2))[2:]

        