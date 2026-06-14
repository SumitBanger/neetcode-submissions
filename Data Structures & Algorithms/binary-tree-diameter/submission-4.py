# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.maxDepth(root)[1]
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0, 0

        leftDepth, leftChildDiam = self.maxDepth(root.left)
        rightDepth, rightChildDiam = self.maxDepth(root.right)

        currentDepth = 1 + max(leftDepth, rightDepth)
        parentDiam = leftDepth + rightDepth

        return (currentDepth, max(leftChildDiam, rightChildDiam, parentDiam))