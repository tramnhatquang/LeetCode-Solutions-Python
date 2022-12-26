from typing import *


def window(arr: List[int]) -> tuple | None:
	sorted_arr = sorted(arr)
	if sorted_arr == arr:
		return None

	left = right = None
	for i in range(len(arr)):
		if sorted_arr[i] != arr[i] and left is None:
			left = i
		elif arr[i] != sorted_arr[i]:
			right = i

	return left, right

	# time: O(n log n)
	# space: O(n)

def optimal_window(arr: List[int]) -> tuple:
	curr_max, curr_min = float('-inf'), float('inf')
	left, right = None, None

	# find the right bound
	for i in range(len(arr)):
		curr_max = max(curr_max, arr[i])
		if arr[i] < curr_max:
			right = i

	# find the left bound
	for i in range(len(arr)):
		curr_min = min(curr_min, arr[i])
		if arr[i] > curr_min:
			left = i

	return left, right



if __name__ == '__main__':
	assert window([1, 2, 3, 4]) is None
	assert window([3, 7, 5, 6, 9]) == (1, 3)
	assert window([3, -1, 2, 0]) == (0, 3)
	assert window([3, 7, 6, 10]) == (1, 2)

	# assert optimal_window([1, 2, 3, 4]) is None
	assert optimal_window([3, 7, 5, 6, 9]) == (1, 3)
	assert optimal_window([3, -1, 2, 0]) == (0, 3)
	assert optimal_window([3, 7, 6, 10]) == (1, 2)