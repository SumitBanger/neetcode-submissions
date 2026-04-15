# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first, second = head, head
        index = 0
        while index < n:
            first = first.next
            index += 1
        
        if first == None:
            head = head.next
            return head
        
        while first and first.next:
            first = first.next
            second = second.next

        nodeToRemove = second.next
        second.next = nodeToRemove.next

        return head


        