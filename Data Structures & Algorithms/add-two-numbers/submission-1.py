# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resListHead = None
        carryForward = 0
        currentVal = 0
        prevNode = None
        while l1 or l2 or carryForward != 0:
            currentNode = ListNode()
            if resListHead == None:
                resListHead = currentNode
            else:
                prevNode.next = currentNode

            sum = carryForward + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            currentVal = sum % 10
            carryForward = sum // 10
            currentNode.val = currentVal
            currentNode.next = None
            prevNode = currentNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return resListHead