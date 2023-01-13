from typing import List


class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		def backtrack(curr, i):
			if len(curr) == k:
				ans.append(curr[:])
				return

			for num in range(i, n + 1):
				curr.append(num)
				backtrack(curr, num + 1)
				curr.pop()

		ans = []
		backtrack([], 1)
		return ans
	# time: O( N! * k / (N - k)! * k!)
