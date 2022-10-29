# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow = fast = head 
        while n > 0:
            fast = fast.next 
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if not fast:
            head = head.next
        elif slow.next:
            slow.next = slow.next.next
        else:
            head = None
        return head
        
        
