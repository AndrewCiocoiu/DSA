class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures) - 1, -1, -1):
            curr = temperatures[i]
            while st and st[-1][0] <= curr:
                st.pop()
            if st:
                temps[i] = st[-1][1] - i 
            st.append((curr, i))
            
        return temps