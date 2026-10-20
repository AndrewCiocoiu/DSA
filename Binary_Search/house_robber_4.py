from functools import cache

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def can_rob(val):
            robbed = 0
            i = 0

            while i < len(nums):
                if nums[i] <= val:
                    robbed += 1
                    i += 2
                else:
                    i += 1
            
            if robbed >= k:
                return True
            else:
                return False

        left = min(nums)
        right = max(nums)

        while left < right:
            mid = (left + right) //  2

            if can_rob(mid):
                right = mid
            else:
                left = mid + 1
            
        return left