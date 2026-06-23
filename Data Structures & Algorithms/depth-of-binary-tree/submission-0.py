# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recurse(root, 0) 
        
    def recurse(self, root: Optional[TreeNode], depth: int): 
        if not root: return depth

        l = self.recurse(root.left, depth + 1)  
        r = self.recurse(root.right, depth + 1)
        
        return max(l, r)