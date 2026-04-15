# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        prevLoopStart = None
        while current:
            countTillNow = 0
            prev = None
            while countTillNow < k:
                if countTillNow == 0:
                    currentLoopStart = current
                if current:
                    nextEle = current.next
                    current.next = prev
                    prev = current
                    current = nextEle
                    countTillNow += 1
                    flag = 0
                else: #reverse again last part of loop till currentLoopStart
                    current = prev
                    prev = None
                    while current:
                        nextEle = current.next
                        current.next = prev
                        prev = current
                        current = nextEle
                    
                    prevLoopStart.next = currentLoopStart
                    flag = 1
                    break

            if prevLoopStart == None:
                head = prev
            else:
                if flag == 0:
                    prevLoopStart.next = prev
            prevLoopStart = currentLoopStart

            if current == None and flag == 0:
                currentLoopStart.next = None
                break

        return head