from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        g = defaultdict(list)
        visiting = set()
        visited = set()

        for s, t in prerequisites:
            g[s].append(t)

        def has_cycle(node):
            if node in visiting:
                return True
            if node in visited:
                return False
            
            visiting.add(node)

            for n in g[node]:
                if has_cycle(n):
                    return True
            
            visiting.remove(node)
            visited.add(node)
            return False
        
        for n in range(numCourses):
            if has_cycle(n):
                return False
        
        return True
        




