from functools import cache

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        @cache
        def DFS(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            total_sum = 0
            for num in nums:
                total_sum += DFS(i - num)
            
            return total_sum
        return DFS(target)