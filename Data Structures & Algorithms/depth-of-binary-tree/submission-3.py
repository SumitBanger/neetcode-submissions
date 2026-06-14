# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        if not root:
            return level
        queue = deque([root])
        while queue:
            level += 1
            levelSize = len(queue)
            for _ in range(levelSize):
                parent = queue.popleft()
                if parent.left:
                    queue.append(parent.left)
                if parent.right:
                    queue.append(parent.right)
                
        return level

        