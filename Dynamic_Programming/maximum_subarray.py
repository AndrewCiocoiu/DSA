class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = float("-inf")
        max_sum = float("-inf")
        for num in nums:
            prev_sum = max(prev_sum + num, num)
            max_sum = max(prev_sum, max_sum)
        
        return max_sum