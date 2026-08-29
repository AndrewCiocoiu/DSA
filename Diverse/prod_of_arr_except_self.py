class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = len(nums) * [1]
        suf = len(nums) * [1]


        for i in range(1, len(nums)):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        

        res = [suf[i] * pref[i] for i in range(len(nums))]

        return res
