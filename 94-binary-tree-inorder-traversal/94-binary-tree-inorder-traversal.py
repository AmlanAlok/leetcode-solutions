# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.ans_1(root)
    
    def ans_1(self, root):
        
        if not root:
            return root
        
        e = []
        
        if root.left:
            e += self.ans_1(root.left)
            
        e.append(root.val)
        
        if root.right:
            e += self.ans_1(root.right)
            
        return e