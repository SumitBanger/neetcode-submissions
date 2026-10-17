# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        length, leftHalf, rightHalf = len(lists), None, None
        if length == 0: return None
        if length == 1: return lists[0]

        mid = length // 2
        leftHalf = self.mergeKLists(lists[0:mid])
        rightHalf = self.mergeKLists(lists[mid: length])
        return self.mergeTwoLists(leftHalf, rightHalf)

        ###### BELOW IS ITERATIVE APPROACH #######
        # Continue merging pairs until only one consolidated list remains
        # while len(lists) > 1:
        #     merged_lists = []
            
        #     # Step through the lists 2 at a time
        #     for i in range(0, len(lists), 2):
        #         list1 = lists[i]
        #         # If there's an odd number of lists, the last one won't have a pair
        #         list2 = lists[i + 1] if (i + 1) < len(lists) else None
                
        #         # Use your exact merge function to combine the pair
        #         merged_lists.append(self.mergeTwoLists(list1, list2))
                
        #     # Overwrite the original array with the newly paired lists
        #     lists = merged_lists
            
        # return lists[0]


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