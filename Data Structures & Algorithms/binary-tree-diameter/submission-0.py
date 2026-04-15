# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
    
        def getHeight(root: Optional[TreeNode]):
            if not root:
                return -1

            leftNodeHeight = getHeight(root.left)
            rightNodeHeight = getHeight(root.right)
            currentNodeHeight = 1 + max(leftNodeHeight, rightNodeHeight)
            currentNodeDiamteter = leftNodeHeight + rightNodeHeight + 2
            diameter[0] = max(diameter[0], currentNodeDiamteter)
            return currentNodeHeight

        getHeight(root)
        return diameter[0]
