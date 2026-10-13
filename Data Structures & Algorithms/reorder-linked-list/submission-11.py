# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        # Find the mid element
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        # Revert the 2nd Half of the LL
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        front, back = head, prev

        # Start joining from front and back together
        while back and front != back:
            nextFromFront, nextFromBack, front.next = front.next, back.next, back
            if back != nextFromFront:
                back.next = nextFromFront
            front, back = nextFromFront, nextFromBack
        