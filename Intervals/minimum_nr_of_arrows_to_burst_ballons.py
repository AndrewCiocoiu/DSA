class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[0])

        merged = []
        for interval in points:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][0] = min(merged[-1][0], interval[0])
                merged[-1][1] = min(merged[-1][1], interval[1])
        
        return len(merged)