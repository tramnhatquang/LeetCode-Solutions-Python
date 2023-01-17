from typing import *


def find_max_prod(arr: List[int]) -> int:
	global_max = float('-inf')
	for i in range(len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] * arr[j] > global_max:
				global_max = arr[i] * arr[j]

	return global_max


# time: O(n^2), not efficient (where n is the length of arr)
# space: O(1)

def find_max_prod_1(arr: List[int]) -> (int, int):
	if not arr:  # sanity check
		return None

	# find the second max number, max number
	# find the second min number, min number
	# compare their products and return the bigger one

	max_num = arr[0]
	second_max = float('-inf')

	min_num = arr[0]
	second_min = float('inf')

	for num in arr:
		if num > max_num:
			second_max = max_num  # second highest
			max_num = num  # first highest
		elif num != max_num and num > second_max:
			second_max = num

		if num < min_num:
			second_min = min_num  # second lowest
			min_num = num  # first lowest
		elif num < second_min:
			second_min = num
	# return max(min_num * second_min, max_num * second_max)
	if max_num * second_max > min_num * second_min:
		return (second_max, max_num)
	return (min_num, second_min)


# time: O(n), n is the length of arr
# space: O(1)
if __name__ == '__main__':
	# run tests
	# assert find_max_prod([1, 2, 3, 4]) == 12
	# assert find_max_prod([-5, -4, 3, 4]) == 20
	# assert find_max_prod([-55, -10, -3, -1]) == 550
	# assert find_max_prod([1, 2]) == 2

	# assert find_max_prod_1([1, 2, 3, 4]) == 12
	# assert find_max_prod_1([-5, -4, 3, 4]) == 20
	# assert find_max_prod_1([-55, -10, -3, -1]) == 550
	# assert find_max_prod_1([1, 2]) == 2

	assert find_max_prod_1([11, 23, 15, 6, -2, 34]) == (23, 34)
	assert find_max_prod_1([11, 23, 15, 6, -35, -35, 34]) == (-35, -35)
