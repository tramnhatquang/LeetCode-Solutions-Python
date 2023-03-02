from typing import List


def game(p: List[int]) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	"""
	The question is about finding the first index where the left sum of index i is greater than
	the right sum of
	"""
	# count the total points in the list
	total_score = 0
	for num in p:
		total_score += 1 if num == 1 else -1

	your_score = 0
	for i, val in enumerate(p):
		if your_score > total_score:
			return i
		your_score += 1 if val == 1 else -1
		total_score -= 1 if val == 1 else -1

	return -1


# time: O(2n) = O(n), n is length of arr
# space: O(1)


if __name__ == '__main__':
	p = [int(x) for x in input().split()]
	res = game(p)
	print(res)
