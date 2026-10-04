from functools import cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        @cache
        def DFS(i, j):
            if i > len(obstacleGrid) - 1 or j > len(obstacleGrid[0]) - 1 or obstacleGrid[i][j]:
                return 0
            if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                return 1
            return DFS(i + 1, j) + DFS(i, j + 1)
        
        return DFS(0, 0)