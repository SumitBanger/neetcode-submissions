# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return max(self.DFS(root)[0], self.DFS(root)[1])


    def DFS(self, root):
        if not root: return -1010

        leftSum, leftSumIncluding = self.DFS(root.left) if root.left else (-1010, -1010)
        rightSum, rightSumIncluding = self.DFS(root.right) if root.right else (-1010, -1010)
        currentSum, totSum, totSumIncluding = root.val, 0, 0

        print(f"currentSum: {currentSum}, leftSum: {leftSum}, leftSumIncluding: {leftSumIncluding}, rightSum: {rightSum}, rightSumIncluding: {rightSumIncluding}")
        
        totSum = max(leftSum, rightSum, leftSumIncluding, rightSumIncluding, (currentSum + leftSumIncluding + rightSumIncluding))
        totSumIncluding = max(currentSum, (currentSum + leftSumIncluding), (currentSum + rightSumIncluding))

        print(f"totSum: {totSum} and totSumIncluding: {totSumIncluding} for currentSum: {currentSum}")
        return totSum, totSumIncluding

        # if currentSum >= 0:
        #     totSum = currentSum + (leftSum if leftSum > 0 else 0) + (rightSum if rightSum > 0 else 0)
        #     print(f"inside IF: currentSum: {currentSum}, leftSum: {leftSum}, rightSum: {rightSum}, totSum: {totSum}")
        # else:
        #     small, large = (leftSum, rightSum) if leftSum <= rightSum else (rightSum, leftSum)
        #     if small < 0 and large < 0:
        #         totSum = max(currentSum, small, large)
        #     else:
        #         totSum = large + (small + currentSum if (small + currentSum) >= 0 else 0)
        #     print(f"inside else: currentSum: {currentSum}, leftSum: {leftSum}, rightSum: {rightSum}, totSum: {totSum}, small: {small}, large:{large}")



        

        