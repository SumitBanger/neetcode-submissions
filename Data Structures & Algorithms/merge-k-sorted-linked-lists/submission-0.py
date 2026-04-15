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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        totalLists = len(lists)
        mergedTillNow = None
        for index in range(totalLists):
            currentList = lists[index]
            mergedTillNow = self.mergeTwoLists(currentList, mergedTillNow)

        return mergedTillNow



        