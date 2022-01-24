# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.ans_1(root)
        
    def ans_1(self, root):
        
        if root is None:
            return []
        else:
            return [root.val] + self.ans_1(root.left) + self.ans_1(root.right)
        
        