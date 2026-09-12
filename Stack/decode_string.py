class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for l in s:
            if l == "]":
                letters = []
                while st[-1] != "[":
                    letters.append(st.pop())
                st.pop()
                times = []
                while st and st[-1].isdigit():
                    times.append(st.pop())
                times = int("".join(times[::-1]))
                uncompressed = "".join(letters[::-1]) * times
                for let in uncompressed:
                    st.append(let)
            else:
                st.append(l)
        
        return "".join(st)