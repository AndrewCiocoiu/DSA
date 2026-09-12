class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            pref[i] = pref[i + 1] * nums[i + 1]
        
        for i in range(1, len(nums), 1):
            suf[i] = suf[i - 1] * nums[i - 1]

        return [suf[i] * pref[i] for i in range(len(nums))]