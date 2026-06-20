# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCount, maxTillNow = 0, float("-infinity")
        return self.getGoodNodesCount(root, goodNodesCount, maxTillNow)
    
    def getGoodNodesCount(self, root, goodNodesCount, maxTillNow):
        if not root:
            return goodNodesCount

        if root.val >= maxTillNow:
            goodNodesCount, maxTillNow = goodNodesCount + 1, root.val
        goodNodesCount = self.getGoodNodesCount(root.left, goodNodesCount, maxTillNow)
        goodNodesCount = self.getGoodNodesCount(root.right, goodNodesCount, maxTillNow)
        return goodNodesCount
        