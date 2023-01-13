# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	def firstBadVersion(self, n: int) -> int:
		# do a binary search on the range [1, n] inclusively
		left, right = 1, n
		while left < right:
			mid = left + (right - left) // 2
			# call API on the mid number
			if isBadVersion(mid) is True:
				right = mid
			else:
				left = mid + 1

		return left

# time: O(log n)
# space: O(1)
