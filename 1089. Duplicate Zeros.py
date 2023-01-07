from typing import List


def duplicateZeros_1(arr: List[int]) -> None:
	res = []
	length = len(arr)
	for num in arr:
		if num == 0:
			res.append(0)
			res.append(0)
		else:
			res.append(num)
	# return res[:len(arr)]
	arr[:] = res[:length]


# time: O(n), space: O(n)

def duplicateZeros_2(arr: List[int]) -> None:
	"""
	Do not return anything, modify arr in-place instead.
	"""
	num_zeroes = arr.count(0)
	length = len(arr)
	# traverse arr backward
	for i in reversed(range(len(arr))):

		# check if the current number's new index is within the original length
		if i + num_zeroes < length:
			arr[i + num_zeroes] = arr[i]

		# otherwise, we ignore and continue to check if it's a zero
		if arr[i] == 0:
			num_zeroes -= 1
			if i + num_zeroes < length:
				arr[i + num_zeroes] = 0


if __name__ == '__main__':
	arr = [1, 0, 2, 3, 0, 4, 5, 0]
	new_arr = duplicateZeros_1(arr)
	print(new_arr)
