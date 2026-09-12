from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)

        for v in grid:
            rows[tuple(v)] += 1

        for i in range(len(grid)):
            col = []
            for j in range(len(grid[0])):
                col.append(grid[j][i])
            cols[tuple(col)] += 1

        count = 0
        for key, value in rows.items():
            if key in cols:
                count += value * cols[key]

        return count
