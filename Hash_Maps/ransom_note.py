from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        rans = Counter(ransomNote)

        for key in rans.keys():
            if mag[key] < rans[key]:
                return False

        return True
        