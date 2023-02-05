class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
        - After sorting, start1 < start2, it's sufficient to compare the end boundaries
            + If end1 < end2: the intervals won't completely cover one another, though they have some overlapping.
            + If end1 >= end2: the interval 2 is covered by the interval 1
        - Edge case: What if two intervals share the start point? start1 = start2
        - If two intervals share the same start point, one has to put the longer interval in front

        Algorithnm:
            1. Sort in the ascending order by the start point. If two intervals share the same start point, put the longer one to be the first.
            2. Initiate the number of non-covered intervals: count = 0
            3. Iterate over sorted intervals and compare end points.
                - If the current interval is not covered by the previous one (end > prev_end), increase the number of non-covered intervals. Assign the current interval to be previous for the next step.
                - Otherwise, the current interval is covered by the previous one. Do nothing.
            4. Return count
        """
        intervals.sort(key=lambda x: [x[0], -x[1]])
        count = 0

        prev_end = 0
        for start, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prev_end:
                count += 1
                prev_end = end

        return count
