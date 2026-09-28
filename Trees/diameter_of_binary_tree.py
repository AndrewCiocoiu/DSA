# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_height(self, root):
        if not root:
            return 0
        return 1 + max(self.find_height(root.left), self.find_height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_sum = 0

        def DFS(root):
            nonlocal max_sum

            if not root:
                return
            DFS(root.left)
            DFS(root.right)
            diam = self.find_height(root.left) + self.find_height(root.right)

            if diam > max_sum:
                max_sum = diam
        
        DFS(root)
        
        return max_sum