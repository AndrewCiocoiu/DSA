class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        
        for i, val in enumerate(citations):
            if val >= n - i:
                return n - i
        
        return 0