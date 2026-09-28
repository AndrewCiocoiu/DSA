# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def BFS(root):
            nonlocal balanced
            
            if not root:
                return 0
        
            left_side = BFS(root.left)
            right_side = BFS(root.right)

            if abs(left_side - right_side) > 1:
                balanced = False
            
            return 1 + max(left_side, right_side)
        
        BFS(root)

        return balanced