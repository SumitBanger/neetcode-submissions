# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If the helper function returns -1, it means the tree is unbalanced
        return self.checkBalanceAndHeight(root) != -1

    def checkBalanceAndHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Check left subtree
        leftHeight = self.checkBalanceAndHeight(root.left)
        if leftHeight == -1: 
            return -1  # Short-circuit if already unbalanced
            
        # Check right subtree
        rightHeight = self.checkBalanceAndHeight(root.right)
        if rightHeight == -1: 
            return -1  # Short-circuit if already unbalanced
            
        # If current node is unbalanced, return -1
        if abs(leftHeight - rightHeight) > 1:
            return -1
            
        # Otherwise, return the true height of this node
        return 1 + max(leftHeight, rightHeight)

    ##### This is my original approach but it's non optimal #####
    #     if not root:
    #         return True
        
    #     leftDepth = self.getHeight(root.left)
    #     rightDepth = self.getHeight(root.right)

    #     return False if abs(leftDepth - rightDepth) > 1 else (self.isBalanced(root.left) and self.isBalanced(root.right))        
    
    # def getHeight(self, root: Optional[TreeNode]):   
    #     if not root:
    #         return 0
    #     return 1 + max(self.getHeight(root.left), self.getHeight(root.right))  