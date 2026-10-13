class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        monotonic_stack = []
        next_greater = {}

        for i in range(len(nums2) - 1, -1, -1):
            while monotonic_stack and monotonic_stack[-1] < nums2[i]:
                monotonic_stack.pop()
            
            if monotonic_stack:
                next_greater[nums2[i]] = monotonic_stack[-1]
            else:
                next_greater[nums2[i]] = -1

            monotonic_stack.append(nums2[i])
        
        res = []

        for num in nums1:
            res.append(next_greater[num])
        
        return res

