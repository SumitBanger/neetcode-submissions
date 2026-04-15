# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [float("-infinity")]
        self.dfs(root, result)
        return result[0]

    
    def dfs(self, root: Optional[TreeNode], result):
        if not root:
            return float("-infinity")

        leftMax = self.dfs(root.left, result)
        rightMax = self.dfs(root.right, result)
        maxWithNodeAndChildren = root.val + max(leftMax, 0) + max(rightMax, 0)
        maxWithNodeAndOneChild = root.val + max(max(leftMax, 0), max(rightMax, 0))
        maxWithoutNode = max(leftMax, rightMax)
        maxTillCurrentNode = max(maxWithNodeAndChildren, maxWithNodeAndOneChild, maxWithoutNode)
        result[0] = max(result[0], maxTillCurrentNode)
        # Since we can return only the max including current node otherwise path would be broken
        return maxWithNodeAndOneChild

        