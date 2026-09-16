class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        res = []
        count = 0

        for interval in intervals:
            if not res or interval[0] >= res[-1][1]:
                res.append(interval) 
            else:
                res[-1][1] = min(res[-1][1], interval[1])
                count += 1
        print(res)
        return count