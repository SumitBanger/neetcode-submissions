# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue, result = deque([root]), []

        while queue:
            inner = []
            length = len(queue)
            while length:
                ele = queue.popleft()
                length -= 1
                inner.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            
            result.append(inner)
        
        return list(result)