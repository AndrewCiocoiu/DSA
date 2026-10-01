class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree_count = [0] * numCourses

        for f, t in prerequisites:
            adj_list[f].append(t)
            indegree_count[t] += 1
        
        def BFS():
            q = deque([x for x in range(numCourses) if indegree_count[x] == 0])
            visited_count = 0

            while q:
                curr = q.popleft()
                visited_count += 1

                for n in adj_list[curr]:
                    indegree_count[n] -= 1
                    if indegree_count[n] == 0:
                        q.append(n)
        
            return visited_count == numCourses
        
        return BFS()