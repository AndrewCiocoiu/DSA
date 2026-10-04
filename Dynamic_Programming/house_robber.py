from functools import cache

class Solution:
    def rob(self, nums: list[int]) -> int:
        @cache
        def DFS(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[i], nums[i - 1])
            
            return max(nums[i] + DFS(i - 2), DFS(i - 1))

        return DFS(len(nums) - 1)