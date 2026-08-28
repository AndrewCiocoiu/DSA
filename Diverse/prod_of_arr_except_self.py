class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suf = []

        pref.append(1)

        curr = 1
        for val in nums:
            curr *= val
            pref.append(curr)
        pref.pop()

        curr = 1
        for val in nums[::-1]:
            curr *= val
            suf.append(curr)
        suf.pop()
        suf = suf[::-1]
        suf.append(1)

        print(pref)
        print(suf)

        res = [suf[i] * pref[i] for i in range(len(nums))]

        return res
