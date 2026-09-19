from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        visited = set()
        visiting = set()
        order = []

        g = defaultdict(list)

        for c, p in prerequisites:
            g[p].append(c)
        

        def has_cycle(node):
            if node in visited:
                return False
            if node in visiting:
                return True
            
            visiting.add(node)

            for n in g[node]:
                if has_cycle(n):
                    return True
            
            visited.add(node)
            visiting.remove(node)
            order.append(node)

            return False

        for i in range(numCourses):
            if has_cycle(i):
                return []
        
        return order[::-1]
        