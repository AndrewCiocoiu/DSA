from functools import cache

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        @cache
        def DFS(i, rem):
            if i >= len(coins):
                return 0
            if rem == 0:
                return 1
            if rem < 0:
                return 0
            
            return DFS(i, rem - coins[i]) + DFS(i + 1, rem)
        
        return DFS(0, amount)