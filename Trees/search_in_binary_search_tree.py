# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def find(root):
            if not root:
                return None
            
            v = root.val

            if v == val:
                return root

            if v < val:
                return find(root.right)
            else:
                return find(root.left)
         
        return find(root)