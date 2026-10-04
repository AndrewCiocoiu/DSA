from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def DFS(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + DFS(i + 1, j + 1)
            
            return max(DFS(i + 1, j), DFS(i, j + 1))
        
        return DFS(0, 0)