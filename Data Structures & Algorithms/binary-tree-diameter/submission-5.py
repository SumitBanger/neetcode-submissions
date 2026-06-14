# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)
        currentDiameter = leftHeight + rightHeight

        return max(leftDiameter, rightDiameter, currentDiameter)


    def getHeight(self, root: Optional[TreeNode]):   
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    #     return self.maxDepth(root)[1]
    
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0, 0

    #     leftDepth, leftChildDiam = self.maxDepth(root.left)
    #     rightDepth, rightChildDiam = self.maxDepth(root.right)

    #     currentDepth = 1 + max(leftDepth, rightDepth)
    #     parentDiam = leftDepth + rightDepth

    #     return (currentDepth, max(leftChildDiam, rightChildDiam, parentDiam))