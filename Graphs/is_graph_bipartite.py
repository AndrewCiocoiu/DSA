class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}

        for i in range(len(graph)):
            if i in color:
                continue
            
            q = deque([i])
            color[i] = 0

            while q:
                current = q.popleft()
                for nbr in graph[current]:
                    if nbr not in color:
                        color[nbr] = 1 - color[current]
                        q.append(nbr)
                    else:
                        if color[nbr] == color[current]:
                            return False
        return True