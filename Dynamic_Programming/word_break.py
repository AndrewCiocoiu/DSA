from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @cache
        def DFS(i):
            n = len(s)

            if i == len(s):
                return True
            
            for j in range(i + 1, n + 1):
                if s[i:j] in words and DFS(j):
                    return True
            
            return False
        
        return DFS(0)
