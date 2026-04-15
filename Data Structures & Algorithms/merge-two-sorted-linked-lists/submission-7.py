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
        current = None
        head = current

        while list1 and list2:
            if list1.val <= list2.val:
                if current:
                    current.next = list1
                    current = list1
                else:
                    current = list1
                    head = current
                
                list1 = list1.next
            else:
                if current:
                    current.next = list2
                    current = list2
                else:
                    current = list2
                    head = current
                list2 = list2.next

        remaining = list1 if list1 else list2
        
        if current:
            current.next = remaining
        else:
            current = remaining
            head = current
        
        return head

        