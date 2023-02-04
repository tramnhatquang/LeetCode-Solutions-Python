from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # intersection of two intervals are defined as [max(s1, s2), min(e1, e2)]
        # where s1, s2 are start times of two lists respectively, e1, e2 are end times of two lists respectively
        # 1. Initialize two pointers, each pointer points at the first interval of each lists
        # 2. We append the intersection of two intervals if they intersect and append the intersected part into the res arr.
        # 3. We only move the pointer pointing at the interval whose end time is smaller than the other one since we know a longer end time can possible lead to an intersection

        # 4. Repeat step 1, 2, 3 until one of intervals is empty

        if not firstList or not secondList:  # sanity check
            return []

        p1 = p2 = 0
        res = []
        while p1 < len(firstList) and p2 < len(secondList):
            # find the intersection interval and append it to the res arr
            intersected_start = max(firstList[p1][0], secondList[p2][0])
            intersected_end = min(firstList[p1][1], secondList[p2][1])

            if intersected_start <= intersected_end:
                res.append([intersected_start, intersected_end])
            # move conditionally by cheking the end times
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return res

        # time: O(m + n) = space,
        # m, n are lengths of a, b respectively
