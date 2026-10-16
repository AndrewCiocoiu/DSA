import sys

sys.setrecursionlimit(20000)
class Solution:
    def find_succesor(self, root):
        if not root:
            return None
        
        while root.left:
            root = root.left
        
        return root

    def delete_node(self, root, key):
        if not root:
            return None
        
        if root.val < key:
            root.right = self.delete_node(root.right, key)
        elif root.val > key:
            root.left = self.delete_node(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succ = self.find_succesor(root.right)
                root.val = succ.val

                root.right = self.delete_node(root.right, succ.val)
        return root    

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        if root.val < low or root.val > high:
            root = self.delete_node(root, root.val)
            
        return root