class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        sign = "-" if num < 0 else ""
        num = abs(num)

        result = []

        while num != 0:
            result.append(str(num % 7))
            num //= 7

        return sign + ''.join(reversed(result))
