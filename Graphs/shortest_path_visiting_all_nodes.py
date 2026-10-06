class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)

        if n <= 1:
            return 0

        target_mask = (1 << n) - 1
        
        visited = [[False] * (1 << n) for _ in range(n)]
        for i in range(n):
            visited[i][1<<i] = True

        queue = deque([(i, 1 << i) for i in range(n)])

        steps = 0
        while queue:
            for i in range(len(queue)):
                node, mask = queue.popleft()

                if mask == target_mask:
                    return steps 
                
                for nbr in graph[node]:
                    next_mask = mask | (1 << nbr)
                    if not visited[nbr][next_mask]:
                        visited[nbr][next_mask] = True
                        queue.append((nbr, next_mask))
            steps += 1
        
        return -1

