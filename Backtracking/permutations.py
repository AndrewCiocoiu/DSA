class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        visited = set()
        path = []
        res = []
        
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                
                path.append(nums[i])
                visited.add(i)

                backtrack()

                path.pop()
                visited.remove(i)
        
        backtrack()

        return res