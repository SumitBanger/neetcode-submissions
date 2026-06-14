# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start, prevStart, result = head, head, None
        while start:
            end, nextStart = self.reverseList(start, k)
            if start != head:
                prevStart.next, prevStart, start = end, start, nextStart
            else:
                start, result = nextStart, end
        
        return result

    def reverseList(self, head, k):
        index, current = 0, head
        while current and index < k:
            current, index = current.next, index + 1
        
        if index < k:
            return (head, None)

        prev, current = None, head
        while current and k:
            current.next, prev, current, k = prev, current, current.next, k - 1
        
        return (prev, current)


    
