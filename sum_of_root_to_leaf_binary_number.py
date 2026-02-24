# class Solution:
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
#         def dfs(node, current):
#             if not node:
#                 return 0
            
#             # Build binary number
#             current = current * 2 + node.val
            
#             # If leaf → return value
#             if not node.left and not node.right:
#                 return current
            
#             # Recur left + right
#             return dfs(node.left, current) + dfs(node.right, current)
        
#         return dfs(root, 0)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        res = 0

        def dfs(node,num):
            if not node:
                return
            nonlocal res
            num += str(node.val)
            if not node.left and not node.right:
                res += int(num,2)
            
            dfs(node.left, num)
            dfs(node.right, num)
        dfs(root, '')

        return res
