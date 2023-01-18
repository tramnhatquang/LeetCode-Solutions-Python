import math
from typing import List


def find_largest_diff(arr) -> int:
	# find the max and min number
	# max_num = max(arr)
	# min_num = min(arr)
	# return max_num - min_num

	max_num = -math.inf
	min_num = math.inf
	for num in arr:
		if num > max_num:
			max_num = num
		elif num < min_num:
			min_num = num

	print('max num: ', max_num)
	print('min num: ', min_num)
	return max_num - min_num


def find_missing_number(arr) -> int:
	n = len(arr) + 1
	total_sum = n * (n + 1) // 2
	return total_sum - sum(arr)


def product(arr: List[int]) -> List[int]:
	n = len(arr)
	left_product = [1] * n
	right_product = [1] * n
	res = [1] * n

	# find the left product arr
	for i in range(1, n):
		left_product[i] = left_product[i - 1] * arr[i - 1]

	# find the right product arr
	for i in range(n - 2, -1, -1):
		right_product[i] = right_product[i + 1] * arr[i + 1]

	# find the result arr
	for i in range(n):
		res[i] = left_product[i] * right_product[i]

	return res


# time: O(n)
# space: O(1) if we do not count the output arr

def solution(nums, k) -> bool:
	dic = {}
	for i, j in enumerate(nums):
		if j in dic and i - dic[j] <= k:
			return True
		dic[j] = i
	return False


if __name__ == '__main__':
	assert solution([1, 2, 3, 1], 3) is True
	assert solution([1, 0, 1, 1], 1) is True
	assert solution([1, 2, 3, 1, 2, 3], 2) is False
