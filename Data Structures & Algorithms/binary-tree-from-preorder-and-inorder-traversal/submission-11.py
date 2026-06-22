# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        rootNode = TreeNode(preorder[0])
        rootValIndex = inorder.index(rootNode.val)
        rootNode.left = self.buildTree(preorder[1: rootValIndex + 1], inorder[: rootValIndex])
        rootNode.right = self.buildTree(preorder[rootValIndex + 1: ], inorder[rootValIndex + 1: ])

        return rootNode
        