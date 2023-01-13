from typing import List


def solution_optimal(arr: List[int]) -> tuple | None:
	left, right = None, None
	n = len(arr)
	max_seen, min_seen = float('-inf'), float('inf')

	for i in range(n):
		max_seen = max(max_seen, arr[i])
		if arr[i] < max_seen:
			right = i

	for i in range(n - 1, -1, -1):
		min_seen = min(min_seen, arr[i])
		if arr[i] > min_seen:
			left = i

	return left, right


# time: O(n), space: O(1)


def solution_brute_force(arr: List[int]) -> tuple | None:
	# observation: the largest window to be sorted =goes from 0 to len(arr) - 1
	# 1. create a new arr and sort the new arr
	# 2. traverse thr the new arr and compare the difference between two arr
	# 3. The first difference is the left bound of the smallest window, the last difference is the right bound of the
	# smallest window
	sorted_arr = sorted(arr)

	left, right = None, None
	for i in range(len(arr)):
		if arr[i] != sorted_arr[i] and left is None:
			left = i
		elif arr[i] != sorted_arr[i]:
			right = i

	# print(left, right)
	return left, right


# time: O(n log n), space: O(n)


if __name__ == '__main__':
	# assert solution_brute_force([1, 2, 3, 4]) == (None, None)
	# assert solution_brute_force([1]) == (None, None)
	# assert solution_brute_force([3, 7, 5, 6, 9]) == (1, 3)
	# assert solution_brute_force([9, 8, 7, 6, 5]) == (0, 4)

	assert solution_optimal([1, 2, 3, 4]) == (None, None)
	assert solution_optimal([1]) == (None, None)
	assert solution_optimal([3, 7, 5, 6, 9]) == (1, 3)
	assert solution_optimal([9, 8, 7, 6, 5]) == (0, 4)
