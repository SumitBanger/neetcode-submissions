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
        
        leftNodeHeight = self.getHeight(root.left)
        rightNodeHeight = self.getHeight(root.right)
        leftNodeDiameter = self.diameterOfBinaryTree(root.left)
        rightNodeDiameter = self.diameterOfBinaryTree(root.right)
        
        return max(leftNodeHeight + rightNodeHeight, leftNodeDiameter, rightNodeDiameter)
        
    def getHeight(self, root: Optional[TreeNode]):   
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        
        # Below solution uses global variable so let's avoid it
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
