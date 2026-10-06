from typing import (
    List,
)
from collections import defaultdict
from collections import deque

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        in_degree = {c: 0 for word in words for c in word}
        adj_list = defaultdict(set)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
        
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj_list[c1]:
                        adj_list[c1].add(c2)
                        in_degree[c2] += 1
                    break
        

        q = deque([c for c, deg in in_degree.items() if deg == 0])
        result = []

        while q:
            curr = q.popleft()
            result.append(curr)

            for n in adj_list[curr]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)

        if len(result) < len(in_degree):
            return ""
        
        return "".join(result)


