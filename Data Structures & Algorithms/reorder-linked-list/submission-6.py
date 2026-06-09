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
        
        prev = temp =  None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        front, reverseList = head, prev

        while reverseList and reverseList != front:
            nextFromFront, nextFromBack = front.next, reverseList.next
            front.next = reverseList
            if reverseList != nextFromFront:
                reverseList.next = nextFromFront
            front, reverseList = nextFromFront, nextFromBack
        