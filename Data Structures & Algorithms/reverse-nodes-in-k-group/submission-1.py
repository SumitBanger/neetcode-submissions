# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        totalLength = self.findLength(head)
        groupsTillNow, totalGroups = 0, totalLength // k
        current = head
        while groupsTillNow < totalGroups:
            currentGroupStart, nextGroupStart = self.reverseGivenListGroup(current, k)
            if groupsTillNow == 0:
                head = currentGroupStart
            else:
                prevGroupEnd.next = currentGroupStart
            
            prevGroupEnd = current
            current = nextGroupStart
            groupsTillNow += 1

        prevGroupEnd.next = current

        return head

    
    def reverseGivenListGroup(self, head: Optional[ListNode], k: int):
        current = head
        countTillNow = 0
        prevEle = None
        while countTillNow < k:
            nextEle = current.next
            current.next = prevEle
            prevEle = current
            current = nextEle
            countTillNow += 1
        
        return (prevEle, nextEle)
    
    def findLength(self, head: Optional[ListNode]):
        current = head
        countTillNow = 0
        while current:
            current = current.next
            countTillNow += 1
        
        return countTillNow


        # This Solution is single pass and although works but is very badly written and not easy to understand
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