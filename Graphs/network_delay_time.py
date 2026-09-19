class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        g = defaultdict(list)

        for s, t, w in times:
            g[s].append((t, w))
        
        def djikstra(node):
            distances = {x: float("inf") for x in range(1, n + 1)}
            distances[node] = 0

            min_heap = [(0, node)]
        
            while min_heap:
                curr_distance, u = heapq.heappop(min_heap)

                if curr_distance > distances[u]:
                    continue

                for v, w in g[u]:
                    new_distance = w + curr_distance

                    if new_distance < distances[v]:
                        distances[v] = new_distance
                        heapq.heappush(min_heap, (new_distance, v))

            return distances

        distance = djikstra(k)

        print(distance)

        return -1 if float("inf") in distance.values() else max(distance.values())