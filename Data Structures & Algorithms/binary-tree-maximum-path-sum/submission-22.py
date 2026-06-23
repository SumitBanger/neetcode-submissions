# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return max(self.DFS(root)[0], self.DFS(root)[1])
        result = [-1010]
        self.getMaxPathSum(root, result)
        return result[0]


    def DFS(self, root):
        leftSum, leftSumIncluding = self.DFS(root.left) if root.left else (-1010, -1010)
        rightSum, rightSumIncluding = self.DFS(root.right) if root.right else (-1010, -1010)
        currentNodeVal = root.val
        totSum = max(leftSum, rightSum, leftSumIncluding, rightSumIncluding, (currentNodeVal + leftSumIncluding + rightSumIncluding))
        totSumIncluding = max(currentNodeVal, (currentNodeVal + leftSumIncluding), (currentNodeVal + rightSumIncluding))
        return totSum, totSumIncluding

    def getMaxPathSum(self, root, result):
        if not root: return -1010

        leftSum = self.getMaxPathSum(root.left, result)
        rightSum = self.getMaxPathSum(root.right, result)
        nodeVal = root.val
        maxWithoutNode = max(leftSum, rightSum)
        maxWithNodeAndOneChild = nodeVal + max(max(leftSum, 0), max(rightSum, 0))
        maxWithNodeAndChildren = nodeVal + max(leftSum, 0) + max(rightSum, 0)
        result[0] = max(result[0], nodeVal, maxWithoutNode, maxWithNodeAndOneChild, maxWithNodeAndChildren)

        return maxWithNodeAndOneChild






        

        