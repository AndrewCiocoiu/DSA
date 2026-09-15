class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        merged_intervals = []

        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals