class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * (len(nums))
        dp[len(nums) - 1] = True

        for i in range(len(nums) - 1, -1, -1):
            for j in range(1, nums[i] + 1, 1):
                if i + j > len(nums) - 1:
                    continue
                if dp[i + j] == True:
                    dp[i] = True
                    break

        return dp[0] 

        