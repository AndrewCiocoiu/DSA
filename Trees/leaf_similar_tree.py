# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root, tree):
            if not root:
                return
            if not root.left and not root.right:
                tree.append(root.val)
                return
            get_leaves(root.left, tree)
            get_leaves(root.right, tree)

        tree1 = []
        tree2 = []

        get_leaves(root1, tree1)
        get_leaves(root2, tree2)


        return tuple(tree1) == tuple(tree2)
        
