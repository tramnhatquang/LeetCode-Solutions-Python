class Solution:
	def arrangeCoins_optimal(self, n: int) -> int:
		# 1 + 2+ ... + k =  k*(k+1)/2 <= n, where n is given, k is the max rows we can build
		# solve the solution -> k ?
		# we can use math formula based on the series formula

		# ANother way is to use BS
		left, right = 1, n

		while left <= right:
			mid = (left + right) // 2
			coins_required = mid * (
					mid + 1) // 2  # use integer division to find the required coins
			if coins_required == n:
				return mid
			elif coins_required > n:
				right = mid - 1
			else:
				left = mid + 1

		return right

	# time: O(log n)
	# space: O(1)

	def arrangeCoins_alternate(self, n: int) -> int:
		# brute force solution (STIMULATION)
		count = 0  # denotes the complete staircase so far
		i = 1  # we start at the first staircase
		while i <= n:
			n -= i
			i += 1  # move on to the next staircase
			count += 1

		return count

	# time: O(n), space: O(1)

	def arrangeCoins_using_math(self, n: int) -> int:
		return (int)((2 * n + 0.25) ** 0.5 - 0.5)
