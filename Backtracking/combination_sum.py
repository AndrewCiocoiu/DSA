class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        path = []

        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break
                
                
                path.append(candidates[i])
                backtrack(i, remain - candidates[i])

                path.pop()
        
        backtrack(0, target)

        return result
            
