from typing import List
class Solution:
	def partitionLabels(self, s: str) -> List[int]:
		# approach 1: Greedy Approach + hash table
		# 1. Keep track of the last index ocurrence of each character in the string
		# 2. Use two pointers.Initally, they both point to the first index of the string. One right pointer will extend the length of partition. At any steps, we check if the last index of the right character is within the end index. If it is larger than end index, we extend the partition end = tbale[right_char]. If we are at the end of the partition left == end, then we'll append a partition size to our answer and set the start of our new partiton to i + 1

		# keep track of the last index of each character in s
		last_index_map = {}
		for index, char in enumerate(s):
			last_index_map[char] = index

		res = []
		end = size = 0
		for index, char in enumerate(s):
			size += 1
			end = max(end, last_index_map[char])

			if index == end:
				res.append(size)
				size = 0

		return res

	# time: O(N), N is the length of S
	# space: O(1), since the hash map only contains at most 26 characters
