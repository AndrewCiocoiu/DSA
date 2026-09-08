class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""
        min_str = min(strs, key=len)

        for i, val in enumerate(min_str):
            for s in strs:
                if(s[i] != min_str[i]):
                    return min_str[:i]
        
        return min_str
