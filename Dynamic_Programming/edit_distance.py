from functools import cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        @cache
        def DFS(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i

            if word1[i] == word2[j]:
                return DFS(i + 1, j + 1)

            insert = DFS(i, j + 1)
            delete = DFS(i + 1, j)
            replace= DFS(i + 1, j + 1)

            return 1 + min(insert, delete, replace)
        
        return DFS(0, 0)