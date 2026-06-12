# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, remainder = ListNode(), 0
        head = dummy
        while l1 or l2 or remainder:
            sumVal = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder
            head.next = ListNode(sumVal % 10)
            head, l1, l2, remainder = head.next, l1.next if l1 else None, l2.next if l2 else None, sumVal // 10
            print(f"sumVal: {sumVal}, remainder: {remainder}")

        return dummy.next
  