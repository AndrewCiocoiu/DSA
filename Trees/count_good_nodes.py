# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def DFS(root, greatest):
            nonlocal count
            if not root:
                return
            
            if root.val >= greatest:
                count += 1
                greatest = root.val
            
            DFS(root.left, greatest)
            DFS(root.right, greatest)

        DFS(root, float("-inf"))

        return count