class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        end = sorted_intervals[0][1]
        remove = 0
        for a in sorted_intervals[1:]:
            if a[0] < end: remove += 1
            else: end = a[1]
        return remove