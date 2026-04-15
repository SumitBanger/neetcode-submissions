# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root, float("-infinity"), float("infinity"))
    
    def dfs(self, root: Optional[TreeNode], minVal, maxVal):
        if not root:
            return True
        rootVal = root.val
        isValidAtCurrent = True if rootVal > minVal and rootVal < maxVal else False
        isValidLeft = self.dfs(root.left, minVal, rootVal)
        isValidRight = self.dfs(root.right, rootVal, maxVal)
        return isValidAtCurrent and isValidLeft and isValidRight