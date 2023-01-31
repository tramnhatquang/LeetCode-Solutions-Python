from typing import *


def find_sum_pairs(arr: List[int], target: int) -> List[List[int]]:
	# assume the given list contains all unique numbers
	# Numbers can be positive or negative
	num_set = set()
	res = []
	for num in arr:
		if target - num in num_set:
			res.append([target - num, num])
		else:
			num_set.add(num)
	print(f'Res is {res}')
	return res


if __name__ == '__main__':
	# find_sum_pairs([1, 3, 2, 5, 46, 6, 7, 4], 5)
	print(len(""))
	print(len(" "))
	res = [""]
	print('Res: ', ''.join(res))
