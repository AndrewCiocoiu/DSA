class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeightLeft = [0] * len(height)
        maxHeightRight = [0] * len(height)

        total = 0

        for i in range(1, len(height)):
            maxHeightLeft[i] = max(maxHeightLeft[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1):
            maxHeightRight[i] = max(maxHeightRight[i + 1], height[i + 1])


        for i, h in enumerate(height):
            rain_water = min(maxHeightLeft[i], maxHeightRight[i]) - h
            if rain_water > 0:
                total += rain_water

        return total