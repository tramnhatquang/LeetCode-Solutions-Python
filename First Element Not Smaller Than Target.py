from typing import List

"""
Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.
"""


def first_not_smaller(arr: List[int], target: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	left, right = 0, len(arr) - 1
	boundary_index = -1
	while left <= right:
		mid = (left + right) // 2
		if target <= arr[mid]:
			right = mid - 1
			boundary_index = mid
		else:
			left = mid + 1
	return boundary_index


# time: O(log n)
# space: O(1)

if __name__ == '__main__':
	arr = [1, 3, 3, 5, 8, 8, 10]
	target = 2
	assert first_not_smaller(arr, target) == 1
	assert first_not_smaller([2, 3, 5, 7, 11, 13, 17, 19], 6) == 3
