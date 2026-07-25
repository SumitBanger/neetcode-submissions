"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def cloneNode(currentNode):
            if currentNode in oldToNew:
                return oldToNew[currentNode]
            
            clone = Node(currentNode.val)
            oldToNew[currentNode] = clone
            for neighbor in currentNode.neighbors:
                clone.neighbors.append(cloneNode(neighbor))

            return clone

        return cloneNode(node) if node else None

        nodeToCopyMap, Q = {}, deque([node])
        if not node: return None

        while Q:
            currentNode = Q.popleft()
            nodeToCopyMap[currentNode] = Node(currentNode.val)
            for neighbor in currentNode.neighbors:
                if neighbor and neighbor not in nodeToCopyMap:
                    Q.append(neighbor)
        
        for originalNode, copyNode in nodeToCopyMap.items():
            for neighbor in originalNode.neighbors:
                copyNode.neighbors.append(nodeToCopyMap[neighbor])

        return nodeToCopyMap[node]

                


        