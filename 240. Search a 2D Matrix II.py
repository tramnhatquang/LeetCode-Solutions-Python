class Solution:
    def searchMatrix_optimal(self, matrix: List[List[int]], target: int) -> bool:
        """
        The brute force sol: Search each cell in the 2D arr and see if it's the target we're looking for. TC: O(m*n), m: number of rows, n: number of cols, SC: O(1)
        Another approach is to start from a bottom left element.
            - When target > element: move to the next element to the right in the same row (sorted) if possible (check 0 <= row_index < ROWS)
            - When target < element: move to the top element along the column (since the col is sorted) if possible (check 0 <= col_index < COLS)
            - When target == element: Return True
            When we break out the loop, return False
        """

        ROWS, COLS = len(matrix), len(matrix[0])
        # start at the bottom left element
        row_index, col_index = ROWS - 1, 0
        while 0 <= row_index < ROWS and 0 <= col_index < COLS:
            curr_value = matrix[row_index][col_index]
            if curr_value < target:# move to the right element in the same row
                col_index += 1
            elif curr_value > target:  # move to the top element in the same column
                row_index -= 1
            else:
                return True
        return False

        # time: O(n + m), m is number of rows, n is number of columns
        # space: O(1)