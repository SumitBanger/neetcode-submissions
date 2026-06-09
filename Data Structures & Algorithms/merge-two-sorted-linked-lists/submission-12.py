# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2, temp = list1, list2, None
        head = mergedListHead = ListNode()
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                mergedListHead.next = ptr1
                ptr1 = ptr1.next
            else:
                mergedListHead.next = ptr2
                ptr2 = ptr2.next
            mergedListHead = mergedListHead.next

        mergedListHead.next = ptr1 if ptr1 else ptr2
        return head.next
        