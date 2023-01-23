from typing import List

"""
Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.
"""


def find_first_occurrence(arr: List[int], target: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	left, right = 0, len(arr) - 1
	boundary_index = -1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			boundary_index = mid  # it can possibly be the first occurrence
			right = mid - 1
		elif arr[mid] > target:
			right = mid - 1
		else:
			left = mid + 1

	return boundary_index


# time: O(log n)
# space: O(1)

if __name__ == '__main__':
	assert find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3) == 1
	assert find_first_occurrence([1, 1, 1, 1, 1, 1, 1], 1) == 0
	assert find_first_occurrence([4, 6, 7, 7, 7, 20], 8) == -1
	assert find_first_occurrence([4], 4) == 0
	assert find_first_occurrence([2, 3, 5, 7, 11], 2) == 0
