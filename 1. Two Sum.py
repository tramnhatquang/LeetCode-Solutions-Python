from typing import *


class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		# approach 1: One pass hash table - While we are iterating and
		# inserting elements into the hash table, we also look back to check
		# if current element's complement already exists in the hash table. If
		# it exists, we have found a solution and return the indices
		# immediately. time: O(n), space: O(n), n is the length of nums

		# stores key-val paris
		# key is the number, val is the index of that number
		hash_table = {}

		for index, num in enumerate(nums):
			complement = target - num
			if complement in hash_table:
				return [index, hash_table[complement]]
			hash_table[num] = index
		return []  # if not found
