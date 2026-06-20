# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCount, maxTillNow = 0, float("-infinity")
        #return self.getGoodNodesCount(root, goodNodesCount, maxTillNow)
        return self.getGoodNodesCount(root, maxTillNow)
    
    def getGoodNodesCount(self, root, goodNodesCount, maxTillNow):
        if not root:
            return goodNodesCount

        if root.val >= maxTillNow:
            goodNodesCount, maxTillNow = goodNodesCount + 1, root.val
        goodNodesCount = self.getGoodNodesCount(root.left, goodNodesCount, maxTillNow)
        goodNodesCount = self.getGoodNodesCount(root.right, goodNodesCount, maxTillNow)
        return goodNodesCount

    def getGoodNodesCount(self, root, maxTillNow):
        if not root:
            return 0
        
        currentNodeGoodNodes = 0
        if root.val >= maxTillNow:
            currentNodeGoodNodes, maxTillNow = 1, root.val
        return currentNodeGoodNodes + self.getGoodNodesCount(root.left, maxTillNow) + self.getGoodNodesCount(root.right, maxTillNow)
        