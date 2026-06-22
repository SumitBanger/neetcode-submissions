# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.DFS(root, result)
        return result[k-1]
    
    def DFS(self, root, result):
        if not root: return 
        
        self.DFS(root.left, result)
        result.append(root.val)
        self.DFS(root.right, result)


        