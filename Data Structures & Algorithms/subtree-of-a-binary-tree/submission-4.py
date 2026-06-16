# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        isSubTreeAtCurrent = self.isSameTree(root, subRoot)
        return isSubTreeAtCurrent or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        elif (not p and q) or (not q and p) or (p.val != q.val):
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)