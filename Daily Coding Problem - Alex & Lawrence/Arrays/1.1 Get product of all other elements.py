from typing import Any


def solution(arr) -> list[Any] | list[None]:
	if not arr:
		return []
	n = len(arr)
	left_product = [1] * n
	right_product = [1] * n
	result = [None] * n

	# calculate the left product
	for i in range(1, n):
		left_product[i] = left_product[i - 1] * arr[i - 1]

	# calculate the right product
	for i in range(n - 2, -1, -1):
		right_product[i] = right_product[i + 1] * arr[i + 1]

	# calculate the result arr
	for i in range(n):
		result[i] = left_product[i] * right_product[i]

	return result


# time: O(n), space: O(n), n is the length of arr


if __name__ == '__main__':
	assert solution([1, 2, 3, 4]) == [24, 12, 8, 6]
	assert solution([1]) == [1]
	assert solution([5, 3, 2]) == [6, 10, 15]
	assert solution([]) == []
