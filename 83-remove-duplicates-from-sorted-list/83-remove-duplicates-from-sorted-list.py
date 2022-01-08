# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.ans_1(head)
        
    
    def ans_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        # start = head
        
        # s = ListNode(0, head)
        prev = head
        c = head.next
        
        while prev is not None and c is not None:
            # print(c.val, prev.val)
            if prev.val == c.val:
                prev.next = c.next
            else:    
                prev = c
            c = c.next
        
        return head
                
                
                