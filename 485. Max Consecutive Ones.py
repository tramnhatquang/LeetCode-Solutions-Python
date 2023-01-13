class Solution:
	def findMaxConsecutiveOnes_optimal(self, nums: List[int]) -> int:
		# algo:
		# 1. Maintain a counter for the number of 1's.
		# 2. Increment the counter by 1, whenever you encounter a 1.
		# 3. Whenever you encounter a 0
		#   - Use the current count of 1's to find the maximum contiguous 1's till now.
		#   - Afterwards, reset the counter for 1's to 0.
		# 4. Return the maximum in the end.

		# trick: counting the contiguous 1s is the same as counting number of 1s between zeroes
		global_max = count = 0
		for index in range(len(nums)):
			if nums[index] == 1:
				count += 1
			else:
				# record the max so far
				global_max = max(global_max, count)

				# reset the count back
				count = 0

		# returns max of two variables to include the last 1 in the arr if it does happen
		return max(global_max, count)

	def findMaxConsecutiveOnes_sliding_window(self, nums: List[int]) -> int:
		# using a sliding window technique
		# sliding window only contains 1s

		left = right = 0
		global_max = 0
		while right < len(nums):
			if nums[right] == 0:
				# window size is the number of consecutive ones we have found so far
				# why not right - left + 1? but right - left
				# since all consecutive ones go from [left, right - 1] inclusviely
				global_max = max(global_max, right - left)

				# left must start at the first 1, there maybe a possible one to next number
				left = right + 1
			right += 1

		return max(global_max, right - left)
# time: O(n), space: O(1)
