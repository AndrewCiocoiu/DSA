from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        if set(count1.keys()) != set(count2.keys()):
            return False

        return Counter(count1.values()) == Counter(count2.values())