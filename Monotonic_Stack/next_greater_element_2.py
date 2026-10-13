class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        st = []
        res = len(nums) * [-1]

        for i in range(len(nums) * 2):
            el = nums[i % len(nums)]
            while st and st[-1][1] < el:
                processed_id, pricessed_val = st.pop()
                res[processed_id % len(nums)] = el
            
            st.append((i, el))
        
        return res