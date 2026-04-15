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
        nodeVal = root.val
        maxIncludingNode = nodeVal + max(leftMax, 0) + max(rightMax, 0)
        maxIncludingNodeAndOneChild = nodeVal + max(max(leftMax, 0), max(rightMax, 0))
        maxWithoutNode = max(leftMax, rightMax)
        result[0] = max(result[0], max(nodeVal, maxIncludingNode, maxIncludingNodeAndOneChild, maxWithoutNode))
        return maxIncludingNodeAndOneChild

        