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

        leftNodeHeight = self.getHeight(root.left)
        rightNodeHeight = self.getHeight(root.right)
        isCurrenBalanced = True if abs(leftNodeHeight - rightNodeHeight) <= 1 else False
        isLeftBalanced = self.isBalanced(root.left)
        isRightBalanced = self.isBalanced(root.right)

        return isCurrenBalanced and isLeftBalanced and isRightBalanced

    def getHeight(self, root: Optional[TreeNode]):   
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))    

