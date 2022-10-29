# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        nxt = None
        prev = None
        head = None
        while list1 and list2:
            if list1.val > list2.val:
                nxt = list2.next
                if prev:
                    prev.next = list2
                    list2.next = list1
                else:
                    head = list2
                    head.next = list1
                prev = list2
                list2 = nxt
            else:
                if prev:
                    prev = list1
                    list1 = list1.next
                else:
                    head = prev = list1
                    list1 = list1.next
                
        if list2:
            if prev:
                prev.next = list2
            else:
                head = list2
        if list1:
            if prev:
                prev.next = list1
            else:
                head = list1
        return head
        
        
