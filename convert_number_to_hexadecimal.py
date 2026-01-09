class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # handle negative numbers using 32-bit two's complement
        num &= 0xFFFFFFFF

        hex_chars = "0123456789abcdef"
        result = []

        while num > 0:
            result.append(hex_chars[num & 15])  # last 4 bits
            num >>= 4

        return "".join(reversed(result))
