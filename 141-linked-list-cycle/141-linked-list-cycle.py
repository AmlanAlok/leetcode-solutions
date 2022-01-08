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
        return self.ans_1(head)
        
    def ans_1(self, head: Optional[ListNode]) -> bool:
        
        d = set()
        c = head
        
        while c is not None:
            if c in d:
                return True
            d.add(c)
            # print(d)
            c = c.next
        
        # print(d)
        
        return False

        # nodes_seen = set()
        # while head is not None:
        #     if head in nodes_seen:
        #         return True
        #     nodes_seen.add(head)
        #     head = head.next
        # return False
            
    
        