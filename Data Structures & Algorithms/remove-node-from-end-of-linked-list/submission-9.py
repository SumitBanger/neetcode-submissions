# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        while n:
            fast, n = fast.next, n - 1

        if not fast:
            head = head.next
            return head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        
        return head

        