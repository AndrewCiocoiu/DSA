class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        left = 0
        right = 0

        min_dif = float("inf")

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_dif = min(right - left + 1, min_dif)
                current_sum -= nums[left]
                left += 1
                
            
        
        return min_dif if min_dif != float('inf') else 0
                
