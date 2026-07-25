"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeToCopyMap, Q, clonedHead = {}, deque([node]), None
        if not node: return None

        while Q:
            currentNode = Q.popleft()
            copyNode = Node(currentNode.val)
            nodeToCopyMap[currentNode] = copyNode
            for neighbor in currentNode.neighbors:
                if neighbor and neighbor not in nodeToCopyMap:
                    Q.append(neighbor)
        
        for originalNode, copyNode in nodeToCopyMap.items():
            copyNeighbors = []
            for neighbor in originalNode.neighbors:
                copyNeighbors.append(nodeToCopyMap[neighbor])
            copyNode.neighbors = copyNeighbors
            if not clonedHead:
                clonedHead = copyNode

        return clonedHead

                


        