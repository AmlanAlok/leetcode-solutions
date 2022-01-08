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
        return self.ans_3(head)
    
    
    def ans_3(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
        
        return True
    
    # My approach after referring solution 2
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

            
    
        