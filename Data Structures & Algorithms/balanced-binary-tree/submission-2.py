# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        leftDepth = self.getHeight(root.left)
        rightDepth = self.getHeight(root.right)

        return False if abs(leftDepth - rightDepth) > 1 else (self.isBalanced(root.left) and self.isBalanced(root.right))        
    
    def getHeight(self, root: Optional[TreeNode]):   
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))  