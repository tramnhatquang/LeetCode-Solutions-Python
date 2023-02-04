"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        res = []
        # merging all intervals into the result arr
        for interval in schedule:
            intervals.extend(interval)

        # sort all the intervals based on start time
        intervals.sort(key=lambda x: x.start)

        # traverse thr the interval and find the common free time
        prev_end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start > prev_end:
                res.append(Interval(prev_end, interval.start))
            # update the prev end
            prev_end = max(prev_end, interval.end)
        return res

        # time: O(n log n), n is the number of intervals in the arr
        # space: O(n)
