# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Use float('-inf') instead of a hardcoded magic number
        self.max_sum = float('-inf')
        
        def get_branch_max(node):
            if not node:
                return 0
            
            # 1. Recursively find the max path of left and right subtrees.
            # If a subtree return is negative, we floor it to 0 (meaning we ignore it).
            left_gain = max(get_branch_max(node.left), 0)
            right_gain = max(get_branch_max(node.right), 0)
            
            # 2. Price of a split path containing the current node acting as the highest apex
            current_split_sum = node.val + left_gain + right_gain
            
            # 3. Update the global maximum path seen across the whole tree
            self.max_sum = max(self.max_sum, current_split_sum)
            
            # 4. Return the maximum non-splitting branch sum to the parent frame
            return node.val + max(left_gain, right_gain)
            
        get_branch_max(root)
        return self.max_sum





        # return max(self.DFS(root)[0], self.DFS(root)[1])
        result = [-1010]
        self.getMaxPathSum(root, result)
        return result[0]


    def getMaxPathSum(self, root, result):
        if not root: return -1010
        leftSum, rightSum = self.getMaxPathSum(root.left, result), self.getMaxPathSum(root.right, result)
        maxWithoutNode = max(leftSum, rightSum)
        maxWithNodeAndOneChild = root.val + max(max(leftSum, 0), max(rightSum, 0))
        maxWithNodeAndChildren = root.val + max(leftSum, 0) + max(rightSum, 0)
        result[0] = max(result[0], maxWithoutNode, maxWithNodeAndOneChild, maxWithNodeAndChildren)
        return maxWithNodeAndOneChild



    # def DFS(self, root):
    #     leftSum, leftSumIncluding = self.DFS(root.left) if root.left else (-1010, -1010)
    #     rightSum, rightSumIncluding = self.DFS(root.right) if root.right else (-1010, -1010)
    #     currentNodeVal = root.val
    #     totSum = max(leftSum, rightSum, leftSumIncluding, rightSumIncluding, (currentNodeVal + leftSumIncluding + rightSumIncluding))
    #     totSumIncluding = max(currentNodeVal, (currentNodeVal + leftSumIncluding), (currentNodeVal + rightSumIncluding))
    #     return totSum, totSumIncluding


        

        