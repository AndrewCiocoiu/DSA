from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adjList = defaultdict(list)

        for edge in connections:
            adjList[edge[0]].append((edge[1], 1))
            adjList[edge[1]].append((edge[0], 0))
        
        visited = set([0])
        st = [0]

        print(adjList)

        count = 0

        while st:
            node = st.pop()
            for edge in adjList[node]:
                if edge[0] not in visited:
                    st.append(edge[0])
                    if edge[1] == 1:
                        count += 1
                    visited.add(edge[0])

        return count