# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode, temp = None, None
        while head:
            temp = head.next
            head.next = prevNode
            prevNode = head
            head = temp
        
        return prevNode
