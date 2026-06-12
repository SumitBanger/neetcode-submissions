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
        oldNewMap, now = {}, head
        while now:
            newNode = Node(now.val)
            oldNewMap[now], now = newNode, now.next

        now = head
        while now:
            newNode, newNode.next, newNode.random, now = oldNewMap[now], oldNewMap[now.next] if now.next else None, oldNewMap[now.random] if now.random else None, now.next

        return oldNewMap[head]