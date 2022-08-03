from collections import Counter
from typing import *


class Solution:
	def numberOfPairs(self, nums: List[int]) -> List[int]:
		# approach 1: Hash table
		#   1. Keep track of the frequency of each number and store them in the hash table
		#   2. The frequency of an integer is odd which means it is a leftover number. Loop over key, value in the hash table. Number of operations for each number is equal to the (frequency // 2) so we need to add it the num_operations. Also, if the freq is even, that number is not a leftover number. If the freq is odd, that number is a leftover number and we increment the num_left by 1

		counter = Counter(nums)
		leftover = operations = 0
		for k, v in counter.items():
			if v % 2 == 1:
				leftover += 1
			operations += v // 2
		return [operations, leftover]

# time: O(n), space: O(n), n is the length of nums
