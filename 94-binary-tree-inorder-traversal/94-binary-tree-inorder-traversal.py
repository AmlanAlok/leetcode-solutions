# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.ans(root)
    
    def ans(self, root: Optional[TreeNode]) -> List[int]:

    #         stack = [root]
    #         ans = []

    #         while stack:

    #             if root is not None:
    #                 root = root.left
    #             else:
        if not root:
            return []
        else:
            return self.ans(root.left) + [root.val] + self.ans(root.right)