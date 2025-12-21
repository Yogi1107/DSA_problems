class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: get sorted unique values
        sorted_unique = sorted(set(arr))

        # Step 2: map value -> rank (mapping value to the index + 1)
        rank = {}
        for i, val in enumerate(sorted_unique):
            rank[val] = i + 1

        # Step 3: build result
        return [rank[x] for x in arr]
