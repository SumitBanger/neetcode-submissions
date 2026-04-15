# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        levelQ = deque([root])

        while levelQ:
            queueLength = len(levelQ)
            for index in range(queueLength):
                currentNode = levelQ.popleft()
                if index == queueLength - 1:
                    result.append(currentNode.val)
                if currentNode.left:
                    levelQ.append(currentNode.left)
                if currentNode.right:
                    levelQ.append(currentNode.right)
                    
        return result