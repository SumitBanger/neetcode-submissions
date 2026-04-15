"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currentToNewNodeMap = {}
        current = head
        while current:
            currentToNewNodeMap[current] = Node(current.val)
            current = current.next

        current = head
        head = currentToNewNodeMap[current] if current else None
        while current:
            newNode = currentToNewNodeMap[current]
            newNode.next = currentToNewNodeMap[current.next] if current.next else None
            newNode.random = currentToNewNodeMap[current.random] if current.random else None
            current = current.next
        
        return head
        