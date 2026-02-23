class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         if len(s) < k:
#             return False
        
#         seen = set()

#         for i in range(len(s)-k+1):
#             substring = s[i:i+k]
#             seen.add(substring)

#         return len(seen) == 2**k


        def hasAllCodes(self, s: str, k: int) -> bool:
            
            if len(s) < k:
                return False
            
            needed = 1 << k  # 2^k
            seen = [False] * needed
            count = 0
            
            num = 0
            
            for i in range(len(s)):
                num = ((num << 1) & (needed - 1)) | int(s[i])
                
                if i >= k - 1:
                    if not seen[num]:
                        seen[num] = True
                        count += 1
                        if count == needed:
                            return True
            
            return False
