from functools import cache

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        @cache
        def DFS(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
            
            return DFS(i + 1, current_sum - nums[i]) + DFS(i + 1, current_sum + nums[i])
        
        return DFS(0, 0)
