# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.ans_2(root)
    
    '''
    Recursive approach
    TC = O(n)
    SC = O(n)
    '''
    def ans_1(self, root):
        
        if root is None:
            return []
        else:
            return [root.val] + self.ans_1(root.left) + self.ans_1(root.right)
    
    '''
    Stack Approach
    TC = O(n)
    SC = O(n)
    '''
    def ans_2(self, root):
        
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            root = stack.pop()
            
            if root:
                stack.append(root.right)
                stack.append(root.left)
                result.append(root.val)
                
        return result
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        