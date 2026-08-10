def find_str(s, wordDict):
    for w in wordDict:
        idx = s.find(w)
        if idx != -1:
            return (idx, len(w))
    return -1

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        while(find_str(s, wordDict) != -1):
            idx = find_str(s, wordDict)
            s = s[:idx[0]] + s[idx[0] + idx[1]:]
        
        if s != "":
            return False
        else:
            return True