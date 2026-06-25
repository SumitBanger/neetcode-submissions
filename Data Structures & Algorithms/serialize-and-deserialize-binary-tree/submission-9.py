# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        result, queue = [], deque([root])
        while queue:
            length = len(queue)
            for index in range(length):
                node = queue.popleft()
                if node:
                    result.append(str(node.val))
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result.append("None")

        string = ",".join(result)
        print(string)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == '': return None
        nodeList, queue, index = data.split(","), deque(), 1
        root = self.getTreeNode(nodeList[0])
        queue.append(root)
        while queue and index < len(nodeList):
            node = queue.popleft()
            if node:
                leftChildVal = nodeList[index]
                rightChildVal = nodeList[index + 1] if index + 1 < len(nodeList) else "None"
                node.left, node.right = self.getTreeNode(leftChildVal), self.getTreeNode(rightChildVal)
                queue.append(node.left)
                queue.append(node.right)
                index = index + 2
        return root

    def getTreeNode(self, value):
        return TreeNode(int(value)) if value != "None" else None

