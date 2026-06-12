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
        if not head:
            return None
        oldToNewNode, newHead, current = {}, None, head
        while current:
            newNode = Node(current.val)
            oldToNewNode[current] = newNode
            current = current.next

        current = head
        while current:
            newNode, newNext, newRandom = oldToNewNode[current], oldToNewNode[current.next] if current.next else None, oldToNewNode[current.random] if current.random else None
            newNode.next, newNode.random = newNext, newRandom
            current = current.next

        return oldToNewNode[head]