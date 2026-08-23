from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = defaultdict(int)
        for num in nums:
            elems[num] += 1

        max_val = -1
        max_key = -1
        
        for key, val in elems.items():
            if val > max_val:
                max_val = val
                max_key = key

        return max_key
        