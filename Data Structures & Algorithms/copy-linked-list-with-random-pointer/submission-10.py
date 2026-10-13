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
            oldNewMap[now], now = Node(now.val), now.next

        now = head
        while now:
            newNode = oldNewMap[now]
            newNode.next, newNode.random = oldNewMap.get(now.next), oldNewMap.get(now.random)
            now = now.next

        return oldNewMap[head]