from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        g = defaultdict(list)

        for s, t in edges:
            g[s].append(t)
            g[t].append(s)

        visited = set()
        def DFS(node, parent):  
            visited.add(node)

            for n in g[node]:
                if n == parent:
                    continue
                if n in visited:
                    return False
                if not DFS(n, node):
                    return False

            return True

        valid = DFS(0, -1)

        if valid and len(visited) == n:
            return True
        else:
            return False 
