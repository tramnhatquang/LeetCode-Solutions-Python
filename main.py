import math


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


if __name__ == '__main__':
	pass
