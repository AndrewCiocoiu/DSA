from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (u, v), val in zip(equations, values):
            adj[u].append((v, val))
            adj[v].append((u, 1.0 / val))
        
        def bfs(start: str, target: str) -> float:
            if start not in adj or target not in adj:
                return -1.0
            
            if start == target:
                return 1.0
            
            q = deque([(start, 1.0)])
            visited = {start}
            
            while q:
                node, curr_val = q.popleft()
                
                if node == target:
                    return curr_val
                
                for nbr, weight in adj[node]:
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append((nbr, curr_val * weight))
            
            return -1.0
        
        return [bfs(s, e) for s, e in queries]