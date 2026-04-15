# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        length = len(preorder)
        if length == 0:
            return None
        
        rootVal = preorder[0]
        rootNode = TreeNode(rootVal)
        if length == 1:
            return rootNode

        rootValIndex = inorder.index(rootVal)
        rootNode.left = self.buildTree(preorder[1:rootValIndex + 1], inorder[0:rootValIndex])
        rootNode.right = self.buildTree(preorder[rootValIndex + 1:length], inorder[rootValIndex + 1:length])

        return rootNode
        