# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        return self.ans_1(head, val)
        
    def ans_1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        s = ListNode(0)
        s.next = head
        
        prev = s
        curr = head
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            
        return s.next
            