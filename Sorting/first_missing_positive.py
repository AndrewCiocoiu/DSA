class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        correct = [0] * (len(nums) + 1)

        for num in nums:
            if num > 0 and num <= len(nums):
                correct[num] = num
        
        for i in range(1, len(correct)):
            if correct[i] != i:
                return i
        return len(correct)
