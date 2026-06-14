# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            parent = queue.popleft()
            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)
            parent.left, parent.right = parent.right, parent.left
        
        return root

        # if not root:
        #     return None
        
        # invertLeft = self.invertTree(root.left)
        # invertRight = self.invertTree(root.right)
        # root.left, root.right = invertRight, invertLeft
        # return root
        