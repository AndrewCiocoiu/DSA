from functools import cache

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        @cache
        def DFS(i):
            if i == 0:
                return 0
            if i < 0:
                return float("inf")
            
            current_min = float("inf")
            for coin in coins:
                current_min = min(current_min, 1 + DFS(i - coin))
            
            return current_min
        
        amount = DFS(amount)
        return amount if amount != float("inf") else -1