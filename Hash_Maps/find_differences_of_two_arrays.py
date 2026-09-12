
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        count1 = set(nums1)
        count2 = set(nums2)

        res1 = []
        res2 = []

        for item in count1:
            if item not in count2:
                res1.append(item)

        for item in count2:
            if item not in count1:
                res2.append(item)
        
        return [res1, res2]