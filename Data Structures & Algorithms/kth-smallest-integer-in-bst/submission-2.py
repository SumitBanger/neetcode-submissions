# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = []
        
        self.dfs(root, result)
        return result[k-1]

    
    def dfs(self, root: Optional[TreeNode], result):     
        if root.left:
            self.dfs(root.left, result)
        if root:
            result.append(root.val)
        if root.right:
            self.dfs(root.right, result)

    
    
    def dfs1(self, root: Optional[TreeNode], k: int, count: int):
        if count == k-1:
            return root.val
        
        if root.left:
            self.dfs(root.left, k, count)
        if root:
            count += 1
            if count == k:
                return root.val
        if root.right:
            self.dfs(root.right, k, count)


        


        