class Solution:
	def maxSubArray_optimal(self, nums: List[int]) -> int:
		# use Kadane's algo
		# Initialize our variables using the first element.
		current_subarray = max_subarray = nums[0]

		# Start with the 2nd element since we already used the first one.
		for num in nums[1:]:
			# If current_subarray is negative, throw it away. Otherwise, keep adding to it.
			current_subarray = max(num, current_subarray + num)
			max_subarray = max(max_subarray, current_subarray)

		return max_subarray

	# time: O(n), space: O(1)
	def maxSubArray_optimal_brute_force(self, nums: List[int]) -> int:
		# more optimal brute force solution
		# The trick is to recognize that all of the subarrays starting at a particular value will share a common prefix.
		global_max = -math.inf
		n = len(nums)
		for i in range(n):
			curr_sum = 0
			for j in range(i, n):
				curr_sum += nums[j]
				global_max = max(global_max, curr_sum)

		return global_max

	# time: O(n^2), space:O(1)

	def maxSubArray_brute_force(self, nums: List[int]) -> int:
		curr_max = -math.inf
		n = len(nums)
		for i in range(n):
			for j in range(i, n + 1):
				curr_max = max(curr_max, sum(nums[i:j]))

		return curr_max
# time: O(n^3), space: O(n) -> super inefficient
