from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give = 1
        i = 0

        while candies > 0:
            result[i % num_people] += min(give, candies)
            candies -= give
            give += 1
            i += 1

        return result
