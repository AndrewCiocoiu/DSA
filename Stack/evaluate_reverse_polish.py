class Solution:

  def evalRPN(self, tokens: List[str]) -> int:
    st = []

    for tok in tokens:
      if tok in {"+", "-", "*", "/"}:
        b = st.pop()
        a = st.pop()

        if tok == "+":
          st.append(a + b)
        elif tok == "-":
          st.append(a - b)
        elif tok == "*":
          st.append(a * b)
        else:

          st.append(int(a / b))
      else:
        st.append(int(tok))

    return st[0]