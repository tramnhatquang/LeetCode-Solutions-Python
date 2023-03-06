from typing import *

"""
https://leetcode.com/discuss/interview-question/3216097/CIsco-OA-SHL-Questions
"""


def find_largest_diff(arr: List[int]) -> int:
	"""
	- Given a list of integers, find the max difference of two elements where the larger number appears after the smaller number. Write an algorithm to find the max difference of two elements where the larger number appears after the smaller number
	- Input: given an arr of int
	- Output: Print an integer representing the max diff of the two elements where the larger number appears after the smaller number. If no such elements are found, print 0
	"""

	# this question is similar to Buy and Sell Stock 1 in LeetCode
	"""
	time: O(n), n is length of arr
	space: O(1)
	"""
	min_diff = 0
	lowest_num = arr[0]
	for num in arr:
		if num < lowest_num:  # keep track of the min number we have seen so far
			lowest_num = num
		elif num - lowest_num > min_diff:
			min_diff = num - lowest_num

	return min_diff


assert find_largest_diff([2, 3, 10, 6, 4, 8, 1]) == 8
assert find_largest_diff([4, 3, 1]) == 0
assert find_largest_diff([5, 3, 1, 7, 4, 15, 25]) == 24
