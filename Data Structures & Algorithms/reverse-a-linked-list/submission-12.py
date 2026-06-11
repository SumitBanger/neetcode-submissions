# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if not head:
            return None
        
        prev, current = None, head
        while current:
            #Python evaluates the entire right side first before assigning anything to the left side. 
            #It creates a temporary tuple in memory containing the old, unchanged values.
            current.next, prev, current = prev, current, current.next
            # temp = current.next
            # current.next = prev
            # prev = current
            # current = temp

        return prev
        
        
        
        
        
        
        
        
        
        
        
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
        
        
        
        
        
        
        # while head:
        #     temp = head.next
        #     head.next = prevNode
        #     prevNode = head
        #     head = temp
        
        # return prevNode
