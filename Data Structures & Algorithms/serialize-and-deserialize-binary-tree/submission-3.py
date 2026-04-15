# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []
        nodesQ = deque([root])
        while nodesQ:
            queueLen = len(nodesQ)
            for index in range(queueLen):
                node = nodesQ.popleft()
                if node:
                    result.append(node.val)
                    nodesQ.append(node.left)
                    nodesQ.append(node.right)
                else:
                    result.append(None)
        
        return ','.join(map(str, result))                
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == 'None': return None
        nodesList = data.split(',')
        nodesListLen = len(nodesList)
        root = TreeNode(int(nodesList[0]))
        nodesQ = deque([root])
        i = 1
        while nodesQ and i < nodesListLen:
            node = nodesQ.popleft()
            
            if node:
                # Process Left Child
                if nodesList[i] != 'None':
                    node.left = TreeNode(int(nodesList[i]))
                    nodesQ.append(node.left)
                i += 1
                
                # Process Right Child (check bounds)
                if i < nodesListLen and nodesList[i] != 'None':
                    node.right = TreeNode(int(nodesList[i]))
                    nodesQ.append(node.right)
                i += 1
        
        return root
