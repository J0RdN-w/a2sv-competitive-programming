# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        start, sindx, end, eindx, curr = head, 1, head, 1, head.next
        while curr:
            end = curr 
            eindx += 1
            curr = curr.next 
            while sindx <= (eindx//2):
                start = start.next
                sindx += 1
        return start
