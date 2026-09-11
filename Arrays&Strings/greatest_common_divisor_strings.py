class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            bigger = str1
            smaller = str2
        else:
            bigger = str2
            smaller = str1
        
        for i in range(len(smaller), 0, -1):
            if len(bigger) % i == 0 and len(smaller) % i == 0:
                construct = ""
                for _ in range(len(smaller) // i):
                    construct += smaller[:i]
                if construct != smaller:
                    continue
                construct = ""
                for _ in range(len(bigger) // i):
                    construct += smaller[:i]
                if construct != bigger:
                    continue
                return smaller[:i]
        
        return ""
                
