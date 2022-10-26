# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        if not head or not head.next:
            return head
        filtered, prev = None, None
        node = head 
        while node:
            if node.next and node.val == node.next.val:
                val = node.val
                node = node.next 
                while node and val == node.val:
                     node = node.next
                if prev:
                    prev.next = None
            else:
                if prev is None:
                    prev = filtered = node
                else:
                    prev.next = node
                    prev = node
                node = node.next 
        return filtered 
        
