from typing import List


class Solution:
	def search(self, nums: List[int], target: int) -> int:
		# If a sorted array is shifted, if you take the middle, always one side will be sorted. Take the recursion according to that rule.
		# 	1. take the middle and compare with target, if matches return.
		#	2. if middle is bigger than left side, it means left is sorted
		#		- if [left] < target < [middle] then do recursion with left, middle - 1 (right)
		#		- left side is sorted, but target not in here, search on right side middle + 1 (left), right
		# 	3. if middle is less than right side, it means right is sorted
		#		- if [middle] < target < [right] then do recursion with middle + 1 (left), right
		#		- right side is sorted, but target not in here, search on left side left, middle -1 (right)

		n = len(nums)

		left, right = 0, n - 1
		while left <= right:
			mid = (left + right) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] >= nums[left]:  # left side is sorted
				if nums[left] <= target < nums[mid]:
					right = mid - 1
				else:
					left = mid + 1
			else:
				if nums[mid] < target <= nums[right]:
					left = mid + 1
				else:
					right = mid - 1

		return -1

# time: O(log n)
# space: O(1)
