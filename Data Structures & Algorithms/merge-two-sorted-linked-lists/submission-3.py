# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        remaining = list1 if list1 else list2
        current.next = remaining
        
        return dummy.next
        
        # Below code is solved without using a Dummy node
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        head, current = None, None

        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head = list1
                    current = list1
                else:
                    current.next = list1
                    current = list1
                list1 = list1.next
            else:
                if not head:
                    head = list2
                    current = list2
                else:
                    current.next = list2
                    current = list2
                list2 = list2.next

        remaining = list1 if list1 else list2
        current.next = remaining
        
        return head

        