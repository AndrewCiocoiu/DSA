from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        prefix_counts = defaultdict(int)
        total = 0

        for current_sum in prefix_sum:
            target_sum = current_sum - k

            if target_sum in prefix_counts:
                total += prefix_counts[target_sum]
            
            prefix_counts[current_sum] += 1

        return total
