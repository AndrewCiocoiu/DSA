class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        h = []

        nums = set(nums)

        for num in nums:
            heapq.heappush(h, -num)

        if len(nums) < 3:
            return max(nums)
        
        heapq.heappop(h)
        heapq.heappop(h)

        return -h[0]