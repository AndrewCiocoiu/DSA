from functools import cache

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        @cache
        def DFS(i, end):
            if i > end:
                return 0
           
            return max(DFS(i + 1, end), nums[i] + DFS(i + 2, end))
        
        return max(DFS(1, len(nums) - 1), DFS(0, len(nums) - 2))