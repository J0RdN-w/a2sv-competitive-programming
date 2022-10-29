# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        rem = 0
        head = sums = None
        while l1 or l2 or rem:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            val += rem
            if head:
                sums.next = ListNode(val % 10)
                sums = sums.next
                rem = val // 10
            else:
                head = sums = ListNode(val % 10)
                rem = val // 10
        return head
                
            
            
            
        
