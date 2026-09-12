class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_window_size = 0

        curr_zero_count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                curr_zero_count += 1
            while curr_zero_count > 1 and left < right:
                if nums[left] == 0:
                    curr_zero_count -= 1
                left += 1
            max_window_size = max(max_window_size, right - left)

        return max_window_size