# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        levelQ = deque([root])
        totalLevels = 0
        while levelQ:
            for i in range(len(levelQ)):
                queueNode = levelQ.popleft()
                if queueNode.left:
                    levelQ.append(queueNode.left)
                if queueNode.right:
                    levelQ.append(queueNode.right)
            
            totalLevels += 1

        return totalLevels

        # This is the recursive solution
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        