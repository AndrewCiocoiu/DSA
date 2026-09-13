class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        visited = set([tuple(entrance)])
        q = deque([tuple(entrance)])

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        count = 0

        while q:
            q_size = len(q)
            

            for _ in range(q_size):
                node = q.popleft()

                if (node[0] == 0 or node[0] == len(maze) - 1 or node[1] == 0 or node[1] == len(maze[0]) - 1) and node != tuple(entrance):
                    return count
                for direction in directions:
                    new_node = (node[0] + direction[0], node[1] + direction[1])
                    if new_node[0] >= 0 and new_node[0] < len(maze) and new_node[1] >= 0 and new_node[1] < len(maze[0]) and maze[new_node[0]][new_node[1]] == '.' and new_node not in visited:
                        q.append(new_node)
                        visited.add(new_node)
            
            count += 1
            

        return -1