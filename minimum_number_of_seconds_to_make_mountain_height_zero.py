import math

class Solution:
    def minNumberOfSeconds(self, h, t):
        l, r = 1, 10**18
        ans = r

        while l <= r:
            mid = (l + r) // 2

            tot = 0

            for x in t:
                val = (2 * mid) // x
                k = int((math.sqrt(1 + 4 * val) - 1) // 2)
                tot += k

                if tot >= h:
                    break

            if tot >= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
        
