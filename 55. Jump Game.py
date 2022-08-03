from functools import lru_cache
from typing import *


class Solution:
	def canJump(self, nums: List[int]) -> bool:
		n = len(nums)

		@lru_cache(None)
		def dp(i):
			if i == n - 1:
				return True

			for j in range(i + 1, min(i + nums[i], n - 1) + 1):
				if dp(j):
					return True
			return False

		return dp(0)
