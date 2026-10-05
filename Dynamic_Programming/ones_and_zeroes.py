from functools import cache

class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        costs = [(s.count('0'), s.count('1')) for s in strs]

        @cache
        def DFS(i, zeros_left, ones_left):
            if i == len(strs) or (zeros_left == 0 and ones_left == 0):
                return 0
            
            ans = DFS(i + 1, zeros_left, ones_left)

            z_cost, o_cost = costs[i][0], costs[i][1]

            if z_cost <= zeros_left and o_cost <= ones_left:
                ans = max(ans, 1 + DFS(i + 1, zeros_left - z_cost, ones_left - o_cost))
            
            return ans

        return DFS(0, m, n)