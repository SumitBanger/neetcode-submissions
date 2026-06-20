# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        leftLimit, rightLimit = float("-infinity"), float("infinity")
        return self.isBSTValid(root, leftLimit, rightLimit)

    def isBSTValid(self, root, leftLimit, rightLimit):
        if not root:
            return True
        
        isCurrentNodeValid = True if leftLimit < root.val < rightLimit else False
        isLeftSubtreeValid = self.isBSTValid(root.left, leftLimit, root.val)
        isRightSubtreeValid = self.isBSTValid(root.right, root.val, rightLimit)
        return isCurrentNodeValid and isLeftSubtreeValid and isRightSubtreeValid

        