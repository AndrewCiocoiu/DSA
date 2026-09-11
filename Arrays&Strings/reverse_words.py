class Solution:
    def reverseWords(self, s: str) -> str:
        new_arr = []
        for w in s.strip().split():
            new_arr.append(w)
        return " ".join(new_arr[::-1])