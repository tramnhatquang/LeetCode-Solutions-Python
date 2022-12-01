from typing import List


def duplicateZeros_1(arr: List[int]) -> List[int]:
	res = []
	for num in arr:
		if num == 0:
			res.append(0)
			res.append(0)
		else:
			res.append(num)
	# return res[:len(arr)]
	return res[:len(arr)]


# time: O(n), space: O(n)

def duplicateZeros_2(arr: List[int]) -> None:
	"""
	Do not return anything, modify arr in-place instead.
	"""


if __name__ == '__main__':
	arr = [1, 0, 2, 3, 0, 4, 5, 0]
	new_arr = duplicateZeros_1(arr)
	print(new_arr)
