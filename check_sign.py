from typing import *


def check_sign(arr: List[int]) -> int:
	sign = 1
	for num in arr:
		if num == 0:
			return 0  # no need to check further
		elif num < 0:
			sign = -sign

	return sign


# time: O(n), space: O(1)

if __name__ == '__main__':
	assert check_sign([1, 2, 3, 4]) == 1
	assert check_sign([-2, -5, -3, -1, -7]) == -1
	assert check_sign([1, 0, 7, 5, 1]) == 0
	assert check_sign([0]) == 0
	assert check_sign([1, -2, -3, 5]) == 1
	assert check_sign([1, 2, 3, -5]) == -1

