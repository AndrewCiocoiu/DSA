# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        is_true = True
        def DFS(root):
            nonlocal is_true

            if not root:
                return 0
            left = DFS(root.left)
            right = DFS(root.right)

            if abs(left - right) > 1:
                is_true = False
            return 1 + max(left, right)   
        
        DFS(root)

        if is_true:
            return True
        else:
            return False
        