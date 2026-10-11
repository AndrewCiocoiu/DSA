# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        adj_list = defaultdict(list)

        def create_adj_list(root):
            if not root:
                return
            if root.left:
                adj_list[root.val].append(root.left.val)
                adj_list[root.left.val].append(root.val)
            if root.right:
                adj_list[root.val].append(root.right.val)
                adj_list[root.right.val].append(root.val)

            create_adj_list(root.left)
            create_adj_list(root.right)

        create_adj_list(root)

        q = deque([start])
        visited = set([start])

        distance_count = 0
        while(q):
            for i in range(len(q)):
                curr = q.popleft()
                for nbr in adj_list[curr]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)
            
            distance_count += 1

        return distance_count - 1
        