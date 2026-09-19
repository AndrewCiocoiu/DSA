from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = [x for x in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if(rank[p1] > rank[p2]):
                parent[p2] = p1
                rank[p1] += rank[p2]
            
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True

        for s, d in edges:
            if not union(s, d):
                return [s, d]