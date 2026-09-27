class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = len(s1)

        for i in range(len(s2) - l + 1):
            perm = s2[i:l+i]
            if Counter(s1) == Counter(perm):
                return True
        
        return False