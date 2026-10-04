from functools import cache
import bisect

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        
        @cache
        def DFS(i):
            if i >= len(days):
                return 0

            one = costs[0] + DFS(i + 1)
            seven = costs[1] + DFS(bisect.bisect_right(days, days[i] + 6))
            thirty = costs[2] + DFS(bisect.bisect_right(days, days[i] + 29))
            return min(one, seven, thirty)
        
        return DFS(0)
                