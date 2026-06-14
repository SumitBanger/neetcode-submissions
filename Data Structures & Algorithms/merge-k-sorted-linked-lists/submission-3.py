# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length, leftHalf, rightHalf = len(lists), None, None

        if length > 2:
            mid = length // 2
            leftHalf = self.mergeKLists(lists[0:mid + 1])
            rightHalf = self.mergeKLists(lists[mid + 1: length])
        elif length == 2:
            leftHalf = lists[0]
            rightHalf = lists[1]
        else:
            leftHalf = lists[0] if length == 1 else None
            rightHalf = None
        return self.mergeTwoLists(leftHalf, rightHalf)


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next, list1 = list1, list1.next
            else:
                dummy.next, list2 = list2, list2.next
            dummy = dummy.next
        
        dummy.next = list1 if list1 else list2
        return head.next