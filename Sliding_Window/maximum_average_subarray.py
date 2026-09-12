class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:   
        prev_sum = sum(nums[:k])
        max_sum = prev_sum / k

        left = 0
        right = k
        while right != len(nums):
            current_sum = (prev_sum - nums[left] + nums[right])
            max_sum = max(current_sum / k, max_sum)
            left += 1
            right += 1
            prev_sum = current_sum

        return max_sum