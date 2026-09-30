class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        max_area = 0

        def DFS(start_coords):
            nonlocal grid

            curr_count = 1

            st = [start_coords]
            r, c = start_coords

            grid[r][c] = 0

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            while st:
                r, c = st.pop()

                for direction in directions:
                    new_r = r + direction[0]
                    new_c = c + direction[1]

                    if new_r < 0 or new_r >= len(grid) or new_c < 0 or new_c >= len(grid[0]) or grid[new_r][new_c] == 0:
                        continue
                    
                    grid[new_r][new_c] = 0
                    st.append((new_r, new_c))
                    curr_count += 1
            
            return curr_count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(DFS((i, j)), max_area)
        
        return max_area
