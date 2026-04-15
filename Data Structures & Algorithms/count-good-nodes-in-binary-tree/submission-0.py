# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxTillNow = -101
        return self.DFS(root, maxTillNow)

    
    def DFS(self, root: TreeNode, maxTillNow):
        if not root:
            return 0
        currentNodeVal, currentNodeGoodNodes = root.val, 0
        if root.val >= maxTillNow:
            maxTillNow, currentNodeGoodNodes = root.val, 1
        leftSubtreeGoodNodes = self.DFS(root.left, maxTillNow)
        rightSubtreeGoodNodes = self.DFS(root.right, maxTillNow)
        return currentNodeGoodNodes + leftSubtreeGoodNodes + rightSubtreeGoodNodes