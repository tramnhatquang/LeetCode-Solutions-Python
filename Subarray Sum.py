"""
Given an array of integers and an integer target, find a subarray that sums to target and return the start and end indices of the subarray.

Input: arr: 1 -20 -3 30 5 4 target: 7

Output: 1 4

Explanation: -20 - 3 + 30 = 7. The indices for subarray [-20,-3,30] is 1 and 4 (right exclusive).
"""

from typing import List

"""
The sum of elements from index 0 to i is called the prefix sum (prefix = from the beginning, prefix sum = sum from the beginning, i.e. index 0). If we have the prefix sum for each index, we can find the sum of any subarray in constant time.

With the knowledge of the prefix sum under our belt, the problem boils down to Two Sum Sorted. We keep a dictionary of prefix_sum: index while going through the array calculating prefix_sum. If at any point, prefix_sum - target is in the dictionary, we have found our subarray.

Time Complexity: O(n)

Space Complexity: O(n)
"""


def subarray_sum_optimal(arr: List[int], target: int) -> List[int]:
	# WRITE YOUR BRILLIANT CODE HERE
	# notice that sum of a subarray [i, j] is equal to sum of [0, j] minus the sum of [0, i - 1]
	# used a hash map to store the prefix sum so far
	prefix = {0: 0}  # where key is the prefix sum up to the value index
	curr_sum = 0
	for right in range(len(arr)):
		curr_sum += arr[right]
		if curr_sum - target in prefix:
			return [prefix[curr_sum - target], right + 1]
		# else, store it into the prefix
		prefix[curr_sum] = right + 1


def subarray_sum_brute_force(arr: List[int], target: int) -> List[int]:
	# WRITE YOUR BRILLIANT CODE HERE
	if sum(arr) == target:
		return [0, len(arr)]

	for i in range(len(arr)):
		for j in range(i, len(arr)):
			if sum(arr[i:j]) == target:
				return [i, j]
	return [-1, -1]
