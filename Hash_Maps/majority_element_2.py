class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        c = Counter(nums)

        res = []

        for k, v in c.items():
            if v > math.floor(len(nums) / 3):
                res.append(k)
            
        return res