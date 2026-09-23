from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        let_count = Counter(s)

        for i,c in enumerate(s):
            if let_count[c] == 1:
                return i
        
        return -1