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

    # This is a optimal O(n.logk) approach
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        while len(lists) > 1:
            mergedList = []
            for index in range(0, len(lists), 2):
                firstList = lists[index]
                secondList = lists[index + 1] if (index + 1 < len(lists)) else None
                mergedList.append(self.mergeTwoLists(firstList, secondList))

            lists = mergedList;

        return lists[0] if lists else None

    # This is a suboptimal O(n.k) approach
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        totalLists = len(lists)
        mergedTillNow = None
        for index in range(totalLists):
            currentList = lists[index]
            mergedTillNow = self.mergeTwoLists(currentList, mergedTillNow)

        return mergedTillNow



        