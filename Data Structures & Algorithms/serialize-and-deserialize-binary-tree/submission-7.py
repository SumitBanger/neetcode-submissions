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
        nodeList, queue = data.split(","), deque()
        root = TreeNode(int(nodeList[0])) if nodeList[0] != "None" else None
        queue.append(root)
        index = 1
        while queue and index < len(nodeList):
            node = queue.popleft()
            if node:
                leftChildVal = nodeList[index]
                rightChildVal = nodeList[index + 1] if index + 1 < len(nodeList) else "None"
                print(f"node: {node.val}, leftChildVal: {leftChildVal}, rightChildVal: {rightChildVal}, index: {index}")
                leftChild = TreeNode(int(leftChildVal)) if leftChildVal != "None" else None
                rightChild = TreeNode(int(rightChildVal)) if rightChildVal != "None" else None
                node.left, node.right = leftChild, rightChild
                queue.append(leftChild)
                queue.append(rightChild)
                index = index + 2


        return root


