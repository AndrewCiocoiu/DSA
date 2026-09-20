from collections import defaultdict
import heapq


class Solution:

    def findCheapestPrice(
        self, n: int, flights: list[list[int]], src: int, dst: int, k: int
    ) -> int:
        g = defaultdict(list)
        for u, v, w in flights:
            g[u].append((v, w))

        stops = [float("inf")] * n

        min_heap = [(0, src, 0)]

        while min_heap:
            cost, u, edges = heapq.heappop(min_heap)

            if u == dst:
                return cost

            if edges >= stops[u]:
                continue
            stops[u] = edges

            if edges <= k:
                for v, w in g[u]:
                    heapq.heappush(min_heap, (cost + w, v, edges + 1))

        return -1