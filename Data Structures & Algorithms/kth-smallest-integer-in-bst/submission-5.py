# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while curr or stack:
            # 1. Travel as far left as possible, pushing paths onto the stack
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process the leftmost node currently available
            curr = stack.pop()
            k -= 1
            
            # 3. If k hits 0, we found our kth smallest element!
            if k == 0:
                return curr.val
            
            # 4. Move to the right subtree to continue ascending order
            curr = curr.right

        # result = []
        # self.DFS(root, result)
        # return result[k-1]
    #     count = 0
    #     return self.DFS1(root, k, count)


    # def DFS1(self, root, k, count):
    #     if count == k - 1: return root.val
    #     if root.left:
    #         self.DFS1(root.left, k, count)
    #     if root:
    #         count += 1
    #         if count == k: return root.val
    #     if root.right:
    #         self.DFS1(root.right, k, count)
    

    # def DFS(self, root, result):
    #     if not root: return 
        
    #     self.DFS(root.left, result)
    #     result.append(root.val)
    #     self.DFS(root.right, result)








        