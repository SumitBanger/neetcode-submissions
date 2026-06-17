# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, result = deque([root] if root else []), []

        while queue:
            perLevelResult = []
            length = len(queue)
            for index in range(length):
                ele = queue.popleft()
                if index == length - 1:
                    perLevelResult.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            
            result.extend(perLevelResult)
        
        return list(result)        