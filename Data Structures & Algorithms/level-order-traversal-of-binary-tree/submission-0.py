# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        levelQ = deque([root])

        while levelQ:
            perLevelResult = []
            for i in range(len(levelQ)):
                currentNode = levelQ.popleft()
                perLevelResult.append(currentNode.val)
                if currentNode.left:
                    levelQ.append(currentNode.left)
                if currentNode.right:
                    levelQ.append(currentNode.right)
            
            result.append(perLevelResult)
        
        return result


        