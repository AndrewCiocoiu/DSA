from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def DFS(i, j):
            if i == j:
                return 1
            if i > j:
                return 0
            
            if s[i] == s[j]:
                return 2 + DFS(i + 1, j - 1)
            
            return max(DFS(i + 1, j), DFS(i, j - 1))
        
        return DFS(0, len(s) - 1)