# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Q How many max elements can be in the linked list?
# Q What is the min and max value of val?
# Q Will all the entries be unique?

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.ans_2(head)
    
    def ans_2(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != None and fast != None:
            
            if slow == fast:
                return True
            if fast.next == None or slow.next == None:
                return False
            
            fast = fast.next.next
            slow = slow.next
                
        return False
            
            
        
    def ans_1(self, head: Optional[ListNode]) -> bool:
        
        d = set()
        c = head
        
        while c is not None:
            if c in d:
                return True
            d.add(c)
            c = c.next
        return False

            
    
        