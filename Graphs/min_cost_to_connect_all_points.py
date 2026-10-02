from collections import defaultdict
import heapq

class Solution:
    def man_distance(self, point_a, point_b):
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        adjList = defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                distance = self.man_distance(points[i], points[j])

                adjList[i].append((distance, j))
                adjList[j].append((distance, i))
        
        total_cost = 0
        visited = {0}

        available_edges = adjList[0].copy()
        heapq.heapify(available_edges)

        while len(visited) != len(points):
            distance, point = heapq.heappop(available_edges)

            if point in visited:
                continue

            total_cost += distance
            visited.add(point)

            for distance, neighbor in adjList[point]:
                if neighbor not in visited:
                    heapq.heappush(available_edges, (distance, neighbor))
        
        return total_cost