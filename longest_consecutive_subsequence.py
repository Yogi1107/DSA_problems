class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if num is the start of a sequence
            if num - 1 not in numSet:
                current = num
                length = 1

                while current + 1 in numSet:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
