# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        reversed = prev
        current = head
        while reversed:
            nextFromFront, nextFromBack = current.next, reversed.next

            current.next = reversed
            if reversed != nextFromFront:
                reversed.next = nextFromFront
            
            current, reversed = nextFromFront, nextFromBack
