# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        front, back = head, prev

        while back and front != back:
            front.next, nextFromFront, nextFromBack = back, front.next, back.next
            if back != nextFromFront:
                back.next = nextFromFront
            front, back = nextFromFront, nextFromBack
        