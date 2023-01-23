class Solution:
	def findMin(self, nums: List[int]) -> int:
		# Observation: after sorting, the arr is divided into two sections:
		#   - one section where all values are larger than the last element
		#   - one section where all values are smaller than the alst element

		# use binary search to find the boundary between two sections which is the minimum number in the arr
		left, right = 0, len(nums) - 1
		boundary_index = -1

		while left <= right:
			mid = (left + right) // 2
			if nums[mid] <= nums[-1]:  # search to the left
				boundary_index = mid
				right = mid - 1
			else:
				left = mid + 1
		return nums[boundary_index]

		# time: O(log n)
		# space: O(1)