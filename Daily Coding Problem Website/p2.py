from typing import *

"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

"""
ex: [2, 4, 5, 6] -> res = [120, 60, 48, 40] 
res = [1, 2, 8, 40]
right = 1

"""


def find_product_each_element_2(arr: List[int]) -> List[int]:
	"""
	- Instead of creating two new arrays to store left and right product of each number, we can use a constant number to hold the prev left or right product when we traverse each side
	"""

	n = len(arr)
	assert n >= 2
	left = 1  # the left most number has left product of 1. Similarly, the right most number has right product of 1
	res = [1] * n
	for i in range(n):
		res[i] = left
		left *= arr[i]  # left will always be updated to the left product

	right = 1
	for i in range(n - 1, -1, -1):
		res[i] *= right
		right *= arr[i]  # right will always be updated to the right product

	return res
	"""
	- time: O(2n) = O(n), n is length of arr
	- space : O(1), if we do not count the output
	"""


def find_product_each_element_1(arr: List[int]) -> List[int]:
	# make sure that arr's length >= 2
	n = len(arr)
	assert n >= 2
	# find the left product of each element and store in an arr called left_product
	left_prod, right_prod = [1] * n, [1] * n

	for i in range(1, n):
		left_prod[i] = left_prod[i - 1] * arr[i - 1]

	# find the right  product of each element and store in an arr called right_product
	for i in range(n - 2, -1, -1):
		right_prod[i] = right_prod[i + 1] * arr[i + 1]

	# multiply each corresponding number from both to find the total product of each element except itself
	res = []
	for i in range(n):
		res.append(left_prod[i] * right_prod[i])

	return res

	"""
	- time: O(3n) = O(n) since we traversed thr arr 3 times
	- space: O(2n) = O(n) for creating two left and right product arr
	"""
