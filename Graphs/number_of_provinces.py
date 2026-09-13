class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        
        def DFS(start):
            st = [start]

            while st:
                node = st.pop()
                visited.add(node)

                for i in range(len(isConnected)):
                    if isConnected[node][i] == 1 and i not in visited:
                        st.append(i)
        
        count = 0

        for i in range(len(isConnected)):
            if i not in visited:
                DFS(i)
                count += 1

        return count
