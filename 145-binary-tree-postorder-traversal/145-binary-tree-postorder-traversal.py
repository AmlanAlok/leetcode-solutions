# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.ans_2(root)
        
    def ans_2(self, root):
        
        stack = deque()
        curr = root
        ans = []
        
        while stack or curr:
            
#             if curr:
#                 stack.append(curr)
#                 if curr.right:
#                     stack.append(curr.right)
#                 # if curr.left:
#                 #     stack.append(curr.left) 
#                 curr = curr.left
                
#             else:
#                 curr = stack.pop()
#                 ans.append(curr.val)
#                 curr = curr.left
            
            if curr:
                if curr.right:
                    stack.append(curr.right)
                stack.append(curr)
                curr = curr.left
            
            else:
                curr = stack.pop()
                if len(stack) > 0 and curr.right == stack[-1]:
                    temp = curr
                    curr = stack.pop()
                    stack.append(temp)
                    # curr = curr.right
                else:
                    ans.append(curr.val)
                    curr = None
                    
        return ans
                
        
        