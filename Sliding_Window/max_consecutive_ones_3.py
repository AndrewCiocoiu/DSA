class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr_changes = 0
        left = 0
        max_window_size = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                    curr_changes += 1
            while curr_changes > k:
                    if nums[left] == 0:
                        curr_changes -= 1
                    left += 1
            max_window_size = max(max_window_size, right - left + 1)
        
        return max_window_size

        