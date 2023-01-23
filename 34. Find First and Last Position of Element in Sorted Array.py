class Solution:
	def searchRange_optimal(self, nums: List[int], target: int) -> List[int]:

		# do two binary search
		#   - the first BS is to find the leftmost target in the arr
		#   - the second BS is to find the rightmost target in the arr

		left, right = 0, len(nums) - 1
		left_most, right_most = -1, -1

		# find the leftmost target
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:  # continue looking to the left space
				left_most = mid
				right = mid - 1
			elif nums[mid] > target:
				right = mid - 1
			else:
				left = mid + 1

		# find the rightmost target:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				right_most = mid
				left = mid + 1
			elif nums[mid] > target:
				right = mid - 1
			else:
				left = mid + 1

		return [left_most, right_most]

	# time: O(log n), n is length of arr
	# space: O(1)
	def searchRange_linear(self, nums: List[int], target: int) -> List[int]:

		# check if we have target
		if target not in nums:
			return [-1, -1]
		left_index = 0
		right_index = len(nums) - 1
		# traverse from left and find the first indx of target
		for index, num in enumerate(nums):
			if num == target:
				left_index = index
				break
		# traverse from right and find the first index of target
		for index in range(len(nums) - 1, -1, -1):
			if nums[index] == target:
				right_index = index
				break

		return [left_index, right_index]

# time: O(3n) = O(n), space: O(1)
