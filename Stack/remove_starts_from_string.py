class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for l in s:
            if l == "*":
                st.pop()
            else:
                st.append(l)
        
        return "".join(st)