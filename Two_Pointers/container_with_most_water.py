class Solution:


    def maxArea(self, height: List[int]) -> int:
        max_count = 0
        left = 0
        right = len(height) - 1

        def calc_height(left, right):
            return min(height[left], height[right]) * (right - left)

        while left < right:
            curr_count = calc_height(left, right)
            if curr_count > max_count:
                max_count = curr_count

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_count 