def decompressRLElist(self, nums):
    result = []
    
    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i + 1]
        
        for _ in range(freq):
            result.append(val)
            
    return result
    