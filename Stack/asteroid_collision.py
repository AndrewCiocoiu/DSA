class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            destructed = False
            negative = False
            if ast < 0:
                while len(st) != 0:
                    if st[-1] < 0:
                        negative = True
                        break
                    if abs(ast) > abs(st[-1]):
                        st.pop()
                    elif abs(ast) < abs(st[-1]):
                        break
                    elif abs(ast) == abs(st[-1]):
                        st.pop()
                        destructed = True
                        break
                if (len(st) == 0 and not destructed) or negative:
                    st.append(ast)
            else:
                st.append(ast)
        
        return st
        