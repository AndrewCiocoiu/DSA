INF = 2**31 - 1


class Solution:
    def BFS(self, treasure_chests, grid):
        q = deque(treasure_chests)
        distance = 1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        while q:
            len_q = len(q)

            for i in range(len_q):
                curr_i, curr_j = q.popleft()

                for dir_i, dir_j in directions:
                    new_i = curr_i + dir_i
                    new_j = curr_j + dir_j

                    if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]) or grid[new_i][new_j] != INF:
                        continue
                    
                    q.append((new_i, new_j))
                    grid[new_i][new_j] = distance

            distance += 1
        
        return grid

                         

    
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        treasure_chests = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasure_chests.append((i, j))
        
        self.BFS(treasure_chests, grid)
