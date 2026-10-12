class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []

        def backtrack(i):
            if i == len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

            backtrack(i + 1)
        
        backtrack(0)

        return res
