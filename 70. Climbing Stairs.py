class Solution:
	def climbStairs_brute_force(self, n: int) -> int:
		# use recursion without memoization
		# base case
		if n <= 2:
			return n

		return self.climbStairs(n - 1) + self.climbStairs(n - 2)
# time: O(2^n)
# space: O(n)
