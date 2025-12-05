class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(left: int, right: int) -> bool:
            # Check if the substring s[left:right+1] is a palindrome
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left character or the right character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left += 1
            right -= 1
        
        return True


# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         def kiem_tra(s,left,right):
#             while left>=0 and right<len(s) and left<=right:
#                 if s[left]!=s[right]:
#                     return False
#                 left+=1
#                 right-=1
#             return True
#         left=0
#         right=len(s)-1
#         if kiem_tra(s,left,right):
#             return True
#         while left<=right:
#             if s[left]!=s[right]:
#                 l=kiem_tra(s,left+1,right)
#                 r=kiem_tra(s,left,right-1)
#                 return r or l
#             left+=1
#             right-=1
#         return True
# __import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))
