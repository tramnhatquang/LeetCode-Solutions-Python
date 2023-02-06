from typing import *


class Solution:

    def rotate_approach_2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right

                # save the top left
                topLeft = matrix[top][left + i]

                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left into the top right
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1
        # time: O(n^2), n is the number of rows in the matrix

        
    def rotate_approach_1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.swap_diagonal(matrix)
        self.reflect(matrix)
        # time: O(N^2), N is the number of rows in the matrix
        # since number of rows in the matrix is equal to the number of columns in the matrix

        # spacE: O(1)

    def swap_diagonal(self, arr: List[int]) -> None:
        """
        Swapping across the swap_diagonal
        """
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                # swap_diagonal
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        print(f'Arr: {arr}')

    def reflect(self, arr: List[int]) -> None:
        """
        Reflecting on each row
        """
        n = len(arr)
        for i in range(n):
            for j in range(n // 2):
                arr[i][j], arr[i][-j-1] = arr[i][-j-1], arr[i][j]
        print(f'Arr: {arr}')
