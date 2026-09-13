# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def BFS(root):
            sums = []
            q = deque([root])
        
            while q:
                q_size = len(q)
                level = []

                for _ in range(q_size):
                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                sums.append(sum(level))

            return sums.index(max(sums)) + 1  
        
        return BFS(root)