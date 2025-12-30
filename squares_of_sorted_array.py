class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*n
        l,r=0,n-1
        for i in range(n-1,-1,-1):
            if abs(nums[l])>abs(nums[r]):
                arr[i]=nums[l]**2
                l+=1
            else:
                arr[i]=nums[r]**2
                r-=1
        return arr

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         result = [x**2 for x in nums]
#         return sorted(result)
        
