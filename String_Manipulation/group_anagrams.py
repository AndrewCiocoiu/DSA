from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = []
        anagram_groups = defaultdict(list)

        for s in strs:
            anagram_groups["".join(sorted(s))].append(s)
        
        for val in anagram_groups.values():
            sol.append(val)

        return sol
        