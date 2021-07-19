# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.recurse(l1, l2, 0)
    
    def recurse(self, l1: ListNode, l2: ListNode, carry: int) -> ListNode:
        if l1 is None and l2 is None:
            if carry == 0:
                return None
            else:
                return ListNode(carry, None)
        else:
            l1Next = None
            l2Next = None
            carryNext = 0
            curSum = 0
            if l1 is None and l2 is not None:
                curSum = carry + l2.val
                l1Next = None
                l2Next = l2.next
            elif l1 is not None and l2 is None:
                curSum = carry + l1.val
                l1Next = l1.next
                l2Next = None                
            else:
                curSum = carry + l2.val + l1.val
                l1Next = l1.next
                l2Next = l2.next
            curVal = curSum % 10
            carryNext = curSum // 10
            return ListNode(curVal, self.recurse(l1Next, l2Next, carryNext))
