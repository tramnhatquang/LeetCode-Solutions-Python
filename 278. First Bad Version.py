# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
	def firstBadVersion(self, n: int) -> int:
		left, right = 1, n
		ans = -1
		while left <= right:
			mid = (left + right) // 2
			if isBadVersion(mid):  # mid couble possibly be the first bad version
				# look to the left space
				ans = mid
				right = mid - 1

			else:  # look to the right space
				left = mid + 1

		return ans

# time: O(log n)
# space: O(1)
