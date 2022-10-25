# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        slow, start, fast, end, curr = head, 1, head, 1, head.next
        while curr:
            fast = curr 
            end += 1
            curr = curr.next 
            while start <= (end//2):
                slow = slow.next
                start += 1
        return slow
            
        
