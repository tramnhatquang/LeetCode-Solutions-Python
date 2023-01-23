class Solution:
	def search(self, nums: List[int], target: int) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = left + (right - left) // 2
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				right = mid - 1
			else:
				left = mid + 1

		return -1  # if not found

# time: O(log n)
# spacE: O(1)
