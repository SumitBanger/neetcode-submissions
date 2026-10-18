# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 1. Map values to their indices in the inorder list for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Track the current index position in the preorder traversal list globally
        self.pre_idx = 0
        
        def helper(in_start, in_end):
            # Base Case: No elements left in the current subtree range
            if in_start > in_end:
                return None
            
            # The first element in preorder traversal window is always the root node
            root_val = preorder[self.pre_idx]
            root_node = TreeNode(root_val)
            self.pre_idx += 1
            
            # O(1) index lookup using our hash map
            root_val_index = inorder_map[root_val]
            
            # Construct left and right subtrees by shifting pointers
            root_node.left = helper(in_start, root_val_index - 1)
            root_node.right = helper(root_val_index + 1, in_end)
            
            return root_node
            
        return helper(0, len(inorder) - 1)


        
                
        if not preorder or not inorder:
            return None
        
        rootNode = TreeNode(preorder[0])
        rootValIndex = inorder.index(rootNode.val)
        rootNode.left = self.buildTree(preorder[1: rootValIndex + 1], inorder[: rootValIndex])
        rootNode.right = self.buildTree(preorder[rootValIndex + 1: ], inorder[rootValIndex + 1: ])

        return rootNode
        