# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def DFS(root):
            nonlocal max_sum

            if not root:
                return 0
            
            left_side = DFS(root.left)
            right_side  = DFS(root.right)

            curr_sum = left_side + right_side
            if curr_sum > max_sum:
                max_sum = curr_sum
            
            return 1 + max(left_side, right_side)

        DFS(root)
        
        return max_sum