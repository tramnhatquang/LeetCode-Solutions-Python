from typing import List


def find_boundary(arr: List[bool]) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	if not arr:
		return -1
	left, right = 0, len(arr) - 1
	res = -1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid]:
			res = mid  # it could be the first True value
			right = mid - 1
		else:
			left = mid + 1
	return res


# time: O(log n)
# space: O(1)
if __name__ == '__main__':
	assert find_boundary([False, False, True, True, True]) == 2
