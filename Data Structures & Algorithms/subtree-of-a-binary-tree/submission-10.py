# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import hashlib

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.seen_hashes = set()
        
        # 1. Traverse the main tree to hash and store every subtree
        self.computeHash(root, store=True)
        
        # 2. Compute the hash of the target subtree
        subroot_hash = self.computeHash(subRoot, store=False)
        
        # 3. If the subRoot's hash is in our set, a structural match exists
        return subroot_hash in self.seen_hashes

    def computeHash(self, node: Optional[TreeNode], store: bool) -> str:
        # Base case: Represent empty children with a unique null identifier
        if not node:
            return "#"
        
        # Post-order traversal: Get hashes of children first
        left_hash = self.computeHash(node.left, store)
        right_hash = self.computeHash(node.right, store)
        
        # Create a unique string fingerprint for the current subtree
        # Adding structural delimiters like ',' ensures values like '12' and '1','2' don't collide
        subtree_str = f"{node.val},{left_hash},{right_hash}"
        
        # Convert the string into a secure SHA-256 hash to prevent collisions
        subtree_hash = hashlib.sha256(subtree_str.encode('utf-8')).hexdigest()
        
        # Only store hashes coming from the main 'root' tree
        if store:
            self.seen_hashes.add(subtree_hash)
            
        return subtree_hash

    

    # def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return False
    #     return (self.isSameTree(root, subRoot) or 
    #             self.isSubtree(root.left, subRoot) or 
    #             self.isSubtree(root.right, subRoot))
    
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if p == q == None:
    #         return True
    #     elif not p or not q or (p.val != q.val):
    #         return False
    #     else:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)