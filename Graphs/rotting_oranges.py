class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
        
        visited = set(rotten_oranges)
        queue = deque(rotten_oranges)
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        while queue:
            q_len = len(queue)

            for _ in range(q_len):
                i, j = queue.popleft()
                grid[i][j] = 2

                for dir_i, dir_j in directions:
                    new_i, new_j = i + dir_i, j + dir_j
                    if new_i >= 0 and new_i < len(grid) and new_j >= 0 and new_j < len(grid[0]) and grid[new_i][new_j] == 1 and (new_i, new_j) not in visited:
                        visited.add((new_i, new_j))
                        queue.append((new_i, new_j))
            
            count += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return count - 1 if count else 0

