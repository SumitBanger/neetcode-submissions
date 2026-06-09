# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, currentNode, temp = None, head, None
        while currentNode:
            temp = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = temp
        return prevNode
