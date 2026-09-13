# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def BFS(root):
            if not root:
                return []

            levels = []
            queue = deque([root])

            while queue:
                q_size = len(queue)
                current_level = []
                
                for _ in range(q_size):
                    curr = queue.popleft()
                    current_level.append(curr.val)

                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                levels.append(current_level[-1])

            return levels

        return BFS(root)
