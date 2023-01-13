class Solution:

	def isPerfectSquare_optimal(self, num: int) -> bool:
		# optimal Solution
		# do a Binary Search starting from 2 up to num inclusively

		# for num > 2, the square root a is always less than num /2 and greater than 1
		# In other words, 1 < a < num /2
		# We can do a binary search on this range
		if num == 1:
			return 1

		left, right = 2, num // 2
		while left <= right:
			mid = (left + right) // 2
			guess_num = mid * mid
			if guess_num == num:
				return True
			elif guess_num > num:
				right = mid - 1
			else:
				left = mid + 1

		return False

	# time: O(log n)
	# space: O(1)

	def isPerfectSquare_brute_force(self, num: int) -> bool:

		# REMEMBER: WE CANNOT USE BUILT-IN FUNCTION LIKE MATH.SQRT

		# easy check
		if num == 1:
			return True

		for i in range(2, num // 2 + 1):
			if i ** i == num:
				return True

		return False

# time: O(n) -> TLE
# space: O(1)
