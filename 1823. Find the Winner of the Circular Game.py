class Solution:
	def findTheWinner(self, n: int, k: int) -> int:
		# APPROACH 1: simulate the process
		# 1. Store all the elemnts in the arr, start_index = 0
		# 2. Follow these procedures below until the arr only has one element left
		#   - find the new_index = (start_index + k - 1) % curr_length of the arr
		#   - del arr[new_index]
		#   - assign the index = new_index

		arr = [num for num in range(1, n + 1)]  # O(n)
		start_index = 0
		while len(arr) != 1:
			new_index = (start_index + k - 1) % len(arr)
			del arr[new_index]
			start_index = new_index

		return arr[0]

	# del takes O(n), n is the length of the arr
	# time: O(n^2), space: O(n) to store the arr
