class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        path = []

        candidates.sort()

        def backtrack(start, remain):
            if remain == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break

                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])

                path.pop()

        backtrack(0, target)

        return res