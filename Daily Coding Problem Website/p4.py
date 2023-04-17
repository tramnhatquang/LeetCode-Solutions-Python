from typing import List

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
- Note that: 0 is neither a negative nor positive number

"""


def find_first_missing_positive_number_2(arr: List[int]) -> int:
	"""
	- The trick is that the first missing positive number must be between 1 and len(arr) + 1 since we can ignore any negative numbers, 0 and any numbers that are bigger than len(array). The basic idea is to use a cyclic sort (putting positive numbers at its correct index, i.e. 1 goes to 0-indexed, 2 goes to 1-index)
	:rtype: int
	"""
	if not arr:
		return 1
	"""
	[3, 1, 1, 2] -> [1, 1, 3, 2]
	0 1 2 3
	
	
	"""

	for i, num in enumerate(arr):

		while i + 1 != num and 1 <= arr[i] <= len(arr):
			# the first condition checks if the number is indeed at the wrong position right now
			# the second condition checks if there is a position at which the specific number can be stored
			correct_index = arr[i] - 1
			arr[i], arr[correct_index] = arr[correct_index], arr[i]
			if arr[i] == arr[correct_index]:
				break

	# iterating through each number and check if the number is placed at its correct index.
	# enumerate(arr, 1) starts the index from 1 instead of 0
	# enumerate(arr) starts the index from 0
	for i, num in enumerate(arr, 1):
		if num != i:
			return i
	return len(arr) + 1


def find_first_missing_positive_number_1(arr: List[int]) -> int:
	"""
	- Add all numbers into a set
	- Use a counter starting from 1then continuously increment the counter and check whether the value is in the set

	"""
	arr_set = set(arr)
	counter = 1
	while counter in arr_set:
		counter += 1
	return counter
	"""
	- time: O(n), n is length of arr
	- space: O(n)
	"""
