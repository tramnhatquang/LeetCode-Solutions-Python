class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        """
        1. We sort the intervals based on start time
        2. Intialize prev_end = intervals[0][1]. Starting from 1 to the last interval in the arr, 
            - Check if the current interval is overlapping with the prev interval or not. Lets's say we are at the i-th index, and we want to check 
                + If intervals[i][0] >= prev_end, there is no overlap, update prev_end = intervals[i][1]
                + Else, intervals[i][0] < prev_end, there is an overlap, and we want to remove the interval that has a larger end time. The reason is that larger end time can lead to more overlaps and we want to minimize the removed intervals, so we increase the count += 1, and update prev_end = min(prev_end, intervals[i][1])
        3. Return the count
        """

        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for interval in intervals[1:]:
            # check overlapping
            if interval[0] >= prev_end: # no overlap
                prev_end = interval[1]
            else: # overlapping
                prev_end = min(prev_end, interval[1])
                count += 1
        return count
    
    # time: O(n log n) due to Timsort algorithm
    # space: O(n)