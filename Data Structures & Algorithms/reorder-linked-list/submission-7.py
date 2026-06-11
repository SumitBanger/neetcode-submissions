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
        if not fast:
            temp, current = head, head.next
            while current != slow:
                temp, current = current, current.next
            temp.next = None

        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        front, back = head, prev
        while (front and back) and (front != back):
            front.next, back.next, front, back = back, front.next, front.next, back.next







        # slow = fast = head
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next
        
        # prev = temp =  None
        # while slow:
        #     temp = slow.next
        #     slow.next = prev
        #     prev = slow
        #     slow = temp
        
        # front, reverseList = head, prev

        # while reverseList and reverseList != front:
        #     nextFromFront, nextFromBack = front.next, reverseList.next
        #     front.next = reverseList
        #     if reverseList != nextFromFront:
        #         reverseList.next = nextFromFront
        #     front, reverseList = nextFromFront, nextFromBack
        