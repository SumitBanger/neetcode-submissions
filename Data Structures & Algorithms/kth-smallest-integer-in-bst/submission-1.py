# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        result = []
        self.dfs(root, result)
        return result[k - 1] 

    def dfs(self, root: Optional[TreeNode], result):
        if not root:
            return
        self.dfs(root.left, result)     
        result.append(root.val)
        self.dfs(root.right, result)


