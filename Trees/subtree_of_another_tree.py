# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def find_target(self, root, target):
        if not root:
            return None

        if root.val == target:
            return root
        
        left_found = self.find_target(root.left, target)
        if left_found:
            return left_found
        
        return self.find_target(root.right, target)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        def valid(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return valid(p.left, q.left) and valid(p.right, q.right)
        
        if valid(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)