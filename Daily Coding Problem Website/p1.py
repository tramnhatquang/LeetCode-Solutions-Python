from typing import *

"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def find_two_numbers(arr: List[int], k: int) -> bool:
	# check if the array has two numbers adding up to k. Return true if it has, otherwise return false
	assert arr  # arr is not empty or None

	num_set = set()
	for num in arr:
		complement = k - num
		if complement in num_set:
			return True
		# store the curr number into the set and move on to the next number
		num_set.add(num)
	return False

# time: O(n), n is length of arr
# space: O(n)
