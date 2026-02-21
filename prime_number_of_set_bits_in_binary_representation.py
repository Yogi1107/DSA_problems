# class Solution:
#     def countPrimeSetBits(self, left: int, right: int) -> int:
#         result = 0
        
#         def isPrime(n):
#             if n < 2:
#                 return False
#             for i in range(2, int(n**0.5) + 1):
#                 if n % i == 0:
#                     return False
#             return True
        
#         for i in range(left, right + 1):
#             b = bin(i).count('1')  # Count the number of 1's in binary
#             if isPrime(b):
#                 result += 1

#         return result

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # Precompute primes up to 32
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        
        result = 0
        for i in range(left, right + 1):
            # Count set bits
            b = bin(i).count('1')
            if b in prime_set:
                result += 1

        return result
