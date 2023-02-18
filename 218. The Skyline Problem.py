class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Using Divide and Conquer to solve this problem
            - Divide the list of buildings into two roughly even sublists.
            - Get the skyline from each of the sublists recursively.
            -  Merge the two skylines together.

        """

        def dc(bs):
            def merge(left, right):
                def update(x, y):
                    if not result or (result[-1][0] != x and result[-1][1] != y):
                        result.append([x, y])
                    else:
                        result[-1][1] = y

                result = []
                curx, cury = 0, 0
                i1, i2 = 0, 0
                ly, ry = 0, 0
                while i1 < len(left) and i2 < len(right):
                    x1, y1 = left[i1]
                    x2, y2 = right[i2]
                    if x1 < x2:
                        i1 += 1
                        ly = y1
                    else:
                        i2 += 1
                        ry = y2
                    curx = min(x1, x2)
                    cury = max(ly, ry)
                    update(curx, cury)

                while i1 < len(left):
                    x1, y1 = left[i1]
                    i1 += 1
                    update(x1, y1)

                while i2 < len(right):
                    x2, y2 = right[i2]
                    i2 += 1
                    update(x2, y2)
                return result

            l = len(bs)
            if l == 0:
                return []
            if l == 1:
                return [[bs[0][0], bs[0][2]], [bs[0][1], 0]]
            left_bs = dc(bs[:l//2])
            right_bs = dc(bs[l//2:])
            return merge(left_bs, right_bs)

        return dc(buildings)

        # time: O(n log n)
        # spacE: O(n)
