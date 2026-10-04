from functools import cache

class Solution:
    def canPartition(self, nums: list[int]) -> bool:

        total = sum(nums)
        
        if total % 2 != 0:
            return False

        @cache
        def DFS(sum_left, sum_right, i):
            if i == len(nums) and sum_left == sum_right:
                return True
            if i == len(nums) and sum_left != sum_right:
                return False
            
            return DFS(sum_left + nums[i], sum_right, i + 1) or DFS(sum_left, sum_right + nums[i], i + 1)

        return DFS(0, 0, 0)