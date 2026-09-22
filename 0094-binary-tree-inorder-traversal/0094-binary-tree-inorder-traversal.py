# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        stack = []
        def ans(node):
            if not node:
                return 
            ans(node.left)
            stack.append(node.val)
            ans(node.right)

        ans(root)    
        return stack
    