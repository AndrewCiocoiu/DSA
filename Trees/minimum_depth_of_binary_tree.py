# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        def DFS(root):
            if not root:
                return 0
            
            if not root.left and root.right:
                return 1 + DFS(root.right)
            elif not root.right and root.left:
                return 1 + DFS(root.left)
            elif root.right and root.left:
                return 1 + min(DFS(root.right), DFS(root.left))
            elif not root.right and not root.left:
                return 1

        
        return DFS(root)