class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        suf_sum = [0] * len(nums)
        pref_sum = [0] * len(nums)

        for i in range(1, len(nums)):
            pref_sum[i] = pref_sum[i - 1] + nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suf_sum[i] = suf_sum[i + 1] + nums[i + 1]
        
        for i in range(len(nums)):
            if suf_sum[i] == pref_sum[i]:
                return i

        return -1