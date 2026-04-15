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
        isSubtreeAtCurrent = self.isSameTree(root, subRoot)

        return isSubtreeAtCurrent or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False

        isCurrentSame = True if (p.val == q.val) else False
        return isCurrentSame and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        