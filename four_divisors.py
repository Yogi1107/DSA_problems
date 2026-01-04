from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        divisors = {}   # number -> list of divisors
        total_sum = 0

        for n in nums:
            divisors[n] = []

            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    divisors[n].append(i)
                    if i != n // i:
                        divisors[n].append(n // i)

                if len(divisors[n]) > 4:
                    break

            if len(divisors[n]) == 4:
                total_sum += sum(divisors[n])

        return total_sum



# class Solution:
#     def sumFourDivisors(self, nums: List[int]) -> int:
#         m = max(nums)
#         divs = [0 for i in range(m+1)]
#         sums = [0 for i in range(m+1)]
#         for i in range(1,m+1,1):
#             for j in range(i,m+1,i):
#                 divs[j]+=1
#                 sums[j]+=i
#         res = 0
#         for i in nums:
#             if divs[i] == 4:
#                 res+=sums[i]
        
#         return res
# __import__("atexit").register(lambda: open('display_runtime.txt','w').write('0'))
