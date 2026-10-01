import itertools

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(nums) + 1):
            res.extend(itertools.combinations(nums, i))
        
        return res