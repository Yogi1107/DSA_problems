class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        max_len = 0
        
        # Iterate through every possible starting index
        for i in range(n):
            seen = set()
            even_distinct = 0
            odd_distinct = 0
            
            # Expand the subarray from i to the end of the list
            for j in range(i, n):
                val = nums[j]
                
                # Only update counts if we haven't seen this number in the current subarray
                if val not in seen:
                    seen.add(val)
                    if val % 2 == 0:
                        even_distinct += 1
                    else:
                        odd_distinct += 1
                
                # Check if the current window is "balanced"
                if even_distinct == odd_distinct:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
